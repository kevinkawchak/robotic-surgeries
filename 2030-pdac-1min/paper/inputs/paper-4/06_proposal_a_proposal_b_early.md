# Proposal A Page 1: Prospective Stand‑Alone PDAC Digital‑Twin Trial, o3pr

## 1. Executive Summary (≤ 300 words)

Pancreatic ductal adenocarcinoma (PDAC) remains the oncology drug‑development "graveyard": >80 % of phase III assets have failed despite compelling biology and sizable capital deployment. Our stand‑alone **digital‑twin (DT) trial** reverses that risk profile. Leveraging six exhaustive technical reports (40 meta‑analyses; >10 000 patients; multi‑omics and imaging datasets), we will create ~10 000 validated *in‑silico* "virtual patients" that capture the full heterogeneity of PDAC biology, tumour‑micro‑environment (TME) and treatment history. The DT platform will prospectively simulate a first‑in‑human (FIH) study of the top‑ranked therapeutic triplet—Daraxonrasib + Mitazalimab + Liposomal Irinotecan—identified in Report 1 (predicted TSVS 8.15).

**Investor value proposition**

- **Capital efficiency** – A 24‑month DT programme costs ≈ US$ 18 m versus US$ 70–90 m for a comparable wet‑lab phase I/II.
- **Speed** – Model‑informed trial design decisions arrive 18 months earlier, accelerating lead asset timelines by ≥ 2 years.
- **Regulatory traction** – Scope aligns with FDA Model‑Informed Drug Development (MIDD) Pilot and EMA qualification advice pathways, de‑risking acceptance of virtual evidence.
- **Portfolio utility** – Once built, the mechanistic/ML architecture can be repurposed for other KRAS‑mutant GI tumours and for adaptive platform trials (Report 5).

Successful execution yields a ready‑to‑file FIH protocol with optimised dose, eligibility, adaptive rules and credible survival priors—reducing phase I attrition risk and enhancing Series B/IPO valuations.

## 2. Scientific Objectives & Hypotheses

| Objective | Key Uncertainty Addressed | Hypothesis |
|---|---|---|
| **O1. Quantify triplet efficacy drivers** | Relative contributions of oncogene inhibition, APC activation and nanoparticle‑chemo to tumour kill | Synergistic tumour control arises when Daraxonrasib‑driven antigen release and Mitazalimab‑mediated dendritic‑cell activation coincide within an optimised pharmacokinetic (PK) window |
| **O2. Resolve TME‑immunity bottlenecks** | Why checkpoint blockade fails in PDAC despite CD40 priming | Effective T‑cell priming requires concurrent stromal remodelling and CXCR4 suppression; DT will identify thresholds of fibroblast density and chemokine gradients that predict response |
| **O3. Derive patient‑level dose–toxicity- efficacy (DTE) surfaces** | Optimal triplet dosing remains unknown | Adaptive digital dose‑finding will map DTE surfaces across 20 covariates (age, ECOG, organ function, genomics) to recommend 2 safe starting doses for the FIH 3 + 3/BOIN design |
| **O4. Validate biomarker‑ guided enrichment** | Which KRAS mutants and TME phenotypes derive most benefit | Virtual responders will concentrate in KRAS‑G12D/V cases with intermediate desmoplasia; predictive signature ≥ 80 % PPV will be prospectively tested |

**Why this matters (plain language)** Each objective tackles a multi‑million‑dollar unknown that routinely sinks early‑phase PDAC trials. Resolving them *before* a single patient is dosed saves capital and lives while sharpening the asset's competitive edge.

## 3. Virtual‑Patient Cohort Construction

**3.1 Population archetypes** Seven archetypes from Report 6 (ARCH‑01 to ARCH‑07) covering age, fitness, stage, KRAS alleles, BRCA/DDR status and stromal phenotypes.

**3.2 Data inputs**

- **Genomics** -- Targeted NGS panels (KRAS hotspot, DDR genes, SWI/SNF alterations).
- **Spatial omics** -- Multiplex IHC for CD8, FAP, CAF subtypes, pFAK.
- **Imaging** -- MRI-elastography-derived stiffness maps, CT radiomics for tumour burden.
- **Longitudinal labs** -- CA19-9 trajectories, neutrophil-lymphocyte ratio.

**3.3 Sampling & size justification**

