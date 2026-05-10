# Coordinate Mapping (4 Cooperating Arms)

## Mapping Rule Overview

Each per-arm `tick_us` MIXED record produces zero or one `XYZCommand` for that arm. FORCE_ONLY records do not produce commands; they update the local force monitor only. Across the 60-second procedure each arm emits up to 60,000 xyz commands (one per ms); the actual count depends on the per-phase strategy below.

## Phase-Conditioned Mapping per Arm

- Phase 1 (0 to 5 s): all 4 arms emit position-hold commands; arm 4 emits image-trigger commands at 30 Hz.
- Phase 2 (5 to 45 s): arm 1 emits 1 kHz cut commands; arm 2 emits 1 kHz coagulate commands; arm 3 emits 100 Hz suction commands; arm 4 emits 30 Hz image commands.
- Phase 3 (45 to 55 s): arm 1 reduces commanded velocity by 75 percent; arm 4 increases image cadence to 100 Hz.
- Phase 4 (55 to 60 s): arms 1 and 3 emit retract trajectories; arm 2 emits final hemostasis pass; arm 4 emits final margin scan.

## Forward Kinematics per Arm

The NeuroSpeed 1.0 has 7 DOF per arm. The DH parameter table lives in `config/kinematics_4arm.yaml`. The forward kinematics computes (ee_x, ee_y, ee_z, ee_qw, ee_qx, ee_qy, ee_qz) from the joint position vector (j1_pos, ..., j7_pos).

## Inverse Kinematics per Arm

A numerical 7-DOF solver with 6-DOF redundancy (the 7th DOF is used for collision avoidance and posture optimization) takes a desired end-effector pose and returns a joint position vector. The solver uses Levenberg-Marquardt with 0.1 mm tolerance and a 5 microsecond per-call wall budget on the conventional high-end server profile.

## Per-Arm Safety Zone Gating

- FORBIDDEN: command is clamped to the boundary, cross-arm emergency-park is triggered.
- ELOQUENT: commanded velocity is reduced to 25 percent of nominal.
- TUMOR_CORE: commanded velocity proceeds at nominal.
- Other zones: pass through unmodified.

## Per-Arm Force Feedback Fusion

The mapper reads the most recent 10 kHz force sample and clamps commanded velocity if force exceeds 80 percent of the per-arm 5.0 N tip force limit (4.0 N tip).

## Cumulative Force Enforcement

The mapper reads per-arm force frames from the heartbeat broadcast and clamps each arm's commanded velocity proportionally if the cumulative exceeds 11.0 N (1 N margin under the 12 N cap).

## Command Latency Budget per Arm

1 ms end-to-end from sensor sample arrival to first commanded actuator update. Of that budget:

- 0.1 ms for inverse kinematics solve.
- 0.5 ms for cross-arm coordination read.
- 0.4 ms for actuator write.

The 1 ms budget is 5 times tighter than the parent 5 ms budget because the 1,000 mm per second arm velocity demands 5 times finer command quantization.

## Cross-References

- `schemas/xyz_command_4arm.schema.json`: per-arm xyz command JSON Schema.
- `src/control/robot_loop_4arm.cpp`: C++20 real-time control loop.
- `src/coordination/arm_heartbeat.cpp`: C++20 heartbeat coordination layer.
- `docs/multi_arm_coordination.md`: heartbeat protocol and cumulative force limit.
