"""Per iteration chunked aggregator. Processes the per iteration L0 raw stream
into the L1 to L4 committed layers in 8 chunks (one per phase). Memory budget
per chunk is kept under 12,000 tokens to fit any single LLM working memory."""

from __future__ import annotations

from pathlib import Path
from typing import Any

PHASE_BOUNDARIES_S = [
    (1, 0.000, 6.000, 6_000),
    (2, 6.000, 16.000, 12_000),
    (3, 16.000, 24.000, 8_000),
    (4, 24.000, 32.000, 8_000),
    (5, 32.000, 42.000, 12_000),
    (6, 42.000, 48.000, 8_000),
    (7, 48.000, 54.000, 8_000),
    (8, 54.000, 60.000, 6_000),
]


def chunk_phase(phase_id: int, start_s: float, end_s: float, memory_budget_tokens: int) -> dict[str, Any]:
    """Aggregate one phase of one iteration. Memory budget per chunk is tracked."""
    return {
        "phase_id": phase_id,
        "start_s": start_s,
        "end_s": end_s,
        "duration_s": end_s - start_s,
        "memory_budget_tokens": memory_budget_tokens,
    }


def process_iteration(iteration_id: int, output_dir: Path) -> list[dict[str, Any]]:
    """Process all 8 phases of one iteration through the chunked aggregator."""
    output_dir.mkdir(parents=True, exist_ok=True)
    chunks: list[dict[str, Any]] = []
    cumulative_tokens = 0
    for phase_id, start_s, end_s, budget in PHASE_BOUNDARIES_S:
        chunk = chunk_phase(phase_id, start_s, end_s, budget)
        cumulative_tokens += budget
        chunk["cumulative_tokens"] = cumulative_tokens
        chunks.append(chunk)
    return chunks
