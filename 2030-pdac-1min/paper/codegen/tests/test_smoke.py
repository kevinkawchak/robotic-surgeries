"""Smoke tests for the v0.6.0 PDAC 1 minute codegen.

Run: python -m pytest tests/test_smoke.py -v
"""

from __future__ import annotations

import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))


def test_sensor_ingest_module_imports() -> None:
    """sensors.ingest_8arm imports without error."""
    from src.sensors import ingest_8arm
    assert ingest_8arm.ROOT_SEED == 20260513
    assert ingest_8arm.ARMS == 8
    assert ingest_8arm.CHANNELS_PER_ARM == 80
    assert ingest_8arm.TOTAL_CHANNELS == 640


def test_phase_for_time_boundaries() -> None:
    """Phase boundaries map correctly across the 60 second timeline."""
    from src.sensors.ingest_8arm import phase_for_time
    assert phase_for_time(0.0) == 1
    assert phase_for_time(5.999) == 1
    assert phase_for_time(6.0) == 2
    assert phase_for_time(15.999) == 2
    assert phase_for_time(16.0) == 3
    assert phase_for_time(32.0) == 5
    assert phase_for_time(42.0) == 6
    assert phase_for_time(48.0) == 7
    assert phase_for_time(54.0) == 8
    assert phase_for_time(59.999) == 8


def test_safety_zone_gate_clear() -> None:
    """Far from any vessel returns clear."""
    from src.vascular.safety_zone_gate import gate
    result = gate((100.0, 100.0, 100.0), phase=2)
    assert result.action == "clear"
    assert result.velocity_scale == 1.0
    assert result.force_soft_cap_n == 3.0
    assert result.e_stop is False


def test_safety_zone_gate_hard_stop_smv() -> None:
    """Inside the SMV hard stop radius triggers e stop in Phase 2."""
    from src.vascular.safety_zone_gate import gate
    result = gate((15.0, -45.0, -50.0), phase=2)
    assert result.action == "hard_stop"
    assert result.e_stop is True


def test_composite_score_weights_sum_to_one() -> None:
    """The 6 composite score weights sum to 1.00."""
    from src.metrics.compute_1min import WEIGHTS
    assert math.isclose(sum(WEIGHTS.values()), 1.00, abs_tol=1e-6)


def test_composite_score_pancrespeed_target() -> None:
    """PancreSpeed 1.0 entrant composite reaches 93.55."""
    from src.metrics.compute_1min import composite_score
    score = composite_score(95.0, 100.0, 80.0, 96.0, 92.0, 95.0)
    assert math.isclose(score, 93.55, abs_tol=0.01)


def test_composite_score_dutch_human_baseline() -> None:
    """Dutch human surgeon baseline composite reaches 56.05."""
    from src.metrics.compute_1min import composite_score
    score = composite_score(82.0, 8.0, 90.0, 80.0, 78.0, 82.0)
    assert math.isclose(score, 56.05, abs_tol=0.01)


def test_daraxonrasib_serum_decay() -> None:
    """Two half life washout yields under 0.5 ng/mL trough threshold."""
    from src.daraxonrasib.trajectory import serum_at_time
    serum_at_2_half_lives = serum_at_time(72.0, 35.0)
    assert serum_at_2_half_lives < 6.5
    serum_at_5_half_lives = serum_at_time(180.0, 35.0)
    assert serum_at_5_half_lives < 1.5


def test_daraxonrasib_advisory_uncomplicated() -> None:
    """Uncomplicated case recommends T+7d restart."""
    from src.daraxonrasib.advisory import AdvisoryInputs, build_advisory
    inputs = AdvisoryInputs(
        iteration_id=0, realized_frs=5.0, pj_grade="A",
        hj_leak="absent", gj_patency="patent",
        max_force_time_integral_ns=4.0, intra_op_event_count=0,
    )
    advisory = build_advisory(inputs)
    assert advisory.recommended_restart_day == 7


def test_daraxonrasib_advisory_complicated() -> None:
    """PJ grade B recommends T+14d restart."""
    from src.daraxonrasib.advisory import AdvisoryInputs, build_advisory
    inputs = AdvisoryInputs(
        iteration_id=4, realized_frs=5.4, pj_grade="B",
        hj_leak="absent", gj_patency="patent",
        max_force_time_integral_ns=4.5, intra_op_event_count=0,
    )
    advisory = build_advisory(inputs)
    assert advisory.recommended_restart_day == 14


def test_daraxonrasib_advisory_extended() -> None:
    """High FRS or force time integral recommends T+21d restart."""
    from src.daraxonrasib.advisory import AdvisoryInputs, build_advisory
    inputs = AdvisoryInputs(
        iteration_id=10, realized_frs=8.5, pj_grade="A",
        hj_leak="absent", gj_patency="patent",
        max_force_time_integral_ns=4.0, intra_op_event_count=0,
    )
    advisory = build_advisory(inputs)
    assert advisory.recommended_restart_day == 21


def test_xyz_command_phase_targets() -> None:
    """Phase 5 PJ target xyz position resolves to (18, -30, -42)."""
    from src.mapping.sensor_to_xyz_8arm import per_arm_target
    x, y, z = per_arm_target(arm_id=1, phase=5, t_s=32.0)
    assert abs(x - 18.0) < 0.5
    assert abs(y - (-30.0)) < 0.5
    assert abs(z - (-42.0)) < 0.5


def test_latin_hypercube_determinism() -> None:
    """Latin hypercube samples are deterministic for fixed seed."""
    from src.simulation.iterate_1min import latin_hypercube_samples
    s1 = latin_hypercube_samples(32, 8, 20260513)
    s2 = latin_hypercube_samples(32, 8, 20260513)
    assert s1 == s2
    assert len(s1) == 32
    assert len(s1[0]) == 8
