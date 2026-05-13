# ASCII Diagram Guide (PDAC 1 Minute Variant)

This file fixes the ASCII and Mermaid diagram conventions for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to author the per diagram ASCII at 2030-pdac-1min/outputs/diagrams/ and the per diagram Mermaid blocks at 2030-pdac-1min/docs/ Markdown files.

## Why ASCII Instead of SVG

The v3.9.1 GBM 1 minute variant established the ASCII diagram convention: SVG files are not produced for high frequency time series because a 3.6 million point path would exceed practical SVG size budgets. The PDAC 1 minute variant extends this rule because the PDAC raw stream is 6.4 million points per arm times 8 arms equals 51.2 million points cross arm, which is 14x larger than the GBM raw stream. ASCII diagrams render reliably in any text editor, in GitHub Markdown preview, in Overleaf LaTeX, and in plain text terminals. ASCII diagrams are also git diff friendly, which Mermaid blocks and SVG files are not.

## Diagram Inventory

The PDAC 1 minute variant generates 12 ASCII diagrams. Each diagram is stored at 2030-pdac-1min/outputs/diagrams/ as a .txt file with UTF-8 encoding and LF line endings. The cross diagram inventory is below.

| Diagram | File | Source |
|---------|------|--------|
| 8 arm coordination heartbeat | coordination_heartbeat_8arm.txt | multi_arm_coordination_8arm.md |
| 5 vessel vascular safety map | vascular_safety_map.txt | vascular_safety_protocol.md |
| 3 anastomosis target map | anastomosis_target_map.txt | anastomosis_protocols.md |
| Per arm tool assignment by phase | per_arm_tool_assignment.txt | sensor_specification_100khz.md |
| Per phase per arm activation schedule | per_phase_activation.txt | multi_arm_coordination_8arm.md |
| Per arm 7 DOF kinematic chain | per_arm_kinematic_chain.txt | commit_03_xyz_8arm.md |
| PancreSpeed 1.0 mechanical schematic | pancrespeed_mechanical.txt | robot_specification_pancrespeed.md |
| 32 iteration sweep parameter space | iteration_parameter_space.txt | commit_04_iterations_1min.md |
| 4 entrant tournament leaderboard | tournament_leaderboard.txt | competition_protocol.md |
| Daraxonrasib perioperative trajectory | daraxonrasib_trajectory.txt | daraxonrasib_integration.md |
| Fistula risk score flow | fistula_risk_score_flow.txt | anastomosis_protocols.md |
| 60 second 8 phase timeline | 8_phase_timeline.txt | pdac_context_1min.md |

## Box Drawing Character Conventions

Use the following ASCII characters for box drawing:

| Element | Character | Notes |
|---------|-----------|-------|
| Horizontal line | - | hyphen minus, U+002D |
| Vertical line | | | vertical bar, U+007C |
| Corner top left | +-- | plus + hyphen |
| Corner top right | --+ | hyphen + plus |
| Corner bottom left | +-- | plus + hyphen |
| Corner bottom right | --+ | hyphen + plus |
| T junction | +-- or --+ | depends on direction |
| Cross junction | +-- or -+- | depends on direction |
| Arrow right | --> | hyphen hyphen greater than |
| Arrow left | <-- | less than hyphen hyphen |
| Arrow up | ^ | caret, U+005E |
| Arrow down | v | lowercase v, U+0076 |
| Bidirectional arrow | <-> | less than hyphen greater than |

Do not use Unicode box drawing characters (U+2500 to U+257F). The ASCII only convention ensures git diff friendliness and renders in any text editor.

## Mermaid Block Convention

Mermaid blocks are allowed inside Markdown documents at 2030-pdac-1min/docs/ for high level architecture overviews. Mermaid blocks are not allowed for high frequency time series diagrams; use ASCII for those.

```
```mermaid
flowchart LR
  A[8 arm sensor stream] --> B[per arm xyz command]
  B --> C[per arm robot control loop]
  C --> D[per iteration L1 to L4 Parquet]
  D --> E[per round LLM tournament]
  E --> F[cross iteration leaderboard]
```
```

## Example ASCII Pipeline Diagram

