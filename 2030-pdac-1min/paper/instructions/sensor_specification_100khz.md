# Sensor Specification (100 kHz Force, 10 kHz Command, 640 Channel, 8 Arm)

This file fixes the sensor stack for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to author the per arm and per channel sensor ingest pipeline at 2030-pdac-1min/src/sensors/ingest_8arm.py and the per channel schema at 2030-pdac-1min/schemas/sensor_record_8arm.{schema.json, proto, avsc}.

## Per Arm Channel Count

Each of the eight arms carries 80 channels. The total channel count is 80 channels per arm times 8 arms equals 640 total channels. The per arm 80 channel breakdown is fixed below and is identical across all eight arms unless noted otherwise in the per arm tool assignment table.

| Channel group | Channel count | Sample rate | Resolution | Purpose |
|---------------|---------------|-------------|------------|---------|
| Joint position (7 DOF, q1 to q7, radians) | 7 | 10 kHz | 24 bit | Per joint position feedback |
| Joint velocity (7 DOF, q1 dot to q7 dot, rad/s) | 7 | 10 kHz | 24 bit | Per joint angular velocity feedback |
| Joint torque (7 DOF, tau1 to tau7, N.m) | 7 | 10 kHz | 24 bit | Per joint torque feedback |
| End effector position (x, y, z, mm) | 3 | 10 kHz | 0.01 mm | Cartesian tip position |
| End effector orientation (qx, qy, qz, qw, quaternion) | 4 | 10 kHz | 1e-6 | Cartesian tip orientation |
| End effector linear velocity (mm/s) | 3 | 10 kHz | 0.1 mm/s | Cartesian tip velocity |
| End effector force (Fx, Fy, Fz, N) | 3 | 100 kHz | 0.01 N | Force feedback at 100 kHz (10x finer than v3.9.1 GBM) |
| End effector torque (Tx, Ty, Tz, N.m) | 3 | 100 kHz | 0.001 N.m | Moment feedback at 100 kHz |
| Tool state enum (idle / approach / engage / coag / cut / suction / suture / withdraw) | 1 | 10 kHz | 8 state | Per arm tool state machine |
| Tool subtype (specific tool model) | 1 | 10 kHz | 16 bit | Per arm installed tool identification |
| Bipolar coagulation current (mA) | 1 | 10 kHz | 0.1 mA | Per arm bipolar generator current |
| Bipolar coagulation voltage (V) | 1 | 10 kHz | 0.1 V | Per arm bipolar generator voltage |
| Suction pressure (kPa) | 1 | 10 kHz | 0.01 kPa | Per arm suction pump pressure |
| Suction flow (mL/s) | 1 | 10 kHz | 0.01 mL/s | Per arm suction flow rate |
| Irrigation flow (mL/s) | 1 | 10 kHz | 0.01 mL/s | Per arm irrigation flow rate |
| Vessel surface proximity (mm) | 1 | 100 kHz | 0.01 mm | PDAC specific. Distance from tip to nearest named vessel surface. |
| NIR indocyanine green intensity (counts) | 4 | 10 kHz | 16 bit | PDAC specific. Four channel near infrared imaging at 800 nm. |
| Pancreatic duct manometry (mmHg) | 1 | 10 kHz | 0.1 mmHg | PDAC specific. Used during Phase 5 pancreaticojejunostomy. |
| Anastomosis ring tension (N) | 1 | 10 kHz | 0.01 N | PDAC specific. Used during Phases 5, 6, 7. |
| Bile spectrophotometry (a.u. at 410, 470, 532, 600 nm) | 4 | 10 kHz | 16 bit | PDAC specific. Used during Phase 6 hepaticojejunostomy bile leak detection. |
| Ultrasound B mode amplitude (8 element linear, dB) | 8 | 10 kHz | 12 bit | PDAC specific. Used for vessel mapping and margin scan. |
| Heartbeat counter (sequence number) | 1 | 10 kHz | 32 bit | Per arm 10 kHz heartbeat broadcast sequence. |
| Heartbeat watchdog (microseconds since last broadcast) | 1 | 10 kHz | 32 bit | Per arm 10 kHz heartbeat broadcast watchdog. |
| Per arm tip force scalar (N) | 1 | 100 kHz | 0.01 N | Per arm scalar magnitude of force vector. |
| Cumulative cross arm tip force (N) | 1 | 100 kHz | 0.01 N | Cross arm sum of tip force magnitudes. |
| Per arm cumulative force-time integral (N.s) | 1 | 100 kHz | 0.001 N.s | Per arm integral of tip force over phase duration. |
| Per arm tool engagement depth (mm) | 1 | 10 kHz | 0.01 mm | Per arm tool insertion depth at tip. |
| Per arm e stop state | 1 | 100 kHz | 4 state (idle / armed / triggered / parked) | Per arm emergency stop state. |
| Per arm temperature (deg C) | 1 | 10 kHz | 0.1 deg C | Per arm internal temperature. |
| Per arm power consumption (W) | 1 | 10 kHz | 0.1 W | Per arm motor power consumption. |
| Per arm collision avoidance state | 1 | 10 kHz | 8 state (clear / proximity / contact / unsafe) | Per arm proximity to nearest neighbor arm. |
| Per arm tool changer state | 1 | 10 kHz | 16 state | Per arm tool changer carousel state. |
| Per arm task identifier | 1 | 10 kHz | 32 bit | Per arm current task identifier in the 8 phase timeline. |
| Per arm phase identifier | 1 | 10 kHz | 4 bit | Per arm current phase (1 to 8). |
| Per arm command queue depth | 1 | 10 kHz | 16 bit | Per arm pending command queue depth. |
| Total per arm channel count | 80 | mixed | mixed | The per arm channel sum. |

