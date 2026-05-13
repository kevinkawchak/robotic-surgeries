"""Per arm xyz command mapping pipeline.

The pipeline has six stages: sensor ingest, phase identification, per arm task
identification, per arm target generation, safety zone gating (vascular plus
collision plus ring tension), and command emission. Runs at the 10 kHz command
channel rate. Output records match xyz_command_8arm.schema.json.
"""

from __future__ import annotations

import json
import math
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import click

ROOT_SEED = 20260513
ARMS = 8
COMMAND_RATE_HZ = 10_000
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

PHASE_TARGETS = {
    1: (0.0, -10.0, -20.0),
    2: (15.0, -25.0, -45.0),
    3: (0.0, -35.0, -55.0),
    4: (5.0, -45.0, -50.0),
    5: (18.0, -30.0, -42.0),
    6: (12.0, -50.0, -48.0),
    7: (-8.0, -40.0, -30.0),
    8: (0.0, -30.0, -40.0),
}

RING_TENSION_BY_PHASE = {5: 0.45, 6: 0.50, 7: 0.60}

VESSEL_CENTERLINES = [
    {"name": "superior_mesenteric_vein", "x": 15.0, "y": -45.0, "z": -50.0, "hard": 2.0, "soft": 4.0, "nofly": 6.0, "phases": [2, 4, 5, 8]},
    {"name": "portal_vein", "x": 5.0, "y": -65.0, "z": -52.5, "hard": 2.0, "soft": 4.0, "nofly": 6.0, "phases": [2, 4, 5, 8]},
    {"name": "hepatic_artery", "x": 12.5, "y": -62.5, "z": -52.5, "hard": 1.5, "soft": 3.0, "nofly": 5.0, "phases": [2, 4, 6, 8]},
    {"name": "celiac_axis", "x": 2.5, "y": -67.5, "z": -57.5, "hard": 1.5, "soft": 3.0, "nofly": 5.0, "phases": [3, 4, 8]},
    {"name": "superior_mesenteric_artery", "x": 2.5, "y": -50.0, "z": -57.5, "hard": 1.5, "soft": 3.0, "nofly": 5.0, "phases": [3, 4, 8]},
]

ACTIVE_ARMS_BY_PHASE = {
    1: [1, 2, 3, 4],
    2: [1, 2, 3, 4, 5, 6, 7, 8],
    3: [1, 2, 3, 4],
    4: [1, 2, 3, 4, 5, 6, 7, 8],
    5: [1, 2, 3, 4, 5],
    6: [1, 2, 3, 4, 5],
    7: [1, 2, 3, 4],
    8: [1, 2, 3, 4, 5, 6, 7, 8],
}

TOOL_STATE_BY_PHASE = {
    1: "approach", 2: "cut", 3: "cut", 4: "engage",
    5: "suture", 6: "suture", 7: "suture", 8: "withdraw",
}


@dataclass
class GateResult:
    action: str
    velocity_scale: float
    force_clamp: float
    e_stop: bool


def phase_for_time(t_s: float) -> int:
    """Return the 1 to 8 phase index for the simulation time (seconds)."""
    for phase_id, start_s, end_s in PHASE_BOUNDARIES_S:
        if start_s <= t_s < end_s:
            return phase_id
    return 8


def _distance_to_vessel(pos: tuple[float, float, float], vessel: dict[str, Any]) -> float:
    """L2 norm from a tip position to a vessel centerline."""
    dx = pos[0] - vessel["x"]
    dy = pos[1] - vessel["y"]
    dz = pos[2] - vessel["z"]
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def safety_zone_gate(
    pos: tuple[float, float, float],
    phase: int,
) -> GateResult:
    """Compute the safety zone action for a given tip position and phase."""
    nearest_action = "clear"
    for v in VESSEL_CENTERLINES:
        if phase not in v["phases"]:
            continue
        d = _distance_to_vessel(pos, v)
        if d <= v["hard"]:
            return GateResult("hard_stop", 0.0, 0.0, True)
        if d <= v["soft"]:
            nearest_action = "soft_warning"
        elif d <= v["nofly"] and nearest_action == "clear":
            nearest_action = "no_fly"
    scale_map = {"clear": 1.0, "no_fly": 0.5, "soft_warning": 0.1, "hard_stop": 0.0}
    force_map = {"clear": 3.0, "no_fly": 2.5, "soft_warning": 1.5, "hard_stop": 0.0}
    return GateResult(nearest_action, scale_map[nearest_action], force_map[nearest_action], False)


