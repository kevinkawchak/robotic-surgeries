# Comparison (4 Entrant Tournament) Execution

This directory captures the live run output of the 4 entrant multi vendor LLM tournament agent at `../../codegen/src/llm/compare_agent_1min.py`. The tournament runs 4 rounds per iteration across 32 iterations, producing 128 per round verdicts and a cross iteration leaderboard. The 4 entrants are PancreSpeed 1.0 (this project's hypothetical 2030 Medtronic 8 arm platform), the hypothetical 2030 Intuitive da Vinci Whipple successor, the hypothetical 2030 Medtronic Hugo PDAC successor, and the 2025 Dutch human surgeon baseline.

## Reproduction

```bash
cd 2030-pdac-1min/paper/codegen
PYTHONPATH=. python -m src.llm.compare_agent_1min \
  --seed 20260513 \
  --iterations 32 \
  --backend ollama \
  --output ../execution/comparison/comparison.json
```

The four LLM backends (Ollama, vLLM, Anthropic Claude Opus 4.7, Anthropic Claude Sonnet 4.6) are stubbed via the `_call_backend` placeholder in the codegen. The leaderboard uses the deterministic composite score formula with a per round random perturbation seeded at `root_seed + iteration_id`. Replacing the stub with a real backend changes only the rationale text, not the leaderboard.

## Files

| File | Description |
|------|-------------|
| `comparison.json` | Full tournament output, 32 iteration rounds plus leaderboard |
| `leaderboard.csv` | 4 entrant cross iteration leaderboard ranked by composite mean |
| `per_round_verdicts.csv` | 128 row per round verdict log (4 rounds x 32 iterations) |
| `robot_vs_human_round3.csv` | Round 3 PancreSpeed vs Dutch baseline detail |
| `comparison_report.md` | Narrative cross iteration leaderboard |

## Cross Iteration Leaderboard

| Rank | Entrant | Mean Composite | CI Low | CI High | Wins | Win Rate |
|------|---------|---------------|--------|---------|------|----------|
| 1 | PancreSpeed 1.0 | 93.735 | 93.235 | 94.235 | 96 | 100.0% |
| 2 | da Vinci Whipple 2030 | 83.886 | 83.386 | 84.386 | 32 | 50.0% |
| 3 | Hugo PDAC 2030 | 80.974 | 80.474 | 81.474 | 0 | 0.0% |
| 4 | Dutch human surgeon baseline | 67.895 | 67.395 | 68.395 | 0 | 0.0% |

PancreSpeed 1.0 wins all 96 rounds in which it competes (Rounds 1, 2, and 3 across 32 iterations).
da Vinci wins 32 of 64 rounds (loses all 32 to PancreSpeed in Round 1, wins all 32 vs Hugo in Round 4).
Hugo PDAC 2030 loses all 64 of its rounds.
The Dutch human surgeon baseline loses all 32 Round 3 matches.

## Round 3 Robot vs Human (PancreSpeed 1.0 vs Dutch Baseline)

Round 3 carries the structural time dimension caveat: the comparison is between a 1 minute robot run and a 5.4 hour human baseline; the time component score is dominated by the orders of magnitude duration delta. The Round 3 mean PancreSpeed composite is 93.857 versus the Dutch baseline mean composite of 67.895, a delta of 25.962 (range 23.61 to 28.21 across the 32 iterations).

PancreSpeed 1.0 wins all 32 of its Round 3 matches at confidence 0.99.

## Tournament Round Structure

```
Round 1: PancreSpeed 1.0 vs da Vinci Whipple 2030
Round 2: PancreSpeed 1.0 vs Hugo PDAC 2030
Round 3: PancreSpeed 1.0 vs Dutch human surgeon baseline (structural caveat applies)
Round 4: da Vinci Whipple 2030 vs Hugo PDAC 2030
```

Total per iteration verdicts: 4
Total cross iteration verdicts: 4 * 32 = 128

## Structural Caveats (Preserved in Every Round)

Every Round 3 verdict carries the explicit caveat: `Structural time dimension caveat: this round compares a 1 minute robot run against a 5.4 hour human baseline; the time component score is dominated by the orders of magnitude duration delta.`

Every round that involves PancreSpeed 1.0 carries the simulation against simulation caveat: `PancreSpeed 1.0 is a hypothetical 2030 platform; comparison is simulation against simulation.`
