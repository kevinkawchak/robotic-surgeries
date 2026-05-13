# Commit 4: Iteration Design (32 Iterations)

This file fixes the Future Commit 4 file list and authoring instructions for the 32 iteration deterministic sweep. The future Claude Code Opus 4.7 1M Max session reads this file to author the per iteration sweep pipeline at 2030-pdac-1min/src/simulation/iterate_1min.py, the high throughput Rust runner at 2030-pdac-1min/src/simulation/runner_1min.rs, and the per iteration sweep configuration at 2030-pdac-1min/config/iterations.yaml.

## Why 32 Iterations Instead of 16

The v3.9.1 GBM 1 minute variant used 16 iterations per benchmarked configuration. The 16 iteration sweep was insufficient to bound the cumulative force violation rate at the 95 percent confidence interval (per the limitation noted in 2030-gbm-1min/paper/full-paper/final-paper/sections/limitations_future.tex). The PDAC 1 minute variant doubles the iteration count to 32, which yields a 95 percent confidence interval on the cumulative force violation rate of approximately +/- 5 percent (at the binomial Wilson interval). The 32 iteration sweep also provides sufficient power to detect a 10 percent difference in the grade B/C postoperative pancreatic fistula rate at the 80 percent power level.

## Per Iteration Free Parameter Space

The per iteration sweep varies eight free parameters across 32 iterations. The parameters are sampled from a deterministic 32 row Latin hypercube design with seed 20260513.

| Parameter | Range | Discretization | Notes |
|-----------|-------|----------------|-------|
| Vessel angle deviation (deg) | -2.5 to +2.5 | 0.1 deg | Perturbs the SMV centerline angle vs the canonical 75 degree abutment |
| Pancreatic duct diameter (mm) | 2.8 to 3.6 | 0.1 mm | Affects fistula risk score and ring tension target |
| Anastomosis ring tension target perturbation (N) | -0.05 to +0.05 | 0.005 N | Perturbs the canonical 0.45 N PJ target |
| Daraxonrasib serum concentration at induction (ng/mL) | 5 to 25 | 1 ng/mL | Perioperative pause variation |
| Arm 1 hybrid scalpel power (W) | 18 to 24 | 0.2 W | Affects bipolar coagulator current |
| Arm 4 NIR indocyanine green dose (mg/kg) | 0.05 to 0.20 | 0.01 mg/kg | Affects bile leak detection sensitivity |
| Coordination master heartbeat jitter (microseconds) | 0 to 50 | 1 microsecond | Perturbs the 100 microsecond watchdog deadline |
| Per arm e stop latency perturbation (microseconds) | 0 to 200 | 5 microseconds | Perturbs the 3 ms cross arm e stop budget |

The deterministic Latin hypercube design ensures even coverage of the 8 dimensional parameter space with 32 samples. The design is reproducible from the seed 20260513 using the scipy.stats.qmc.LatinHypercube class.

## Per Iteration Composite Score

The per iteration composite score is computed by the metric pipeline at 2030-pdac-1min/src/metrics/compute_1min.py. The composite score uses frozen weights identical to the v3.9.1 GBM composite weights with one PDAC specific addition (the anastomosis quality component).

| Component | Weight | Range | Notes |
|-----------|--------|-------|-------|
| Quality (negative margin, no major complication) | 0.30 | 0 to 100 | -0.10 vs GBM to make room for anastomosis quality |
| Time (60 second target) | 0.20 | 0 to 100 | -0.05 vs GBM because PDAC is multi anastomosis |
| Cost (per arm energy consumption + tool cost) | 0.15 | 0 to 100 | -0.05 vs GBM because more arms cost more |
| Safety (no vessel hard stop, no cumulative force violation) | 0.15 | 0 to 100 | +0.05 vs GBM because PDAC is more dangerous |
| Patient experience (LOS, pain, return to therapy) | 0.05 | 0 to 100 | same as GBM |
| Anastomosis quality (PDAC specific: ring tension stability, manometry, leak detection) | 0.15 | 0 to 100 | new component, 0.05 of weight pulled from quality, 0.05 from time, 0.05 from cost |
| Composite score total weight | 1.00 | 0 to 100 | sum of weights |

The per iteration composite score is recorded in 2030-pdac-1min/data/robot_outcomes_1min.parquet. The mean composite score across 32 iterations is the headline metric reported in the per round LLM tournament at commit_05_competition_1min.md.

## Per Iteration Deterministic Seed

The per iteration seed is derived from the simulation root seed 20260513 plus the per iteration index. The deterministic seed contract is:

```
per_iteration_seed = root_seed + iteration_index
root_seed = 20260513
iteration_index in [0, 31]
```

The per iteration seed is consumed by every stochastic component of the simulation pipeline (vessel angle deviation, pancreatic duct diameter, anastomosis ring tension target perturbation, Daraxonrasib serum concentration, arm 1 hybrid scalpel power, arm 4 NIR indocyanine green dose, coordination master heartbeat jitter, per arm e stop latency perturbation). The deterministic seed contract ensures that any future re generation of the per iteration sweep produces bit identical per iteration Parquet files at the L2, L3, and L4 layers.

## Per Iteration Runtime Budget

The per iteration runtime budget on a single high end server (Intel Xeon Platinum 8480+, 56 cores, 256 GB RAM) is 90 seconds for the Python iterate_1min.py runner and 12 seconds for the Rust runner_1min.rs runner. The cross 32 iteration runtime budget is therefore 48 minutes (Python) or 6.4 minutes (Rust). The future Claude Code session is expected to use the Python runner for the publication run and the Rust runner for the high throughput ablation runs.

## Per Iteration Output Tree

The per iteration output tree is:

```
2030-pdac-1min/data/iterations/
  run_00000_L1_20ms.parquet           # publication arm sample only
  run_00000_L2_1s.parquet              # 8 arms by 60 rows
  run_00000_L3_phase.parquet           # 8 arms by 8 rows
  run_00000_L4_anastomosis.parquet     # 3 rows cross arm
  run_00000_daraxonrasib.parquet       # 1 row per iteration, perioperative trajectory
  run_00000_events.parquet             # variable length
  run_00000_L0_raw.zenodo_pointer.json # DOI + SHA 256 manifest
  run_00001_...
  ...
  run_00031_...
  index.jsonl                          # one row per iteration with seed + composite score
  aggregate.duckdb                     # cross iteration DuckDB index
```

## Cross References

- pdac_context_1min.md fixes the 8 phase timeline.
- sensor_specification_100khz.md fixes the 640 channel sensor stack.
- anastomosis_protocols.md fixes the per anastomosis target table.
- file_size_pyramid_1min.md fixes the per iteration committed budget.
- chunking_strategy.md fixes the per iteration chunking pattern.
- competition_protocol.md fixes the per round LLM tournament that consumes the per iteration composite scores.
- commit_05_competition_1min.md fixes the four entrant tournament.
- daraxonrasib_integration.md fixes the perioperative Daraxonrasib trajectory.
