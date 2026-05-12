# Proposal B Page 3: Prospective Stand-Alone PDAC Digital-Twin Trial, ops4

**Secondary Endpoints**
- Progression-free survival
- Objective response rate by virtual RECIST
- Biomarker-stratified outcomes (FRIES+/-, chromatin remodeling defects)
- Optimal dosing schedule identification

**Interim Analyses (Bayesian Framework)**

**Month 3**: Safety run-in (n=1,000) - stop for toxicity if Grade 4 AE rate >30%
**Month 6**: Futility analysis (n=5,000) - stop arm if Pr(HR<0.8) <10%
**Month 12**: Efficacy analysis (n=10,000) - graduate to hybrid trial if Pr(HR<0.65) >80%

**Adaptive Elements**

- Response-adaptive randomization favoring superior arms
- Biomarker threshold optimization for FRIES signature
- Dose modification algorithms based on cumulative toxicity

**Why this matters**: This in silico trial will identify the optimal treatment strategy, patient selection biomarkers, and dosing schedules before exposing any real patients to experimental therapy, potentially preventing 200+ patients from receiving suboptimal treatment.

## 7. Regulatory & Ethical Alignment

**FDA Model-Informed Drug Development (MIDD) Pilot Program**

Our proposal aligns with FDA MIDD objectives through:

- **Dose Optimization**: Virtual dose-ranging preventing unnecessary Phase I escalation cohorts
- **Patient Enrichment**: Biomarker-driven selection strategies with quantified predictive value
- **Trial Design**: Adaptive features tested in silico before clinical implementation

**EMA Qualification Process**

Pursuing parallel EMA qualification opinion for:

- FRIES biomarker signature as patient selection tool
- Net Clinical Benefit as novel endpoint for PDAC trials
- Virtual patient generation methodology for rare subgroups

**Good Simulation Practice Compliance**

- **Version Control:** Git-based tracking with regulatory audit trails
- **Documentation:** SDLC documentation per IEEE standards
- **Reproducibility:** Containerized environments with fixed random seeds
- **Data Integrity:** 21 CFR Part 11 compliant data managemen

**Ethical Considerations**

While no human subjects are involved, we maintain:

- Transparent reporting of model limitations
- Public sharing of validated model components
- Patient advocacy group engagement for outcome prioritization

**Why this matters**: Regulatory endorsement of our DT approach could establish a new paradigm for oncology drug development, reducing time to approval by 2-3 years while improving patient outcomes through better trial design.

## 8. Operational Roadmap & Budget

**Phase 1: Model Development (Months 1-8)**
- Core model architecture build: 3 computational biologists, 2 software engineers
- QSP module integration: 2 systems pharmacologists
- Clinical data curation: 1 clinical informaticist, 1 biostatistician

**Phase 2: Verification & Calibration (Months 9-14)**
- V&V experiments: 2 validation scientists
- Parameter optimization: 1 ML engineer
- Clinical validation: 1 oncologist consultant (0.5 FTE)

**Phase 3: Trial Execution (Months 15-20)**
- Large-scale simulations: Cloud compute allocation
- Real-time analysis: 2 data scientists
- Regulatory documentation: 1 regulatory affairs specialist

**Phase 4: Reporting & Transition (Months 21-24)**
- Final analysis and manuscript preparation
- Regulatory submissions
- Hybrid trial protocol development

---

# Proposal B Page 4: Prospective Stand-Alone PDAC Digital-Twin Trial, ops4

**Budget Summary (24 months)**

| Category | Cost |
|---|---|
| Personnel (10.5 FTE average) | $4.2M |
| Cloud Computing (AWS) | $1.5M |
| Validation Studies | $1.8M |
| Regulatory Consulting | $0.5M |
| Overhead (15%) | $0.5M |
| **Total** | **$8.5M** |

**Why this matters**: This investment is <10% of a traditional Phase II/III program cost while providing superior mechanistic insights and de-risking critical development decisions.

## 9. Risk Register & Mitigations

**Technical Risks**

| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| Model complexity prevents convergence | High | Medium | Modular architecture with fallback simplified models |
| Insufficient parameter identifiability | High | Low | Bayesian priors from 40 meta-analyses constrain parameter space |

**Regulatory Risks**

| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| FDA rejects virtual evidence | High | Low | Early MIDD pilot engagement, precedent from COVID vaccine trials |
| EMA qualification delays | Medium | Medium | Parallel FDA/EMA submissions, interim opinions |

**Commercial Risks**

| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| Competing therapy launches | Medium | Medium | Platform adaptability to incorporate new agents |
| IP challenges on biomarkers | Low | Low | Freedom-to-operate analysis, academic partnerships |

**Why this matters**: Proactive risk management ensures project continuity and protects investor value through systematic mitigation strategies.

## 10. Milestones & Go/No-Go Criteria

**Critical Success Milestones**

**M1 (Month 8)**: Model achieves C-statistic >0.75 for progression prediction on holdout NAPOLI-1 data
- Go: Proceed to full validation
- No-Go: Refine model architecture

