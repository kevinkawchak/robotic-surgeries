# Cross Iteration Tournament Report (v0.6.0)

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../releases.md)
[![Entrants](https://img.shields.io/badge/Entrants-4-purple.svg)](comparison.json)
[![Iterations](https://img.shields.io/badge/Iterations-32-orange.svg)](comparison.json)
[![Rounds](https://img.shields.io/badge/Rounds-128-blue.svg)](comparison.json)

This report aggregates the 32 per iteration 4 entrant multi vendor tournaments into a single cross iteration leaderboard for the v0.6.0 PDAC 1 minute 8 arm Whipple simulation.

## Cross Iteration Leaderboard

| Rank | Entrant | Composite mean | 95 percent CI | Win rate | Total wins |
|------|---------|----------------|---------------|----------|------------|
| 1 | PancreSpeed_1_0 | 93.55 | [93.42, 93.68] | 1.000 | 96 |
| 2 | da_Vinci_Whipple_2030 | 84.10 | [83.95, 84.25] | 0.328 | 21 |
| 3 | Hugo_PDAC_2030 | 80.60 | [80.45, 80.75] | 0.172 | 11 |
| 4 | Dutch_human_baseline | 56.05 | [55.85, 56.25] | 0.000 | 0 |

PancreSpeed_1_0 wins every Round 1, 2, and 3 across all 32 iterations (96 wins of 96). Round 4 is approximately a coin flip between the two non PancreSpeed robot entrants; da_Vinci_Whipple_2030 wins 21 of 32 Round 4 matchups (65.6 percent), Hugo_PDAC_2030 wins 11 (34.4 percent). The Dutch human surgeon baseline does not win any round, with the structural time dimension caveat preserved in every Round 3 rationale.

## Per Component Leaderboard

| Component | PancreSpeed_1_0 | da_Vinci_Whipple_2030 | Hugo_PDAC_2030 | Dutch_human_baseline |
|-----------|------------------|------------------------|------------------|------------------------|
| Quality | 95.0 | 88.0 | 85.0 | 82.0 |
| Time | 100.0 | 78.0 | 70.0 | 8.0 |
| Cost | 80.0 | 70.0 | 75.0 | 90.0 |
| Safety | 96.0 | 90.0 | 86.0 | 80.0 |
| Patient experience | 92.0 | 88.0 | 84.0 | 78.0 |
| Anastomosis quality | 95.0 | 90.0 | 87.0 | 82.0 |
| Composite total | 93.55 | 84.10 | 80.60 | 56.05 |

## Per Round Win Distribution

| Round | PancreSpeed_1_0 wins | da_Vinci_2030 wins | Hugo_PDAC_2030 wins | Dutch_human_baseline wins |
|-------|----------------------|--------------------|--------------------|-----------------------------|
| 1 | 32 | 0 | n/a | n/a |
| 2 | 32 | n/a | 0 | n/a |
| 3 | 32 | n/a | n/a | 0 |
| 4 | n/a | 21 | 11 | n/a |

## Structural Caveat

Round 3 compares a 1 minute robot run against a 5.4 hour human baseline. The Time component score (PancreSpeed 100.0 vs Dutch human 8.0) is dominated by the orders of magnitude duration delta. The caveat is preserved verbatim in every Round 3 per iteration rationale at `comparison.json`.

## Cross References

- `comparison.json` per iteration per round verdicts.
- `../prompts/comparison_prompt_1min.md` versioned tournament prompt.
- `../src/llm/compare_agent_1min.py` agent implementation.
- `../../instructions/competition_protocol.md` 4 entrant tournament specification.
- `../../instructions/commit_05_competition_1min.md` per round format specification.
