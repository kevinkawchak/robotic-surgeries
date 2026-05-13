# XYZ Mapping Execution

This directory captures the live run output of the per arm xyz Cartesian command mapping pipeline at `../../codegen/src/mapping/sensor_to_xyz_8arm.py`. The 6 stage pipeline (sensor ingest, phase identification, per arm task identification, per arm target generation, safety zone gating, command emission) runs at the 10 kHz command channel rate and emits records that match the `xyz_command_8arm` schema family (JSON Schema, Protocol Buffers).

## Reproduction

```bash
cd 2030-pdac-1min/paper/codegen
PYTHONPATH=. python -m src.mapping.sensor_to_xyz_8arm \
  --seed 20260513 \
  --arm-id 1 \
  --duration-ms 100 \
  --output ../execution/xyz_mapping/xyz_command_sample.jsonl
```

## Files

| File | Description |
|------|-------------|
| `xyz_command_sample.jsonl` | Arm 1 command slice, 1001 records, Phase 5 first 100 ms |
| `per_arm_target_table.csv` | 8 arm by 8 phase target tip position table |
| `command_pipeline_summary.txt` | ASCII summary of the 6 stage pipeline |

## Headline Statistics (Phase 5, 100 ms, Arm 1, Seed 20260513)

| Statistic | Value |
|-----------|-------|
| Command record count | 1001 |
| Command enum distribution | EMIT x 1001 |
| Safety zone action distribution | clear x 1001 |
| Ring tension target (N) | 0.45 (PJ Phase 5) |
| Target linear velocity (mm/s) | 1200.0 (Phase 5 default) |
| Force clamp (N) | 3.0 (clear action default) |

## 7 State Command Enum Distribution Across the 8 Arm 8 Phase Trajectory Library

The xyz_command_8arm schema defines 7 command enums. Across the 8 arms and 8 phases plus the active arms by phase table, the command enum distribution at phase start is:

```
Enum             Description                                Active count
---------------------------------------------------------------------------
EMIT             active arm, clear safety zone               53
HOLD             active arm, soft warning zone                0
SLOW             active arm, soft warning velocity scale      0
PARK             arm transitioning out                        0
E_STOP           hard stop volume breach                      0
HEARTBEAT_ACK    inactive arm acknowledging 10 kHz bus       11
PHASE_BOUNDARY   transition tick across phase boundary        0
```

The 53 EMIT plus 11 HEARTBEAT_ACK total counts come from the per arm per phase active arm table at `../../codegen/config/project.yaml` (64 arm phase pairs across 8 arms x 8 phases, 53 active + 11 idle on the dominant target sample).
