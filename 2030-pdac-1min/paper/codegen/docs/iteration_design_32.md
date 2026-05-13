# Iteration Design Overview (32 Iterations)

This document fixes the 32 iteration deterministic sweep design with Latin hypercube parameter space. The full sweep configuration lives at `config/iterations.yaml` and the per iteration runner lives at `src/simulation/iterate_1min.py`.

## Why 32 Iterations

The v3.9.1 GBM 1 minute variant used 16 iterations per benchmarked configuration. The 16 iteration sweep was insufficient to bound the cumulative force violation rate at the 95 percent confidence interval. The PDAC 1 minute variant doubles the iteration count to 32, which yields a 95 percent confidence interval on the cumulative force violation rate of approximately plus or minus 5 percent (at the binomial Wilson interval). The 32 iteration sweep also provides sufficient power to detect a 10 percent difference in the grade B/C postoperative pancreatic fistula rate at the 80 percent power level.

## Latin Hypercube Free Parameter Space

| Parameter | Range | Discretization | Notes |
|-----------|-------|----------------|-------|
| Vessel angle deviation (deg) | -2.5 to +2.5 | 0.1 deg | Perturbs the SMV centerline angle vs canonical 75 deg abutment |
| Pancreatic duct diameter (mm) | 2.8 to 3.6 | 0.1 mm | Affects fistula risk score and ring tension target |
| Anastomosis ring tension target perturbation (N) | -0.05 to +0.05 | 0.005 N | Perturbs canonical 0.45 N PJ target |
| Daraxonrasib serum concentration at induction (ng/mL) | 5 to 25 | 1 ng/mL | Perioperative pause variation |
| Arm 1 hybrid scalpel power (W) | 18 to 24 | 0.2 W | Affects bipolar coagulator current |
| Arm 4 NIR ICG dose (mg/kg) | 0.05 to 0.20 | 0.01 mg/kg | Affects bile leak detection sensitivity |
| Coordination master heartbeat jitter (microseconds) | 0 to 50 | 1 microsecond | Perturbs 100 microsecond watchdog deadline |
| Per arm e stop latency perturbation (microseconds) | 0 to 200 | 5 microseconds | Perturbs 3 ms cross arm e stop budget |

The deterministic Latin hypercube design ensures even coverage of the 8 dimensional parameter space with 32 samples. The design is reproducible from the seed 20260513 using the `scipy.stats.qmc.LatinHypercube` class.

## Per Iteration Output Tree

```
data/iterations/
  run_00000_L1_20ms.parquet           # publication arm sample only
  run_00000_L2_1s.parquet              # 8 arms by 60 rows
  run_00000_L3_phase.parquet           # 8 arms by 8 rows
  run_00000_L4_anastomosis.parquet     # 3 rows cross arm
  run_00000_daraxonrasib.parquet       # 1 row per iteration
  run_00000_events.parquet             # variable length
  run_00000_L0_raw.zenodo_pointer.json # DOI + SHA 256 manifest
  ...
  run_00031_*
  index.jsonl                          # one row per iteration with seed + composite score
  aggregate.duckdb                     # cross iteration DuckDB index
```

## Per Iteration Runtime Budget

| Platform | Per iteration runtime (s) | 32 iteration runtime |
|----------|---------------------------|----------------------|
| Linux Xeon 8480+ + Python | 90 | 48 minutes |
| Linux Xeon 8480+ + Rust | 12 | 6.4 minutes |
| MacOS M3 Ultra + Python | 60 | 32 minutes |
| Windows i9 + Python | 80 | 43 minutes |
| NVIDIA A100 80GB | 30 | 16 minutes |

## Cross References

- `../../instructions/commit_04_iterations_1min.md` fixes the per iteration sweep design.
- `../../instructions/file_size_pyramid_1min.md` fixes the per iteration committed budget.
- `../../instructions/competition_protocol.md` fixes the composite score weights.