**M2 (Month 14)**: FRIES biomarker shows >3-fold enrichment in virtual responders with p<0.001
- Go: Include biomarker stratification in trial
- No-Go: Develop alternative selection strategy

**M3 (Month 20)**: Triplet therapy demonstrates HR <0.65 with acceptable toxicity in >30% of patients
- Go: Proceed to hybrid DT-human trial design
- No-Go: Test alternative combinations

**M4 (Month 24)**: FDA provides positive MIDD feedback on trial design
- Go: Launch Phase I/II with DT-optimized protocol
- No-Go: Revise per regulatory guidance

**Transition Criteria to Hybrid Trial**

Virtual trial graduates to hybrid human-DT trial when:

1. Primary efficacy threshold met (HR <0.65)
2. Biomarker-defined population identified (>30% prevalence)
3. Optimal dose/schedule determined (NCB maximized)
4. Regulatory alignment achieved
5. Clinical partner secured

**Why this matters**: Clear, quantifiable milestones ensure disciplined capital deployment and maximize probability of clinical success while providing multiple value-creation opportunities throughout development.

---

# Top 3 PDAC DT Proposals: Timeline Comparison & ROI Analysis

**Figure (3Proposals1Timeline):** Top 3 Proposals Timeline. June 12, 2025, ops4. [Image: images/Image-Pro3-Ops4-03.png]

> **Top 3 proposal 24 month timelines differed in phase types and times, especially for Proposal D by model o3ch.**

**Figure (3Proposals2Radar):** Top 3 Proposal Radar Charts. June 12, 2025, son4. [Image: images/Image-Pro3-Son4-06.png]

> **Return on investment favored Proposal D by o3ch overall based on three 9/10 scores in Technical Innovation, Risk Reduction, and Portfolio Utility.**

---

# Top 3 PDAC DT Proposals: FTE Allocation & Budget Waterfall

**Figure (3Proposals3FTE):** Top 3 Proposal FTE Allocation. June 12, 2025, ops4. [Image: images/Image-Pro3-Ops4-08.png]

> **Proposals A & B utilized the majority of FTE employees within 12-14 months. Proposal D used higher FTE counts that were centered through M4-M22.**

**Figure (3Proposals4Budget):** Top 3 Proposal Budget Waterfall. June 12, 2025, ops4. [Image: images/Image-Pro3-Ops4-01.png]

> **Budgets were highest for Proposals A & D at $17.8M and $10.5M respectively.**
> 
> **Proposal A by o3pr distributed the price of running a simulated trial the best, with costs ranging from $1.7M for Regulatory to $4.5M for DT execution.**
> 
> **Proposal B by ops4 had a wider distribution of expenses from $0.5M for Regulatory to $4.2M for Personnel.**
> 
> **Proposal D by o3ch also had a lopsided distribution, starting at $0.3M for Data Curation and ending with $4.1M for Overhead/IP.**

---

# Discussion

The ability of digital twins to build, run, and learn simulated environments provides safety and effectiveness advantages for clinical trials in oncology. Digital twins have increased in responsibilities ranging from cohort selection processes to insightful patient stratification. These artificial intelligence layers have allowed for greater "what-if" questions to be proposed in real time with predictive monitoring and adverse events being observed for patient well being.

A number of PDAC digital twin initiatives have been conducted by organizations including Frederick National Laboratory, Johns Hopkins University, and Genentech. Digital twin focal points included simulating one million pancreatic cancer patients by the National Lab, while Johns Hopkins partnered with Cedars-Sinai to use "molecular twins" with mult-omic data to predict patient PDAC outcomes. Genentech predicted kinetics for patients with pancreatic cancer using digital twint to elucidate the role of Tscm in clinical persistence of TCR-engineered cell therapy.

High performance conversational AI models have been released in 2025 to help locate clinical trial papers, perform analyses, judge multiple answers, and create visualizations - justifying end-to-end PDAC proposal generations. The meta-analyses by o3re depict an average of 10,196 words in 19.3 minutes per generation. The 40 meta-analysis areas allowed for a broad search of clinical trial data in a consistent format, which was ideal for next processing steps. The g25p model returned one verification for each of the meta-analyses and self scored at 95%, shown in 40MAAnalysis. This more automated process has allowed for a larger study, as speed was improved vs. prior works that manually checked traces [15KawchakAgent, 16KawchakLung, 17KawchakGlioblastoma]. However, due to current g25p limitations in grounding multiple sources at this scale while searching for URLs and scoring correlations, verification accuracy was limited.

The resulting 40 meta-analyses in Dataset 1 were processed using six variants of Standard C prompts by g25p to yield six impactful report areas to help guide future PDAC clinical trials. The full 400,000+ word dataset and each respective report were compared and a new verification table was produced, as shown in for Report 1 in Report06_Verify. Each report was visualized with 10 charts, with most relevant charts used to support included proposals.

