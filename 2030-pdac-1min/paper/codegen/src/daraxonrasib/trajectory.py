"""Daraxonrasib perioperative trajectory.

The RASolute 302 perioperative protocol pauses Daraxonrasib 72 hours before
any major surgical procedure and restarts 7 days postoperatively (uncomplicated)
or 14 days postoperatively (complicated). The trajectory is identical across
all 32 iterations and is part of the deterministic seed contract.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import click

HALF_LIFE_HOURS = 36.0
INDUCTION_DOSE_MG = 300.0
STEADY_STATE_SERUM_NG_PER_ML = 35.0
TROUGH_THRESHOLD_NG_PER_ML = 0.5

TRAJECTORY_POINTS = [
    {"t_relative_to_surgery": "T-30d", "dose_mg": 300.0, "serum_ng_per_ml": 35.0, "action": "induction"},
    {"t_relative_to_surgery": "T-72h", "dose_mg": 0.0, "serum_ng_per_ml": 35.0, "action": "pause"},
    {"t_relative_to_surgery": "T-36h", "dose_mg": 0.0, "serum_ng_per_ml": 17.5, "action": "one_half_life_washout"},
    {"t_relative_to_surgery": "T-12h", "dose_mg": 0.0, "serum_ng_per_ml": 6.0, "action": "two_half_life_washout"},
    {"t_relative_to_surgery": "T 0", "dose_mg": 0.0, "serum_ng_per_ml": 0.45, "action": "surgery_begins"},
    {"t_relative_to_surgery": "T+60s", "dose_mg": 0.0, "serum_ng_per_ml": 0.45, "action": "surgery_ends"},
    {"t_relative_to_surgery": "T+7d_if_uncomplicated", "dose_mg": 300.0, "serum_ng_per_ml": 35.0, "action": "restart"},
    {"t_relative_to_surgery": "T+14d_if_complicated", "dose_mg": 300.0, "serum_ng_per_ml": 35.0, "action": "delayed_restart"},
]


@dataclass
class IterationTrajectory:
    iteration_id: int
    seed: int
    induction_dose_mg: float
    induction_serum_ng_per_ml: float
    t_minus_72h_pause_applied: bool
    t_zero_serum_ng_per_ml: float
    t_plus_60s_serum_ng_per_ml: float


def serum_at_time(t_hours_relative_to_pause: float, induction_serum: float = 35.0) -> float:
    """Compute serum concentration via 1 compartment exponential decay."""
    if t_hours_relative_to_pause < 0:
        return induction_serum
    k = math.log(2) / HALF_LIFE_HOURS
    return induction_serum * math.exp(-k * t_hours_relative_to_pause)


def build_iteration_trajectory(
    iteration_id: int, seed: int, induction_serum_ng_per_ml: float = STEADY_STATE_SERUM_NG_PER_ML,
) -> IterationTrajectory:
    """Build a per iteration perioperative trajectory."""
    t_zero_serum = serum_at_time(72.0, induction_serum_ng_per_ml)
    t_plus_60s_serum = serum_at_time(72.0 + (60.0 / 3600.0), induction_serum_ng_per_ml)
    return IterationTrajectory(
        iteration_id=iteration_id,
        seed=seed,
        induction_dose_mg=INDUCTION_DOSE_MG,
        induction_serum_ng_per_ml=induction_serum_ng_per_ml,
        t_minus_72h_pause_applied=True,
        t_zero_serum_ng_per_ml=round(t_zero_serum, 3),
        t_plus_60s_serum_ng_per_ml=round(t_plus_60s_serum, 3),
    )


@click.command()
@click.option("--seed", type=int, default=20260513)
@click.option("--iterations", type=int, default=32)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=Path("data/iterations/daraxonrasib_trajectory.csv"),
)
def main(seed: int, iterations: int, output: Path) -> None:
    """Generate per iteration perioperative trajectory records."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow([
            "iteration_id", "seed", "induction_dose_mg", "induction_serum_ng_per_ml",
            "t_minus_72h_pause_applied", "t_zero_serum_ng_per_ml",
            "t_plus_60s_serum_ng_per_ml",
        ])
        for i in range(iterations):
            traj = build_iteration_trajectory(i, seed + i)
            w.writerow([
                traj.iteration_id, traj.seed, traj.induction_dose_mg,
                traj.induction_serum_ng_per_ml, traj.t_minus_72h_pause_applied,
                traj.t_zero_serum_ng_per_ml, traj.t_plus_60s_serum_ng_per_ml,
            ])
    click.echo(f"wrote {iterations} trajectories to {output}")


if __name__ == "__main__":
    main()
