# Sensor Specification (4 Arms, Mixed 1 kHz / 10 kHz Force)

## Per-Arm Channel Inventory

The Medtronic NeuroSpeed 1.0 emits 50 channels per arm at mixed sample rates. The 4-arm total is 200 channels.

### Group 1: Joint Kinematics at 1 kHz (21 channels per arm)

| Channel ID | Quantity | Unit | Sample rate | Resolution |
|------------|----------|------|-------------|------------|
| j1_pos to j7_pos | Joint positions 1 to 7 | radian | 1 kHz | 8.7e-5 rad |
| j1_vel to j7_vel | Joint velocities 1 to 7 | radian per second | 1 kHz | 8.7e-5 rad/s |
| j1_trq to j7_trq | Joint torques 1 to 7 | newton meter | 1 kHz | 0.001 Nm |

### Group 2: End-Effector Pose at 1 kHz (7 channels per arm)

| Channel ID | Quantity | Unit | Sample rate | Resolution |
|------------|----------|------|-------------|------------|
| ee_x, ee_y, ee_z | End-effector position | millimeter | 1 kHz | 0.01 mm |
| ee_qw, ee_qx, ee_qy, ee_qz | End-effector orientation | unit quaternion | 1 kHz | 1e-5 |

### Group 3: End-Effector Force and Torque at 10 kHz (6 channels per arm)

| Channel ID | Quantity | Unit | Sample rate | Resolution |
|------------|----------|------|-------------|------------|
| ee_fx, ee_fy, ee_fz | End-effector force | newton | 10 kHz | 0.001 N |
| ee_tx, ee_ty, ee_tz | End-effector torque | newton meter | 10 kHz | 0.0001 Nm |

### Group 4: Navigation Deviation at 1 kHz (3 channels per arm)

| Channel ID | Quantity | Unit | Sample rate | Resolution |
|------------|----------|------|-------------|------------|
| nav_dx, nav_dy, nav_dz | Navigation deviation from plan | millimeter | 1 kHz | 0.01 mm |

### Group 5: Tool Flags and Adjuncts at 1 kHz (7 channels per arm)

| Channel ID | Quantity | Unit | Sample rate | Resolution | Notes |
|------------|----------|------|-------------|------------|-------|
| ttip_temp | Tool tip temperature | degree Celsius | 1 kHz | 0.1 C | Thermocouple |
| irr_flow | Irrigation flow rate | mL per minute | 1 kHz | 1 mL/min | Arms 2 and 3 only |
| suc_flow | Suction flow rate | mL per minute | 1 kHz | 1 mL/min | Arm 3 only |
| co2_insuf | CO2 insufflation | n/a | n/a | n/a | Reserved, held at 0.0 |
| us_present | Ultrasound active flag | boolean | 1 kHz | 1 bit | Arm 4 only |
| ala_uv | 5-ALA UV active flag | boolean | 1 kHz | 1 bit | Arm 4 only |
| imri_active | iMRI scan active flag | boolean | 1 kHz | 1 bit | Arm 4 only |

### Group 6: Safety Enums and Metadata at 1 kHz (6 channels per arm)

| Channel ID | Quantity | Unit | Sample rate | Resolution | Notes |
|------------|----------|------|-------------|------------|-------|
| estop_state | E-stop circuit state | boolean | 1 kHz | 1 bit | 0 nominal, 1 engaged |
| safety_zone | Safety zone classification | enum | 1 kHz | 8 levels | NONE, OUTER, INNER, ELOQUENT, FORBIDDEN, TUMOR_CORE, TUMOR_MARGIN, VESSEL |
| robot_state | Task-order lifecycle state | enum | 1 kHz | 8 levels | IDLE, SETUP, DOCKED, READY, ACTIVE, PAUSE, COMPLETE, ABORT |
| arm_id | Arm identifier | enum | 1 kHz | 4 levels | ARM_1, ARM_2, ARM_3, ARM_4 |
| heartbeat_ok | Inter-arm heartbeat status flag | boolean | 1 kHz | 1 bit | 1 nominal, 0 missed |
| tick_align_flag | Mixed tick alignment flag | boolean | 1 kHz | 1 bit | 1 if 50 channels, 0 if force-only |

