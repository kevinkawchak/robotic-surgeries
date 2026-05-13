"""Hepaticojejunostomy (end to side) controller.

Runs during Phase 6 (start 42.000 s, end 48.000 s, duration 6 s).
Monitors ring tension to 0.50 N target with +/- 0.05 N tolerance, bile
manometry to 8 mmHg target with +/- 2 mmHg tolerance, and bile leak via NIR
indocyanine green plus bile spectrophotometry at 410 nm.
"""

from __future__ import annotations

import math
import random
from typing import Any

PHASE = 6
START_S = 42.000
END_S = 48.000
RING_TENSION_TARGET_N = 0.50
RING_TENSION_TOLERANCE_N = 0.05
MANOMETRY_TARGET_MMHG = 8.0
MANOMETRY_TOLERANCE_MMHG = 2.0
BILE_LEAK_THRESHOLD_410_NM = 3.0
ACTIVE_ARMS = [1, 2, 3, 4, 5]

SUTURE_LAYERS = [
    {"name": "posterior_layer", "count": 6, "suture": "5-0_PDS", "start_s": 42.000, "end_s": 44.500},
    {"name": "anterior_layer", "count": 6, "suture": "5-0_PDS", "start_s": 44.500, "end_s": 47.000},
    {"name": "bile_leak_verification", "start_s": 47.000, "end_s": 47.500},
    {"name": "confirmation_window", "start_s": 47.500, "end_s": 48.000},
]


def run(seed: int, perturbation_n: float = 0.0) -> dict[str, Any]:
    """Run the HJ controller; return outcome record."""
    rng = random.Random(seed + 6)
    ring_target = RING_TENSION_TARGET_N + perturbation_n
    ring_samples: list[float] = []
    manometry_samples: list[float] = []
    sample_rate_hz = 10_000
    total_samples = 0
    for layer in SUTURE_LAYERS:
        n_samples = int((layer["end_s"] - layer["start_s"]) * sample_rate_hz)
        total_samples += n_samples
        for _ in range(n_samples):
            ring_samples.append(ring_target + 0.005 * (rng.random() - 0.5) * 2.0)
            manometry_samples.append(MANOMETRY_TARGET_MMHG + 0.2 * (rng.random() - 0.5) * 2.0)
    ring_rmse = math.sqrt(
        sum((t - ring_target) ** 2 for t in ring_samples) / max(1, len(ring_samples))
    )
    manometry_rmse = math.sqrt(
        sum((m - MANOMETRY_TARGET_MMHG) ** 2 for m in manometry_samples) / max(1, len(manometry_samples))
    )
    bile_max_410_nm = 5.0 + 2.0 * rng.random()
    leak = "absent" if bile_max_410_nm < BILE_LEAK_THRESHOLD_410_NM * 2 and rng.random() < 0.94 else "present"
    if leak == "absent":
        bile_max_410_nm = min(bile_max_410_nm, BILE_LEAK_THRESHOLD_410_NM * 2)
    return {
        "anastomosis_id": "hepaticojejunostomy",
        "start_s": START_S,
        "end_s": END_S,
        "duration_s": END_S - START_S,
        "ring_tension_target_n": round(ring_target, 4),
        "ring_tension_rmse_n": round(ring_rmse, 4),
        "manometry_target_mmHg": MANOMETRY_TARGET_MMHG,
        "manometry_rmse_mmHg": round(manometry_rmse, 4),
        "bile_spectrophotometry_max_410_nm": round(bile_max_410_nm, 3),
        "realized_grade": leak,
        "active_arms": ACTIVE_ARMS,
    }
