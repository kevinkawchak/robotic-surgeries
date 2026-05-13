# Commit 3: Cartesian XYZ Mapping (8 Arm)

This file fixes the Future Commit 3 file list and authoring instructions for the eight arm per arm xyz command mapping. The future Claude Code Opus 4.7 1M Max session reads this file to author the per arm xyz mapping pipeline at 2030-pdac-1min/src/mapping/sensor_to_xyz_8arm.py, the per arm command schema at 2030-pdac-1min/schemas/xyz_command_8arm.{schema.json, proto}, and the per arm 7 DOF DH parameter table at 2030-pdac-1min/config/kinematics_8arm.yaml.

## Purpose of Cartesian XYZ Mapping

The sensor record (from sensor_specification_100khz.md) is per arm in joint space (q1 to q7, qd1 to qd7, tau1 to tau7) plus per arm in Cartesian space (ee_pos, ee_quat, ee_vel, ee_force, ee_torque). The Cartesian xyz command stream is the inverse: a per arm sequence of target tip positions (x, y, z), target tip orientations (quaternion), target tip linear velocities, and per arm tool state transitions, all expressed in the patient frame (origin = umbilicus). The mapping converts sensor to Cartesian command at the 10 kHz command channel rate, applies the vascular safety zone gate (vascular_safety_protocol.md), applies the multi arm collision avoidance state machine (multi_arm_coordination_8arm.md), applies the anastomosis ring tension control loop (anastomosis_protocols.md), and emits per arm xyz commands to the per arm robot control loop at 2030-pdac-1min/src/control/robot_loop_8arm.cpp.

## Per Arm Command Record Schema

