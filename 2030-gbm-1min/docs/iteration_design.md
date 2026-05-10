# Iteration Design (16-Iteration Sweep, 1-Minute Variant)

## Iteration Count and Rationale

16 iterations balance statistical power against the doubled per-iteration committed footprint of the 4-arm topology. 16 is the default iteration count for v3.9.1; later releases may scale to 32 or 64 if Zenodo bandwidth allows. The default tournament size of 4 (defined in `comparison_methodology.md`) is independent of the iteration count.

## Sweep Dimensions

The only parameters that vary between iterations:

- Seed: integer in [20260510, 20260525] inclusive, one per iteration.
- Per-arm sensor noise sigma: 0.01 to 0.05 mm linearly across iterations.
- Per-arm force feedback gain: 0.8 to 1.2 linearly.
- Inverse kinematics solver tolerance: 1e-6 to 1e-3 logarithmically.
- Random surgical adverse event injection probability: fixed at 0.05 per iteration.
- Heartbeat jitter sigma: 0 to 50 microseconds linearly across iterations to test the 3 ms watchdog.

## Fixed Parameters (never vary)

- Patient identity: PAT-GBM-0001.
- Robot make and model: Medtronic NeuroSpeed 1.0.
- Kinematic limits per arm: per `config/kinematics_4arm.yaml`.
- Safety limits per arm: 5.0 N tip, 1.0 N lateral.
- Cumulative force limit: 12 N.
- Procedure phases: 4 phases (60 s total).
- Per-arm tool assignment: arm 1 hybrid, arm 2 bipolar, arm 3 suction, arm 4 imaging.

## Parameter Sweep Table (16 tuples)

| iter | seed | noise_sigma_mm | force_gain | ik_tol | jitter_sigma_us |
|------|------|----------------|------------|--------|------------------|
| 01 | 20260510 | 0.0100 | 0.8000 | 1.0e-06 | 0.00 |
| 02 | 20260511 | 0.0127 | 0.8267 | 1.6e-06 | 3.33 |
| 03 | 20260512 | 0.0153 | 0.8533 | 2.7e-06 | 6.67 |
| 04 | 20260513 | 0.0180 | 0.8800 | 4.4e-06 | 10.00 |
| 05 | 20260514 | 0.0207 | 0.9067 | 7.2e-06 | 13.33 |
| 06 | 20260515 | 0.0233 | 0.9333 | 1.2e-05 | 16.67 |
| 07 | 20260516 | 0.0260 | 0.9600 | 1.9e-05 | 20.00 |
| 08 | 20260517 | 0.0287 | 0.9867 | 3.2e-05 | 23.33 |
| 09 | 20260518 | 0.0313 | 1.0133 | 5.2e-05 | 26.67 |
| 10 | 20260519 | 0.0340 | 1.0400 | 8.5e-05 | 30.00 |
| 11 | 20260520 | 0.0367 | 1.0667 | 1.4e-04 | 33.33 |
| 12 | 20260521 | 0.0393 | 1.0933 | 2.3e-04 | 36.67 |
| 13 | 20260522 | 0.0420 | 1.1200 | 3.7e-04 | 40.00 |
| 14 | 20260523 | 0.0447 | 1.1467 | 6.2e-04 | 43.33 |
| 15 | 20260524 | 0.0473 | 1.1733 | 1.0e-03 | 46.67 |
| 16 | 20260525 | 0.0500 | 1.2000 | 1.0e-03 | 50.00 |

## Iteration Runtime Budget

- Mac M3 Ultra recipe: 30 seconds wall-clock per iteration.
- A100 GPU recipe: 12 seconds wall-clock per iteration.
- Conventional 32-core server: 60 seconds wall-clock per iteration.

## Total Compute Budget

16 iterations times 30 to 60 seconds equals 8 to 16 minutes serial.

## Storage Budget

- 16 iterations times 510 KB committed equals 8.2 MB committed.
- 16 iterations times 26 MB Zenodo equals 416 MB Zenodo.

## Failure Handling

A failed iteration writes a record to `index.jsonl` with `status: "failed"` and a stack trace pointer. Failed iterations do not block subsequent iterations.

## Reproducibility

Each iteration's L1 to L3 Parquet files embed the seed in the `meta_seed` column and the iteration ID in the `meta_iteration_id` column. Bit-identical reruns require identical seeds and parameter tuples.

## Cross-References

- `src/simulation/runner_1min.rs`: Rust high-throughput engine.
- `src/simulation/iterate_1min.py`: Python orchestrator.
- `data/iterations/aggregate.duckdb`: cross-iteration analytical store.
- `docs/file_size_pyramid_1min.md`: per-iteration L0 to L3 plus events budget.
- `data/iterations/run_NNNNN_L0_raw.zenodo_pointer.json`: per-iteration L0 archive pointers.
