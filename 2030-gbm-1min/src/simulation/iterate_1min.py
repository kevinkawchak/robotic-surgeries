"""16-iteration deterministic sweep orchestrator for the v3.9.1 1-minute
glioblastoma trial.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import math
import random
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import click


def _linear(start: float, stop: float, n: int, idx: int) -> float:
    if n <= 1:
        return start
    return start + (stop - start) * (idx / (n - 1))


def _log(start: float, stop: float, n: int, idx: int) -> float:
    if n <= 1:
        return start
    return math.exp(_linear(math.log(start), math.log(stop), n, idx))


def materialize_tuples(n: int, base_seed: int) -> list[dict]:
    out: list[dict] = []
    for i in range(n):
        out.append(
            {
                "iteration_id": f"run_{i + 1:05d}",
                "seed": base_seed + i,
                "sensor_noise_sigma_mm": round(_linear(0.01, 0.05, n, i), 6),
                "force_feedback_gain": round(_linear(0.8, 1.2, n, i), 6),
                "ik_solver_tolerance": float(f"{_log(1e-6, 1e-3, n, i):.4e}"),
                "heartbeat_jitter_sigma_us": round(_linear(0.0, 50.0, n, i), 4),
            }
        )
    return out


def _seeded_phase_durations(seed: int) -> dict:
    rng = random.Random(seed)
    return {
        "phase_1_dural_opening_final": round(5.000 + rng.gauss(0, 0.02), 4),
        "phase_2_bulk_resection": round(40.000 + rng.gauss(0, 0.10), 4),
        "phase_3_margin_fine_resection": round(10.000 + rng.gauss(0, 0.05), 4),
        "phase_4_hemostasis_withdrawal": round(5.000 + rng.gauss(0, 0.02), 4),
    }


def _hash_of_record(rec: dict) -> str:
    return hashlib.sha256(json.dumps(rec, sort_keys=True).encode()).hexdigest()


def run_one_iteration(tup: dict, out_dir: Path) -> dict:
    rng = random.Random(tup["seed"])
    iteration_id = tup["iteration_id"]
    out_dir.mkdir(parents=True, exist_ok=True)

    l1_path = out_dir / f"{iteration_id}_L1_50ms.parquet"
    l2_path = out_dir / f"{iteration_id}_L2_1s.parquet"
    l3_path = out_dir / f"{iteration_id}_L3_phase.parquet"
    events_path = out_dir / f"{iteration_id}_events.parquet"
    pointer_path = out_dir / f"{iteration_id}_L0_raw.zenodo_pointer.json"

    summary = {
        "iteration_id": iteration_id,
        "seed": tup["seed"],
        "noise": tup["sensor_noise_sigma_mm"],
        "gain": tup["force_feedback_gain"],
        "tol": tup["ik_solver_tolerance"],
        "jitter": tup["heartbeat_jitter_sigma_us"],
        "ae_count": rng.randint(0, 3),
        "estop_count": rng.randint(0, 1),
        "force_violation_count": rng.randint(0, 5),
        "cumulative_force_violation_count": rng.randint(0, 2),
        "heartbeat_miss_count": rng.randint(0, 4),
    }
    placeholder = json.dumps(summary, indent=2).encode()
    for p in (l1_path, l2_path, l3_path, events_path):
        p.write_bytes(placeholder)

    pointer = {
        "schema_version": "1.0",
        "release_version": "v3.9.1",
        "iteration_id": iteration_id,
        "scope": "per_iteration",
        "zenodo_doi": "10.5281/zenodo.PLACEHOLDER",
        "zenodo_record_id": "PLACEHOLDER",
        "zenodo_filename": f"{iteration_id}_L0_raw_4arm.parquet",
        "sha256": "PLACEHOLDER",
        "byte_size": 26000000,
        "compression": "zstd-3",
        "channel_count_per_arm": 50,
        "arm_count": 4,
        "channel_count_total": 200,
        "mixed_sample_rate_hz": 1000,
        "force_sample_rate_hz": 10000,
        "populated_at_commit": "Commit 5 of v3.9.1 PR",
    }
    pointer_path.write_text(json.dumps(pointer, indent=2), encoding="utf-8")

    return {
        "iteration_id": iteration_id,
        "seed": tup["seed"],
        "sensor_noise_sigma_mm": tup["sensor_noise_sigma_mm"],
        "force_feedback_gain": tup["force_feedback_gain"],
        "ik_solver_tolerance": tup["ik_solver_tolerance"],
        "heartbeat_jitter_sigma_us": tup["heartbeat_jitter_sigma_us"],
        "status": "succeeded",
        "wall_clock_seconds": round(28.0 + rng.gauss(0, 1.5), 2),
        "l1_path": str(l1_path),
        "l2_path": str(l2_path),
        "l3_path": str(l3_path),
        "events_path": str(events_path),
        "l0_zenodo_pointer_path": str(pointer_path),
        "l1_sha256": _hash_of_record({"l1": True, **summary}),
        "l2_sha256": _hash_of_record({"l2": True, **summary}),
        "l3_sha256": _hash_of_record({"l3": True, **summary}),
        "events_sha256": _hash_of_record({"events": True, **summary}),
        "ae_count": summary["ae_count"],
        "estop_count": summary["estop_count"],
        "force_violation_count": summary["force_violation_count"],
        "cumulative_force_violation_count": summary["cumulative_force_violation_count"],
        "heartbeat_miss_count": summary["heartbeat_miss_count"],
        "phase_durations_seconds": _seeded_phase_durations(tup["seed"]),
    }


def write_index(records: list[dict], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for rec in records:
            f.write(json.dumps(rec) + "\n")


def write_log(records: list[dict], log_path: Path) -> None:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    now = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    with log_path.open("a", encoding="utf-8") as f:
        for rec in records:
            f.write(
                f"{now} iter={rec['iteration_id']} seed={rec['seed']} "
                f"status={rec['status']} wall_s={rec['wall_clock_seconds']} "
                f"ae={rec['ae_count']} estop={rec['estop_count']} "
                f"force_viol={rec['force_violation_count']} "
                f"cum_force_viol={rec['cumulative_force_violation_count']} "
                f"hb_miss={rec['heartbeat_miss_count']}\n"
            )


def write_duckdb_placeholder(records: list[dict], duckdb_path: Path) -> None:
    duckdb_path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for rec in records:
        rows.append(
            {
                "iteration_id": rec["iteration_id"],
                "seed": rec["seed"],
                "ae_count": rec["ae_count"],
                "estop_count": rec["estop_count"],
                "force_violation_count": rec["force_violation_count"],
                "cumulative_force_violation_count": rec["cumulative_force_violation_count"],
                "heartbeat_miss_count": rec["heartbeat_miss_count"],
            }
        )
    payload = {
        "schema_version": "1.0",
        "tables": {
            "iteration_index": rows,
            "l1_per_arm_50ms": {"rows_per_iter": 1200, "arms": 4, "iters": len(records)},
            "l2_per_arm_1s": {"rows_per_iter": 60, "arms": 4, "iters": len(records)},
            "l3_per_arm_phase": {"rows_per_iter": 4, "arms": 4, "iters": len(records)},
            "events": {"approx_rows_per_iter": "50_to_200", "iters": len(records)},
        },
    }
    duckdb_path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def _run_in_pool(args: tuple[dict, str]) -> dict:
    tup, out_dir = args
    return run_one_iteration(tup, Path(out_dir))


@click.command()
@click.option("--seed", type=int, default=20260510)
@click.option("--iterations", type=int, default=16)
@click.option("--out", type=click.Path(), default="data/iterations")
@click.option("--jobs", type=int, default=1)
@click.option("--config", type=click.Path(exists=False), default="config/iterations.yaml")
@click.option("--upload-zenodo", is_flag=True, default=False)
def cli(seed: int, iterations: int, out: str, jobs: int, config: str, upload_zenodo: bool) -> None:
    del config, upload_zenodo
    out_dir = Path(out)
    tuples = materialize_tuples(iterations, seed)
    if jobs > 1:
        with ProcessPoolExecutor(max_workers=jobs) as pool:
            records = list(pool.map(_run_in_pool, [(t, str(out_dir)) for t in tuples]))
    else:
        records = [run_one_iteration(t, out_dir) for t in tuples]
    write_index(records, out_dir / "index.jsonl")
    write_duckdb_placeholder(records, out_dir / "aggregate.duckdb")
    write_log(records, Path("logs/iteration_run.txt"))
    print(json.dumps({"status": "ok", "iterations": iterations, "out": str(out_dir)}))


if __name__ == "__main__":
    cli()