- **Latin-hyper-cube sampling** across 42 correlated covariates → 9,600 virtual patients ensures convergence of survival and toxicity endpoints (Monte-Carlo SE <3%).
- Stratified oversampling of rare KRAS-G12C (2%) and BRCAm (6%) maintains external validity for sensitivity analyses.

**Why this matters** A realistic virtual cohort is the linchpin of model credibility; regulators require demographic and biomarker distributions to mirror intended FIH populations.

## 4. Digital‑Twin Architecture

| Layer | Function | Key Methods |
|---|---|---|
| **A. Macro‑scale PDE tumour‑growth model** | Simulate spatial tumour volumes under therapy | Reaction–diffusion PDEs calibrated to imaging; incorporates nutrient gradients & hypoxia |
| **B. Multi‑compartment QSP (whole‑body)** | Integrate PK/PD of three drugs, DARAXONRASIB metabolism, immune cell trafficking | 82 ODEs; humanised from Report 6 INT‑series parameters |
| **C. Agent‑based TME module** | Cell‑level interactions (cancer / CAF / APC / T‑cell) | 10 000 agents per voxel; CAF mechanotransduction rules from Reports 2 & 4 |
| **D. ML calibration layer** | Align model outputs with real‑world meta‑analytic endpoints | Bayesian hierarchical calibration using TSVS‑derived priors (Report 1) & CBS sequences (Report 3) |
| **E. Decision‑analytics wrapper** | Generate adaptive trial operating characteristics | Reinforcement‑learning engine optimises interim rules |

**Data‑flow diagram**
`Clinical priors → Pre‑processor → PDE & QSP cores → Agent‑based TME → ML residual learner ⇌ Calibration DB → Post‑processor → Trial simulator`

**Runtime requirements**

- Cloud (GPU + CPU) cluster: 500 vCPU / 30 A100-GPU hours per 1,000 twins = 4 hours wall-time per batch.
- Costs budgeted at US$3.4 million over 24 months.

**Why this matters** A modular, hybrid‑mechanistic architecture avoids "black‑box" objections and allows reuse for other assets—maximising return on digital‑infrastructure spend.

## 5. Verification, Validation & Uncertainty Quantification Plan

| Credibility Activity | ASME V&V 40 Tier | Methodology | Acceptance Target |
|---|---|---|---|
| **Code verification** | 1A (Low risk) | Unit tests, CI/CD with 90 %+ coverage | <1 % numerical error |
| **Algorithmic verification** | 1B | Benchmarks against analytic PDE solutions | RMS error <5 % |
| **Clinical validation** | 2B (Medium) | Back‑test against 15 pivotal trials (e.g., NAPOLI‑1, OPTIMIZE‑1) | HR prediction within 0.1 |
| **Prospective validation** | 3 (Medium‑high) | Compare DT‑predicted safety run‑in (n = 20 real pts) to virtual DLT rates | κ > 0.75 concordance |
| **Uncertainty quantification** | N/A | Global Sobol indices + Bayesian posterior predictive checks | 90 % CI width <15 % for OS HR |

---

# Proposal A Page 2: Prospective Stand‑Alone PDAC Digital‑Twin Trial, o3pr

**Why this matters** Meeting pre‑specified credibility targets is essential for FDA & EMA acceptance of DT evidence to inform dose and eligibility—translating to shorter, smaller FIH trials.

## 6. Prospective DT Trial Protocol

| Element | Virtual Specification |
|---|---|
| **Eligibility** | KRAS‑mut PDAC, ECOG 0‑1, adequate marrow/liver; excludes BRCAm & MSI‑H (alternative SOC) |
| **Arms** | A) Triplet at DT‑derived Recommended Starting Dose (RSD‑1) ; B) Triplet at RSD‑2 (20 % lower); C) Virtual SOC control (nal‑IRI + 5‑FU/LV) |
| **Primary endpoints** | Virtual Dose‑Limiting Toxicity (vDLT) rate (cycle 1); Virtual Objective Response Rate (vORR) at 12 weeks |
| **Secondary** | PFS, OS, immune‑TME metrics |
| **Sample size** | 2 400 virtual pts (3 × 800) gives 90 % power to detect ≥ 15 % ORR delta |
| **Interim analyses** | Bayesian futility after every 200 twins; stop arm if Pr(ORR > control) < 10 % |
| **Decision rules** | Advance dose with vDLT < 30 % and highest expected utility (efficacy × NCB) |

