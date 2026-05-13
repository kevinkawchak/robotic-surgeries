# XYZ Mapping Output (v0.6.0)

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../../releases.md)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.18445179-blue)](https://doi.org/10.5281/zenodo.18445179)
[![Command Rate](https://img.shields.io/badge/Command-10%20kHz-orange.svg)](../../data/xyz_command_sample_8arm.jsonl)

This directory contains the publication grade xyz mapping outputs for the v0.6.0 PDAC 1 minute 8 arm Whipple simulation.

## Per Arm Command Pipeline

The per arm xyz mapping pipeline at `../../src/mapping/sensor_to_xyz_8arm.py` runs at the 10 kHz command channel rate and has six stages:

1. Sensor ingest from `data/sensor_sample_8arm.jsonl`.
2. Phase identification from the tick index against the 8 phase 60 second timeline.
3. Per arm task identification from the per arm tool assignment table.
4. Per arm target generation from the per phase per task target trajectory library.
5. Safety zone gating through the 5 vessel safety zone gate plus the multi arm collision avoidance state machine plus the anastomosis ring tension control loop.
6. Command emission to `data/xyz_command_sample_8arm.jsonl`.

## Per Arm 7 State Command Enum

| Enum | Meaning |
|------|---------|
| EMIT | normal motion state |
| HOLD | pause motion at the current tip |
| SLOW | scale motion to 10 percent |
| PARK | retract the arm to the docking station |
| E_STOP | immediately halt motion at the current tip |
| HEARTBEAT_ACK | acknowledge the 10 kHz heartbeat broadcast without emitting motion |
| PHASE_BOUNDARY | record a phase transition marker without emitting motion |

## Cross References

- `../../schemas/xyz_command_8arm.{schema.json, proto}` fixes the per record schema.
- `../../src/mapping/sensor_to_xyz_8arm.py` fixes the mapping pipeline.
- `../../config/kinematics_8arm.yaml` fixes the per arm 7 DOF DH parameters.
- `../../src/control/robot_loop_8arm.cpp` fixes the per arm Cartesian command emitter.
- `../../src/coordination/arm_heartbeat_10khz.cpp` fixes the 10 kHz broadcast bus.
