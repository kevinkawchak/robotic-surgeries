"""640 channel sensor ingest pipeline for the 8 arm PDAC 1 minute simulation.

The pipeline reads per arm per tick sensor records at mixed 100 kHz force plus
10 kHz command rates and emits JSONL records that match the sensor_record_8arm
schema family (JSON Schema, Protocol Buffers, Avro). The deterministic seed
contract (root_seed = 20260513) yields bit identical output for fixed inputs.
"""

from __future__ import annotations

import json
import math
import random
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable

import click

ROOT_SEED = 20260513
ARMS = 8
CHANNELS_PER_ARM = 80
TOTAL_CHANNELS = ARMS * CHANNELS_PER_ARM
COMMAND_RATE_HZ = 10_000
FORCE_RATE_HZ = 100_000
DURATION_S = 60.0

PHASE_BOUNDARIES_S = [
    (1, 0.000, 6.000),
    (2, 6.000, 16.000),
    (3, 16.000, 24.000),
    (4, 24.000, 32.000),
    (5, 32.000, 42.000),
    (6, 42.000, 48.000),
    (7, 48.000, 54.000),
    (8, 54.000, 60.000),
]

TOOL_BY_ARM = {
    1: "hybrid_scalpel_needle_driver",
    2: "bipolar_coag_needle_driver",
    3: "articulated_retractor_grasper",
    4: "linear_8el_us_imri_nir",
    5: "bipolar_suction",
    6: "suction_bipolar",
    7: "suction_irrigation",
    8: "nir_5ala_sample_collector",
}

TOOL_SUBTYPE_BY_ARM = {1: 1001, 2: 1002, 3: 1003, 4: 1004, 5: 1005, 6: 1006, 7: 1007, 8: 1008}


@dataclass
class ArmState:
    arm_id: int
    q: list[float] = field(default_factory=lambda: [0.0] * 7)
    qd: list[float] = field(default_factory=lambda: [0.0] * 7)
    tau: list[float] = field(default_factory=lambda: [0.0] * 7)
    ee_pos: list[float] = field(default_factory=lambda: [0.0, 0.0, 0.0])
    ee_quat: list[float] = field(default_factory=lambda: [0.0, 0.0, 0.0, 1.0])
    ee_vel: list[float] = field(default_factory=lambda: [0.0, 0.0, 0.0])
    force_time_integral: float = 0.0
    last_phase: int = 0


def phase_for_time(t_s: float) -> int:
    """Return the 1 to 8 phase index for the simulation time in seconds."""
    for phase_id, start_s, end_s in PHASE_BOUNDARIES_S:
        if start_s <= t_s < end_s:
            return phase_id
    return 8


def _base_offset(arm_id: int) -> tuple[float, float, float]:
    """Return the per arm base frame offset (mm) in the patient frame."""
    table = {
        1: (400.0, -200.0, 300.0),
        2: (400.0, 200.0, 300.0),
        3: (400.0, -400.0, 200.0),
        4: (400.0, 400.0, 200.0),
        5: (-400.0, -200.0, 300.0),
        6: (-400.0, 200.0, 300.0),
        7: (-400.0, -400.0, 200.0),
        8: (-400.0, 400.0, 200.0),
    }
    return table[arm_id]


def _per_arm_target(arm_id: int, phase: int, t_s: float) -> tuple[float, float, float]:
    """Compute a deterministic per arm target tip position in patient frame.

    The targets converge on the upper abdomen anatomy: the SMV at (15, -25, -45),
    the portal vein at (5, -55, -55), the hepatic artery at (20, -60, -50),
    and the three anastomosis sites for Phases 5 6 7.
    """
    targets_by_phase = {
        1: (0.0, -10.0, -20.0),
        2: (15.0, -25.0, -45.0),
        3: (0.0, -35.0, -55.0),
        4: (5.0, -45.0, -50.0),
        5: (18.0, -30.0, -42.0),
        6: (12.0, -50.0, -48.0),
        7: (-8.0, -40.0, -30.0),
        8: (0.0, -30.0, -40.0),
    }
    target = targets_by_phase[phase]
    bx, by, bz = _base_offset(arm_id)
    arm_factor = 1.0 + 0.05 * (arm_id - 1)
    return (
        target[0] + 0.1 * math.sin(2 * math.pi * t_s * arm_factor),
        target[1] + 0.1 * math.cos(2 * math.pi * t_s * arm_factor),
        target[2] + 0.05 * math.sin(2 * math.pi * t_s * arm_factor * 0.5),
    )


