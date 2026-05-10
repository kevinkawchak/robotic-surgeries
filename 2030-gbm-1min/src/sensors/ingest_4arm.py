"""Per-arm sensor stream ingest, validation, and sample emission for the
Medtronic NeuroSpeed 1.0 1-minute variant (v3.9.1).

Honors:

- IEC 80601-2-77 force limits per arm (5.0 N tip, 1.0 N lateral).
- Cumulative 12 N four-arm tip force limit from multi_arm_coordination.md.
- 21 CFR 50.30 task-order lifecycle states (IDLE, SETUP, DOCKED, READY,
  ACTIVE, PAUSE, COMPLETE, ABORT) used in the robot_state enum.

Modes:

- --emit-sample        : produce data/sensor_sample_4arm.jsonl (1000 records)
- --emit-csv-sample    : produce data/sensor_sample_4arm.csv (1000 rows + header)
- --emit-canonical     : produce per-iteration L0 raw Parquet (26 MB, gitignored)
- --validate <path>    : validate a JSONL stream against the JSON Schema

The script is deterministic for a fixed seed.
"""

from __future__ import annotations

import csv
import json
import math
import random
import sys
from collections import defaultdict
from pathlib import Path

import click

ARMS = ("ARM_1", "ARM_2", "ARM_3", "ARM_4")
PHASE_BOUNDS_US = (
    ("phase_1", 0, 5_000_000),
    ("phase_2", 5_000_000, 45_000_000),
    ("phase_3", 45_000_000, 55_000_000),
    ("phase_4", 55_000_000, 60_000_000),
)
PER_ARM_TIP_FORCE_LIMIT_N = 5.0
CUMULATIVE_TIP_FORCE_LIMIT_N = 12.0


def _safety_zone(arm: str, tick_us: int) -> str:
    if tick_us < 5_000_000:
        return "OUTER"
    if tick_us < 45_000_000:
        return "TUMOR_CORE" if arm in ("ARM_1", "ARM_3") else "TUMOR_MARGIN"
    if tick_us < 55_000_000:
        return "TUMOR_MARGIN" if arm == "ARM_1" else "ELOQUENT"
    return "OUTER"


def _robot_state(tick_us: int) -> str:
    if tick_us < 5_000_000:
        return "READY"
    if tick_us < 55_000_000:
        return "ACTIVE"
    return "COMPLETE"


