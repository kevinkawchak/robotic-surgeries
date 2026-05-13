# Competition Protocol (Four Entrant Multi Vendor Tournament)

This file fixes the four entrant multi vendor LLM tournament protocol for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to author the LLM tournament agent at 2030-pdac-1min/src/llm/compare_agent_1min.py, the tournament prompt at 2030-pdac-1min/prompts/comparison_prompt_1min.md, and the cross entrant comparison results at 2030-pdac-1min/results/comparison.json and 2030-pdac-1min/results/comparison_report.{md, pdf}.

## Why Four Entrants Instead of Single Vendor

The v3.9.1 GBM 1 minute variant ran a four entrant tournament where all four entrants were variants of the same Medtronic platform (current ROSA ONE Brain v3.0, hypothetical 2030 NeuroSpeed 1.0, two prior release snapshots). The single vendor framing was flagged as a limitation in 2030-gbm-1min/paper/full-paper/final-paper/sections/limitations_future.tex (item b: Add a competing 4-arm robot vendor entry to the LLM tournament so the leaderboard is not single vendor). The PDAC 1 minute variant addresses this limitation directly by enrolling four entrants from four different vendors (Medtronic, Intuitive, Verb, and human surgeons).

## Four Entrants

| Entrant | Type | Source | Notes |
|---------|------|--------|-------|
| PancreSpeed 1.0 (hypothetical 2030 Medtronic) | Robot | This project | 8 arm, 100 kHz force, 10 kHz cmd, 3 ms e stop |
| da Vinci Whipple 2030 (hypothetical Intuitive successor) | Robot | Public roadmap | 6 arm (single port plus 5 cooperating boom arms), 50 kHz force, 5 kHz cmd, 5 ms e stop |
| Hugo PDAC 2030 (hypothetical Medtronic Hugo successor) | Robot | Public roadmap | 6 arm modular cart, 30 kHz force, 3 kHz cmd, 8 ms e stop |
| Dutch Cohort 1000 human surgeon baseline | Human | 2025 nationwide cohort | 1000 robotic pancreaticoduodenectomies, mean operative time 5.4 hours, mean ideal outcome rate 47 percent |

The three robot entrants are scored under the per iteration composite score function defined in commit_04_iterations_1min.md. The human surgeon baseline is scored under the same composite score function but the per iteration metrics are derived from the 2025 Dutch cohort summary statistics rather than from a per iteration simulation.

## Composite Score Weights (Frozen)

The composite score weights are frozen across the four entrants and across all 32 iterations. The weights are reproduced from commit_04_iterations_1min.md for orientation.

| Component | Weight | PancreSpeed 1.0 target | da Vinci 2030 target | Hugo PDAC 2030 target | Dutch human target |
|-----------|--------|------------------------|----------------------|------------------------|---------------------|
| Quality | 0.30 | 95 | 88 | 85 | 82 |
| Time | 0.20 | 100 | 78 | 70 | 8 (5.4 hr vs 60 s) |
| Cost | 0.15 | 80 | 70 | 75 | 90 |
| Safety | 0.15 | 96 | 90 | 86 | 80 |
| Patient experience | 0.05 | 92 | 88 | 84 | 78 |
| Anastomosis quality | 0.15 | 95 | 90 | 87 | 82 |
| Composite total | 1.00 | 93.55 | 84.10 | 80.60 | 56.05 |

The PancreSpeed 1.0 target composite is 93.55, the da Vinci 2030 target is 84.10, the Hugo PDAC 2030 target is 80.60, and the Dutch human surgeon baseline is 56.05. The headline result expected from the 32 iteration sweep is therefore PancreSpeed 1.0 winning the four entrant tournament with the structural time dimension caveat (1 minute robot versus 5.4 hour human baseline) preserved in every rationale.

## Per Round Tournament Format

The LLM tournament runs four rounds per iteration. Each round is a pairwise comparison; the per round winner is the entrant with the higher per round composite score. The four rounds are:

| Round | Entrant A | Entrant B | Comparison |
|-------|-----------|-----------|------------|
| 1 | PancreSpeed 1.0 | da Vinci 2030 | Modern vs prior generation top platform |
| 2 | PancreSpeed 1.0 | Hugo PDAC 2030 | Modern vs prior generation modular |
| 3 | PancreSpeed 1.0 | Dutch human baseline | Modern vs current human (structural time dimension caveat applies) |
| 4 | da Vinci 2030 | Hugo PDAC 2030 | Cross competitor benchmark |

Across 32 iterations the cross round expected outcome is PancreSpeed 1.0 wins Rounds 1, 2, and 3; Round 4 is a coin flip (estimated 60 percent da Vinci 2030 wins). The cross iteration leaderboard reports per entrant mean composite score, win rate, and confidence interval.

## On Prem LLM Backend

The LLM tournament agent at 2030-pdac-1min/src/llm/compare_agent_1min.py runs on premises and supports three local backends and one cloud backend (with explicit privacy isolation flag):

| Backend | Model | Use case |
|---------|-------|----------|
| Ollama | Llama 3.3 70B Instruct | Default on premises, low latency |
| vLLM | Llama 3.3 70B Instruct or DeepSeek V3 | High throughput on premises |
| Anthropic Claude | claude-opus-4-7 (1M context) | Cloud, PHI cleared, full context for cross iteration analysis |
| Anthropic Claude | claude-sonnet-4-6 | Cloud, PHI cleared, faster than Opus |

The future Claude Code session selects the backend at runtime via the COMPARE_AGENT_BACKEND environment variable.

## Tournament Prompt Skeleton

The LLM tournament prompt at 2030-pdac-1min/prompts/comparison_prompt_1min.md is reproduced in skeleton below. The future Claude Code session fills in the per round entrant context.

```
You are the on premises LLM judge for the PDAC 1 minute robotic surgery tournament.
You will compare two entrants per round and emit a per round verdict.

Frozen composite weights: Quality 0.30, Time 0.20, Cost 0.15, Safety 0.15,
Patient experience 0.05, Anastomosis quality 0.15.

Structural caveat: Round 3 compares a 1 minute robot run against a 5.4 hour
human baseline. Preserve this caveat in your rationale.

Per entrant inputs: 32 per iteration L3 per phase Parquet rows, 32 per
iteration L4 per anastomosis Parquet rows, 32 per iteration event log
entries.

Emit a per round JSON verdict with fields:
  round: 1 to 4
  entrant_a: string
  entrant_b: string
  entrant_a_composite_mean: float
  entrant_b_composite_mean: float
  winner: entrant_a or entrant_b
  confidence: 0.0 to 1.0
  rationale: 200 word prose grounded in the per iteration L3 / L4 / event data
  caveats: list of strings
```

## Cross Iteration Leaderboard

The cross iteration leaderboard at 2030-pdac-1min/results/comparison_report.md aggregates the 32 per iteration tournaments into a single 4 entrant ranking. The leaderboard reports per entrant mean composite score, 95 percent confidence interval, win rate across the 4 rounds, total wins across the 4 rounds times 32 iterations equals 128 round results, and a per entrant component breakdown.

## Cross References

- commit_04_iterations_1min.md fixes the 32 iteration sweep and the per iteration composite score function.
- robot_specification_pancrespeed.md fixes the PancreSpeed 1.0 entrant.
- anastomosis_protocols.md fixes the anastomosis quality component.
- pdac_context_1min.md fixes the 8 phase timeline and the Dutch cohort baseline.
- gbm_errors_addressed.md fixes the single vendor gap that this protocol explicitly closes.
