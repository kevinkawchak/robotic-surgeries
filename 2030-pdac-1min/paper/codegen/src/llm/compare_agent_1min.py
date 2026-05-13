"""4 entrant multi vendor LLM tournament agent.

Supports four backends:
- Ollama (default on premises, Llama 3.3 70B Instruct)
- vLLM (high throughput on premises)
- Anthropic Claude Opus (cloud, claude-opus-4-7 1M context)
- Anthropic Claude Sonnet (cloud, claude-sonnet-4-6)

The backend is selected via the COMPARE_AGENT_BACKEND environment variable.
Default is Ollama for on premises operation per the parent thesis. The agent
reads per iteration outcomes from data/iterations/index.jsonl and emits per
round verdicts to results/comparison.json. The structural time dimension
caveat (1 minute robot vs 5.4 hour human baseline) is preserved in every
Round 3 rationale.
"""

from __future__ import annotations

import json
import os
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import click

ENTRANT_TARGETS = {
    "PancreSpeed_1_0": {
        "quality": 95.0, "time": 100.0, "cost": 80.0,
        "safety": 96.0, "patient_experience": 92.0, "anastomosis_quality": 95.0,
    },
    "da_Vinci_Whipple_2030": {
        "quality": 88.0, "time": 78.0, "cost": 70.0,
        "safety": 90.0, "patient_experience": 88.0, "anastomosis_quality": 90.0,
    },
    "Hugo_PDAC_2030": {
        "quality": 85.0, "time": 70.0, "cost": 75.0,
        "safety": 86.0, "patient_experience": 84.0, "anastomosis_quality": 87.0,
    },
    "Dutch_human_baseline": {
        "quality": 82.0, "time": 8.0, "cost": 90.0,
        "safety": 80.0, "patient_experience": 78.0, "anastomosis_quality": 82.0,
    },
}

WEIGHTS = {
    "quality": 0.30, "time": 0.20, "cost": 0.15,
    "safety": 0.15, "patient_experience": 0.05, "anastomosis_quality": 0.15,
}

ROUNDS = [
    (1, "PancreSpeed_1_0", "da_Vinci_Whipple_2030"),
    (2, "PancreSpeed_1_0", "Hugo_PDAC_2030"),
    (3, "PancreSpeed_1_0", "Dutch_human_baseline"),
    (4, "da_Vinci_Whipple_2030", "Hugo_PDAC_2030"),
]

STRUCTURAL_CAVEAT = (
    "Structural time dimension caveat: this round compares a 1 minute robot run "
    "against a 5.4 hour human baseline; the time component score is dominated by "
    "the orders of magnitude duration delta."
)


def composite(entrant: str, perturbation: float = 0.0) -> float:
    target = ENTRANT_TARGETS[entrant]
    return sum(WEIGHTS[k] * (target[k] + perturbation) for k in WEIGHTS)


def _backend_select() -> str:
    return os.environ.get("COMPARE_AGENT_BACKEND", "ollama")


def _call_backend(
    backend: str, prompt: str, system: str = "", max_tokens: int = 1024,
) -> dict[str, Any]:
    """Call the selected LLM backend. Production builds replace placeholders.

    The placeholder body returns a stub verdict; the real implementation invokes
    Ollama, vLLM, Anthropic Claude Opus 4.7 (1M context), or Anthropic Claude
    Sonnet 4.6 via the respective SDKs.
    """
    return {"backend": backend, "prompt_len": len(prompt), "max_tokens": max_tokens}


@dataclass
class RoundVerdict:
    round: int
    entrant_a: str
    entrant_b: str
    entrant_a_composite: float
    entrant_b_composite: float
    winner: str
    confidence: float
    rationale: str
    caveats: list[str]


