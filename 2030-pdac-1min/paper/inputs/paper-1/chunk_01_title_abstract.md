# Accelerating FDA Compliance and Cost Efficiency of *in silico* Clinical Trials via AI Digital Twin Pancreatic Cancer Simulation

**Author:** Kevin Kawchak  
**Affiliation:** Chief Executive Officer, ChemicalQDevice, San Diego, CA  
**Date:** September 30, 2025  
**Contact:** kevink@chemicalqdevice.com  

---

## Abstract

**Question of Interest:**

Can a bidirectional PDAC digital twin, subjected to M15-aligned verification, validation, uncertainty quantification, and applicability assessment, provide sufficiently credible comparative predictions of arm-level efficacy/safety (ORR, DCR, mPFS, mOS, HRs, G3+ AE, dropout) to prioritize Phase II platform-trial arms and inform design choices (e.g., eligibility mix, progression threshold, horizon), thereby reducing empirical iteration while preserving patient safety?

**Context of Use:**

A cohort-level digital twin simulates a 10-arm PDAC platform trial (≈100 patients/arm, 36-month horizon, dt=1 day). Tumor dynamics use a two-compartment sensitive/resistant Emax framework with archetype-driven growth rates and a lognormal "sensitivity multiplier." Survival uses a base hazard with post-progression and biomarker multipliers; toxicity generates G3+ events with dropout probability; a rule-based policy effects 1L→2L→BSC transitions. The twin executes a closed-loop sense–analyze–recommend–act–learn cycle with per-patient logs.

Data/knowledge used: drug parameters and archetypes transferred from prior QSP work and literature; control-arm external targets from MPACT (Arm A), NAPOLI-1 (Arm G), and POLO (Arms J/K). Specific role of model outcomes: rank arms, estimate HRs and endpoint distributions, test design assumptions. Other evidence: an a priori VV40/FDA test suite executed-Verification/Numerics (V-01 dt-convergence; V-02 seed reproducibility; V-03 zero-efficacy; V-04 zero-growth; V-05 boundary conditions; V-06 toxicity logic), Validation & Sensitivity (S-01..S-09, covering Emax/EC50/half-life, growth, resistance, dropout, hazard multipliers), UQ (UQ-01..03, sigma variation, age SD, 10-seed ensembles), and Applicability (A-01 population drift, A-03 RECIST threshold, A-04 horizon; A-02 dosing schedule reserved). External validation: Arm A close on ORR and mOS, low on mPFS; Arm G underpredicts mPFS/OS; J/K farther off-acknowledged calibration limitations.

**Model Influence: Medium**

Justification: The twin informs internal prioritization and design (arm ranking, sample size tuning, eligibility mix, sensitivity to rules) but is not the sole basis for regulatory or labeling decisions. Outputs are triangulated with literature comparators and expert judgment. Verification and UQ support reliable computation; partial external fit tempers influence.

**Consequence of Wrong Decision: Medium**

Justification: If mis-prioritized, resources could shift to a less active arm and expose Phase II participants to suboptimal regimens; however, care remains within accepted standards under IRB/DSMB oversight, and no patient-facing recommendations are made by the software. Thus, consequences are meaningful for efficacy and development efficiency, but with mitigations for safety.

**Model Risk: Medium**

Justification: Combining Medium Model Influence with Medium Consequence yields Medium risk (per M15 and ASME V&V 40 logic). Credibility activities were commensurate: code/calculation verification (dt stability; seed reproducibility; boundary/logic checks), model robustness via sensitivity to key biological/clinical assumptions (S-01..S-09), stochastic/UQ ensembles (UQ-03), and applicability to population mix, RECIST thresholds, and horizon (A-01, A-03, A-04). External validation is partly met for A and G with documented gaps, transparently constraining scope.

**Model Impact: Medium (with a path to High)**

Justification: Relative to current regulatory expectations, the twin provides MIDD evidence suitable for planning and interaction: clearly stated Question/COU; risk-informed Model Evaluation; pre-specified Technical Criteria via the VV40 test suite; reproducible code and patient-level logs; ensemble uncertainty bands; and applicability analyses. This supports early FDA interactions (e.g., MIDD/Q-sub) for arm prioritization and design what-if analyses, potentially saving time and cost versus purely empirical iteration. Impact is not rated High because simultaneous multi-endpoint external calibration (A, G, J/K) and prospectively defined quantitative acceptance targets/CIs need strengthening; completion of A-02 dosing applicability and expanded external validation would elevate impact.