The per arm 80 channels times 8 arms equals 640 total channels per simulation tick.

## Per Arm Tool Assignment for the PDAC Procedure

The per arm tool assignment table fixes which tool each of the eight arms carries during the 60 second procedure. The tool assignment is identical across all 32 iterations and is part of the deterministic seed contract.

| Arm | Tool | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Phase 6 | Phase 7 | Phase 8 |
|-----|------|---------|---------|---------|---------|---------|---------|---------|---------|
| 1 | Hybrid ultrasonic-water-plasma scalpel + needle driver | Kocher | SMV dissect | Uncinate dissect | Specimen | PJ stitch | HJ stitch | GJ stitch | Withdraw |
| 2 | Bipolar coagulator + needle driver | Mobilize | PV dissect | Mesentery retract | Specimen | PJ stitch | HJ stitch | GJ stitch | Hemostasis |
| 3 | Articulated retractor + grasper | Retract duodenum | Hepatic artery control | Celiac axis | Hemostasis | PJ retract | HJ retract | GJ retract | Withdraw |
| 4 | Linear 8 element ultrasound + iMRI probe + NIR imaging | Vessel map | Vessel map | Vessel map | Margin scan | Imaging | Bile leak NIR | Patency | Final scan |
| 5 | Bipolar coagulator + suction | Stand by | Branch coag | Stand by | Margin verify | Ring tension monitor | Bile leak NIR | Stand by | Drain placement |
| 6 | Suction + bipolar coag | Stand by | Branch coag | Stand by | Margin verify | Bowel loop stabilize | Bowel loop stabilize | Stand by | Drain placement |
| 7 | Suction + irrigation | Stand by | Suction | Stand by | Margin verify | Bowel loop stabilize | Bowel loop stabilize | Stand by | Patency confirm |
| 8 | NIR imaging + 5-ALA UV + sample collector | Stand by | Imaging | Stand by | Margin verify | Bowel loop stabilize | Bowel loop stabilize | Stand by | Final NIR scan |

The per arm tool subtype channel records the tool model identifier; the per arm tool state enum records the per millisecond state machine value.

## Sample Record Schema (per tick)

