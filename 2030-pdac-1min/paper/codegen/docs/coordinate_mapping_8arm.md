# Coordinate Mapping Overview (8 Arm, 7 DOF DH)

This document fixes the per arm 7 DOF Denavit Hartenberg parameter table and the per arm base frame offset for the eight arm PancreSpeed 1.0 platform. The full xyz command record schema lives at `../../instructions/commit_03_xyz_8arm.md`; this overview document orients the codegen tree.

## Per Arm 7 DOF DH Parameters

| Link i | a_i (mm) | alpha_i (deg) | d_i (mm) | theta_i offset (deg) | Joint range (deg) | Max velocity (deg/s) | Max torque (N.m) |
|--------|----------|---------------|----------|----------------------|-------------------|----------------------|-------------------|
| 1 | 0 | 90 | 360 | 0 | -180 to +180 | 540 | 320 |
| 2 | 0 | -90 | 0 | 0 | -135 to +135 | 540 | 320 |
| 3 | 0 | 90 | 420 | 0 | -180 to +180 | 540 | 200 |
| 4 | 0 | -90 | 0 | 0 | -135 to +135 | 540 | 200 |
| 5 | 0 | 90 | 400 | 0 | -180 to +180 | 720 | 80 |
| 6 | 0 | -90 | 0 | 0 | -135 to +135 | 720 | 80 |
| 7 | 0 | 0 | 126 | 0 | -360 to +360 | 720 | 40 |

The per arm 7 DOF kinematic chain yields a workspace radius of approximately 1.3 m at the tip and a peak tip linear velocity of 1,200 mm/s at the 6th joint maximum angular velocity of 720 deg/s. The per arm positioning accuracy at 1,200 mm/s is 0.05 mm RMS in the patient frame.

## Per Arm Base Frame Offset

| Arm | Base x (mm) | Base y (mm) | Base z (mm) | Base yaw (deg) | Side |
|-----|-------------|-------------|-------------|----------------|------|
| 1 | +400 | -200 | +300 | -22.5 | right |
| 2 | +400 | +200 | +300 | -22.5 | right |
| 3 | +400 | -400 | +200 | -22.5 | right |
| 4 | +400 | +400 | +200 | -22.5 | right |
| 5 | -400 | -200 | +300 | +22.5 | left |
| 6 | -400 | +200 | +300 | +22.5 | left |
| 7 | -400 | -400 | +200 | +22.5 | left |
| 8 | -400 | +400 | +200 | +22.5 | left |

The per arm base frame offsets place arms 1 to 4 on the patient right side and arms 5 to 8 on the patient left side. The base frame yaw of plus or minus 22.5 degrees centers the per arm workspace on the upper abdomen vasculature.

## Per Arm XYZ Command Enum

The per arm xyz command record uses a 7 state command enum identical across all eight arms:

| Enum | Meaning |
|------|---------|
| EMIT | normal motion state |
| HOLD | pause motion at the current tip |
| SLOW | scale motion to 10 percent |
| PARK | retract the arm to the docking station |
| E_STOP | immediately halt motion at the current tip |
| HEARTBEAT_ACK | acknowledge the 10 kHz heartbeat broadcast without emitting motion |
| PHASE_BOUNDARY | record a phase transition marker without emitting motion |

## Per Arm XYZ Mapping Pipeline

The per arm xyz mapping pipeline at `src/mapping/sensor_to_xyz_8arm.py` has six stages: sensor ingest, phase identification, per arm task identification, per arm target generation, safety zone gating, and command emission. Each stage runs at the 10 kHz command channel rate.

## Cross References

- `../../instructions/commit_03_xyz_8arm.md` fixes the per arm xyz command record schema.
- `../../instructions/robot_specification_pancrespeed.md` fixes the per arm 7 DOF kinematic chain.
- `../../instructions/vascular_safety_protocol.md` fixes the safety zone gate inputs.
- `../../instructions/anastomosis_protocols.md` fixes the per anastomosis ring tension targets.