With each of the 6 combined reports in Dataset 2, the following models: o3pr, ops4, g25p, o3ch, and grk3 generated Proposals A, B, C, D, E respectfully based on Standard F Prompt 63. Each model used the correct three-drug combination with the highest TSVS value of 8.15 from Report 1 in their proposal: Daraxonrasib + Mitazalimab + Liposomal Irinotecan, indicating a high level of artificial intelligence contextual awareness. ops4, g25p, o3ch, and grk3 showed proficiency in incorporating references from other reports, but only o3pr consistently incorporated references. These findings are apparent in the average of the five models' judge scores of the proposals in the five radar charts by son4 in 5ProposalsRadar, with o3pr having the highest Report/MA Cited score of 9.20/10, followed by ops4 at 8.98. Final funding probabilities followed a similar trend: o3pr = 8.66, ops4 = 8.58, o3ch = 8.54, g25p = 6.74, grk3 = 5.62.

The top three proposals: o3pr, ops4, o3ch were combined for further analysis in charts by ops4 and son4 to yield several coherent synopses. The PDAC digital twin trial timeline comparison in 3Proposals1Timeline illustrated the 24 month differences in proposed model build, verification and validation, execution, and additional information. Proposal A by o3pr yielded the simplest time line with four phases equally spaced at 6 months, while Proposal D by o3ch was the most complex, with six phases of varying time periods. The three return on investment radar plots in 3Proposals2Radar show Proposal A strengths in Regulatory Advantage (9) and Speed to Market (8); while Proposal B was most proficient in Capital Efficiency (9). Proposal D by o3ch surprisingly ranked the highest in three areas: Technical Innovation (9), Risk Reduction (9), and Portfolio Utility (9). These results indicate that Proposal D may have the most overall ROI advantages, a trend not seen elsewhere in the study.

The resource allocation comparison in 3Proposals3FTE provided perspectives of Full-Time Equivalent employees necessary to complete the 24 month PDAC digital twin trial. Proposal A FTE count proceeded from 12 employees in the first 6 months for model build, and reduced to 6 employees in the last 6 months. Proposal B showed a sharper decline: with FTE count = 9 for M1-8, rapidly decreasing to 1 in the last six months of the reporting phase. Proposal D experienced the highest overall FTE counts, with lower employees for the first three and last months, and maximized at 16 for months 10-14 and 15-18.

The trial budget waterfall comparison depicted Proposal A by o3pr as having the highest budget at $17.8M for the dose-finding Phase I/early-Phase II digital twin trial, with an emphasis of DT Execution ($4.4M) and Cloud/Compute at $4.0M. Proposal B by ops4 had the lowest budget at $8.5M for a randomised, efficacy-driven Phase IIb–III-like trial, with a strong reliance on personnel at $4.2M, followed by validation studies at $1.8M. Proposal D by o3ch had a total budget of $10.5M, favoring overhead/IP at $4.1M, with worth validation/UQ and virtual trial at $1.4M each.

---

# Limitations and Future Work

A main limitation for the end-to-end study was the output accuracy when disparate data sources required verifications. For Part I, the o3re model performed several complex steps in addressing a detailed prompt, searching the internet for relevant trials, and reporting back a 10,000 word meta-analysis with pooled data. The current verification process of accuracies is preliminary, as only one model, g25p, had the available context length to simultaneously ground multiple data from 400,000+ words in Dataset 1, search the internet for matching clinical trial URLs, and create a table that sampled each meta-analysis one time, shown in 40MAAnalysis. Although the technique provided several layers of information from the meta-analyses, the additional complexity of URL searches with matching article values may have contributed to a higher than expected average score across forty samples of 0.95. In addition, small changes to un-optimized prompts led to less favorable ranges of utility.

Part II report generations were again limited to the use of g25p, due to context length limitations of the 400K word dataset experienced with the other models. The g25p model had again to be utilized in verifications due to high context lengths in comparing to Dataset 1. Other models would have been preferred to reduce chances of model bias amplification, but could not accept the larger input size. The report charts generated by son4 had to be screened for quality for use in the paper which were based on formatting, the level of detail, or how convincing the visualization was. A small number of the charts had to be corrected using grk3 for the Python code to be generated properly. The Part III and Part IV digital twin trial AI proposals charts by son4 or ops4 faced the same level of scrutiny to be included with the final paper, with ops4 having less formatting errors. Overall, this paper represents high levels automation in processing multiple tasks across workflows, while verification steps will need to improve in exact recall as increasing number of jobs are managed by AI.

Future work will likely first focus on optimizing a scaled down version of the 10,000 virtual patient 24 month trial inspired by oncology proposals presented in this study. These efforts are expected to be accomplished by obtaining simulated patient data using multiple o3re generations from clinical trial data across the internet. The study will primarily focus on putting into action summarized clinical trial data to better improve the decision making process to aid drug efficacy.

---

*"PDAC is projected to overtake colorectal cancer before 2040, moving only behind lung cancer as a leading cause of cancer-related mortality."* - Halbrook C., et al. [01QuoteHalbrook]

*"Pancreatic cancer has a poor prognosis, with a 5-year survival rate of less than 9%, primarily because of nonspecific symptoms and late detection."* - Urooj W., et al. [03QuoteUrooj]

*"Artificial intelligence (AI) and machine learning (ML) are emerging as pivotal tools in revolutionizing PDAC care across various dimensions."* - Mukund A., et al. [02QuoteMukund]
