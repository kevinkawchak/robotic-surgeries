"""6 component composite score for the PDAC 1 minute per iteration outcome.

Weights are frozen across all 32 iterations and across all 4 tournament
entrants. The score is computed by combining the per iteration realized
outcomes (anastomosis grade, force exposure, time, cost, patient experience).
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import click

WEIGHTS = {
    "quality": 0.30,
    "time": 0.20,
    "cost": 0.15,
    "safety": 0.15,
    "patient_experience": 0.05,
    "anastomosis_quality": 0.15,
}


@dataclass
class CompositeRecord:
    iteration_id: int
    seed: int
    quality: float
    time: float
    cost: float
    safety: float
    patient_experience: float
    anastomosis_quality: float
    composite_score: float


def composite_score(
    quality: float,
    time: float,
    cost: float,
    safety: float,
    patient_experience: float,
    anastomosis_quality: float,
) -> float:
    """Apply the frozen composite score weights and return a 0 to 100 scalar."""
    components = {
        "quality": quality,
        "time": time,
        "cost": cost,
        "safety": safety,
        "patient_experience": patient_experience,
        "anastomosis_quality": anastomosis_quality,
    }
    return sum(WEIGHTS[k] * components[k] for k in WEIGHTS)


def compute_from_iteration_record(record: dict[str, Any]) -> CompositeRecord:
    """Build a CompositeRecord from a per iteration outcome dict."""
    return CompositeRecord(
        iteration_id=record["iteration_id"],
        seed=record["seed"],
        quality=record["quality"],
        time=record["time"],
        cost=record["cost"],
        safety=record["safety"],
        patient_experience=record["patient_experience"],
        anastomosis_quality=record["anastomosis_quality"],
        composite_score=composite_score(
            record["quality"], record["time"], record["cost"],
            record["safety"], record["patient_experience"], record["anastomosis_quality"],
        ),
    )


@click.command()
@click.option(
    "--input-index",
    type=click.Path(path_type=Path, exists=False),
    default=Path("data/iterations/index.jsonl"),
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=Path("outputs/metrics/composite_scores.jsonl"),
)
def main(input_index: Path, output: Path) -> None:
    """Read the per iteration index and emit composite score records."""
    if not input_index.exists():
        click.echo(f"index not found at {input_index}; run iterate_1min first")
        return
    output.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with input_index.open("r", encoding="utf-8") as f_in, output.open("w", encoding="utf-8") as f_out:
        for line in f_in:
            r = json.loads(line)
            if "composite_score" in r:
                f_out.write(json.dumps({"iteration_id": r["iteration_id"], "composite_score": r["composite_score"]}, separators=(",", ":")))
                f_out.write("\n")
                n += 1
    click.echo(f"wrote {n} composite score records to {output}")


if __name__ == "__main__":
    main()