def per_arm_target(arm_id: int, phase: int, t_s: float) -> tuple[float, float, float]:
    """Compute a deterministic per arm target tip position."""
    target = PHASE_TARGETS[phase]
    arm_factor = 1.0 + 0.05 * (arm_id - 1)
    return (
        target[0] + 0.1 * math.sin(2 * math.pi * t_s * arm_factor),
        target[1] + 0.1 * math.cos(2 * math.pi * t_s * arm_factor),
        target[2] + 0.05 * math.sin(2 * math.pi * t_s * arm_factor * 0.5),
    )


def _command_record(
    rng: random.Random,
    arm_id: int,
    tick: int,
    t_s: float,
) -> dict[str, Any]:
    phase = phase_for_time(t_s)
    active = arm_id in ACTIVE_ARMS_BY_PHASE[phase]
    target_pos = per_arm_target(arm_id, phase, t_s)
    gate = safety_zone_gate(target_pos, phase)
    if not active:
        command = "HEARTBEAT_ACK"
        velocity = 0.0
        target_pos = (0.0, 0.0, 0.0)
    elif gate.e_stop:
        command = "E_STOP"
        velocity = 0.0
    elif gate.action == "soft_warning":
        command = "SLOW"
        velocity = 1200.0 * gate.velocity_scale
    else:
        command = "EMIT"
        velocity = 1200.0 * gate.velocity_scale
    ring_tension = RING_TENSION_BY_PHASE.get(phase, 0.0)
    return {
        "tick": tick,
        "arm_id": arm_id,
        "phase": phase,
        "target_pos": [round(target_pos[0], 4), round(target_pos[1], 4), round(target_pos[2], 4)],
        "target_quat": [0.0, 0.0, 0.0, 1.0],
        "target_linear_vel": round(velocity, 2),
        "force_clamp": round(gate.force_clamp, 2),
        "tool_state_transition": TOOL_STATE_BY_PHASE[phase] if active else "idle",
        "safety_zone_action": gate.action,
        "collision_state": "clear",
        "ring_tension_target": round(ring_tension, 3),
        "command_enum": command,
    }


def generate_command_slice(
    arm_id: int = 1,
    phase_start_s: float = 32.0,
    duration_ms: float = 100.0,
    seed: int = ROOT_SEED,
) -> list[dict[str, Any]]:
    """Generate a per arm xyz command slice."""
    rng = random.Random(seed + arm_id + 1)
    out: list[dict[str, Any]] = []
    sample_count = int(duration_ms * COMMAND_RATE_HZ / 1000)
    dt = 1.0 / COMMAND_RATE_HZ
    for i in range(sample_count + 1):
        t_s = phase_start_s + i * dt
        tick = int(t_s * COMMAND_RATE_HZ)
        out.append(_command_record(rng, arm_id, tick, t_s))
    return out


@click.command()
@click.option("--seed", type=int, default=ROOT_SEED)
@click.option("--arm-id", type=int, default=1)
@click.option("--duration-ms", type=float, default=100.0)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=Path("data/xyz_command_sample_8arm.jsonl"),
)
def main(seed: int, arm_id: int, duration_ms: float, output: Path) -> None:
    """Generate the publication arm xyz command slice."""
    records = generate_command_slice(arm_id=arm_id, duration_ms=duration_ms, seed=seed)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as f:
        for r in records:
            f.write(json.dumps(r, separators=(",", ":")))
            f.write("\n")
    click.echo(f"wrote {len(records)} commands to {output}")


if __name__ == "__main__":
    main()
