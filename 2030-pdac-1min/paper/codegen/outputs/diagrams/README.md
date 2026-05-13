# Diagrams Index (v0.6.0)

[![Release](https://img.shields.io/badge/Release-v0.6.0-brightgreen.svg)](../../../../releases.md)
[![Diagrams](https://img.shields.io/badge/Diagrams-12-purple.svg)](.)

This directory contains the 12 PDAC specific ASCII diagrams generated for the v0.6.0 PDAC 1 minute simulation. Each diagram lives as a .txt file with UTF-8 encoding and LF line endings.

| File | Purpose | Source instruction |
|------|---------|---------------------|
| coordination_heartbeat_8arm.txt | 8 arm coordination heartbeat | `multi_arm_coordination_8arm.md` |
| vascular_safety_map.txt | 5 vessel vascular safety map | `vascular_safety_protocol.md` |
| anastomosis_target_map.txt | 3 anastomosis target map | `anastomosis_protocols.md` |
| per_arm_tool_assignment.txt | Per arm tool assignment by phase | `sensor_specification_100khz.md` |
| per_phase_activation.txt | Per phase per arm activation schedule | `multi_arm_coordination_8arm.md` |
| per_arm_kinematic_chain.txt | Per arm 7 DOF kinematic chain | `commit_03_xyz_8arm.md` |
| pancrespeed_mechanical.txt | PancreSpeed 1.0 mechanical schematic | `robot_specification_pancrespeed.md` |
| iteration_parameter_space.txt | 32 iteration sweep parameter space | `commit_04_iterations_1min.md` |
| tournament_leaderboard.txt | 4 entrant tournament leaderboard | `competition_protocol.md` |
| daraxonrasib_trajectory.txt | Daraxonrasib perioperative trajectory | `daraxonrasib_integration.md` |
| fistula_risk_score_flow.txt | Fistula risk score flow | `anastomosis_protocols.md` |
| 8_phase_timeline.txt | 60 second 8 phase timeline | `pdac_context_1min.md` |

Diagrams use ASCII characters only (no Unicode box drawing) to ensure git diff friendliness and reliable rendering in GitHub Markdown preview, Overleaf, and plain text terminals.