**Why this matters** A fully prospective virtual protocol mirrors real‑world execution, generating regulatory‑grade evidence and optimising FIH dose without exposing patients to undue risk.

## 7. Regulatory & Ethical Alignment

- **FDA MIDD Pilot** – Matches category 3 ("Model-based trial design"); pre-IND meeting slot targeted Q1-2026.
- **EMA Qualification Opinion** – Seek CHMP endorsement for DT use as supportive evidence; precedents: ICH E16.
- **Good Simulation Practice (GSP) 2023** adherence – Documentation, version control, audit trails.
- **21 CFR Part 11** – Cloud platform with validated e-records, time-stamped logs, role-based access.
- **Ethics** – Eliminates real-patient exposure during high-uncertainty dosing; aligns with 3Rs (Replacement, Reduction, Refinement) of clinical research.

**Why this matters** Early alignment ensures virtual evidence is accepted *de‑facto* rather than "nice‑to‑have," enabling faster regulatory green lights and investor liquidity events.

## 8. Operational Roadmap & Budget (24 months)

| Phase | Month | Key Tasks | FTE | Cost (US$ m) |
|---|---|---|---|---|
| **I. Model Build** | 0‑6 | Data ingestion, code verification, baseline calibration | 8 scientists, 4 eng. | 3.2 |
| **II. V&V** | 6‑12 | Historical validation, UQ loops | 6 scientists | 2.1 |
| **III. Prospective DT execution** | 12‑18 | Run virtual trial, interim analyses | 5 scientists | 4.5 (incl. compute) |
| **IV. Reporting & Regulatory** | 18‑24 | CSR drafting, FDA/EMA meetings | 4 scientists, 2 RA | 1.7 |
| **Contingency (15 %)** | — | Scope creep, cloud spikes | — | 2.3 |
| **Total** | — | — | — | **17.8 m** |

**Why this matters** An $18 m ask with clear phase gates compares favourably to physical trials and fits typical Series‑A/B financing envelopes.

## 9. Risk Register & Mitigations

| Category | Risk | Impact | Probability | Mitigation |
|---|---|---|---|---|
| **Technical** | Model over‑fits historical data | Invalid predictions | Med | Hold‑out trial set; external blinded challenge |
| **Regulatory** | FDA rejects DT evidence | Delay | Low‑med | Pre‑IND engagement; align to V&V 40 matrix |
| **Data** | Missing covariate correlations | Reduced validity | Med | Impute via copula & sensitivity analyses |
| **Commercial** | Competitor runs FIH first | Diluted differentiation | Med | Fast‑track DT to compress timelines |
| **Funding** | Cost over‑run on cloud | Low‑med | Real‑time spend dashboards; auto‑scaling policies | |

## 10. Milestones & Go/No‑Go Criteria

| Time‑point | Milestone | Success Metric | Go/No‑Go Threshold |
|---|---|---|---|
| M 6 | Baseline model calibrated | HR(PFS) error ≤ 0.1 in 10 historical trials | No‑Go if > 0.15 |
| M 12 | V&V complete | All Tier 2 metrics within targets | No‑Go if ≥ 2 metrics fail |
| M 18 | Virtual interim #2 | Pr(ORR gain) ≥ 0.8 for ≥ 1 dose | No‑Go if none ≥ 0.5 |
| M 24 | Regulatory pre‑IND readout | FDA written feedback endorses DT use | No‑Go if major objections remain |

Passing all Go criteria triggers transition to a **hybrid DT + human phase I/II platform**, unlocking Series B financing and potential co‑development partnerships.

*Prepared by **PDAC‑DT‑Architect**, June 2025*

---

# Proposal B, Report 6: ECOG Performance Status, Patient Archetypes

## Opus 4 Extended

Proposal B by ops4 completed each of the 10 deliverables required by Prompt 63. Section 2 regarding Scientific Objectives & Hypotheses provided a mechanistic synergy validation in regards to "KRAS inhibition (tumor kill/antigen release), CD40 activation (APC priming), and cytotoxic chemotherapy (immunogenic cell death)" based on an anticipated HR 0.45 for overall survival, but did not cite Report 1 where the information was based on. The proposal also aimed to resolve clinical uncertainties in a hypothesis with Maintenance therapy with daraxonrasib monotherapy after induction to extend "progression-free survival by >6 months in KRAS-mutant populations "

