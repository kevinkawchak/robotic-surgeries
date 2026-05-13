# Anastomosis Protocols (Three Anastomoses, PDAC Specific)

This file fixes the three anastomosis protocols (pancreaticojejunostomy duct to mucosa, hepaticojejunostomy end to side, gastrojejunostomy or duodenojejunostomy antecolic) for the PAT-PDAC-0001 patient. The future Claude Code Opus 4.7 1M Max session reads this file to author the three per anastomosis controllers at 2030-pdac-1min/src/anastomosis/pancreaticojejunostomy.py, 2030-pdac-1min/src/anastomosis/hepaticojejunostomy.py, and 2030-pdac-1min/src/anastomosis/gastrojejunostomy.py.

## Why Anastomosis Quality Dominates PDAC Outcomes

The pancreaticojejunostomy is the most consequential reconstructive step in the Whipple procedure. The 2025 Dutch nationwide cohort of 1000 robotic pancreaticoduodenectomies reported a grade B/C postoperative pancreatic fistula rate of 24.4 percent. A grade B fistula extends hospital stay by 7 to 14 days; a grade C fistula carries a 30 day mortality of approximately 25 percent. The hepaticojejunostomy and gastrojejunostomy are technically less consequential but together account for 8 to 12 percent of major morbidity. The anastomosis protocols therefore define per anastomosis ring tension targets, per anastomosis manometry targets, per anastomosis duration budgets, and per anastomosis leak detection thresholds. Every per iteration realized anastomosis event is logged to run_NNNNN_L4_anastomosis.parquet and contributes to the per iteration composite score.

## Three Anastomosis Targets

| Anastomosis | Target ring tension (N) | Tolerance band (N) | Manometry target (mmHg) | Manometry tolerance (mmHg) | Duration budget (s) | Phase |
|-------------|--------------------------|--------------------|-------------------------|----------------------------|---------------------|-------|
| Pancreaticojejunostomy (duct to mucosa) | 0.45 | +/- 0.05 | duct 12 | +/- 2 | 10 | 5 |
| Hepaticojejunostomy (end to side) | 0.50 | +/- 0.05 | bile 8 | +/- 2 | 6 | 6 |
| Gastrojejunostomy (antecolic) | 0.60 | +/- 0.05 | not applicable | not applicable | 6 | 7 |

The target ring tension values are derived from the 2025 Heidelberg robotic pancreas surgery group reference values for duct to mucosa anastomosis in soft pancreatic gland with 3.2 mm pancreatic duct. The tolerance band is +/- 0.05 N at the 10 kHz ring tension sensor sample rate. If the per anastomosis ring tension drifts outside the tolerance band for more than 100 milliseconds, a per iteration anastomosis ring tension violation event is logged.

## Pancreaticojejunostomy (Duct to Mucosa) Protocol

The pancreaticojejunostomy is performed during Phase 5 (start 32.000 s, end 42.000 s, duration 10 s). The duct to mucosa technique is used. The protocol is:

1. Phase 5 start (32.000 s). Arm 1 (hybrid scalpel + needle driver) approaches the pancreatic stump from the patient right. Arm 2 (bipolar coagulator + needle driver) approaches from the patient left. Arms 3 and 4 retract the bowel loop and the pancreatic stump. Arm 5 monitors anastomosis ring tension.
2. Outer layer (32.000 to 35.500 s). Arms 1 and 2 place four interrupted outer layer sutures (5-0 Prolene) at 12, 3, 6, and 9 o'clock around the pancreatic stump to jejunal serosa. Ring tension target 0.45 N.
3. Duct to mucosa anastomosis (35.500 to 39.500 s). Arms 1 and 2 place eight interrupted duct to mucosa sutures (6-0 Prolene) around the pancreatic duct to jejunal mucosa. Ring tension target 0.45 N. Duct manometry target 12 mmHg.
4. Inner layer (39.500 to 41.500 s). Arms 1 and 2 place four interrupted inner layer sutures (5-0 Prolene) at 12, 3, 6, and 9 o'clock to reinforce the outer layer. Ring tension target 0.45 N.
5. Phase 5 end (41.500 to 42.000 s). Arm 5 confirms ring tension stability for the final 500 milliseconds. Per iteration anastomosis ring tension stability is recorded in run_NNNNN_L4_anastomosis.parquet.

The per iteration realized pancreaticojejunostomy outcome is one of three values: grade A (subclinical, no clinical relevance), grade B (clinically relevant, requires intervention), or grade C (severe, requires reoperation). The realized grade is computed by the per iteration composite score function in src/metrics/compute_1min.py from the per iteration realized ring tension stability, duct manometry stability, and force time integral exposure.

