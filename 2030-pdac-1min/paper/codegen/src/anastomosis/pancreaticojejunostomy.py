"""Pancreaticojejunostomy (duct to mucosa) controller.

Runs during Phase 5 (start 32.000 s, end 42.000 s, duration 10 s).
Monitors ring tension to 0.45 N target with +/- 0.05 N tolerance, manometry
to 12 mmHg target with +/- 2 mmHg tolerance, and emits the realized grade
(A, B, or C) at the 42.000 s confirmation window.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass
from typing import Any

PHASE = 5
START_S = 32.000
END_S = 42.000
RING_TENSION_TARGET_N = 0.45
RING_TENSION_TOLERANCE_N = 0.05
MANOMETRY_TARGET_MMHG = 12.0
MANOMETRY_TOLERANCE_MMHG = 2.0
ACTIVE_ARMS = [1, 2, 3, 4, 5]

SUTURE_LAYERS = [
    {"name": "outer_layer", "count": 4, "suture": "5-0_Prolene", "start_s": 32.000, "end_s": 35.500},
    {"name": "duct_to_mucosa", "count": 8, "suture": "6-0_Prolene", "start_s": 35.500, "end_s": 39.500},
    {"name": "inner_layer", "count": 4, "suture": "5-0_Prolene", "start_s": 39.500, "end_s": 41.500},
    {"name": "confirmation_window", "start_s": 41.500, "end_s": 42.000},
]


@dataclass
class PJControllerState:
    ring_tension_rmse_n: float
    manometry_rmse_mmHg: float
    ring_violation_count: int
    manometry_violation_count: int
    realized_grade: str


def run(seed: int, perturbation_n: float = 0.0) -> dict[str, Any]:
    """Run the PJ controller across all four suture layers; return outcome record."""
    rng = random.Random(seed + 5)
    ring_target = RING_TENSION_TARGET_N + perturbation_n
    ring_samples: list[float] = []
    manometry_samples: list[float] = []
    ring_violation_count = 0
    manometry_violation_count = 0
    sample_rate_hz = 10_000
    for layer in SUTURE_LAYERS:
        n_samples = int((layer["end_s"] - layer["start_s"]) * sample_rate_hz)
        for _ in range(n_samples):
            tension = ring_target + 0.005 * (rng.random() - 0.5) * 2.0
            manometry = MANOMETRY_TARGET_MMHG + 0.2 * (rng.random() - 0.5) * 2.0
            ring_samples.append(tension)
            manometry_samples.append(manometry)
            if abs(tension - ring_target) > RING_TENSION_TOLERANCE_N:
                ring_violation_count += 1
            if abs(manometry - MANOMETRY_TARGET_MMHG) > MANOMETRY_TOLERANCE_MMHG:
                manometry_violation_count += 1
    ring_rmse = math.sqrt(
        sum((t - ring_target) ** 2 for t in ring_samples) / max(1, len(ring_samples))
    )
    manometry_rmse = math.sqrt(
        sum((m - MANOMETRY_TARGET_MMHG) ** 2 for m in manometry_samples) / max(1, len(manometry_samples))
    )
    grade_v = rng.random()
    if ring_violation_count == 0 and manometry_violation_count == 0 and grade_v < 0.92:
        grade = "A"
    elif grade_v < 0.985:
        grade = "B"
    else:
        grade = "C"
    return {
        "anastomosis_id": "pancreaticojejunostomy",
        "start_s": START_S,
        "end_s": END_S,
        "duration_s": END_S - START_S,
        "ring_tension_target_n": round(ring_target, 4),
        "ring_tension_rmse_n": round(ring_rmse, 4),
        "manometry_target_mmHg": MANOMETRY_TARGET_MMHG,
        "manometry_rmse_mmHg": round(manometry_rmse, 4),
        "ring_violation_count": ring_violation_count,
        "manometry_violation_count": manometry_violation_count,
        "realized_grade": grade,
        "active_arms": ACTIVE_ARMS,
    }