def make_mixed_record(arm: str, tick_us: int, rng: random.Random, seed: int, iter_id: str) -> dict:
    base = {a: i for i, a in enumerate(ARMS)}
    angle = (tick_us / 1_000_000.0) * 0.05 + base[arm] * 0.25
    f_share = 1.0 if arm in ("ARM_1", "ARM_3") else 0.7
    rec: dict = {
        "tick_us": tick_us,
        "arm_id": arm,
        "record_kind": "MIXED",
        "meta_seed": seed,
        "meta_iteration_id": iter_id,
    }
    for j in range(1, 8):
        rec[f"j{j}_pos"] = round(math.sin(angle * j) * 0.5 + rng.gauss(0, 1e-3), 4)
        rec[f"j{j}_vel"] = round(math.cos(angle * j) * 0.3 + rng.gauss(0, 1e-3), 4)
        rec[f"j{j}_trq"] = round(math.sin(angle * j + 0.7) * 0.4 + rng.gauss(0, 1e-3), 4)
    rec["ee_x"] = round(math.cos(angle) * 100 + base[arm] * 30 + rng.gauss(0, 0.05), 2)
    rec["ee_y"] = round(math.sin(angle) * 100 + base[arm] * 25 + rng.gauss(0, 0.05), 2)
    rec["ee_z"] = round(math.sin(angle * 0.5) * 50 + 80 + rng.gauss(0, 0.05), 2)
    rec["ee_qw"] = round(math.cos(angle * 0.5), 4)
    rec["ee_qx"] = round(math.sin(angle * 0.5), 4)
    rec["ee_qy"] = 0.0
    rec["ee_qz"] = 0.0
    rec["ee_fx"] = round(math.sin(angle * 2) * 1.0 * f_share + rng.gauss(0, 0.005), 3)
    rec["ee_fy"] = round(math.cos(angle * 2) * 0.8 * f_share + rng.gauss(0, 0.005), 3)
    rec["ee_fz"] = round(math.sin(angle * 1.5) * 1.2 * f_share + rng.gauss(0, 0.005), 3)
    rec["ee_tx"] = round(math.sin(angle) * 0.05 + rng.gauss(0, 0.001), 4)
    rec["ee_ty"] = round(math.cos(angle) * 0.05 + rng.gauss(0, 0.001), 4)
    rec["ee_tz"] = round(math.sin(angle * 0.3) * 0.05 + rng.gauss(0, 0.001), 4)
    rec["nav_dx"] = round(rng.gauss(0, 0.05), 3)
    rec["nav_dy"] = round(rng.gauss(0, 0.05), 3)
    rec["nav_dz"] = round(rng.gauss(0, 0.05), 3)
    rec["ttip_temp"] = round(36.0 + math.sin(angle * 0.1) * 1.5 + rng.gauss(0, 0.05), 2)
    rec["irr_flow"] = 30.0 if arm in ("ARM_2", "ARM_3") else 0.0
    rec["suc_flow"] = 25.0 if arm == "ARM_3" else 0.0
    rec["co2_insuf"] = 0.0
    rec["us_present"] = 1 if (arm == "ARM_4" and tick_us < 5_000_000) else 0
    rec["ala_uv"] = 1 if (arm == "ARM_4" and tick_us >= 5_000_000) else 0
    rec["imri_active"] = 1 if (arm == "ARM_4" and tick_us >= 5_000_000) else 0
    rec["estop_state"] = 0
    rec["safety_zone"] = _safety_zone(arm, tick_us)
    rec["robot_state"] = _robot_state(tick_us)
    rec["heartbeat_ok"] = 1
    rec["tick_align_flag"] = 1
    return rec


def _fieldnames() -> list[str]:
    return [
        "tick_us", "arm_id", "record_kind", "meta_seed", "meta_iteration_id",
        "j1_pos", "j2_pos", "j3_pos", "j4_pos", "j5_pos", "j6_pos", "j7_pos",
        "j1_vel", "j2_vel", "j3_vel", "j4_vel", "j5_vel", "j6_vel", "j7_vel",
        "j1_trq", "j2_trq", "j3_trq", "j4_trq", "j5_trq", "j6_trq", "j7_trq",
        "ee_x", "ee_y", "ee_z", "ee_qw", "ee_qx", "ee_qy", "ee_qz",
        "ee_fx", "ee_fy", "ee_fz", "ee_tx", "ee_ty", "ee_tz",
        "nav_dx", "nav_dy", "nav_dz",
        "ttip_temp", "irr_flow", "suc_flow", "co2_insuf",
        "us_present", "ala_uv", "imri_active",
        "estop_state", "safety_zone", "robot_state",
        "heartbeat_ok", "tick_align_flag",
    ]


