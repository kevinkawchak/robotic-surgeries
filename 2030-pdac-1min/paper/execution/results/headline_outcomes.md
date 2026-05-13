# Headline Outcomes (v0.7.0 Execution)

This file is the single point of truth for the v0.7.0 PDAC 1 minute execution outcomes. All numbers are produced by running the codegen v0.6.0 modules at root seed 20260513 on 13 May 2026.

## Cross Iteration Statistics (32 Iterations, Seed 20260513)

| Statistic | Value |
|-----------|-------|
| Iteration count | 32 |
| Root seed | 20260513 |
| PancreSpeed 1.0 mean composite | 93.298 |
| PancreSpeed 1.0 composite std | 1.225 |
| PancreSpeed 1.0 composite 95% CI | +/- 0.462 |
| PancreSpeed 1.0 composite range | [88.431, 93.735] |

## 4 Entrant Tournament Cross Iteration Leaderboard

| Rank | Entrant | Mean Composite | Total Wins (of 96 played) | Win Rate |
|------|---------|---------------|---------------------------|----------|
| 1 | PancreSpeed 1.0 | 93.735 | 96 | 100.0% |
| 2 | da Vinci Whipple 2030 | 83.886 | 32 | 50.0% |
| 3 | Hugo PDAC 2030 | 80.974 | 0 | 0.0% |
| 4 | Dutch human surgeon baseline | 67.895 | 0 | 0.0% |

## Anastomosis Outcomes (Iteration Sweep View, Publication Number)

| Anastomosis | Outcome Field | Distribution | Rate |
|-------------|---------------|--------------|------|
| PJ | Grade A | 32 of 32 | 100.0% |
| HJ | Leak absent | 30 of 32 | 93.75% |
| GJ | Patent | 30 of 32 | 93.75% |

## Fistula Risk Score (Realized, 32 Iterations)

| FRS Range | Description | Count |
|-----------|-------------|-------|
| 0 to 2 | Low fistula risk | 0 |
| 3 to 6 | Intermediate fistula risk | 32 |
| 7 to 10 | High fistula risk | 0 |

Mean realized FRS: 5.24. Range: 4.93 to 5.55. All 32 iterations fall in the intermediate FRS band.

## Daraxonrasib Postoperative Restart Day Distribution

| Recommended Restart Day | Count | Share |
|-------------------------|-------|-------|
| T+7d (uncomplicated) | 29 | 90.6% |
| T+14d (complicated) | 3 | 9.4% |
| T+21d (FRS >= 8 OR force time integral > 8 N s) | 0 | 0.0% |

## Vascular Safety Statistics

| Statistic | Value |
|-----------|-------|
| 5 vessel zones | SMV, PV, HA, CA, SMA |
| 4 actions | clear, no_fly, soft_warning, hard_stop |
| Cross iteration safety zone violations | 0 |
| Cross iteration collision state violations | 0 |
| Hard stop sample path verified | Yes (5 hard_stop verdicts in a 100 tick approach path) |

## Composite Score Component Weights (Frozen)

| Component | Weight |
|-----------|--------|
| Quality | 0.30 |
| Time | 0.20 |
| Cost | 0.15 |
| Safety | 0.15 |
| Patient experience | 0.05 |
| Anastomosis quality | 0.15 |
| Sum | 1.00 |

## Round 3 Structural Caveat (Preserved in Every Rationale)

`Structural time dimension caveat: this round compares a 1 minute robot run against a 5.4 hour human baseline; the time component score is dominated by the orders of magnitude duration delta.`

`PancreSpeed 1.0 is a hypothetical 2030 platform; comparison is simulation against simulation.`

## Cross Reference

- Per family `README.md` files document the artifact level reproduction.
- The headline outcomes table in the top level `../README.md` is the human readable summary.
- The codegen v0.6.0 README at `../../codegen/README.md` documents the source modules and the cross platform runtime recipes.
