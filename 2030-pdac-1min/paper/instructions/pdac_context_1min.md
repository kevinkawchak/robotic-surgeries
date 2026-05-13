# PDAC Clinical Context (1 Minute Variant)

This file fixes the patient, the disease, the procedure, and the 8 phase 60 second timeline that every other instruction file in this directory references. The future Claude Code Opus 4.7 1M Max session reads this file together with the parent README.md and the daraxonrasib_integration.md file to ground the entire simulation in PDAC clinical reality.

## Synthetic Patient PAT-PDAC-0001

The simulation is anchored on a single synthetic patient whose attributes are fully specified below so that the future generated tree at 2030-pdac-1min/ is bit deterministic for the fixed seed 20260513.

| Field | Value |
|-------|-------|
| Patient ID | PAT-PDAC-0001 |
| Age (years) | 68 |
| Sex | Male |
| Performance Status | ECOG 1 |
| BMI (kg per m squared) | 26.4 |
| Diagnosis | Pancreatic ductal adenocarcinoma, head of pancreas |
| Tumor diameter (cm) | 3.4 |
| Vascular abutment | Superior mesenteric vein, 75 degrees |
| Resectability category (NCCN 2026) | Borderline resectable |
| KRAS mutation | G12D |
| Microsatellite status | MSI stable |
| CA 19 9 at diagnosis (U/mL) | 412 |
| CA 19 9 after neoadjuvant (U/mL) | 78 |
| Bilirubin at diagnosis (mg/dL) | 3.1 |
| Bilirubin after biliary stent (mg/dL) | 0.9 |
| Neoadjuvant regimen | modified FOLFIRINOX times 4 cycles |
| Neoadjuvant response (RECIST 1.1) | Partial response |
| Daraxonrasib eligibility | Yes per RASolute 302 broad pan KRAS criteria |
| Sarcopenia | Mild (psoas index 5.6 cm squared per m squared) |
| Frailty (CFS) | 3 |
| Fistula risk score (preoperative) | Moderate (gland soft, duct 3.2 mm) |

The patient is synthetic and not derived from any real EHR or identifiable cohort. No IRB, no informed consent, and no real patient data are used. The future generated simulation tree at 2030-pdac-1min/ will reproduce the cross simulation limitation language from 2030-gbm-1min/paper/full-paper/final-paper/sections/limitations_future.tex in the equivalent PDAC paper.

## Surgical Procedure

The procedure is a classic pancreaticoduodenectomy (Whipple) with pylorus preservation, with portomesenteric venous resection if vessel margin requires it, with artery first uncinate dissection, with three named anastomoses (pancreaticojejunostomy duct to mucosa, hepaticojejunostomy end to side, gastrojejunostomy or duodenojejunostomy antecolic), with two closed suction drains, and with a single pass through cumulative force, hemostasis verification, and final margin scan. The instruction set assumes the surgical platform is the hypothetical 2030 Medtronic PancreSpeed 1.0 eight arm parallel coelomic oncology robot defined in robot_specification_pancrespeed.md.

The pre op preparation (anesthesia, port placement, table positioning, eight arm docking, artery first window opening, four major vascular landmark identification) is precomputed and frozen at simulation start. The simulation begins at the moment the eight arms are docked and the four major vascular landmarks (superior mesenteric vein, portal vein, hepatic artery, celiac axis) have been identified by the imaging arms. The simulation ends at the 60.000 second mark.

## Eight Phase 60 Second Timeline

The 8 phase timeline below is the canonical phase definition that every other instruction file in this directory references. Each phase has a fixed start time, end time, duration, and primary actor list. Phase boundaries are enforced at the 10 kHz command channel resolution (100 microsecond ticks) and are gated by the multi arm coordination heartbeat watchdog defined in multi_arm_coordination_8arm.md.

| Phase | Start (s) | End (s) | Duration (s) | Primary actors | Key sensors active |
|-------|-----------|---------|--------------|----------------|--------------------|
| Pre op (frozen, precomputed) | T-3600 | T+0 | 60 minutes | All eight arms dock | Pre op imaging |
| Phase 1 exploration and Kocher maneuver | 0.000 | 6.000 | 6 s | Arms 1, 2, 3, 4 | NIR indocyanine green, ultrasound, force, ee tip position |
| Phase 2 vascular control and venous dissection | 6.000 | 16.000 | 10 s | Arms 1, 2, 3, 4, 5, 6, 7, 8 | Vessel surface proximity, NIR, force, bipolar coag current |
| Phase 3 uncinate dissection (artery first) | 16.000 | 24.000 | 8 s | Arms 1, 2, 3, 4 | Vessel surface proximity, force, NIR, ultrasound |
| Phase 4 specimen removal and en bloc resection | 24.000 | 32.000 | 8 s | Arms 1, 2, 3, 4, 5, 6, 7, 8 | Force, NIR, ultrasound, margin scan |
| Phase 5 pancreaticojejunostomy reconstruction | 32.000 | 42.000 | 10 s | Arms 1, 2, 3, 4, 5 | Pancreatic duct manometry, anastomosis ring tension, force |
| Phase 6 hepaticojejunostomy reconstruction | 42.000 | 48.000 | 6 s | Arms 1, 2, 3, 4, 5 | Bile spectrophotometry, anastomosis ring tension, NIR, force |
| Phase 7 gastrojejunostomy reconstruction | 48.000 | 54.000 | 6 s | Arms 1, 2, 3, 4 | Anastomosis ring tension, force, NIR |
| Phase 8 hemostasis verification, drain placement, arm withdrawal | 54.000 | 60.000 | 6 s | All eight arms | Force, NIR, ultrasound, final margin scan |

