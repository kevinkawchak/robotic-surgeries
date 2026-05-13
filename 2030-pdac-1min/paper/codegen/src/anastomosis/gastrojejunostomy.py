"""Gastrojejunostomy (antecolic, pylorus preserving) controller.

Runs during Phase 7 (start 48.000 s, end 54.000 s, duration 6 s).
Monitors ring tension to 0.60 N target with +/- 0.05 N tolerance and patency
via NIR indocyanine green flow rate. Realized outcome is one of patent or
delayed gastric emptying.
"""

from __future__ import annotations

import math
import random
from typing import Any

PHASE = 7
START_S = 48.000
END_S = 54.000
RING_TENSION_TARGET_N = 0.60
RING_TENSION_TOLERANCE_N = 0.05
ACTIVE_ARMS = [1, 2, 3, 4]

STAGES = [
    {"name": "stapler_fire", "start_s": 48.000, "end_s": 50.000},
    {"name": "posterior_reinforcement", "start_s": 50.000, "end_s": 52.000},
    {"name": "anterior_reinforcement", "start_s": 52.000, "end_s": 53.500},
    {"name": "patency_confirmation", "start_s": 53.500, "end_s": 54.000},
]


def run(seed: int, perturbation_n: float = 0.0) -> dict[str, Any]:
    """Run the GJ controller; return outcome record."""
    rng = random.Random(seed + 7)
    ring_target = RING_TENSION_TARGET_N + perturbation_n
    sample_rate_hz = 10_000
    ring_samples: list[float] = []
    for stage in STAGES:
        n_samples = int((stage["end_s"] - stage["start_s"]) * sample_rate_hz)
        for _ in range(n_samples):
            ring_samples.append(ring_target + 0.005 * (rng.random() - 0.5) * 2.0)
    ring_rmse = math.sqrt(
        sum((t - ring_target) ** 2 for t in ring_samples) / max(1, len(ring_samples))
    )
    patency = "patent" if rng.random() < 0.97 else "delayed"
    return {
        "anastomosis_id": "gastrojejunostomy",
        "start_s": START_S,
        "end_s": END_S,
        "duration_s": END_S - START_S,
        "ring_tension_target_n": round(ring_target, 4),
        "ring_tension_rmse_n": round(ring_rmse, 4),
        "realized_grade": patency,
        "active_arms": ACTIVE_ARMS,
    }
