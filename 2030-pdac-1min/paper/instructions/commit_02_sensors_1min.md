# Commit 2: Sensor Specifications and Ingest Pipeline

This file fixes the Future Commit 2 file list and authoring instructions for the 640 channel sensor specification and ingest pipeline.

## Commit 2 File List

The future Commit 2 emits the following files at 2030-pdac-1min/.

| File | Purpose | Approx size |
|------|---------|-------------|
| schemas/sensor_record_8arm.schema.json | JSON Schema for the 640 channel sensor record | 8 KB |
| schemas/sensor_record_8arm.proto | Protocol Buffers schema | 4 KB |
| schemas/sensor_record_8arm.avsc | Avro schema | 6 KB |
| src/sensors/ingest_8arm.py | 640 channel sensor ingest pipeline | 12 KB |
| src/sensors/__init__.py | Package marker | 0.1 KB |
| data/sensor_sample_8arm.jsonl | 1001 row sample slice of one arm during Phase 5 PJ | 1 MB |
| data/sensor_sample_8arm.csv | Same as jsonl but in CSV format for human review | 800 KB |
| outputs/sensors/sensor_sample_8arm.csv | 81 column by 1001 row publication sample | 600 KB |
| outputs/sensors/per_arm_summary.csv | 80 channel by 8 arm per channel summary stats | 200 KB |
| outputs/sensors/README.md | Publication grade README for the sensors subdirectory | 4 KB |

## Commit 2 Authoring Order

1. Generate the three sensor record schemas (JSON Schema, Protocol Buffers, Avro) per the 80 channel per arm table in sensor_specification_100khz.md.
2. Generate the per arm 640 channel ingest pipeline in src/sensors/ingest_8arm.py per the per arm tool assignment table.
3. Generate the 1001 row sample slice in data/sensor_sample_8arm.jsonl for arm 1 during Phase 5 pancreaticojejunostomy (first 100 milliseconds, 10 kHz, then decimate to 50 Hz then upsample to 1001 rows).
4. Generate the publication sample slice in outputs/sensors/sensor_sample_8arm.csv with 81 columns (1 tick + 80 channels) and 1001 rows. This mirrors the v3.9.1 GBM 54 by 1001 sample feat scaled to 80 channels.
5. Generate the per arm summary stats in outputs/sensors/per_arm_summary.csv with 80 channels times 8 arms equals 640 rows and 6 columns (channel name, min, max, mean, std, p95).
6. Generate the publication grade README in outputs/sensors/README.md with DOI badges, channel inventory table, sample slice description, and cross references.

## Cross References

- sensor_specification_100khz.md fixes the 640 channel sensor stack.
- pdac_context_1min.md fixes the 8 phase timeline and per arm tool assignment.
- multi_arm_coordination_8arm.md fixes the 10 kHz heartbeat broadcast bus.
- file_size_pyramid_1min.md fixes the per iteration committed budget.
