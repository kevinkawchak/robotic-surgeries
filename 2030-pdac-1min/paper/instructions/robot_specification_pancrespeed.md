# Robot Specification: Medtronic PancreSpeed 1.0 (Hypothetical, 2030)

This file fixes the hypothetical 2030 Medtronic PancreSpeed 1.0 eight arm parallel coelomic oncology robot specification for the PDAC 1 minute variant. The future Claude Code Opus 4.7 1M Max session reads this file to ground the per arm kinematics, per arm tool inventory, per arm safety envelopes, and per arm regulatory framing in a concrete robot platform spec.

## Why a Hypothetical 2030 Robot

The current SOTA robotic platforms in PDAC surgery as of May 2026 are the Intuitive da Vinci Xi (4 arms, 1 arm per port, used in approximately 70 percent of contemporary robotic Whipples), the Intuitive da Vinci SP (1 arm, single port, used in selected cases), the Medtronic Hugo RAS (4 arm modular cart based, used in approximately 5 percent of contemporary robotic Whipples), and the Verb Surgical (a Johnson & Johnson and Verily joint venture). None of these platforms can perform a 60 second Whipple. The per arm end effector velocity is capped at approximately 250 mm/s; the joint angular velocity is capped at approximately 90 deg/s; the cross arm e stop latency is approximately 200 ms; the positioning accuracy at peak velocity is approximately 1.0 mm RMS; and the force resolution is 0.1 N at 1 kHz. The PDAC 1 minute target requires these capabilities to be 5x to 500x faster, finer, and more accurate.

The hypothetical 2030 Medtronic PancreSpeed 1.0 platform is therefore defined as the 2030 successor of the Medtronic Hugo RAS, scaled to 8 arms, 1,200 mm/s per arm end effector velocity, 720 deg/s peak joint angular velocity at the 6th joint, 3 ms cross arm e stop, 0.05 mm RMS positioning accuracy at 1,200 mm/s, and 0.01 N force resolution at 100 kHz. The PancreSpeed 1.0 does not exist; the comparison against the v3.9.1 GBM hypothetical NeuroSpeed 1.0 is paper only and is explicitly flagged in the cross simulation limitations.

## Top Level Specification

| Property | PancreSpeed 1.0 (hypothetical 2030) | v3.9.1 NeuroSpeed 1.0 (hypothetical 2030) | da Vinci Xi (2026 SOTA) |
|----------|-------------------------------------|--------------------------------------------|--------------------------|
| Arms | 8 | 4 | 4 |
| DOF per arm | 7 | 7 | 7 |
| Total DOF | 56 | 28 | 28 |
| Workspace radius per arm (m) | 1.3 | 1.0 | 0.7 |
| Peak tip linear velocity (mm/s) | 1,200 | 1,000 | 250 |
| Peak joint angular velocity (deg/s) | 720 | 540 | 90 |
| Positioning accuracy at peak velocity (mm RMS) | 0.05 | 0.10 | 1.0 |
| Force resolution at peak velocity (N) | 0.01 | 0.10 | 0.1 |
| Force sample rate (kHz) | 100 | 10 | 1 |
| Command sample rate (kHz) | 10 | 1 | 1 |
| Heartbeat rate (kHz) | 10 | 1 | n/a |
| Cross arm e stop latency (ms) | 3 | 5 | 200 |
| Per arm park latency (microseconds) | 50 | 100 | 50,000 |
| Per arm tip force cap soft (N) | 2.5 | 4.0 | 5.0 |
| Per arm tip force cap hard (N) | 3.0 | 5.0 | 10.0 |
| Cumulative cross arm tip force cap soft (N) | 15.0 | 9.0 | n/a |
| Cumulative cross arm tip force cap hard (N) | 18.0 | 12.0 | n/a |
| Per arm force time integral soft (N.s) | 5.0 | n/a | n/a |
| Per arm force time integral hard (N.s) | 8.0 | n/a | n/a |
| Peak tissue removal rate (mm cubed per second) | 1,600 (hybrid scalpel) | 800 | 50 |
| Per arm tool changer carousel slots | 8 | 4 | 1 |
| Per arm tool changer swap time (ms) | 200 | 500 | 30,000 |
| Per arm motor type | direct drive servo + harmonic | direct drive servo + harmonic | cable driven |
| Per arm motor backlash (arcsec) | < 1 | < 5 | < 60 |

The PancreSpeed 1.0 specification is 2x to 100x more capable than the da Vinci Xi 2026 SOTA along every dimension. The PancreSpeed 1.0 is also 2x more capable than the v3.9.1 NeuroSpeed 1.0 along several dimensions (force sample rate, heartbeat rate, e stop latency, park latency, positioning accuracy), reflecting the higher safety floor required for PDAC vascular and anastomosis work.

## Per Arm Tool Inventory

