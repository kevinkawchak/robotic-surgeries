# Sensor Execution

This directory captures the live run output of the 640 channel sensor ingest pipeline at `../../codegen/src/sensors/ingest_8arm.py`. The publication arm sample slice covers the first 100 milliseconds of Phase 5 (pancreaticojejunostomy) at the 10 kHz command rate, producing exactly 1001 records that match the `sensor_record_8arm` JSON Schema.

## Reproduction

```bash
cd 2030-pdac-1min/paper/codegen
PYTHONPATH=. python -m src.sensors.ingest_8arm \
  --seed 20260513 \
  --arm-id 1 \
  --duration-ms 100 \
  --output ../execution/sensors/sensor_sample_8arm.jsonl
```

## Files

| File | Description |
|------|-------------|
| `sensor_sample_8arm.jsonl` | Arm 1 sample slice, 1001 records, Phase 5 first 100 ms |
| `per_arm_summary.csv` | Per arm tip force min/mean/max plus first ee_pos across the 100 ms sample |
| `channel_inventory.csv` | Per arm 80 channel inventory, totalling 640 channels across 8 arms |
| `sensor_channel_ascii.txt` | ASCII channel map of the 640 channel sensor stack |

## Headline Statistics (Phase 5, 100 ms, Arm 1, Seed 20260513)

| Statistic | Value |
|-----------|-------|
| Record count | 1001 |
| First tick | 3200000 |
| Last tick | 3210000 |
| Tip force min (N) | 0.5635 |
| Tip force mean (N) | 0.6186 |
| Tip force max (N) | 0.6671 |
| Force time integral max (N s) | 0.006185 |
| First ee_pos (mm) | (17.9953, -29.8968, -42.0012) |
| Ring tension nominal (N) | 0.45 (PJ Phase 5 target) |
| Phase boundary engagement | yes (Phase 5 active throughout) |

## Cross Arm Sample Snapshot

The 8 arm sample at Phase 5 produces deterministic per arm tip force and per arm ee_pos initial values. All 8 arms produce the same tip force range because the rng is seeded with `root_seed + arm_id` per arm independently, and the analytical signal is identical across arms; the spatial offsets differ per arm because the per arm base frame offset moves the tip position.

```
arm_id   tip_force_min   tip_force_mean   tip_force_max   first_ee_pos_mm
1        0.5635          0.6186           0.6671          (17.9953, -29.8968, -42.0012)
2        0.5635          0.6186           0.6671          (17.9392, -30.0772, -42.0427)
3        0.5635          0.6186           0.6671          (18.0911, -29.9737, -42.0257)
4        0.5635          0.6186           0.6671          (17.9068, -29.9729, -41.9712)
5        0.5635          0.6186           0.6671          (18.0608, -30.0800, -41.9477)
6        0.5635          0.6186           0.6671          (17.9955, -29.9024, -41.9998)
7        0.5635          0.6186           0.6671          (17.9453, -30.0764, -42.0443)
8        0.5635          0.6186           0.6671          (18.0956, -29.9695, -42.0292)
```

## Validation

The 1001 records were spot validated for schema conformity (every record has the 36 top level keys defined in `../../codegen/schemas/sensor_record_8arm.schema.json`), phase boundary correctness (phase=5 throughout the Phase 5 window), heartbeat monotonicity (`heartbeat_seq` matches `tick` rollover), and deterministic reproducibility (re running the command at the same seed yields a bit identical JSONL file).