## Hepaticojejunostomy (End to Side) Protocol

The hepaticojejunostomy is performed during Phase 6 (start 42.000 s, end 48.000 s, duration 6 s). The end to side technique is used. The protocol is:

1. Phase 6 start (42.000 s). Arm 1 (needle driver) approaches the common bile duct stump. Arm 2 (needle driver) holds the jejunal loop. Arms 3 and 4 retract. Arm 5 (NIR indocyanine green) monitors bile leak.
2. Posterior layer (42.000 to 44.500 s). Arms 1 and 2 place six interrupted posterior layer sutures (5-0 PDS) from the bile duct to the jejunal serosa. Ring tension target 0.50 N.
3. Anterior layer (44.500 to 47.000 s). Arms 1 and 2 place six interrupted anterior layer sutures (5-0 PDS) to complete the anastomosis. Ring tension target 0.50 N. Bile manometry target 8 mmHg.
4. Bile leak verification (47.000 to 47.500 s). Arm 5 NIR indocyanine green imaging confirms no extravasation. Bile spectrophotometry (410, 470, 532, 600 nm) confirms no bile in the field.
5. Phase 6 end (47.500 to 48.000 s). Arm 5 confirms ring tension stability and NIR signal stability for the final 500 milliseconds.

The per iteration realized hepaticojejunostomy outcome is one of two values: leak absent (clinically irrelevant) or leak present (clinically relevant, requires intervention). The leak detection threshold is bile spectrophotometry signal at 410 nm above the calibrated baseline by 3 standard deviations for more than 100 milliseconds.

## Gastrojejunostomy (Antecolic, Pylorus Preserving) Protocol

The gastrojejunostomy is performed during Phase 7 (start 48.000 s, end 54.000 s, duration 6 s). The antecolic, pylorus preserving technique is used. The protocol is:

1. Phase 7 start (48.000 s). Arm 1 (linear stapler) approaches the proximal jejunum. Arm 2 (needle driver) holds the duodenal stump. Arms 3 and 4 retract. The pylorus is preserved.
2. Stapler fire (48.000 to 50.000 s). Arm 1 fires a single 60 mm linear stapler across the duodenal jejunal junction. Ring tension target 0.60 N.
3. Posterior layer reinforcement (50.000 to 52.000 s). Arms 1 and 2 place four interrupted posterior layer sutures (4-0 Vicryl) to reinforce the stapler line.
4. Anterior layer reinforcement (52.000 to 53.500 s). Arms 1 and 2 place four interrupted anterior layer sutures (4-0 Vicryl) to reinforce the stapler line and complete the anastomosis.
5. Phase 7 end (53.500 to 54.000 s). Arm 4 confirms patency by NIR indocyanine green flow. Per iteration anastomosis ring tension stability is recorded.

The per iteration realized gastrojejunostomy outcome is one of two values: patent (clinically irrelevant) or delayed gastric emptying (clinically relevant, requires intervention). The delayed gastric emptying detection threshold is NIR indocyanine green flow rate below the calibrated baseline by 2 standard deviations for more than 200 milliseconds.

## Fistula Risk Score Recap

The fistula risk score (FRS) is the primary intra simulation safety endpoint and the secondary intra simulation outcome endpoint. The four FRS inputs are tracked in run_NNNNN_L4_anastomosis.parquet per iteration. The FRS table is:

| FRS total | Risk category | Expected grade B/C fistula rate |
|-----------|---------------|----------------------------------|
| 0 to 2 | Negligible | < 1 percent |
| 3 to 6 | Moderate | 5 to 10 percent |
| 7 to 10 | High | 15 to 25 percent |

The synthetic patient PAT-PDAC-0001 has a moderate preoperative FRS of 5 (gland soft = 2, PDAC = 0, duct 3.2 mm = 2, EBL projected 200 mL = 1). The simulation seed 20260513 will produce a per iteration realized FRS within the 4 to 6 range. The expected grade B/C fistula rate in simulation is therefore 5 to 10 percent across the 32 iteration sweep; the PDAC target is to drive the simulated rate to under 5 percent by tuning the ring tension control loop and the duct manometry control loop.

## Cross References

- pdac_context_1min.md fixes the three anastomosis target table.
- sensor_specification_100khz.md fixes the ring tension, duct manometry, and bile spectrophotometry sensors.
- multi_arm_coordination_8arm.md fixes the cross arm ring tension coordination at 10 kHz.
- commit_03_xyz_8arm.md fixes the per arm xyz command schema during anastomosis phases.
- commit_04_iterations_1min.md fixes the per iteration L4 anastomosis Parquet schema.
- daraxonrasib_integration.md fixes the postoperative Daraxonrasib restart timing based on the realized anastomosis grades.