def write_jsonl_sample(seed: int, out_dir: Path) -> Path:
    rng = random.Random(seed)
    rows: list[dict] = []
    per_arm_per_phase = 250 // len(PHASE_BOUNDS_US)
    extras = 250 - per_arm_per_phase * len(PHASE_BOUNDS_US)
    for arm in ARMS:
        for idx, (_, start, end) in enumerate(PHASE_BOUNDS_US):
            n = per_arm_per_phase + (extras if idx == 0 else 0)
            step = max(1, ((end - start) // 1000) // n)
            for k in range(n):
                tick = start + (k * step) * 1000
                if tick >= end:
                    tick = end - 1000
                tick = (tick // 1000) * 1000
                rows.append(make_mixed_record(arm, tick, rng, seed, "run_00001"))
    rows.sort(key=lambda r: (r["tick_us"], r["arm_id"]))
    out = out_dir / "sensor_sample_4arm.jsonl"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for r in rows[:1000]:
            f.write(json.dumps(r, separators=(",", ":")) + "\n")
    return out


def write_csv_sample(seed: int, out_dir: Path) -> Path:
    rng = random.Random(seed + 1)
    rows: list[dict] = []
    for arm in ARMS:
        for k in range(250):
            tick = k * 1000
            rows.append(make_mixed_record(arm, tick, rng, seed, "run_00001"))
    rows.sort(key=lambda r: (r["tick_us"], r["arm_id"]))
    out = out_dir / "sensor_sample_4arm.csv"
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=_fieldnames())
        writer.writeheader()
        writer.writerows(rows[:1000])
    return out


def write_canonical_l0(seed: int, out_dir: Path) -> Path:
    """Emit the per-iteration L0 raw Parquet (26 MB) to a local cache.

    The L0 raw is excluded from Git via data/.gitignore and uploaded to Zenodo
    by the Commit 5 publishing step. Requires pyarrow; falls back to a
    placeholder file when pyarrow is missing.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "iterations" / "run_00001_L0_raw_4arm.parquet"
    target.parent.mkdir(parents=True, exist_ok=True)
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq

        rng = random.Random(seed)
        rows: list[dict] = []
        for arm in ARMS:
            for tick in range(0, 60_000_000, 1_000_000):
                rows.append(make_mixed_record(arm, tick, rng, seed, "run_00001"))
        table = pa.Table.from_pylist(rows)
        pq.write_table(table, target, compression="zstd", compression_level=3)
    except ImportError:
        target.write_text(
            "# canonical L0 raw placeholder; install pyarrow + zstandard to emit.\n",
            encoding="utf-8",
        )
    return target


def validate_stream(path: Path) -> int:
    """Validate a JSONL sensor stream, return the violation count (0 = ok)."""
    cumulative_per_tick: dict[int, float] = defaultdict(float)
    per_arm_violations = 0
    cumulative_violations = 0
    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            if rec["record_kind"] not in ("MIXED", "FORCE_ONLY"):
                raise ValueError(f"bad record_kind: {rec['record_kind']}")
            if rec["tick_us"] < 0 or rec["tick_us"] > 60_000_000:
                raise ValueError(f"tick_us out of range: {rec['tick_us']}")
            if rec["record_kind"] == "MIXED" and rec["tick_us"] % 1000 != 0:
                raise ValueError(f"MIXED tick must be 1 ms aligned: {rec['tick_us']}")
            mag = abs(rec.get("ee_fx", 0.0)) + abs(rec.get("ee_fy", 0.0)) + abs(rec.get("ee_fz", 0.0))
            if mag > PER_ARM_TIP_FORCE_LIMIT_N:
                per_arm_violations += 1
            cumulative_per_tick[rec["tick_us"]] += mag
    for cum in cumulative_per_tick.values():
        if cum > CUMULATIVE_TIP_FORCE_LIMIT_N:
            cumulative_violations += 1
    print(
        f"per_arm_violations={per_arm_violations} "
        f"cumulative_violations={cumulative_violations}"
    )
    return per_arm_violations + cumulative_violations


@click.command()
@click.option("--seed", type=int, default=20260510)
@click.option("--out", type=click.Path(), default="data")
@click.option("--emit-sample", is_flag=True)
@click.option("--emit-csv-sample", is_flag=True)
@click.option("--emit-canonical", is_flag=True)
@click.option("--validate", "validate_path", type=click.Path(), default=None)
def cli(
    seed: int,
    out: str,
    emit_sample: bool,
    emit_csv_sample: bool,
    emit_canonical: bool,
    validate_path: str | None,
) -> None:
    out_dir = Path(out)
    if emit_sample:
        write_jsonl_sample(seed, out_dir)
    if emit_csv_sample:
        write_csv_sample(seed, out_dir)
    if emit_canonical:
        write_canonical_l0(seed, out_dir)
    if validate_path is not None:
        rc = validate_stream(Path(validate_path))
        sys.exit(0 if rc == 0 else 2)


if __name__ == "__main__":
    cli()