Deliverable 5 concerning the Verification, Validation & Uncertainty Quantification Plan addressed each of Prompt 63 requirements regarding several credibility goals. This was accomplished by generating an "ASME V&V 40 Risk-Informed Credibility Framework" with four model components corresponding to risk tiers and V&V activities. Proposed prospective V&V experiments across four areas included a clinical trial emulation for "Retrospective simulation of POLO and NAPOLI-1 trials as benchmarks." In addition, statistical metrics were established for calibration using "Hosmer-Lemeshow p>0.05 across risk deciles" and "Uncertainty: 90% prediction intervals containing observed outcomes."

Proposal B utilized the Report 6 Table 1 virtual patient profiles advantageously to help guide the prospective digital twin trial. This included selections of genomic profiles, baseline lab distributions, and ECOG values from source data. R6ECOG below corresponds to the original report and the Proposal B Key Features column in Deliverable 3. Proposal B took advantage of white space formatting more than other generations, and was the second longest at 1,955 words. Overall, Proposal B did not surpass Proposal A in PDAC Trial Impact or Deliverable Completion, as some sections were verbose and less substantive. Although several examples utilizing source data were found, reports or meta-analyses were not cited. These events led to less credibility and likely the lower Report/MA Cited score by the AI judges. The Proposal B Funding Probability and Overall Average scores of 8.58 and 8.78 led to a second place performance, although Proposal D by o3ch was a close third. Proposal D consisted of a similar format and effect to Proposal A, but with lower overall performance seen in Supplementary-71-ProD. Proposal C by g25p was verbose with less meaningful detail, but provided consistent citations found in Supplementary-70-ProC. Proposal E by grok3 was the shortest proposal, and tended to unnecessarily cite reports at times, as shown Supplementary-72-ProE.

**Figure (R6ECOG):** AI Report 6 Table 1 Metrics. June 12, 2025, son4. [Image: images/Image-RP06-1-03.png]

> **Report 6 ECOG Performance across patient archetypes was included in the Proposal B Section 3 "Key Features" column as ECOG 1/2/3**

---

# Proposal B Page 1: Prospective Stand-Alone PDAC Digital-Twin Trial, ops4

## 1. Executive Summary

**Value Proposition:** We propose a 24-month digital-twin (DT) trial simulating 10,000 virtual pancreatic cancer patients to de-risk the clinical development of a novel three-drug combination: daraxonrasib (pan-KRAS inhibitor) + mitazalimab (CD40 agonist) + liposomal irinotecan. This combination achieved the highest Therapeutic Synergy & Viability Score (8.15/10) among untested regimens, with predicted 55% reduction in mortality risk.

**Investment Opportunity:** Traditional PDAC trials cost $50-100M with 80% failure rates. Our DT trial requires $8.5M investment to:

- Predict optimal dosing schedules reducing Phase I duration by 6 months
- Identify biomarker-defined responder populations increasing Phase II success probability from 20% to 45%
- Generate regulatory-grade evidence for FDA MIDD pilot program qualification
- Provide go/no-go decision framework saving $40M in potential Phase III costs

**Competitive Advantage:** We leverage unprecedented meta-analytic data from 40 trials (2010-2025) parameterizing patient heterogeneity, treatment responses, and resistance mechanisms. Our multi-scale model integrates tumor-stroma-immune dynamics with validated clinical endpoints, enabling prospective prediction of exceptional responders and resistance patterns.

**Exit Strategy:** Upon achieving primary milestones, the validated DT platform becomes a licensable asset for pharmaceutical partners, with projected ROI of 5-10x through risk-adjusted development cost savings and accelerated time-to-market for a $2B+ PDAC therapeutic opportunity.

## 2. Scientific Objectives & Hypotheses

**Primary Objectives**

1. **Mechanistic Synergy Validation**: Quantify the three-way synergistic interaction between KRAS inhibition (tumor kill/antigen release), CD40 activation (APC priming), and cytotoxic chemotherapy (immunogenic cell death) predicted to yield HR 0.45 for overall survival.
2. **Resistance Mechanism Identification**: Elucidate primary and acquired resistance pathways, particularly the role of chromatin remodeling gene mutations (ARID1A, SMARCB1) identified in 73% of exceptional responders to stromal-targeting agents.
3. **Optimal Sequencing Strategy**: Determine whether concurrent triple therapy versus sequential doublet approaches maximize the Net Clinical Benefit score while maintaining acceptable toxicity profiles.

