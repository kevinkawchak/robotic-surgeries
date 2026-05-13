# Architecture Overview (8 Arm, 1 Minute Whipple)

This document fixes the high level architecture of the v0.6.0 PDAC 1 minute simulation. The pipeline reads per arm sensor records at mixed 10 kHz command plus 100 kHz force rates, applies the per arm xyz mapping with vascular safety and anastomosis gating, emits per arm xyz commands through a 10 kHz heartbeat broadcast bus, and records 32 iteration deterministic outcomes for the 4 entrant multi vendor LLM tournament.

## Pipeline Stages

```
+============================================================================+
|              2030-PDAC-1MIN ARCHITECTURE OVERVIEW (8 arm, 60 s)            |
+============================================================================+
|                                                                            |
|   +----------------+   +-----------------+   +-------------------------+   |
|   | sensor ingest  |-->| sensor to xyz   |-->| robot control loop      |   |
|   | 640 channels   |   | mapping +       |   | per arm 7 DOF           |   |
|   | 100 kHz force  |   | safety zone gate|   | 10 kHz Cartesian command|   |
|   | 10 kHz command |   | + anastomosis   |   | + heartbeat broadcast   |   |
|   +-------+--------+   +--------+--------+   +-----------+-------------+   |
|           |                     |                        |                 |
|           v                     v                        v                 |
|   +-------+--------+   +--------+--------+   +-----------+-------------+   |
|   | per iteration  |-->| per iteration   |-->| 4 entrant LLM tournament|   |
|   | aggregator     |   | composite score |   | (PancreSpeed 1.0 vs    |   |
|   | (L1 L2 L3 L4)  |   | 6 components    |   | da Vinci 2030 vs       |   |
|   |                |   | (Q T Co S Px A) |   | Hugo PDAC 2030 vs      |   |
|   |                |   |                 |   | Dutch human baseline)  |   |
|   +-------+--------+   +--------+--------+   +-----------+-------------+   |
|           |                                              |                 |
|           v                                              v                 |
|   +-------+-----------------+              +-------------+---------------+ |
|   | Zenodo L0 raw (13.2 GB) |              | cross iteration leaderboard | |
|   | 32 iterations x 412 MB  |              | per round verdicts          | |
|   | per iteration deposition|              | structural caveat preserved | |
|   +-------------------------+              +-----------------------------+ |
+============================================================================+
```

## Component Inventory

- 640 channel sensor ingest at `src/sensors/ingest_8arm.py` with schema at `schemas/sensor_record_8arm.{schema.json, proto, avsc}`.
- Per arm sensor to xyz Cartesian mapping at `src/mapping/sensor_to_xyz_8arm.py` with schema at `schemas/xyz_command_8arm.{schema.json, proto}` and kinematics at `config/kinematics_8arm.yaml`.
- Per arm robot control loop at `src/control/robot_loop_8arm.cpp` and coordination broadcast at `src/coordination/arm_heartbeat_10khz.cpp` plus `src/coordination/arm_collision_avoidance.cpp`.
- Vascular safety zone gate at `src/vascular/safety_zone_gate.py` with the 5 vessel volume table at `config/vascular_safety_zones.yaml`.
- Three anastomosis controllers at `src/anastomosis/pancreaticojejunostomy.py`, `src/anastomosis/hepaticojejunostomy.py`, `src/anastomosis/gastrojejunostomy.py` with targets at `config/anastomosis_targets.yaml`.
- Daraxonrasib perioperative trajectory at `src/daraxonrasib/trajectory.py` and LLM bound advisory at `src/daraxonrasib/advisory.py`.
- 32 iteration deterministic sweep at `src/simulation/iterate_1min.py` (Python) and `src/simulation/runner_1min.rs` (Rust).
- 6 component composite score at `src/metrics/compute_1min.py`.
- 4 entrant LLM tournament at `src/llm/compare_agent_1min.py` with prompt at `prompts/comparison_prompt_1min.md`.
- Zenodo L0 deposition patcher at `src/zenodo/patch_pointers.py`.

## Deterministic Seed Contract

The root simulation seed is `20260513`. The per iteration seed is `root_seed + iteration_index` where `iteration_index` ranges over `[0, 31]`. Every stochastic component of the pipeline consumes the per iteration seed; re generation from the same seed yields bit identical Parquet outputs at the L2, L3, and L4 layers. The Claude Code generation pass that authors the simulation tree itself is not deterministic across re generations and is flagged in the cross simulation caveat block.

## Cross References

- `../../instructions/multi_arm_coordination_8arm.md` fixes the 10 kHz heartbeat broadcast bus.
- `../../instructions/pdac_context_1min.md` fixes the 8 phase 60 second timeline.
- `../../instructions/robot_specification_pancrespeed.md` fixes the PancreSpeed 1.0 platform.
- `../../instructions/vascular_safety_protocol.md` fixes the 5 vessel safety zones.
- `../../instructions/anastomosis_protocols.md` fixes the 3 anastomosis protocols.
- `../../instructions/daraxonrasib_integration.md` fixes the perioperative trajectory.
