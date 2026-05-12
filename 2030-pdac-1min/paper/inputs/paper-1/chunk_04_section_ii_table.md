# Section II: Python Digital Twin Phase II Trial Simulation

## Virtual Trial Design & Population

**Global Configuration:** n_patients=1000, max_months=36, dt=1.0 (daily timestep), cycle_length=28 days, assessment_interval=56 days, random seed=20260115

**Patient Archetypes:** 7 distinct phenotypes with prevalence-based allocation: ARCH-01 Young Fit (14%, age 60±10), ARCH-02 Elderly Frail (18%, age 75±6), ARCH-03 Locally Advanced (9%), ARCH-04 BRCA-mutated (20%), ARCH-05 KRAS-G12C (21%), ARCH-06 Stroma-High (9%), ARCH-07 Refractory (9%)

**Biomarker Assignment:** gBRCA: 20% of patients, KRAS-G12C: 21%, KRAS-G12D: 35% of eligible, CD47-high: 60%, HA-high: 9%; primary resistance flag: 40% of patients

**Baseline Parameters:** Age: 30-90 years, ECOG: 0-2 distribution by archetype, CA19-9: lognormal(median varies by archetype), tumor growth rate: 0.005-0.009/day, drug sensitivity multiplier: lognormal(mean=-0.2, sigma=0.4)

## Treatment Regimens & Drug Modeling

**10 Treatment Arms:** A: Gem+nab-P (1L control), B: Gem/nab-P+Magrolimab, C: Gem/nab-P+MRTX1133, D: Gem/nab-P+PEGPH20, E: Gem/nab-P+Pembro+Mitazalimab, G: nal-IRI+5-FU (2L control), H: nal-IRI/5-FU+Daraxonrasib+Mitazalimab, I: Daraxonrasib+Mitazalimab, J: Olaparib maintenance, K: Placebo/BSC

**Drug Parameters:** 11 drugs with Emax (0.001-0.035), EC50 (0.5-1.0), half-life (1-14 days); Examples: gemcitabine (Emax=0.030, t½=1d), olaparib (Emax=0.035, EC50=0.5), pembrolizumab (Emax=0.003, t½=14d)

**Dosing Schedule:** Chemotherapy: days 1,8,15 of 28-day cycle; Targeted agents: daily; Immunotherapy: weekly; nal-IRI/5-FU: biweekly

**Toxicity Model:** Regimen-specific Grade 3+ AE probabilities (0.036-0.054 per cycle) with conditional dropout probabilities (0.06-0.55); implemented via REGIMEN_TOXICITY dictionary

## Digital Twin Bidirectional System

**DigitalTwin Class:** Analyzes patient state each cycle, assesses tumor response (CR/PR/SD/PD), recommends treatment changes, maintains decision log and treatment history, switches lines (1L→2L→BSC) based on progression

**PatientSimulator Class:** Tracks tumor volumes (sensitive + resistant compartments), simulates daily PK/PD via integrate_dynamics(), calculates hazard rates for survival, monitors progression (RECIST: 20% increase + 0.2cm absolute), manages drug concentrations with clearance

**Tumor Dynamics:** Lotka-Volterra model: growth with logistic term (K=100), drug kill rates differentiated for sensitive (full) vs resistant (10%) compartments, resistance allocation: 40% primary (60/40 split) vs 60% acquired (95/5 split)

**Adaptive Decisions:** Treatment switches triggered by: progression (PD), Grade 3+ toxicity with dropout, ECOG deterioration; assessed every 56 days (2 cycles)

**Survival Modeling:** Base hazard=0.0012/day, modified by: tumor burden (log1p), BRCA status (×0.25), progression status (×5.0); daily mortality check via Bernoulli trial

## Simulation Process & Outputs

**Main Simulation Loop:** 38 cycles (1064 days), progress bar; processes all 1000 patients in parallel; cycle-by-cycle: simulate_cycle()→analyze_patient_data()→recommend_treatment()→update regimen

**Response Assessment:** Best overall response per RECIST 1.1: CR (≤-99.9%), PR (≤-30%), SD (stable >56 days), PD (progression); calculated from tumor nadir tracking

**Generated Output Files:** pdac_digital_twin_calibrated_final.csv (main results), patient_logs (1000 individual CSV files), adaptation_log.csv (treatment switches), km_data_by_arm.csv (survival curves), waterfall_plot_data.csv (best responses), adaptation_summary.csv (arm-level statistics)

**Performance Metrics:** Total runtime: 13.12 seconds for 1000 patients × 36 months; generates 38,000+ data points per patient; creates comprehensive audit trail for regulatory review