**Key Hypotheses to Test**

**H1**: The FAK-Responsive Immune-Excluded Signature (FRIES) - high stromal FAP expression, peripheral CD8+ density ratio >5:1, intact MHC-I - predicts >3-fold enhancement in response to combination therapy.

**H2**: Pre-existing chromatin remodeling defects (ARID1A loss) create synthetic lethality with pan-KRAS inhibition through disrupted mechanotransduction signaling.

**H3**: Maintenance therapy with daraxonrasib monotherapy after induction extends progression-free survival by >6 months in KRAS-mutant populations achieving initial response.

**Why this matters**: Current PDAC development fails due to treating heterogeneous tumors uniformly. Our DT trial will prospectively identify which 30% of patients will respond exceptionally, enabling enriched clinical trials with doubled success rates.

## 3. Virtual-Patient Cohort Construction

**Population Archetypes**

Based on the comprehensive patient profiles from meta-analyses, we will generate 10,000 virtual patients distributed across seven validated archetypes:

| Archetype | N (%) | Key Features | Genomic Profile | Baseline CA19-9 |
|---|---|---|---|---|
| Young_Fit_Metastatic | 2,500 (25%) | Age 61±10, ECOG 0-1 | KRAS G12D (40%), G12V (30%) | 5,200±4,500 U/mL |
| Elderly_Frail_Metastatic | 1,500 (15%) | Age 76±5, ECOG 1-2 | Standard distribution | 4,800±4,100 U/mL |
| LAPC_Standard | 1,000 (10%) | Age 64±10, ECOG 0-1 | Standard distribution | 1,500±2,500 U/mL |
| Young_Fit_BRCAm | 500 (5%) | Age 60±11, ECOG 0-1 | gBRCA1/2 (100%), KRAS (85%) | 3,500±3,200 U/mL |
| Metastatic_KRAS_G12C | 300 (3%) | Age 64±9, ECOG 0-1 | KRAS G12C (100%), TP53 (40%) | 6,100±5,000 U/mL |
| Chromatin_Remodeling_Defect | 1,200 (12%) | Age 62±8, ECOG 0-1 | ARID1A/SMARCB1 loss (100%) | 4,500±3,800 U/mL |
| Immune_Excluded | 3,000 (30%) | Age 65±9, ECOG 0-1 | High FAP, CD8+ ratio >5:1 | 5,500±4,800 U/mL |

**Multi-Omic Input Generation**

Each virtual patient will have synthetically generated:
- **Genomic profile**: 400-gene panel including KRAS variants, DDR genes, chromatin remodelers
- **Transcriptomic signatures**: 20-gene panels for immune activation, stromal density, DNA repair
- **Digital pathology**: H&E-derived tumor cellularity, stromal fraction, immune infiltration patterns
- **Baseline imaging**: Synthetic CT volumetrics for measurable disease (RECIST criteria)

**Sampling Strategy**

Patients generated using hierarchical Bayesian framework:
1. Sample archetype based on real-world PDAC epidemiology
2. Generate correlated clinical features within archetype constraints
3. Apply biological correlation matrices (e.g., ARID1A loss correlates with high FAK expression)
4. Validate against TCGA-PAAD and COMPASS trial distributions

**Why this matters**: Previous trials failed by treating PDAC as homogeneous. Our virtual cohort captures the full spectrum of biological diversity, enabling precision medicine strategies that could triple response rates in defined subgroups.

## 4. Digital-Twin Architecture

**Model Hierarchy**

The DT integrates four computational layers operating at different biological scales:

**Layer 1: Tumor Growth Dynamics (Cellular Scale)**
- **3D Reaction-Diffusion PDEs** modeling tumor expansion, nutrient gradients, hypoxia
- Gompertzian growth with carrying capacity modulated by stromal density
- Drug penetration barriers based on measured tumor stiffness (MRE values)

---

# Proposal B Page 2: Prospective Stand-Alone PDAC Digital-Twin Trial, ops4

**Layer 2: Quantitative Systems Pharmacology (Molecular Scale)**

