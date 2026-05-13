"""LLM bound advisory layer for postoperative Daraxonrasib restart timing.

The advisory is produced at the 60 second mark of the simulation and is
recorded in results/daraxonrasib_advisory.json. The advisory is a software
function under the FDA SaMD framework. The advisory is not a clinical
decision; it is a recommendation that a board certified oncologist reviews
before any actual Daraxonrasib restart.
"""

from __future__ import annotations

import json
import os
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any

import click


@dataclass
class AdvisoryInputs:
    iteration_id: int
    realized_frs: float
    pj_grade: str
    hj_leak: str
    gj_patency: str
    max_force_time_integral_ns: float
    intra_op_event_count: int


@dataclass
class Advisory:
    iteration_id: int
    recommended_restart_day: int
    rationale: str
    caveats: list[str]


def build_advisory(inputs: AdvisoryInputs) -> Advisory:
    """Apply the decision logic to build a per iteration advisory."""
    caveats = [
        "FDA SaMD framework: this advisory is a software function intended to support a board certified oncologist; not a clinical decision.",
        "Daraxonrasib is paused 72 hours pre op per RASolute 302 protocol; intra op serum is at the trough below 0.5 ng/mL.",
    ]
    high_force = inputs.max_force_time_integral_ns > 8.0
    high_frs = inputs.realized_frs >= 8
    complicated = (
        inputs.pj_grade in ("B", "C")
        or inputs.hj_leak == "present"
        or inputs.gj_patency == "delayed"
        or inputs.intra_op_event_count > 0
    )
    if high_force or high_frs:
        day = 21
        rationale = (
            f"Iteration {inputs.iteration_id}: per arm force time integral "
            f"{inputs.max_force_time_integral_ns:.3f} N.s and realized FRS {inputs.realized_frs:.1f} "
            "trigger an extended pause and multi disciplinary review. Recommend T+21d Daraxonrasib "
            "restart with review by surgical oncology, medical oncology, and hepatobiliary surgery."
        )
        caveats.append("Multi disciplinary review required before any actual Daraxonrasib restart.")
    elif complicated:
        day = 14
        rationale = (
            f"Iteration {inputs.iteration_id}: realized PJ grade {inputs.pj_grade}, HJ leak "
            f"{inputs.hj_leak}, GJ patency {inputs.gj_patency}, and "
            f"{inputs.intra_op_event_count} intra op events indicate complicated recovery. "
            "Recommend T+14d Daraxonrasib restart per RASolute 302 perioperative pause protocol."
        )
    else:
        day = 7
        rationale = (
            f"Iteration {inputs.iteration_id}: realized PJ grade A, HJ leak absent, GJ patent, "
            "and no intra op events indicate uncomplicated recovery. Recommend T+7d Daraxonrasib "
            "restart per RASolute 302 perioperative pause protocol."
        )
    return Advisory(
        iteration_id=inputs.iteration_id,
        recommended_restart_day=day,
        rationale=rationale,
        caveats=caveats,
    )


@click.command()
@click.option(
    "--input-index",
    type=click.Path(path_type=Path),
    default=Path("data/iterations/index.jsonl"),
)
@click.option(
    "--output",
    type=click.Path(path_type=Path),
    default=Path("results/daraxonrasib_advisory.json"),
)
def main(input_index: Path, output: Path) -> None:
    """Emit per iteration postoperative Daraxonrasib restart advisories."""
    advisories: list[dict[str, Any]] = []
    if not input_index.exists():
        click.echo(f"index not found at {input_index}")
        return
    with input_index.open("r", encoding="utf-8") as f:
        for line in f:
            r = json.loads(line)
            inputs = AdvisoryInputs(
                iteration_id=r["iteration_id"],
                realized_frs=r.get("realized_frs", 5.0),
                pj_grade=r.get("realized_pj_grade", "A"),
                hj_leak=r.get("realized_hj_leak", "absent"),
                gj_patency=r.get("realized_gj_patency", "patent"),
                max_force_time_integral_ns=r.get("max_force_time_integral_ns", 4.0),
                intra_op_event_count=r.get("intra_op_event_count", 0),
            )
            advisories.append(asdict(build_advisory(inputs)))
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as f:
        json.dump({"advisories": advisories}, f, indent=2)
    click.echo(f"wrote {len(advisories)} advisories to {output}")


if __name__ == "__main__":
    main()
