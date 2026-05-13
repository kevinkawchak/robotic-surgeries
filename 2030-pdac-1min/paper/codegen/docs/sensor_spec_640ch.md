# Sensor Specification Overview (640 Channels)

This document fixes the 80 channel per arm sensor stack times 8 arms equals 640 channels at mixed 10 kHz command plus 100 kHz force resolution. The full per channel breakdown lives at `../../instructions/sensor_specification_100khz.md`; this overview document orients the codegen tree.

## Channel Groups (Per Arm, 80 Channels)

| Group | Channels | Rate | Width |
|-------|----------|------|-------|
| Joint position q1 to q7 | 7 | 10 kHz | 24 bit |
| Joint velocity qd1 to qd7 | 7 | 10 kHz | 24 bit |
| Joint torque tau1 to tau7 | 7 | 10 kHz | 24 bit |
| End effector position xyz | 3 | 10 kHz | 0.01 mm |
| End effector quaternion qxyzw | 4 | 10 kHz | 1e-6 |
| End effector linear velocity | 3 | 10 kHz | 0.1 mm/s |
| End effector force Fxyz | 3 | 100 kHz | 0.01 N |
| End effector torque Txyz | 3 | 100 kHz | 0.001 N.m |
| Tool state enum | 1 | 10 kHz | 8 state |
| Tool subtype | 1 | 10 kHz | 16 bit |
| Bipolar current | 1 | 10 kHz | 0.1 mA |
| Bipolar voltage | 1 | 10 kHz | 0.1 V |
| Suction pressure | 1 | 10 kHz | 0.01 kPa |
| Suction flow | 1 | 10 kHz | 0.01 mL/s |
| Irrigation flow | 1 | 10 kHz | 0.01 mL/s |
| Vessel surface proximity (PDAC) | 1 | 100 kHz | 0.01 mm |
| NIR ICG intensity 4 ch (PDAC) | 4 | 10 kHz | 16 bit |
| Pancreatic duct manometry (PDAC) | 1 | 10 kHz | 0.1 mmHg |
| Anastomosis ring tension (PDAC) | 1 | 10 kHz | 0.01 N |
| Bile spectrophotometry 4 ch (PDAC) | 4 | 10 kHz | 16 bit |
| Ultrasound B mode 8 element (PDAC) | 8 | 10 kHz | 12 bit |
| Heartbeat sequence + watchdog | 2 | 10 kHz | 32 bit |
| Per arm tip force scalar | 1 | 100 kHz | 0.01 N |
| Cumulative cross arm tip force | 1 | 100 kHz | 0.01 N |
| Per arm force time integral | 1 | 100 kHz | 0.001 N.s |
| Per arm tool engagement depth | 1 | 10 kHz | 0.01 mm |
| Per arm e stop state | 1 | 100 kHz | 4 state |
| Per arm temperature | 1 | 10 kHz | 0.1 deg C |
| Per arm power | 1 | 10 kHz | 0.1 W |
| Per arm collision state | 1 | 10 kHz | 4 state |
| Per arm tool changer state | 1 | 10 kHz | 16 state |
| Per arm task id | 1 | 10 kHz | 32 bit |
| Per arm phase id | 1 | 10 kHz | 4 bit |
| Per arm command queue depth | 1 | 10 kHz | 16 bit |
| Total per arm | 80 | mixed | mixed |

## Publication Sample Slice

The publication sample slice at `outputs/sensors/sensor_sample_8arm.csv` is 81 columns (1 tick + 80 channels) by 1001 rows. The 1001 rows are the first 100 milliseconds of Phase 5 pancreaticojejunostomy stitch sub task for arm 1, sampled at 10 kHz for the command channels and decimated from 100 kHz to 10 kHz for the force channels.

## Schema Files

The per record schema is published in three formats at `schemas/`:

- `sensor_record_8arm.schema.json` (JSON Schema, draft 2020-12)
- `sensor_record_8arm.proto` (Protocol Buffers proto3)
- `sensor_record_8arm.avsc` (Apache Avro 1.11)

All three formats are kept bit identical for the same record; the proto3 and avsc formats are derived from the JSON Schema by the codegen pipeline.

## Cross References

- `../../instructions/sensor_specification_100khz.md` fixes the full 80 channel per arm breakdown.
- `../../instructions/multi_arm_coordination_8arm.md` fixes the 10 kHz heartbeat broadcast bus.
- `../../instructions/file_size_pyramid_1min.md` fixes the per iteration committed budget.