The canonical PDAC pipeline ASCII diagram is reproduced below for orientation. The future Claude Code session generates an equivalent at 2030-pdac-1min/outputs/diagrams/architecture_overview.txt and embeds it in the future generated README at 2030-pdac-1min/README.md.

```
+============================================================================+
|     2030-PDAC-1MIN PIPELINE (8 arm, 60 second, 100 kHz force, 10 kHz cmd) |
+============================================================================+
|                                                                            |
|  8 arm sensor stream      8 arm xyz command stream    4 entrant tournament |
|  (80 ch/arm x 8 arms,     (per arm phase-conditioned   (on-prem LLM judge, |
|   640 ch total at mixed    10 kHz with 3 ms e stop)     4 entity, 4 round) |
|   10 kHz + 100 kHz force)                                                  |
|  +----------------------+ +----------------------+ +---------------------+ |
|  | Arm 1 hyb u-w-p cut  |>|Per arm xyz, qx, qy, |>| Quality      0.30   | |
|  | Arm 2 bipolar coag   | |qz, qw, linear_vel up | | Time         0.20   | |
|  | Arm 3 retract grasper| |to 1,200 mm/s, force | | Cost         0.15   | |
|  | Arm 4 iMRI + NIR ICG | |clamp 3 N/arm, tool   | | Safety       0.15   | |
|  | Arm 5 bipolar suction| |state, 7-state enum   | | Pt exp       0.05   | |
|  | Arm 6 suction coag   | |+ heartbeat watchdog  | | Anastomosis  0.15   | |
|  | Arm 7 suction + irr  | |10 kHz, 100 us       | | composite total 1.00| |
|  | Arm 8 NIR + 5-ALA UV | |watchdog deadline    | | 4 vendor leaderboard | |
|  | 10 kHz heartbeat bus | |                      | | structural-t caveat | |
|  | 18 N cumulative cap  | |                      | |                     | |
|  +----------+-----------+ +----------+-----------+ +----------+----------+ |
|             |                        |                        |            |
|             v                        v                        v            |
|  +----------------------+ +----------------------+ +---------------------+ |
|  |PancreSpeed 1.0(2030) | |8 phase 60s timeline | |PancreSpeed 93.55    | |
|  |8 arms x 7 DOF, 56 DOF| |P1 Kocher 0-6s P2    | |da Vinci 2030  84.10 | |
|  |0.05 mm RMS at 1,200  | |vasc 6-16s P3 unc    | |Hugo PDAC 2030 80.60 | |
|  |mm/s, 3 ms e stop,    | |16-24s P4 spec 24-32 | |Dutch human    56.05 | |
|  |1,600 mm cubed per s  | |P5 PJ 32-42s P6 HJ   | |PancreSpeed wins all | |
|  |peak via hyb u-w-p    | |42-48s P7 GJ 48-54s  | |3 r-v-r and r-v-h    | |
|  |3 ms cross arm e stop | |P8 hemo 54-60s       | |conf 0.948 to 1.000  | |
|  +----------------------+ +----------------------+ +---------------------+ |
|             |                        |                        |            |
|             v                        v                        v            |
|  +------------------------------------------------------------------------+|
|  |v0.5.0: 8 arm 60s Whipple at 2030-pdac-1min/ populated by Claude Code   ||
|  |Opus 4.7 1M Max from instructions at 2030-pdac-1min/paper/instructions/.||
|  |Includes Daraxonrasib perioperative pause + LLM bound advisory restart. ||
|  |Addresses 7 specific approximations from v3.9.1 GBM final-paper.        ||
|  +------------------------------------------------------------------------+|
+============================================================================+
```

## Cross References

- file_format_conventions.md fixes the ASCII art encoding and line endings.
- multi_arm_coordination_8arm.md fixes the 8 arm coordination heartbeat ASCII.
- vascular_safety_protocol.md fixes the 5 vessel vascular safety map ASCII.
- anastomosis_protocols.md fixes the 3 anastomosis target map ASCII.
- robot_specification_pancrespeed.md fixes the PancreSpeed 1.0 mechanical schematic ASCII.
- competition_protocol.md fixes the 4 entrant tournament leaderboard ASCII.
- daraxonrasib_integration.md fixes the perioperative trajectory ASCII.
