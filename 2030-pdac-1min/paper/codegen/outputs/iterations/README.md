# Iterations Output (v0.6.0)

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../../releases.md)
[![Iterations](https://img.shields.io/badge/Iterations-32-purple.svg)](../../config/iterations.yaml)
[![Seed](https://img.shields.io/badge/Seed-20260513-orange.svg)](../../config/project.yaml)

This directory documents the cross iteration outputs of the 32 iteration deterministic Latin hypercube sweep.

## Cross Iteration Headline

Mean composite score across 32 iterations: **92.42** (with 4 grade B PJ outcomes pulling the mean below the 93.55 target). 95 percent confidence interval [92.28, 92.56]. The PancreSpeed 1.0 entrant wins every Round 1, 2, and 3 comparison against the three other entrants with confidence above 0.94.

## Per Iteration Sweep

| Iteration | Seed | Composite | PJ grade | HJ leak | GJ patency | FRS |
|-----------|------|-----------|----------|---------|------------|-----|
| 0 | 20260513 | 93.55 | A | absent | patent | 5.0 |
| 1 | 20260514 | 93.42 | A | absent | patent | 4.8 |
| 4 | 20260517 | 85.92 | B | absent | patent | 5.4 |
| 11 | 20260524 | 85.84 | B | absent | patent | 5.6 |
| 15 | 20260528 | 85.91 | B | absent | patent | 5.5 |
| 19 | 20260532 | 85.89 | B | present | patent | 5.7 |
| 27 | 20260540 | 85.86 | B | absent | delayed | 5.5 |
| ... | ... | ... | ... | ... | ... | ... |

Full index at `../../data/iterations/index.jsonl`. Per iteration L3 phase tables at `../../data/iterations/run_NNNNN_L3_phase.csv`.

## Realized Outcomes

- Grade A pancreaticojejunostomy outcomes: 27 of 32 (84.4 percent)
- Grade B pancreaticojejunostomy outcomes: 5 of 32 (15.6 percent)
- Grade C pancreaticojejunostomy outcomes: 0 of 32 (0.0 percent)
- Hepaticojejunostomy leak absent: 31 of 32 (96.9 percent)
- Gastrojejunostomy patent: 31 of 32 (96.9 percent)
- Realized FRS range: 4.6 to 5.7 (moderate)

The target rate of < 5 percent grade B/C combined is not yet met in the v0.6.0 baseline (current 15.6 percent); the future work catalog identifies the ring tension control loop tuning as the primary improvement vector.

## Cross References

- `../../src/simulation/iterate_1min.py` Python runner.
- `../../src/simulation/runner_1min.rs` Rust runner.
- `../../src/metrics/compute_1min.py` composite score.
- `../../config/iterations.yaml` sweep configuration.
- `../../../instructions/commit_04_iterations_1min.md` design specification.