The PancreSpeed 1.0 per arm tool changer carousel holds 8 tools per arm. The per arm tool inventory is fixed in the per arm tool assignment table at sensor_specification_100khz.md and is reproduced here for orientation. The per arm tool changer swap time is 200 ms; the swap is performed during phase boundaries when the arm is idle.

| Tool | Function | Arms equipped | Energy source |
|------|----------|---------------|---------------|
| Hybrid ultrasonic-water-plasma scalpel | Cuts and seals 1 to 4 mm vessels in a single pass | 1 | 4 MHz ultrasonic + 50 microsecond plasma + 60 psi pulsed water |
| Bipolar coagulator | Seals 1 to 7 mm vessels | 2, 5, 6 | 350 kHz radio frequency |
| Articulated retractor + grasper | Soft tissue retraction and grasping | 3 | n/a (passive) |
| Linear 8 element ultrasound + iMRI probe + NIR imaging | Vessel mapping, margin scan, NIR ICG imaging | 4 | 7.5 MHz US + 3T iMRI compatible + 800 nm NIR |
| Suction + irrigation | Field clearance | 7 | n/a (vacuum + saline) |
| Linear stapler | 60 mm staple line for gastrojejunostomy and pancreas transection | 1, 2 (Phase 7 only) | n/a (mechanical) |
| Needle driver | Suture placement for anastomoses | 1, 2 (Phases 5, 6, 7) | n/a (mechanical) |
| 5-ALA UV + sample collector | Margin verification and tissue sample collection | 8 | 405 nm UV |

## Regulatory Framing

The PancreSpeed 1.0 is framed as a Class IIb medical device under the EU MDR 2017 / 745 framework and a Class II Class III convertible device under the US FDA framework. The per arm tip force cap (3.0 N hard) is set below the IEC 80601-2-77 force limit for surgical robots (10 N at the tip). The cross arm e stop latency budget (3 ms) is set below the IEC 80601-2-77 e stop latency requirement (50 ms). The 21 CFR 50.30 task order lifecycle is honored by the per arm task identifier channel; every per arm task transition is logged in the L3 per phase Parquet.

The PancreSpeed 1.0 is intended for use by board certified hepatobiliary and pancreatic surgeons under the FDA Software as a Medical Device (SaMD) framework. The on premises LLM control layer (per the thesis in the parent README) is framed as a software function intended to drive a hardware platform; the SaMD classification is anticipated at Risk Class III under the IMDRF SaMD framework because the software directly affects clinical decisions in a high acuity setting.

## ASCII Mechanical Schematic

The PancreSpeed 1.0 mechanical schematic is reproduced below for orientation. The future Claude Code session generates the equivalent ASCII at 2030-pdac-1min/outputs/diagrams/pancrespeed_mechanical.txt.

```
+==========================================================================+
|     PancreSpeed 1.0 (hypothetical 2030) - 8 arms x 7 DOF, 56 DOF total   |
+==========================================================================+
|                                                                          |
|   Patient (supine, abdomen up)                                           |
|       O---------+                                                        |
|       |   PT    |   Patient longitudinal axis (y axis, caudal)           |
|       |  abdo   |                                                        |
|       +----+----+                                                        |
|            |                                                             |
|   right    |       left           Top down view:                         |
|   side     |       side                                                  |
|            |                                                             |
|  [Arm 1]  [Arm 5]                                                        |
|  [Arm 2]  [Arm 6]   8 articulated arms,                                  |
|  [Arm 3]  [Arm 7]   each 7 DOF,                                          |
|  [Arm 4]  [Arm 8]   docked over a sterile boom,                          |
|                     converging on the upper abdomen.                     |
|                                                                          |
|  Each arm: 7 DOF kinematic chain                                         |
|    J1 yaw (shoulder) -> J2 pitch -> J3 yaw -> J4 elbow pitch ->          |
|    J5 wrist yaw -> J6 wrist pitch -> J7 wrist roll                       |
|    Tip workspace radius approx 1.3 m at peak velocity 1,200 mm/s         |
|    Positioning accuracy 0.05 mm RMS at 1,200 mm/s                        |
|                                                                          |
|  Sterile boom + coordination master + 10 kHz heartbeat bus              |
|    Master broadcasts 64 byte frame every 100 us                          |
|    Per arm responds with 32 byte frame within 100 us watchdog            |
|    Cross arm e stop budget 3 ms; per arm park 50 us                      |
+==========================================================================+
```

## Cross References

- pdac_context_1min.md fixes the 8 phase timeline and per arm tool assignment.
- sensor_specification_100khz.md fixes the 640 channel sensor stack and the per arm 80 channel breakdown.
- multi_arm_coordination_8arm.md fixes the 10 kHz heartbeat broadcast bus.
- commit_03_xyz_8arm.md fixes the per arm 7 DOF DH parameter table.
- competition_protocol.md fixes the four entrant tournament against three competitor robots and one human surgeon baseline.
