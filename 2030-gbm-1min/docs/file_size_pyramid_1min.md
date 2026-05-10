# File Size Pyramid (Layer 4 Addendum, 1-Minute Variant)

This document is the per-iteration file size pyramid that splits the canonical L0 raw record into committed L1 to L3 aggregates plus an event log. The L0 raw is archived to Zenodo. The 16-iteration sweep fits inside the GitHub 10 MB committed cap while preserving millisecond ground truth on Zenodo.

## Pyramid Levels (per iteration)

| Level | Sample rate | Per-arm rows in 1 min | Per-arm size | 4-arm size | All 16 iterations | Within 10 MB total? |
|-------|-------------|------------------------|--------------|------------|---------------------|--------------------|
| L0 raw mixed | 1 to 10 kHz mixed | 600,000 | 6.6 MB | 26 MB | 416 MB | Zenodo only, never Git |
| L1 100 Hz aggregate | 100 Hz | 6,000 | 600 KB | 2.4 MB | 38 MB | No, exceeds 10 MB cap |
| L1 20 Hz aggregate (recommended) | 20 Hz | 1,200 | 120 KB | 480 KB | 7.7 MB | YES |
| L2 1 Hz aggregate | 1 Hz | 60 | 6 KB | 24 KB | 384 KB | YES |
| L3 per-phase aggregate | per-phase | 4 | under 1 KB | under 4 KB | under 64 KB | YES |
| Event log | event-driven | 50 to 200 | 2 KB | 8 KB | 128 KB | YES |

## L1 (20 Hz aggregate, 50 ms window)

For each 50 ms window the L1 record carries:

- Per-arm window timestamp tick_50ms (range 0 to 1199, integer).
- Per-arm mean joint position vector (7 doubles).
- Per-arm mean joint velocity vector (7 doubles).
- Per-arm peak joint torque vector (7 doubles), absolute value.
- Per-arm mean end-effector position (3 doubles).
- Per-arm peak end-effector force vector (3 doubles), absolute value, taken over the 500 force samples in the 50 ms window.
- Per-arm peak end-effector torque vector (3 doubles).
- Per-arm peak navigation deviation vector (3 doubles).
- Per-arm safety_zone enum (most permissive observed in window).
- Per-arm robot_state enum (last observed in window).
- Per-arm cumulative tip-force-violation event count for the window.
- Per-arm heartbeat_ok bit (1 if every 1 ms heartbeat in the window was ok, else 0).
- meta_seed integer.
- meta_iteration_id string.
- arm_id enum.

L1 size per arm: 1,200 records times 50 columns at zstd-3 equals approximately 120 KB. Across 4 arms: 480 KB.

## L2 (1 Hz aggregate, 1 second window)

For each 1 second window the L2 record carries:

- Per-arm window timestamp tick_1s (range 0 to 59, integer).
- Per-arm mean and peak end-effector position (6 doubles).
- Per-arm peak end-effector force vector (3 doubles).
- Per-arm cumulative tip force violations in window.
- Per-arm cumulative E-stop engagement count in window.
- Per-arm cumulative AE injection count in window.
- Per-arm tissue removal volume in window (mm cubed).
- Per-arm safety_zone enum (most permissive observed in window).
- Per-arm robot_state enum (last observed in window).
- meta_seed and meta_iteration_id and arm_id.

L2 size per arm: 60 records times 20 columns at zstd-3 equals approximately 6 KB. Across 4 arms: 24 KB.

## L3 (per-phase aggregate, 4 records per iteration)

For each of the 4 phases (Phase 1 through Phase 4) the L3 record carries:

- Phase ID (1 through 4) and phase name.
- Phase start_us and end_us integers.
- Per-arm cumulative tip force violations in phase.
- Per-arm cumulative E-stop engagement count in phase.
- Per-arm cumulative AE injection count in phase.
- Per-arm tissue removal volume in phase.
- Per-arm peak end-effector force vector across phase.
- Per-arm peak end-effector velocity scalar across phase.
- Per-arm phase-end safety_zone and robot_state.
- meta_seed, meta_iteration_id, arm_id.

L3 size per iteration: 4 records times 4 arms times 20 columns at zstd-3 equals approximately 4 KB.

## Event Log (event-driven)

For each detected event (force violation, E-stop engagement, AE injection, gap detection, heartbeat miss, safety zone transition) the event log emits one record with:

- Event timestamp tick_us.
- Event kind enum.
- arm_id enum.
- Event payload as JSON string.
- meta_seed, meta_iteration_id.

Event log size per iteration: typically 50 to 200 events at 40 bytes each plus zstd-3 compression equals approximately 8 KB.

## L0 Raw Archive Pointer

Each iteration includes a single hand-authored file at Commit 4 and populated at Commit 5: `data/iterations/run_NNNNN_L0_raw.zenodo_pointer.json`. This file points to the Zenodo deposition for that iteration's L0 raw and includes the SHA-256 of the L0 Parquet on Zenodo.

## Per-Iteration Output Schema (Layer 4 committed)

| File | Format | Size | Authoring approach |
|------|--------|------|--------------------|
| `data/iterations/run_NNNNN_L1_50ms.parquet` | Parquet zstd-3 | 480 KB across 4 arms | Script-generated, committed |
| `data/iterations/run_NNNNN_L2_1s.parquet` | Parquet zstd-3 | 24 KB across 4 arms | Script-generated, committed |
| `data/iterations/run_NNNNN_L3_phase.parquet` | Parquet zstd-3 | under 4 KB across 4 arms | Script-generated, committed |
| `data/iterations/run_NNNNN_events.parquet` | Parquet zstd-3 | 8 KB | Script-generated, committed |
| `data/iterations/run_NNNNN_L0_raw.zenodo_pointer.json` | JSON | 1 KB | Hand-authored at Commit 4, populated at Commit 5 |

Per-iteration committed total: approximately 510 KB across all five files. The per-iteration file count is 5; across 16 iterations this is 80 files.

## Total Repository Storage Budget for v3.9.1

| Bucket | Size |
|--------|------|
| Per-iteration committed (16 iterations times 510 KB) | 8.2 MB |
| Schemas, scripts, configs, README, viz (fixed overhead) | 1.5 MB |
| Total committed | 9.7 MB |
| Zenodo L0 archive (16 iterations times 26 MB) | 416 MB |

## File Size Cap Enforcement

```
find 2030-gbm-1min -type f -size +10M -print | (! grep -q .) || (echo "ERROR: file over 10 MB"; exit 1)
find 2030-gbm-1min -name '*.parquet' -size +5M -print | (! grep -q .) || (echo "ERROR: parquet over 5 MB"; exit 1)
```

## Compression Default Override (zstd-3 vs Snappy)

The 1-minute variant overrides the parent Snappy default to zstd-3 because zstd-3 is approximately 30 percent smaller than Snappy at the same decompression speed for the dense numeric Parquet payloads produced by the L1 to L3 aggregates.
