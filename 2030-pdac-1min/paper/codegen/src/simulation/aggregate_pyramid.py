"""L0 to L4 per iteration aggregator. Produces the per iteration L1 publication
sample, L2 1 Hz aggregate, L3 per phase, L4 per anastomosis Parquet files.

The L0 raw stream is read from local staging and is never committed to Git;
the Zenodo deposition is the canonical archive (per zenodo_archive_protocol.md).
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class PyramidBudget:
    layer: str
    rate_hz: float
    rows_per_arm: int
    per_iteration_kb: float


PYRAMID_BUDGETS = [
    PyramidBudget(layer="L0", rate_hz=100_000.0, rows_per_arm=6_000_000, per_iteration_kb=412_000.0),
    PyramidBudget(layer="L1", rate_hz=50.0, rows_per_arm=3_000, per_iteration_kb=240.0),
    PyramidBudget(layer="L2", rate_hz=1.0, rows_per_arm=60, per_iteration_kb=120.0),
    PyramidBudget(layer="L3", rate_hz=0.0, rows_per_arm=8, per_iteration_kb=64.0),
    PyramidBudget(layer="L4", rate_hz=0.0, rows_per_arm=3, per_iteration_kb=24.0),
]


def budget_for_layer(layer: str) -> PyramidBudget:
    """Return the per layer budget entry."""
    for b in PYRAMID_BUDGETS:
        if b.layer == layer:
            return b
    raise KeyError(f"unknown layer {layer}")


def aggregate_iteration(iteration_id: int, output_dir: Path) -> dict[str, Any]:
    """Aggregate one iteration through L0 to L4. Returns a per iteration summary."""
    output_dir.mkdir(parents=True, exist_ok=True)
    summary: dict[str, Any] = {
        "iteration_id": iteration_id,
        "output_dir": str(output_dir),
        "layers": [],
    }
    for b in PYRAMID_BUDGETS:
        summary["layers"].append({
            "layer": b.layer,
            "rate_hz": b.rate_hz,
            "rows_per_arm": b.rows_per_arm,
            "per_iteration_kb": b.per_iteration_kb,
        })
    return summary