## Sample Rate

- Per-arm mixed: 1 kHz commands plus 10 kHz force.
- Mixed tick at 1 kHz carries all 50 channels (record_kind = MIXED).
- 9 force-only ticks per millisecond carry only the 6 force channels (record_kind = FORCE_ONLY).
- Across 4 arms the multiplexed stream emits 40,000 records per second.

## Tick Alignment

The monotonic microsecond timestamp begins at 0 at the start of Phase 1 (procedure start). The first MIXED tick is 0; the last MIXED tick is 59,999,000. The 9 FORCE_ONLY ticks per millisecond fill the sub-millisecond positions at tick_us mod 1000 in {100, 200, 300, 400, 500, 600, 700, 800, 900}.

## Per-Channel Units and Tolerances

All units, ranges, and resolutions are listed in the per-group tables above. The validation rules below enforce the ranges.

## Per-Arm Coordinate Frame and Quaternion Convention

- World frame origin: Mayfield clamp pin midpoint, shared across all 4 arms.
- Positive X: patient left.
- Positive Y: patient anterior.
- Positive Z: patient superior.
- Quaternion convention: scalar-first (qw, qx, qy, qz).

## Validation Rules

- `tick_us` is a non-negative integer in [0, 60_000_000].
- `arm_id` is one of ARM_1, ARM_2, ARM_3, ARM_4.
- `record_kind` is one of MIXED, FORCE_ONLY.
- For MIXED records, `tick_us` mod 1000 equals 0 and all 50 channels are present.
- For FORCE_ONLY records, `tick_us` mod 100 equals 0 and `tick_us` mod 1000 is not 0; only the 6 force channels are present.
- All force values fall within +/- 50 N.
- All torque values fall within +/- 5 Nm.
- Per-arm tip force enforced under 5.0 N.
- Cumulative ee force across all 4 arms at the same tick_us must remain under 12 N.
- `safety_zone` is one of NONE, OUTER, INNER, ELOQUENT, FORBIDDEN, TUMOR_CORE, TUMOR_MARGIN, VESSEL.
- `robot_state` is one of IDLE, SETUP, DOCKED, READY, ACTIVE, PAUSE, COMPLETE, ABORT.

## Stream Framing per Arm

Each tick is one record. Record boundaries are newlines in JSONL and length-prefixed in Protocol Buffers binary form. The 4 arms are multiplexed by ascending tick_us then ascending arm_id.

## Storage Estimate

Per-iteration L0 raw: 26 MB across 4 arms at mixed 1 kHz plus 10 kHz force across 60 seconds. Across 16 iterations: 416 MB. The L0 raw is archived to Zenodo per `zenodo_archive_protocol.md` and is never committed to Git.

## Per-Arm Dropped Tick Reconstruction Policy

- Missing FORCE_ONLY ticks within a 1 ms window are linearly interpolated from the surrounding samples.
- Missing MIXED ticks are flagged as a gap and trigger an emergency arm-park per the multi-arm coordination protocol.
- Gap detection: any inter-arrival time exceeding 200 microseconds for FORCE_ONLY or 1.5 ms for MIXED triggers a gap report log entry.
- Gap report log: `logs/sensor_gap_report.jsonl` with one record per detected gap.

## Cross-References

- `schemas/sensor_record_4arm.schema.json`: JSON Schema 2020-12.
- `schemas/sensor_record_4arm.proto`: Protocol Buffers 3.
- `schemas/sensor_record_4arm.avsc`: Apache Avro JSON.
- `src/sensors/ingest_4arm.py`: Python 3.10 ingest script that validates and emits samples.
- `docs/file_size_pyramid_1min.md`: per-iteration L0 to L3 plus events budget.