The per arm xyz command record is per tick (10 kHz, 100 microsecond tick). The record schema is reproduced below in JSON Schema notation; the Protocol Buffers schema at 2030-pdac-1min/schemas/xyz_command_8arm.proto is derived from this notation.

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "xyz_command_8arm.schema.json",
  "type": "object",
  "required": ["tick", "arm_id", "phase", "target_pos", "target_quat", "target_linear_vel", "force_clamp", "tool_state_transition", "safety_zone_action", "collision_state", "ring_tension_target", "command_enum"],
  "properties": {
    "tick": {"type": "integer", "description": "100 microsecond tick index, 0 to 599999"},
    "arm_id": {"type": "integer", "minimum": 1, "maximum": 8},
    "phase": {"type": "integer", "minimum": 1, "maximum": 8},
    "target_pos": {"type": "array", "items": {"type": "number"}, "minItems": 3, "maxItems": 3, "description": "x, y, z in mm in patient frame"},
    "target_quat": {"type": "array", "items": {"type": "number"}, "minItems": 4, "maxItems": 4, "description": "qx, qy, qz, qw quaternion"},
    "target_linear_vel": {"type": "number", "description": "mm/s, 0 to 1,200"},
    "force_clamp": {"type": "number", "description": "N, 0.0 to 3.0"},
    "tool_state_transition": {"type": "string", "enum": ["idle", "approach", "engage", "coag", "cut", "suction", "suture", "withdraw"]},
    "safety_zone_action": {"type": "string", "enum": ["clear", "no_fly", "soft_warning", "hard_stop"]},
    "collision_state": {"type": "string", "enum": ["clear", "proximity", "contact", "unsafe"]},
    "ring_tension_target": {"type": "number", "description": "N, 0.0 to 1.0"},
    "command_enum": {"type": "string", "enum": ["EMIT", "HOLD", "SLOW", "PARK", "E_STOP", "HEARTBEAT_ACK", "PHASE_BOUNDARY"]}
  }
}
```

The seven state command enum is identical across all eight arms. The EMIT state is the normal motion state; HOLD pauses motion at the current tip; SLOW scales motion to 10 percent; PARK retracts the arm to the docking station; E_STOP immediately halts motion at the current tip; HEARTBEAT_ACK acknowledges the 10 kHz heartbeat broadcast without emitting motion; PHASE_BOUNDARY records a phase transition marker without emitting motion.

## Per Arm 7 DOF DH Parameter Table

The eight arms of the Medtronic PancreSpeed 1.0 platform are identical in mechanical design; the per arm 7 DOF DH parameter table is therefore reproduced once and applied to all eight arms with a per arm base frame offset.

| Link i | a_i (mm) | alpha_i (deg) | d_i (mm) | theta_i offset (deg) | Joint range (deg) | Max velocity (deg/s) | Max torque (N.m) |
|--------|----------|---------------|----------|----------------------|-------------------|----------------------|-------------------|
| 1 | 0 | 90 | 360 | 0 | -180 to +180 | 540 | 320 |
| 2 | 0 | -90 | 0 | 0 | -135 to +135 | 540 | 320 |
| 3 | 0 | 90 | 420 | 0 | -180 to +180 | 540 | 200 |
| 4 | 0 | -90 | 0 | 0 | -135 to +135 | 540 | 200 |
| 5 | 0 | 90 | 400 | 0 | -180 to +180 | 720 | 80 |
| 6 | 0 | -90 | 0 | 0 | -135 to +135 | 720 | 80 |
| 7 | 0 | 0 | 126 | 0 | -360 to +360 | 720 | 40 |

The per arm 7 DOF kinematic chain yields a workspace radius of approximately 1.3 meters at the tip, with a peak tip linear velocity of 1,200 mm/s at the 6th joint maximum angular velocity of 720 deg/s. The per arm positioning accuracy at 1,200 mm/s is 0.05 mm RMS in the patient frame, which is 2x finer than the v3.9.1 GBM NeuroSpeed 1.0 0.1 mm RMS specification at the same velocity.

## Per Arm Base Frame Offset

The eight arms have fixed base frame offsets in the patient frame. The base frame is the geometric center of the per arm shoulder joint. The base frame offsets are below.

| Arm | Base x (mm) | Base y (mm) | Base z (mm) | Base orientation (deg, yaw from patient longitudinal axis) |
|-----|-------------|-------------|-------------|--------------------------------------------------------------|
| 1 | +400 | -200 | +300 | -22.5 |
| 2 | +400 | +200 | +300 | -22.5 |
| 3 | +400 | -400 | +200 | -22.5 |
| 4 | +400 | +400 | +200 | -22.5 |
| 5 | -400 | -200 | +300 | +22.5 |
| 6 | -400 | +200 | +300 | +22.5 |
| 7 | -400 | -400 | +200 | +22.5 |
| 8 | -400 | +400 | +200 | +22.5 |

The per arm base frame offsets place arms 1 to 4 on the patient right side and arms 5 to 8 on the patient left side. The base frame yaw of +/- 22.5 degrees centers the per arm workspace on the upper abdomen vasculature. The per arm base frame offsets are part of the deterministic seed contract.

## XYZ Command Generator Pipeline

The future Claude Code session authors the per arm xyz command generator at 2030-pdac-1min/src/mapping/sensor_to_xyz_8arm.py. The pipeline has six stages, ordered from sensor input to xyz command output:

1. Sensor ingest. The 640 channel sensor record at the 100 kHz force plus 10 kHz command rate is read from 2030-pdac-1min/data/sensor_sample_8arm.jsonl.
2. Phase identification. The current 8 phase index is identified by the tick index and the phase boundary table in pdac_context_1min.md.
3. Per arm task identification. The per arm task is identified by the per arm tool assignment table in sensor_specification_100khz.md.
4. Per arm target generation. The per arm target tip position, target tip orientation, target linear velocity, and target ring tension are generated from the per phase per task target trajectory.
5. Safety zone gating. The per arm target tip position is gated through the vascular safety zone gate at vascular_safety_protocol.md and the multi arm collision avoidance state machine at multi_arm_coordination_8arm.md.
6. Command emission. The per arm xyz command record is written to 2030-pdac-1min/data/xyz_command_sample_8arm.jsonl at the 10 kHz command rate.

## Per Arm Per Phase Trajectory Library

The per arm per phase target trajectory is a fixed sequence of waypoints in the patient frame. The trajectory library is stored at 2030-pdac-1min/config/per_arm_trajectory_library.yaml and is part of the deterministic seed contract. The library contains 64 trajectories (8 arms times 8 phases) plus 24 anastomosis sub trajectories (8 arms times 3 anastomoses, where only arms 1, 2, 3, 4, 5 are active during Phases 5 and 6 and only arms 1, 2, 3, 4 are active during Phase 7).

## Cross References

- pdac_context_1min.md fixes the 8 phase timeline and the per arm tool assignment.
- sensor_specification_100khz.md fixes the 640 channel sensor stack.
- multi_arm_coordination_8arm.md fixes the cross arm e stop latency budget.
- vascular_safety_protocol.md fixes the per vessel safety volumes that the xyz command gate enforces.
- anastomosis_protocols.md fixes the per anastomosis ring tension targets that the xyz command emitter tracks.
- commit_04_iterations_1min.md fixes the 32 iteration sweep that the xyz command pipeline is benchmarked across.