The sensor record schema is per arm and per tick. The 80 channels per arm are flattened into a single record with a per arm prefix. The record schema is reproduced below in JSON Schema notation; the Protocol Buffers and Avro schemas at 2030-pdac-1min/schemas/sensor_record_8arm.{proto, avsc} are derived from this notation.

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "sensor_record_8arm.schema.json",
  "type": "object",
  "required": ["tick", "arm_id", "phase", "q", "qd", "tau", "ee_pos", "ee_quat", "ee_vel", "ee_force", "ee_torque", "tool_state", "tool_subtype", "bipolar_current", "bipolar_voltage", "suction_pressure", "suction_flow", "irrigation_flow", "vessel_proximity", "nir_icg", "duct_manometry", "ring_tension", "bile_spectrophotometry", "us_b_mode", "heartbeat_seq", "heartbeat_watchdog", "tip_force_scalar", "cumulative_cross_arm_force", "force_time_integral", "engagement_depth", "estop_state", "temperature", "power", "collision_state", "tool_changer_state", "task_id", "phase_id", "queue_depth"],
  "properties": {
    "tick": {"type": "integer", "description": "100 microsecond tick index, 0 to 599999"},
    "arm_id": {"type": "integer", "minimum": 1, "maximum": 8},
    "phase": {"type": "integer", "minimum": 1, "maximum": 8},
    "q": {"type": "array", "items": {"type": "number"}, "minItems": 7, "maxItems": 7},
    "qd": {"type": "array", "items": {"type": "number"}, "minItems": 7, "maxItems": 7},
    "tau": {"type": "array", "items": {"type": "number"}, "minItems": 7, "maxItems": 7},
    "ee_pos": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
    "ee_quat": {"type": "array", "items": {"type": "number"}, "minItems": 4, "maxItems": 4},
    "ee_vel": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
    "ee_force": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
    "ee_torque": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3},
    "tool_state": {"type": "string", "enum": ["idle", "approach", "engage", "coag", "cut", "suction", "suture", "withdraw"]},
    "tool_subtype": {"type": "integer"},
    "bipolar_current": {"type": "number"},
    "bipolar_voltage": {"type": "number"},
    "suction_pressure": {"type": "number"},
    "suction_flow": {"type": "number"},
    "irrigation_flow": {"type": "number"},
    "vessel_proximity": {"type": "number"},
    "nir_icg": {"type": "array", "items": {"type": "number"}, "minItems": 4, "maxItems": 4},
    "duct_manometry": {"type": "number"},
    "ring_tension": {"type": "number"},
    "bile_spectrophotometry": {"type": "array", "items": {"type": "number"}, "minItems": 4, "maxItems": 4},
    "us_b_mode": {"type": "array", "items": {"type": "number"}, "minItems": 8, "maxItems": 8},
    "heartbeat_seq": {"type": "integer"},
    "heartbeat_watchdog": {"type": "integer"},
    "tip_force_scalar": {"type": "number"},
    "cumulative_cross_arm_force": {"type": "number"},
    "force_time_integral": {"type": "number"},
    "engagement_depth": {"type": "number"},
    "estop_state": {"type": "string", "enum": ["idle", "armed", "triggered", "parked"]},
    "temperature": {"type": "number"},
    "power": {"type": "number"},
    "collision_state": {"type": "string", "enum": ["clear", "proximity", "contact", "unsafe"]},
    "tool_changer_state": {"type": "integer"},
    "task_id": {"type": "integer"},
    "phase_id": {"type": "integer"},
    "queue_depth": {"type": "integer"}
  }
}
```

## Sample Record CSV Slice

The future Claude Code session writes a publication grade sample slice at 2030-pdac-1min/outputs/sensors/sensor_sample_8arm.csv containing 81 columns by 1001 rows. The 81 columns are: 1 tick column plus 80 per arm channels (one arm at a time, for the per arm sample). The 1001 rows are the first 100 milliseconds of Phase 5 pancreaticojejunostomy stitch sub task, sampled at 10 kHz for the per arm command channels and downsampled from 100 kHz to 10 kHz for the force channels (decimate by 10, last sample retained). This sample mirrors the v3.9.1 GBM 54 by 1001 sample feat at 2030-gbm-1min/outputs/sensors/sensor_sample_4arm.csv, scaled to the PDAC 80 channel per arm width.

## Pyramid Output Schema

The per iteration committed Parquet pyramid has five layers. The full L0 raw is archived to Zenodo per zenodo_archive_protocol.md and is never committed to Git. The committed pyramid layers are documented in file_size_pyramid_1min.md.

| Layer | Tick rate | Window | Per iteration size (KB) | Purpose |
|-------|-----------|--------|-------------------------|---------|
| L0 (Zenodo only, not committed) | 100 kHz force, 10 kHz cmd | 60 s | 412,000 (412 MB) | Raw mixed rate stream per arm. |
| L1 (committed) | 50 Hz | 60 s (3,000 rows) | 480 (per arm) | Downsampled 10 kHz to 50 Hz; per arm Parquet. |
| L2 (committed) | 1 Hz | 60 s (60 rows) | 120 (per arm) | Per arm 1 second aggregate (mean, max, p95). |
| L3 (committed) | 1 row per phase | 8 rows | 64 (per arm) | Per phase aggregate (start, end, mean, max, violations). |
| L4 (committed, PDAC specific) | 1 row per anastomosis event | 3 rows | 24 (cross arm) | Per anastomosis ring tension stability, manometry stability, bile spectrophotometry signal. |
| Event log (committed) | event driven | per iteration | 32 (cross arm) | E stop, collision, vessel hard stop, anastomosis ring tension violation events. |

The per iteration committed total is 480 + 120 + 64 = 664 KB per arm times 8 arms equals 5.3 MB, plus 24 KB L4 plus 32 KB events equals 5.4 MB per iteration. Across 32 iterations that is 171 MB. The instruction set caps this at 33.4 MB total by retaining only L2, L3, L4, and events plus a single L1 sample for the publication arm. The pyramid budget is fixed in file_size_pyramid_1min.md.

## Sensor Calibration

Each 100 kHz force channel uses a 24 bit ADC with a +/- 50 N full scale range and a 10 microsecond settling time. Each 10 kHz command channel uses a 24 bit ADC with a +/- 2 pi radian full scale joint range and a 50 microsecond settling time. The vessel surface proximity sensor uses a confocal laser triangulation probe with 0.01 mm resolution at 100 kHz. The NIR indocyanine green sensor uses a four channel narrow band photodiode array centered at 800 nm with a 10 microsecond integration time. The pancreatic duct manometry sensor uses a fiber optic pressure sensor with 0.1 mmHg resolution and a 100 microsecond settling time. The bile spectrophotometry sensor uses a four channel narrow band photodiode array centered at 410, 470, 532, and 600 nm with a 10 microsecond integration time per channel.

## Cross References

- pdac_context_1min.md fixes the 8 phase timeline and the per arm tool assignment.
- multi_arm_coordination_8arm.md fixes the 10 kHz heartbeat broadcast contract.
- file_size_pyramid_1min.md fixes the per iteration committed budget.
- chunking_strategy.md fixes the L0 to L4 chunking pattern.
- commit_02_sensors_1min.md fixes the future Claude Code Commit 2 file list and authoring instructions.
