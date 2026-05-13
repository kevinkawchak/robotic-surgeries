"""Vascular safety zone gate.

Reads per arm tip position from the sensor stream at 10 kHz and applies the 5
vessel safety zone gate per phase. Defends in depth against the 100 kHz vessel
surface proximity sensor, which can trigger the per arm e stop at one tick
latency (10 microseconds) if the tip position breaches the hard stop volume.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

VESSELS = [
    {
        "name": "superior_mesenteric_vein",
        "centerline_start": (15.0, -25.0, -45.0),
        "centerline_end": (15.0, -65.0, -55.0),
        "hard_stop_r": 2.0,
        "soft_warning_r": 4.0,
        "no_fly_r": 6.0,
        "active_phases": {2, 4, 5, 8},
    },
    {
        "name": "portal_vein",
        "centerline_start": (5.0, -55.0, -55.0),
        "centerline_end": (5.0, -75.0, -50.0),
        "hard_stop_r": 2.0,
        "soft_warning_r": 4.0,
        "no_fly_r": 6.0,
        "active_phases": {2, 4, 5, 8},
    },
    {
        "name": "hepatic_artery_common",
        "centerline_start": (5.0, -60.0, -50.0),
        "centerline_end": (20.0, -65.0, -55.0),
        "hard_stop_r": 1.5,
        "soft_warning_r": 3.0,
        "no_fly_r": 5.0,
        "active_phases": {2, 4, 6, 8},
    },
    {
        "name": "celiac_axis",
        "centerline_start": (0.0, -65.0, -60.0),
        "centerline_end": (5.0, -70.0, -55.0),
        "hard_stop_r": 1.5,
        "soft_warning_r": 3.0,
        "no_fly_r": 5.0,
        "active_phases": {3, 4, 8},
    },
    {
        "name": "superior_mesenteric_artery",
        "centerline_start": (0.0, -35.0, -55.0),
        "centerline_end": (5.0, -65.0, -60.0),
        "hard_stop_r": 1.5,
        "soft_warning_r": 3.0,
        "no_fly_r": 5.0,
        "active_phases": {3, 4, 8},
    },
]

ACTIONS = {
    "clear": {"velocity_scale": 1.0, "force_soft_cap_n": 3.0, "e_stop": False},
    "no_fly": {"velocity_scale": 0.5, "force_soft_cap_n": 2.5, "e_stop": False},
    "soft_warning": {"velocity_scale": 0.1, "force_soft_cap_n": 1.5, "e_stop": False},
    "hard_stop": {"velocity_scale": 0.0, "force_soft_cap_n": 0.0, "e_stop": True},
}


@dataclass
class GateResult:
    vessel: str
    distance_mm: float
    action: str
    velocity_scale: float
    force_soft_cap_n: float
    e_stop: bool


def _distance_to_segment(
    p: tuple[float, float, float],
    a: tuple[float, float, float],
    b: tuple[float, float, float],
) -> float:
    """L2 distance from a point to a line segment in 3D."""
    ax, ay, az = a
    bx, by, bz = b
    px, py, pz = p
    abx, aby, abz = bx - ax, by - ay, bz - az
    apx, apy, apz = px - ax, py - ay, pz - az
    ab2 = abx * abx + aby * aby + abz * abz
    if ab2 == 0.0:
        dx, dy, dz = px - ax, py - ay, pz - az
        return math.sqrt(dx * dx + dy * dy + dz * dz)
    t = max(0.0, min(1.0, (apx * abx + apy * aby + apz * abz) / ab2))
    cx, cy, cz = ax + t * abx, ay + t * aby, az + t * abz
    dx, dy, dz = px - cx, py - cy, pz - cz
    return math.sqrt(dx * dx + dy * dy + dz * dz)


def gate(tip_pos: tuple[float, float, float], phase: int) -> GateResult:
    """Compute the safety zone action for a tip position in a given phase."""
    nearest_action = "clear"
    nearest_vessel = "none"
    nearest_distance = 1e9
    for v in VESSELS:
        if phase not in v["active_phases"]:
            continue
        d = _distance_to_segment(tip_pos, v["centerline_start"], v["centerline_end"])
        if d <= v["hard_stop_r"]:
            action = ACTIONS["hard_stop"]
            return GateResult(v["name"], d, "hard_stop", action["velocity_scale"], action["force_soft_cap_n"], action["e_stop"])
        if d <= v["soft_warning_r"] and nearest_action != "soft_warning":
            nearest_action = "soft_warning"
            nearest_vessel = v["name"]
            nearest_distance = d
        elif d <= v["no_fly_r"] and nearest_action == "clear":
            nearest_action = "no_fly"
            nearest_vessel = v["name"]
            nearest_distance = d
        if d < nearest_distance and nearest_action == "clear":
            nearest_distance = d
            nearest_vessel = v["name"]
    action = ACTIONS[nearest_action]
    return GateResult(nearest_vessel, nearest_distance, nearest_action, action["velocity_scale"], action["force_soft_cap_n"], action["e_stop"])


def evaluate_path(
    path: list[tuple[float, float, float]], phase: int,
) -> list[GateResult]:
    """Evaluate the safety zone gate over a path of tip positions."""
    return [gate(p, phase) for p in path]
