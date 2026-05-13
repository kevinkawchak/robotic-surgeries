# File Size Pyramid (1 Minute Variant, 5 Layers)

This file fixes the per iteration committed Parquet pyramid budget for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to author the per iteration aggregator pipeline at 2030-pdac-1min/src/simulation/aggregate_pyramid.py and the per iteration DuckDB index at 2030-pdac-1min/data/iterations/aggregate.duckdb.

## Pyramid Rationale

The full L0 raw sensor stream at mixed 100 kHz force plus 10 kHz command across 8 arms is 412 MB per iteration and 13.2 GB across 32 iterations. The GitHub single file commit cap is 10 MB; the committed Parquet soft cap is 5 MB. The pyramid therefore retains the L0 layer at Zenodo only (per zenodo_archive_protocol.md) and commits only the L1, L2, L3, L4, and event log layers to Git. The per iteration committed budget is 980 KB; the cross iteration committed total is 33.4 MB.

## Five Layer Budget Table

| Layer | Rate | Window | Rows per arm | Rows total | Per iteration size (KB) | Cumulative size (MB) |
|-------|------|--------|--------------|------------|-------------------------|----------------------|
| L0 (Zenodo only, not committed) | 100 kHz force, 10 kHz cmd | 60 s | 600,000 force, 600,000 cmd | 4.8 M force, 4.8 M cmd | 412,000 (412 MB) | 13,184 (13.2 GB) |
| L1 (committed, publication sample only) | 50 Hz | 60 s | 3,000 | 3,000 | 240 | 7.7 |
| L2 (committed, cross iteration aggregate) | 1 Hz | 60 s | 60 | 480 (8 arms) | 120 | 3.8 |
| L3 (committed, per phase aggregate) | 1 per phase | 8 phases | 8 | 64 (8 arms) | 64 | 2.0 |
| L4 (committed, PDAC specific, per anastomosis event) | 1 per event | 3 events | 3 | 3 (cross arm) | 24 | 0.8 |
| Event log (committed, event driven) | event driven | per iteration | variable | variable | 32 | 1.0 |
| Per iteration committed total | mixed | mixed | mixed | mixed | 480 | 15.4 |
| Iteration metadata + DuckDB index | one shot | per release | n/a | n/a | n/a | 2.0 |
| Cross release committed total | mixed | mixed | mixed | mixed | n/a | 17.4 |

The per iteration L1 sample is retained only for the publication arm (arm 1 during Phase 5 pancreaticojejunostomy, the first 100 milliseconds, sampled at 10 kHz then decimated to 50 Hz). The L1 sample mirrors the v3.9.1 GBM 54 by 1001 sensor sample feat scaled to 80 columns and 3,000 rows (downsampled to 1001 rows for the committed CSV slice).

The per iteration L2 layer commits an 8 arm by 60 second aggregate Parquet at 1 Hz; the per second per arm aggregate stores mean, max, p95, and violation count for the per arm tip force scalar, the per arm force time integral, the per arm collision avoidance state, the per arm safety zone action, the per arm vessel surface proximity, and the per arm anastomosis ring tension.

The per iteration L3 layer commits an 8 phase per arm aggregate Parquet at 1 row per phase; the per phase per arm aggregate stores phase start tick, phase end tick, phase duration, per phase per arm mean tip force, per phase per arm max tip force, per phase per arm force time integral, per phase per arm safety zone violation count, per phase per arm collision state violation count, and per phase per arm anastomosis ring tension stability.

The per iteration L4 layer (PDAC specific) commits a 3 anastomosis event Parquet at 1 row per event; the per event aggregate stores anastomosis identifier, anastomosis start tick, anastomosis end tick, anastomosis duration, anastomosis ring tension stability (RMSE from target), anastomosis manometry stability (RMSE from target), anastomosis bile spectrophotometry signal (max 410 nm above baseline), and anastomosis realized grade (A, B, or C for pancreaticojejunostomy; leak absent or present for hepaticojejunostomy; patent or delayed for gastrojejunostomy).

The per iteration event log commits a variable length Parquet of event records; per record fields are tick, arm_id, event_type (one of: e_stop, collision, vessel_hard_stop, anastomosis_ring_tension_violation, anastomosis_manometry_violation, anastomosis_bile_leak), severity (soft / hard), and resolution (auto / manual).

## Single Per Iteration Commit File Layout

The per iteration commit produces five Parquet files plus one pointer JSON file. The pointer JSON file points at the Zenodo L0 deposition for the per iteration raw stream.

| File | Path | Size (KB) | Notes |
|------|------|-----------|-------|
| L1 sample (publication arm only) | 2030-pdac-1min/data/iterations/run_NNNNN_L1_20ms.parquet | 240 | only for arm 1 Phase 5 sample iteration |
| L2 aggregate | 2030-pdac-1min/data/iterations/run_NNNNN_L2_1s.parquet | 120 | 8 arms by 60 rows |
| L3 per phase | 2030-pdac-1min/data/iterations/run_NNNNN_L3_phase.parquet | 64 | 8 arms by 8 rows |
| L4 per anastomosis | 2030-pdac-1min/data/iterations/run_NNNNN_L4_anastomosis.parquet | 24 | 3 rows cross arm |
| Event log | 2030-pdac-1min/data/iterations/run_NNNNN_events.parquet | 32 | variable |
| Zenodo L0 pointer | 2030-pdac-1min/data/iterations/run_NNNNN_L0_raw.zenodo_pointer.json | 0.5 | DOI + SHA 256 manifest |

The per iteration committed total is approximately 480 KB (240 + 120 + 64 + 24 + 32 = 480 KB), well under the 10 MB cap and the 5 MB Parquet soft cap. The cross 32 iteration committed total is approximately 15.4 MB plus 2 MB of cross iteration aggregate and DuckDB index, totalling 17.4 MB.

## DuckDB Cross Iteration Index

The future Claude Code session authors the cross iteration DuckDB index at 2030-pdac-1min/data/iterations/aggregate.duckdb. The DuckDB index loads the 32 per iteration L2, L3, and L4 Parquet files into three tables (l2, l3, l4) and exposes them as queryable views. The DuckDB file itself is approximately 2 MB and is committed to Git.

The DuckDB index supports the per iteration composite score computation, the per round LLM tournament comparison, the per phase aggregate visualization, and the per anastomosis outcome accounting. The cross iteration index also supports the per iteration realized FRS calibration against the preoperative FRS prediction.

## Compression Settings

All committed Parquet files use the zstd-3 compression default. The zstd-3 default is required for the 100 kHz force channels because the high frequency tip dynamics are not amenable to dictionary encoding alone; zstd-3 achieves approximately 4x compression on the force channels and 6x compression on the command channels.

## Cross References

- chunking_strategy.md fixes the L0 to L4 chunking pattern.
- sensor_specification_100khz.md fixes the 640 channel sensor stack that L1 to L4 aggregate.
- anastomosis_protocols.md fixes the per anastomosis event that L4 records.
- commit_04_iterations_1min.md fixes the 32 iteration sweep design.
- zenodo_archive_protocol.md fixes the L0 deposition layout that the pointer JSON references.