The per phase actor list is reproduced in commit_03_xyz_8arm.md and is the contract under which the future xyz command generator in src/mapping/sensor_to_xyz_8arm.py emits per arm commands at the 10 kHz command channel rate.

## Vascular Anatomy Reference (PAT-PDAC-0001)

The four major vascular landmarks have fixed coordinates in the patient frame for the duration of the simulation. The frame origin is the umbilicus. The x axis points to the patient's right, the y axis points caudal, and the z axis points anterior.

| Vessel | x (mm) | y (mm) | z (mm) | No fly radius (mm) | Soft warning radius (mm) | Hard stop radius (mm) |
|--------|--------|--------|--------|--------------------|--------------------------|------------------------|
| Superior mesenteric vein | +15 | -25 | -45 | 2.0 | 4.0 | 6.0 |
| Portal vein | +5 | -55 | -55 | 2.0 | 4.0 | 6.0 |
| Hepatic artery (common) | +20 | -60 | -50 | 1.5 | 3.0 | 5.0 |
| Celiac axis | +0 | -65 | -60 | 1.5 | 3.0 | 5.0 |
| Superior mesenteric artery | +0 | -35 | -55 | 1.5 | 3.0 | 5.0 |

The per vessel no fly, soft warning, and hard stop radii are reproduced in vascular_safety_protocol.md and are enforced by the safety zone gate in src/vascular/safety_zone_gate.py at the 10 kHz command channel rate.

## Three Anastomosis Targets (PAT-PDAC-0001)

The three named anastomoses each have fixed target locations in the patient frame, fixed ring tension targets, and fixed bile or pancreatic duct manometry targets.

| Anastomosis | x (mm) | y (mm) | z (mm) | Target ring tension (N) | Manometry target (mmHg) | Duration (s) | Phase |
|-------------|--------|--------|--------|-------------------------|-------------------------|--------------|-------|
| Pancreaticojejunostomy (duct to mucosa) | +18 | -30 | -42 | 0.45 +/- 0.05 | duct 12 +/- 2 | 10 | 5 |
| Hepaticojejunostomy (end to side) | +12 | -50 | -48 | 0.50 +/- 0.05 | bile 8 +/- 2 | 6 | 6 |
| Gastrojejunostomy (antecolic) | -8 | -40 | -30 | 0.60 +/- 0.05 | not applicable | 6 | 7 |

The ring tension targets and manometry targets are reproduced in anastomosis_protocols.md and are tracked in run_NNNNN_L4_anastomosis.parquet per iteration.

## Daraxonrasib Eligibility and Perioperative Trajectory

The patient is eligible for Daraxonrasib per the RASolute 302 broad pan KRAS criteria (KRAS G12D mutation, ECOG 1, no contraindications). The perioperative serum concentration trajectory is defined in daraxonrasib_integration.md and tracked in run_NNNNN_daraxonrasib.parquet per iteration. The simulation does not administer Daraxonrasib intraoperatively; the drug is paused 72 hours before surgery and restarted 7 days postoperatively per the RASolute 302 perioperative pause protocol. The intraoperative serum concentration is therefore at the trough level and the LLM bound advisory layer in src/daraxonrasib/advisory.py emits an advisory at the 60 second mark on the timing of postoperative restart based on the per arm cumulative force exposure, the per anastomosis ring tension stability, and the pancreatic fistula risk score realized in the simulation.

## Fistula Risk Score Inputs

The fistula risk score (FRS) is the primary intra simulation safety endpoint and the secondary intra simulation outcome endpoint. The four FRS inputs are tracked in run_NNNNN_L4_anastomosis.parquet per iteration.

| Input | Source | Range | Risk weight |
|-------|--------|-------|-------------|
| Gland texture | Pre operative imaging | soft / firm | soft = 2, firm = 0 |
| Pathology | Pre operative histology | PDAC / other | PDAC = 0, other = 1 |
| Pancreatic duct diameter (mm) | Pre operative imaging | 1 to 6 | 1 mm = 4, 6 mm = 0 |
| Estimated blood loss (mL) | Intra operative arm 7 suction | 0 to 1000+ | 0 = 0, 1000+ = 4 |

The synthetic patient PAT-PDAC-0001 has a moderate preoperative FRS (gland soft = 2, PDAC = 0, duct 3.2 mm = 2, EBL projected 200 mL = 1, total 5 of 10). The simulation seed 20260513 will produce a per iteration realized FRS within the 4 to 6 range. The fistula risk score and the resulting grade B/C postoperative pancreatic fistula classification are part of the composite score weights frozen in competition_protocol.md.

## Cross References

- robot_specification_pancrespeed.md fixes the eight arm robot platform.
- sensor_specification_100khz.md fixes the 640 channel sensor stack.
- multi_arm_coordination_8arm.md fixes the 10 kHz heartbeat watchdog.
- vascular_safety_protocol.md fixes the no fly, soft warning, and hard stop volumes.
- anastomosis_protocols.md fixes the three anastomosis protocols.
- daraxonrasib_integration.md fixes the perioperative trajectory.
- commit_03_xyz_8arm.md fixes the per arm xyz command schema.
- commit_04_iterations_1min.md fixes the 32 iteration sweep design.
- commit_05_competition_1min.md fixes the four entrant tournament.