def _sample_record(
    rng: random.Random,
    arm: ArmState,
    tick: int,
    t_s: float,
    phase: int,
) -> dict[str, Any]:
    """Generate one sensor record for a given arm at a given tick.

    The record is deterministic for the (arm_id, tick) pair when the rng was
    seeded with (root_seed + iteration_index + arm_id).
    """
    target = _per_arm_target(arm.arm_id, phase, t_s)
    for i in range(7):
        arm.q[i] += 0.0001 * (rng.random() - 0.5)
        arm.qd[i] = 0.001 * math.sin(2 * math.pi * t_s + i)
        arm.tau[i] = 0.5 + 0.02 * (rng.random() - 0.5)
    arm.ee_pos = [
        round(target[0] + 0.01 * (rng.random() - 0.5), 4),
        round(target[1] + 0.01 * (rng.random() - 0.5), 4),
        round(target[2] + 0.01 * (rng.random() - 0.5), 4),
    ]
    arm.ee_quat = [0.0, 0.0, 0.0, 1.0]
    arm.ee_vel = [
        50.0 + 5.0 * math.sin(2 * math.pi * t_s),
        20.0 + 2.0 * math.cos(2 * math.pi * t_s),
        10.0,
    ]
    fx = 0.5 + 0.05 * math.sin(2 * math.pi * 50 * t_s)
    fy = 0.3 + 0.05 * math.cos(2 * math.pi * 50 * t_s)
    fz = 0.2 + 0.02 * math.sin(2 * math.pi * 25 * t_s)
    ee_force = [round(fx, 4), round(fy, 4), round(fz, 4)]
    tip_force_scalar = math.sqrt(fx * fx + fy * fy + fz * fz)
    arm.force_time_integral += tip_force_scalar * (1.0 / FORCE_RATE_HZ)
    if phase != arm.last_phase:
        arm.force_time_integral = 0.0
        arm.last_phase = phase
    tool_state_by_phase = {
        1: "approach", 2: "cut", 3: "cut", 4: "engage",
        5: "suture", 6: "suture", 7: "suture", 8: "withdraw",
    }
    estop_state = "armed"
    collision_state = "clear"
    record: dict[str, Any] = {
        "tick": tick,
        "arm_id": arm.arm_id,
        "phase": phase,
        "q": [round(v, 6) for v in arm.q],
        "qd": [round(v, 6) for v in arm.qd],
        "tau": [round(v, 6) for v in arm.tau],
        "ee_pos": arm.ee_pos,
        "ee_quat": arm.ee_quat,
        "ee_vel": [round(v, 4) for v in arm.ee_vel],
        "ee_force": ee_force,
        "ee_torque": [0.001, 0.001, 0.001],
        "tool_state": tool_state_by_phase[phase],
        "tool_subtype": TOOL_SUBTYPE_BY_ARM[arm.arm_id],
        "bipolar_current": 0.0 if arm.arm_id != 2 else round(50.0 + 5.0 * rng.random(), 3),
        "bipolar_voltage": 0.0 if arm.arm_id != 2 else round(40.0 + 2.0 * rng.random(), 3),
        "suction_pressure": 0.0 if arm.arm_id != 7 else round(20.0 + 1.0 * rng.random(), 3),
        "suction_flow": 0.0 if arm.arm_id != 7 else round(5.0 + 0.5 * rng.random(), 3),
        "irrigation_flow": 0.0 if arm.arm_id != 7 else round(2.0 + 0.2 * rng.random(), 3),
        "vessel_proximity": round(8.0 + 2.0 * math.sin(2 * math.pi * t_s), 4),
        "nir_icg": [round(1000.0 + 50.0 * rng.random(), 2) for _ in range(4)],
        "duct_manometry": round(12.0 + 0.5 * math.sin(2 * math.pi * t_s), 3) if phase == 5 else 0.0,
        "ring_tension": round(0.45 + 0.02 * math.sin(2 * math.pi * t_s), 4) if phase in (5, 6, 7) else 0.0,
        "bile_spectrophotometry": [round(100.0 + 5.0 * rng.random(), 2) for _ in range(4)],
        "us_b_mode": [round(30.0 + 5.0 * math.sin(2 * math.pi * t_s + i), 2) for i in range(8)],
        "heartbeat_seq": tick,
        "heartbeat_watchdog": int(50 + 10 * rng.random()),
        "tip_force_scalar": round(tip_force_scalar, 4),
        "cumulative_cross_arm_force": round(tip_force_scalar * ARMS, 4),
        "force_time_integral": round(arm.force_time_integral, 6),
        "engagement_depth": round(5.0 + 0.5 * math.sin(2 * math.pi * t_s), 4),
        "estop_state": estop_state,
        "temperature": round(37.0 + 0.1 * rng.random(), 3),
        "power": round(50.0 + 5.0 * rng.random(), 3),
        "collision_state": collision_state,
        "tool_changer_state": 0,
        "task_id": (phase * 1000) + arm.arm_id,
        "phase_id": phase,
        "queue_depth": int(2 + 2 * rng.random()),
    }
    return record


def generate_sample_slice(
    arm_id: int = 1,
    phase_start_s: float = 32.0,
    duration_ms: float = 100.0,
    sample_rate_hz: int = COMMAND_RATE_HZ,
    seed: int = ROOT_SEED,
) -> Iterable[dict[str, Any]]:
    """Yield a sample slice of one arm for the first duration_ms of phase 5."""
    rng = random.Random(seed + arm_id)
    arm = ArmState(arm_id=arm_id)
    sample_count = int(duration_ms * sample_rate_hz / 1000)
    dt = 1.0 / sample_rate_hz
    for i in range(sample_count + 1):
        t_s = phase_start_s + i * dt
        phase = phase_for_time(t_s)
        tick = int(t_s * FORCE_RATE_HZ)
        record = _sample_record(rng, arm, tick, t_s, phase)
        yield record


def write_jsonl(records: Iterable[dict[str, Any]], path: Path) -> int:
    """Write records to a JSONL file. Return the row count."""
    path.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with path.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, separators=(",", ":")))
            f.write("\n")
            n += 1
    return n


@click.command()
@click.option("--seed", type=int, default=ROOT_SEED, help="Root simulation seed.")
@click.option("--arm-id", type=int, default=1, help="Publication arm id (1 to 8).")
@click.option("--duration-ms", type=float, default=100.0, help="Sample slice duration (ms).")
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=Path("data/sensor_sample_8arm.jsonl"),
    help="Output JSONL path.",
)
def main(seed: int, arm_id: int, duration_ms: float, output: Path) -> None:
    """Generate the publication arm sample slice."""
    records = list(
        generate_sample_slice(
            arm_id=arm_id,
            phase_start_s=32.0,
            duration_ms=duration_ms,
            sample_rate_hz=COMMAND_RATE_HZ,
            seed=seed,
        )
    )
    n = write_jsonl(records, output)
    click.echo(f"wrote {n} records to {output}")


if __name__ == "__main__":
    main()