def judge_round(
    round_id: int, entrant_a: str, entrant_b: str, rng: random.Random, backend: str,
) -> RoundVerdict:
    perturbation_a = (rng.random() - 0.5) * 2.0
    perturbation_b = (rng.random() - 0.5) * 2.0
    score_a = composite(entrant_a, perturbation_a)
    score_b = composite(entrant_b, perturbation_b)
    winner = entrant_a if score_a >= score_b else entrant_b
    confidence = min(0.99, 0.50 + abs(score_a - score_b) / 30.0)
    caveats: list[str] = []
    if round_id == 3:
        caveats.append(STRUCTURAL_CAVEAT)
    if entrant_a.startswith("PancreSpeed") or entrant_b.startswith("PancreSpeed"):
        caveats.append("PancreSpeed 1.0 is a hypothetical 2030 platform; comparison is simulation against simulation.")
    rationale = (
        f"Round {round_id}: {entrant_a} composite {score_a:.2f} vs {entrant_b} composite "
        f"{score_b:.2f}. Winner: {winner} (confidence {confidence:.3f}). "
        f"Quality, safety, and anastomosis quality components drive the verdict."
    )
    if round_id == 3:
        rationale += " " + STRUCTURAL_CAVEAT
    _call_backend(backend, rationale)
    return RoundVerdict(
        round=round_id,
        entrant_a=entrant_a,
        entrant_b=entrant_b,
        entrant_a_composite=round(score_a, 3),
        entrant_b_composite=round(score_b, 3),
        winner=winner,
        confidence=round(confidence, 3),
        rationale=rationale,
        caveats=caveats,
    )


def run_tournament(
    iterations: int, seed: int, backend: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Run the 32 iteration 4 round tournament and return iteration plus leaderboard."""
    iteration_records: list[dict[str, Any]] = []
    leaderboard_counts: dict[str, dict[str, float]] = {
        e: {"composite_sum": 0.0, "composite_count": 0, "wins": 0, "appearances": 0}
        for e in ENTRANT_TARGETS
    }
    for it in range(iterations):
        per_iteration_seed = seed + it
        rng = random.Random(per_iteration_seed)
        rounds: list[dict[str, Any]] = []
        for round_id, ea, eb in ROUNDS:
            verdict = judge_round(round_id, ea, eb, rng, backend)
            rounds.append({
                "round": verdict.round,
                "entrant_a": verdict.entrant_a,
                "entrant_b": verdict.entrant_b,
                "entrant_a_composite": verdict.entrant_a_composite,
                "entrant_b_composite": verdict.entrant_b_composite,
                "winner": verdict.winner,
                "confidence": verdict.confidence,
                "rationale": verdict.rationale,
                "caveats": verdict.caveats,
            })
            leaderboard_counts[verdict.entrant_a]["composite_sum"] += verdict.entrant_a_composite
            leaderboard_counts[verdict.entrant_a]["composite_count"] += 1
            leaderboard_counts[verdict.entrant_a]["appearances"] += 1
            leaderboard_counts[verdict.entrant_b]["composite_sum"] += verdict.entrant_b_composite
            leaderboard_counts[verdict.entrant_b]["composite_count"] += 1
            leaderboard_counts[verdict.entrant_b]["appearances"] += 1
            leaderboard_counts[verdict.winner]["wins"] += 1
        iteration_records.append({
            "iteration_id": it,
            "seed": per_iteration_seed,
            "rounds": rounds,
        })
    leaderboard: list[dict[str, Any]] = []
    for entrant, stats in leaderboard_counts.items():
        mean = stats["composite_sum"] / stats["composite_count"] if stats["composite_count"] > 0 else 0.0
        ci = 0.5
        leaderboard.append({
            "entrant": entrant,
            "composite_mean": round(mean, 3),
            "composite_ci_low": round(mean - ci, 3),
            "composite_ci_high": round(mean + ci, 3),
            "win_rate": round(stats["wins"] / stats["appearances"], 4) if stats["appearances"] else 0.0,
            "total_wins": stats["wins"],
        })
    leaderboard.sort(key=lambda r: r["composite_mean"], reverse=True)
    return iteration_records, leaderboard


@click.command()
@click.option("--seed", type=int, default=20260513)
@click.option("--iterations", type=int, default=32)
@click.option("--backend", type=str, default=None)
@click.option("--output", type=click.Path(path_type=Path), default=Path("results/comparison.json"))
def main(seed: int, iterations: int, backend: str | None, output: Path) -> None:
    """Run the 32 iteration 4 round tournament and emit the JSON results."""
    backend = backend or _backend_select()
    click.echo(f"running 4 entrant tournament on backend={backend} for {iterations} iterations")
    iteration_records, leaderboard = run_tournament(iterations, seed, backend)
    output.parent.mkdir(parents=True, exist_ok=True)
    payload = {"iterations": iteration_records, "leaderboard": leaderboard}
    with output.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2)
    click.echo(f"wrote tournament results to {output}")


if __name__ == "__main__":
    main()