- **KRAS-MAPK pathway model**: 47 ODEs capturing G12D/V/C mutation-specific signaling
- **CD40-immune activation cascade**: APCs → T-cell priming → cytotoxic response
- **DNA damage response network**: PARP-ATR-CHK1 interactions for synthetic lethality

**Layer 3: Agent-Based TME Module (Tissue Scale)**
- 10⁶ agents representing tumor cells, CAFs, TAMs, T-cells, endothelium
- Spatial interactions governing immune exclusion, stromal barriers
- Cytokine/chemokine diffusion fields (IL-6, TGF-β, CXCL12)

**Layer 4: Machine Learning Calibration (Patient Scale)**
- Neural ODEs mapping patient features → QSP parameters
- Gaussian process emulators for computationally expensive modules
- Uncertainty quantification through ensemble predictions

**Data Flow Architecture**

```
Patient Features → ML Calibration → QSP Parameters
                                            ↓
Imaging/Pathology → Spatial Initialization → ABM Simulation
                                                      ↓
Treatment Protocol → PK/PD Module → Drug Concentrations
                                                ↓
                          Tumor Response ← Response Integration
```

**Runtime Requirements**
- **Compute**: 500 CPU-hours per patient (parallelizable to 2 hours wall-time)
- **Memory**: 32GB RAM per simulation instance
- **Storage**: 1TB for full cohort trajectories and sensitivity analyses
- **Platform**: Cloud-native (AWS/GCP) with HIPAA-compliant infrastructure

**Why this matters**: This multi-scale architecture captures the complex interplay between drug action, immune response, and stromal barriers that determine PDAC treatment success, providing mechanistic insights impossible to obtain from clinical trials alone.

## 5. Verification, Validation & Uncertainty Quantification Plan

**ASME V&V 40 Risk-Informed Credibility Framework**

| Model Component | Risk Tier | Credibility Goal | V&V Activities |
|---|---|---|---|
| PK/PD Module | Low | Level 3 | Code verification against published daraxonrasib data |
| Tumor Growth | Medium | Level 4 | Validation against RECIST trajectories from NAPOLI-1, POLO trials |
| Immune Response | High | Level 5 | Prospective prediction of OPTIMIZE-1 CD40 agonist outcomes |
| Resistance Evolution | High | Level 5 | Blind prediction of progression patterns from withheld patient cohorts |

**Proposed Prospective V&V Experiments**

1. **Pharmacokinetic Validation**: Partner with daraxonrasib manufacturer for early Phase I PK data
2. **Imaging Correlation Study**: 50-patient MRI/CT dataset with matched biopsies for spatial validation
3. **Ex Vivo Validation**: Patient-derived organoids (n=20) testing predicted drug sensitivities
4. **Clinical Trial Emulation**: Retrospective simulation of POLO and NAPOLI-1 trials as benchmarks

**Statistical Metrics**

- **Discrimination**: C-statistic >0.75 for 6-month progression prediction
- **Calibration**: Hosmer-Lemeshow p>0.05 across risk deciles
- **Clinical Utility**: Decision curve analysis showing net benefit at 20% threshold
- **Uncertainty**: 90% prediction intervals containing observed outcomes

**Why this matters**: Regulatory acceptance requires rigorous validation. Our V&V plan exceeds FDA MIDD pilot requirements, building confidence that virtual predictions translate to real patient benefits.

## 6. Prospective DT Trial Protocol

**Trial Design: VIRTUAL-PIONEER**

**Title**: Virtual Platform for Investigating Optimal PDAC Triple Therapy Regimens

**Virtual Eligibility Criteria**
- Metastatic or locally advanced PDAC
- KRAS-mutant (G12D, G12V, G12C, or other)
- ECOG PS 0-1
- No prior KRAS inhibitor exposure
- Adequate organ function per standard criteria

**Treatment Arms (2:2:1 randomization)**

**Arm A (Control)**: Nanoliposomal irinotecan + 5-FU/LV (standard second-line)
**Arm B (Doublet)**: Daraxonrasib + mitazalimab
**Arm C (Triplet)**: Daraxonrasib + mitazalimab + liposomal irinotecan

**Primary Endpoints**
- Overall survival at 12 months
- Net Clinical Benefit score (survival minus toxicity-weighted time)
