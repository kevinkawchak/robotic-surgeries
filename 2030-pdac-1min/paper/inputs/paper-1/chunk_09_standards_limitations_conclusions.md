# Standard 1: AI Peer Review to First Digital Twin Notebook

**Purpose:** A quad AI notebook peer review of the author's previous QSP trial B1_Final_Trial_Code.ipynb was performed using the prompt: "What are all of the problems with this QSP virtual trial study?" in four separate conversations of ChatGPT, Gemini, Opus, and Grok. The four outputs were combined and used in Prompt 01, below with ChatGPT to obtain a consolidated Top 12 list of Peer Review corrections (02_QspTWIN_Top12).

**Prompt 01:** "Included are several code reviews (ABCD Code Review 02Sep25.docx) of the attached script (B1_Final_Trial_Code.ipynb). Please consolidate the actions that need to be updated into a long list (Starting at 1 being most important) regarding the most important issues that need to be resolved continued through the least important issues. Include relevant code, and actual examples of replacement code where applicable. A copy of the paper is also attached for reference (additional VVUQ and playbook were also performed)." Attached: 10.5281/zenodo.17001136 pdf, B1_Final_Trial_Code.ipynb, ABCD Code Review 02Sep25.docx.

**Purpose:** For best overall results, a main trial protocol was first created in text (05_QspTWIN_Simulation_gpt5).

**Prompt 02:** "Based on the attached documentation (C1_Final_Protocol.docx, QSP Metastatic Pancreatic Cancer AI Clinical Trial Simulation From Protocol to Prediction: Code, VVUQ, and Playbook.pdf, and 02_QspTWIN_Top12.docx), create the full plain text protocol necessary to conduct a 1,000 total patient digital twin PDAC simulation that a) generates a continuous stream of patient data, b) analyzes the patient data, and c) returns back treatment recommendations to the patients, and d) after patients are treated sends their updated recordings back to the digital twin. This process continues and updates bi-directionally throughout the course of the trial. Use the C1_Final_Protocol as a template for structuring the new digital twin simulation protocol. Simultaneously address issues and include recommendations found in 02_QspTWIN_Top12 while creating the new text protocol. This digital twin simulation is designed to simulate the digital twin's involvements in a clinical trial, in which the digital twin operates bi-directionally to improve the quality of assessing and intervening with the patients of the clinical trial. It is important to note that all patient data must be generated (this is a simulation, as there are no sensors gathering actual patient data). Provide only the full plain text protocol required to run the digital twin simulation. It is important that relevant parameters and variables be in the form of easy to interpret tables where appropriate, being concise and not too verbose (but include brief comments for each relevant section). These parameters and variables will be used as tables in future steps. Each patient is an independent cycle of treatment–feedback–update regardless of arm assignment. Update frequency should be every cycle. Provide instructions to output an appropriate number of CSVs (patient log file(s)) using a format similar to the attached template. Write the protocol to output patient/arm/archetypes (whichever are most relevant) (with corresponding timer(s), and the final time) visual updates as the trial progresses, with tables (endpoints, useful information for forest plots, kaplan meier curves, etc.)(visualizations will use these tables in later steps). Obtain additional context of the trial from the main paper QSP Metastatic Pancreatic Cancer AI Clinical Trial Simulation From Protocol to Prediction: Code, VVUQ, and Playbook.pdf. Essentially, the new digital twin simulation should be a complete standalone work represented in the plain text protocol, while fixing issues from the previous QSP trial, and taking context from the main paper. Only return the full plain text protocol." Attached: 02_QspTWIN_Top12.docx, QSP Paper 10.5281/zenodo.17001136, C1_Final_Protocol.docx

**Purpose:** The first usable Python notebook by ops41 (06_QspTWIN_Simulation_ops41) was obtained using the prompt below.

**Prompt 03:** "Convert the attached 05_QspTWIN_Simulation_gpt5 text protocol into a standalone fully functional Python notebook. Provide any installs that would be needed for running in Colab. Be sure to carry over the full meaning of digital twin simulation from the text protocol, while following the B1_Final_Trial_Code.ipynb template as a guide. It is important that the bi-directional nature of the digital twin simulation is intact throughout the entire trial (a) generates a continuous stream of patient data, b) analyzes the patient data, and c) returns back treatment recommendations to the patients, and d) after patients are treated sends their updated recordings back to the digital twin). It is also important to note that all patient data must be generated (this is a simulation, as there are no sensors gathering actual patient data). Use naming conventions that are logical if not specified. Additionally, it is important that relevant parameters and variables must be in the form of easy to update tables where appropriate, being concise and not too verbose (but include brief comments for each relevant section). Provide instructions to output an appropriate number of CSVs (patient log file(s)) using a format similar to the attached template. Write the protocol to output patient/arm/archetypes (whichever are most relevant) (with corresponding timer(s), and the final time) visual updates as the trial progresses, with tables (endpoints, useful information for forest plots, kaplan meier curves, etc.)(visualizations will use these tables in later steps). Essentially, the new digital twin simulation should be a complete standalone Python notebook to run in Colab." Attached: 05_QspTWIN_Simulation_gpt5.docx, B1_Final_Trial_Code.ipynb

Standard 1 Process Diagram: Prior QSP Python Code → Quad AI Code Review → Prior QSP Main Paper → Consolidated Peer Review → Main Text Protocol → Digital Twin First Code

---

# Standard 2: Parameter Optimization and External Validation

**Purpose:** ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb (in ops41) was obtained using the Prompt 04 instructions.

**Prompt 04:** "The original 06c_QspTWIN_Simulation_ops41.ipynb is attached. Its four csv files are attached at the end of Combined_06c_QspTWIN_Simulation_ops41. Each of the tests with results are based on the original notebook and are included in Combined_06c_QspTWIN_Simulation_ops41. Provide a full new digital twin simulation Python notebook based on the attached notebook that learns from the results in the tests and addresses control and experiment arm ORR/DCR, PFS/OS values being off, and other pertinent clinical trial related values.

Provide additional analysis on these three files, as some of the metrics in the main results and/or csv files appeared to be a step in the correct direction.

06c_QspTWIN_Simulation_ops41_Test_1_Numerical_Stability_Experiment_v6e1.ipynb
06c_QspTWIN_Simulation_ops41_tumor_sensitive_005.ipynb
06c_QspTWIN_Simulation_ops41_Test_3_Sensitivity_Analysis_and_Clinical_Calibration.ipynb

Return only the new full Python notebook of the digital twin simulation." Attached: 06c_QspTWIN_Simulation_ops41.ipynb, Combined_06c_QspTWIN_Simulation_ops41.docx.

**Purpose:** Based only on control arms A and G literature values, ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb produced the best and most acceptable calibration results for control arms versus other LLMs. (Output: fixg25p3_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb)

**Prompt 05:** Provide the full new Python code to the attached script based on the following control arm recommendations. Only make changes based on the recommendations: "START" Arm A - STD_CHEMO (Gemcitabine + nab-Paclitaxel)

Simulation values (from CSV): median OS 0.00 mo, median PFS 36.00 mo (censored), ORR 0.0%, DCR 59.1%, ≥G3 AE (proxy dose_adjusted) 0%.
Clinical targets (control): OS ≈ 8.5 mo, PFS ≈ 5.5 mo, ORR ≈ 23%, DCR ≈ 60–70%, many ≥G3 AEs.

Metric | Simulation | Target | Notebook parameter(s) | Recommended range | Expected impact
OS ↑ | 0.00 mo | ~8.5 mo | DRUG_PARAMS['gemcitabine']['Emax'] | 0.065–0.080 (from 0.045) | More kill per dose, better survival
DRUG_PARAMS['nab_paclitaxel']['Emax'] | 0.050–0.070 (from 0.035)
PatientSimulator.tumor_sensitive (init) | 0.70–0.80 (from 0.75) | Slightly more shrink-able clone
DigitalTwin.calculate_hazard → base_hazard | 0.0012–0.0016 / 30 (from 0.002/30) | Calibrate background hazard to OS

Attached: ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb.

**Purpose:** Gemini found ops41_Combined_06c_QspTWIN_Simulation_ops41) to be the best current notebook.

**Prompt 06:** Provide in a large table a comparison between the three notebooks in terms of which is most appropriate for use moving forward (with other relevant pros and cons between the notebooks). Attached: ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb, fixg25p_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb, fixg25p3_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb

**Purpose:** Gemini found fix_ops41_g25p3_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb (Notebook A) the best performing notebook vs. other notebooks.

**Prompt 07:** For all notebooks, create tables that detail which notebook is accomplishing all of the requirements to be a bi-directional digital twin simulation. This means that the following must be correctly performed: a) generates a continuous stream of patient data, b) analyzes the patient data, and c) returns back treatment recommendations to the patients, and d) after patients are treated sends their updated recordings back to the digital twin. This process continues and updates bi-directionally throughout the course of the trial. Assign notebooks to single letters in the beginning (A, B, C, etc.), to make identification easy.
Most importantly, compare in tables the clinical trial simulation performance versus expected values for arms, archetypes, etc. This should cover metrics such as ORR, DCR, OS, PFS, etc. Compare notebooks based on their performance vs. expected values for patients who are alive vs. progressed through each cycle (and why do patients stop progressing at a specific cycle, and other values that do not make sense based on the code.) Attached: fixg25p_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb, fixg25p2_1SurvivalHR_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb, fixg25p3_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb, fixops41_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb, ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb.

Standard 2 Process Diagram: Prior DT Notebook → Prior DT Log Files → Parameter Optimization → External Validation → Notebook Comparisons → Top Current Notebook

---

# Standard 3: Re-Optimize Baseline Characteristics, Notebook Speedup, VVUQ

**Purpose:** 1kpatient_transferb1_g25p_t02_tp090_fix_ops41_g25p3_gpt5_ops41_combined_06c_qsptwin_simulation_ops41.ipynb was obtained by g25p (Temp=0.2, Top P=0.9) significantly improving simulation summary results by re-calibrating from old Notebook B1_Final_Trial_Code.ipynb

**Prompt 08:** Transfer all respective Arch, Arm, Drug, Biomarker, Toxicity/G3+ AE, etc. settings from B1 to create a new notebook based on fix_ops41. The end result needs to have similar values to ORR/DCR/PFS/OS/G3+ AE in the final summary. Test to make sure the output values are similar between B1 and the new code based on fix_ops41. Make sure each arm shows up in the trial summary statistics. Do not lose any functionality of the digital twin simulator from fix_ops41, and make sure each of the CSVs output and function correctly. Keep all formatting, outputs, and csvs as close to the original fix_ops41 notebook. Essentially, calibrate the new notebook based on B1 settings without making unnecessary changes to fix_ops41. Attached: B1_Final_Trial_Code.ipynb and fix_ops41_g25p3_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb

**Purpose:** Faster notebook VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090_fix_ops41_g25p3_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41 was obtained with increased runtime speed by over 12x.

**Prompt 09:** Optimize the included notebook for running on the v6e-1 TPU on Colab. It is important that all outputs for the notebook and csv files remain identical to the original notebook. Essentially, the only difference should be a faster new notebook in Python. Only include the new optimized notebook. Attached: 1KPatient_transferB1_g25p_T02_TP090_fix_ops41_g25p3_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb.

**Purpose:** Obtained VV40/FDA Tests, Set Arms to 100 Patients Each, Truncate File Name Length. Output: VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090 (ops41)

**Prompt 10:** Using a prior paper's VVUQ supplementary and the included section below: develop regulatory-grade tests the user can perform throughout different iterations of the attached notebook in Colab. These tests must include the exact parameters or variables in the notebook and exact values (at least two new values typically) to change to. For instance, the prior paper used several tests based on "dt" and "grid_size" by varying each respective number across separate notebooks to prove that the notebook was numerically stable. Likewise biological similarity/sensitivity analyses changed 1 or 2 values at a time to show that the notebook was biologically stable. The goal here is to use some of the paper author's prior effective approaches for numerical and biological stability, while addressing regulatory-grade requirements under the ASME V&V 40 standard and FDA requirements. Only the exact tests of specific values to change are required. The results will also be used to optimize TRIAL SUMMARY STATISTICS at the bottom of the notebook. "START RECOMMENDATIONS" Objective: Elevate the QSP digital twin model to a regulatory-grade level of credibility by implementing thorough verification, validation, and uncertainty quantification (VVUQ) practices, and by clearly defining its context of use. In doing so, ensure that model outputs can be trusted by external stakeholders (regulators, clinicians, investors) and thus reduce regulatory burdens (e.g. by allowing model-informed decisions in place of some empirical tests). 12 6 13 4 Justification & Details: In the prior study, substantial effort went into model validation and uncertainty analysis (the playbook included a dedicated VVUQ report, Part D) to build confidence in the simulation results. The current project should expand on this foundation by aligning with formal credibility guidelines. One such guideline is the ASME V&V 40 standard, which provides a framework for assessing computational model credibility in the context of medical applications. Additionally, FDA's own recommendations for model-informed submissions highlight the need to evaluate model risk – considering both the influence of model results on decision-making and the potential consequences if the model is wrong... Attached: VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090_fix_ops41_g25p3_gpt5_ops41_Combined_06c_QspTWIN_Simulation_ops41.ipynb + Prior Paper D1_VVUQ_Report.pdf.

Standard 3 Process Diagram: Prior QSP Python Code → Baseline Characteristics → Parameter Settings → Updated Notebook → Notebook Speedup → New VVUQ Code Tests

---

# Standard 4: Model Simplification, Refactoring, and Calibrations

**Purpose:** Apply4d_VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090.ipynb was outputted, along with user assistance: Improved calibration by lowering both mPFS and mOS.

**Prompt 11:** Compare the attached Notebook E to the rest of the notebooks in multiple tables. Do you know what you are doing? Attached: 100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090.ipynb, Other Inputs: Apply4c_VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090.ipynb.

**Purpose:** Ref2_Apply4d_VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090 was outputted as next notebook.

**Prompt 12:** Provide the exact full new Python notebook (no JSON) to remove components of this notebook that are preventing optimization to the attached PROJECTED TRIAL SUMMARY STATISTICS with additional tabular explanations. All of the digital twin interactions must remain ((a) generates a continuous stream of patient data, b) analyzes the patient data, and c) returns back treatment recommendations to the patients, and d) after patients are treated sends their updated recordings back to the digital twin.)) Arms, Drug Params, and Archetypes must remain as is, but could be reduced in complexity if required. Trial result summaries and csv output methods must also remain the same. Essentially, remove the extra details that are preventing calibration from occurring, keeping biological and mechanic requirements of a pancreatic cancer digital twin trial simulation. Comment on the changes made to the new full notebook. PROJECTED TRIAL SUMMARY STATISTICS (Based on Clinical Data)
Arm   N      ORR%   DCR% | mPFS     PFS-6 | mOS      OS-12 | Safety (G3+/Drop%) --- ----- ------ ------ | -------- ----- | -------- ----- | ------------------ A   110    23.0%  57.0% |  5.5 mo  42.0% |  8.5 mo  35.0% | 38.0% / 20.0% B   100    25.0%  60.0% |  5.8 mo  44.0% |  9.0 mo  37.0% | 40.0% / 22.0% C   100    33.0%  81.0% |  7.2 mo  55.0% | 10.5 mo  42.0% | 42.0% / 15.0% D   90     23.0%  57.0% |  5.5 mo  42.0% |  8.5 mo  35.0% | 40.0% / 22.0% E   100    25.0%  60.0% |  6.0 mo  45.0% |  9.5 mo  38.0% | 45.0% / 25.0% G   100    16.0%  52.0% |  3.1 mo  26.0% |  6.1 mo  26.0% | 27.0% / 15.0% H   100    35.0%  82.0% |  5.4 mo  40.0% |  8.0 mo  32.0% | 35.0% / 20.0% I   100    30.0%  80.0% |  4.5 mo  35.0% |  7.0 mo  28.0% | 30.0% / 10.0% J   100    23.0%  53.0% |  7.4 mo  48.0% | 19.0 mo  52.0% | 49.0% / 9.0% K   100    12.0%  37.0% |  3.8 mo  31.0% | 19.2 mo  50.0% | 23.0% / 2.0%
Looking at the simulation output compared to the projected trial statistics, there are several significant discrepancies that indicate problems with the model calibration and implementation. Let me provide detailed tables analyzing these issues:... Attached: Apply4d_VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090.ipynb.

**Purpose:** fixdtA_Ref2d3USER_Apply4d_VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090.ipynb Was found to be the Rank 1 notebook.

**Prompt 13:** Analyze like the other notebooks: (Rank 1) Attached: (from g25p g25p_Ref2d3USER Comparisons Notebook Analysis and Grading. g25p_Ref2d3USER Comparisons Notebook Analysis and Grading file (many optimizations)) Attached: g25p_Ref2d3USER_Apply4d_VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090.ipynb

**Purpose:** Convert final digital twin notebook to a text protocol. Output = (Text_final_g25p_Ref2d3USER_Apply4d_VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090)

**Prompt 14:** Based on the attached template (05_QspTWIN_Simulation_gpt5.docx): create a new text based trial that incorporates all information from the attached Python notebook (final_g25p_Ref2d3USER_Apply4d_VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090.ipynb). The new text based trial must follow the format of the template, but now in the context of the attached notebook. Do not truncate or remove any of the necessary organizational components of the prompt template, and make sure that the new text instructions contain all of the information from the attached script to run a text based trial on an LLM with the same results as using the script reproducibly on an IDE (be accurate to the script, as some differences exist between the template and the script). The attached script is complex, with other components that were added: therefore the new trial instructions should be more complex and longer than the template. Attached: 05_QspTWIN_Simulation_gpt5.docx, final_g25p_Ref2d3USER_Apply4d_VV40_100Arms_VectorizationJITParallel_1KPatient_transferB1_g25p_T02_TP090.ipynb

Standard 4 Process Diagram: Notebook Comparisons → Notebook Calibrations → Simplified Model → Notebook Refactoring → Final Summary → User Calibrations

---

# Section: Limitations and Future Work

The final trial notebook utilizes archetype assignments, biomarker flags, and a single lognormal "drug sensitivity multiplier." It does not perform patient-specific parameter estimation from longitudinal data (e.g., Bayesian updating of PK/PD or tumor growth parameters). In addition, physiologic fidelity differences existed with the model used a simplified Emax PK/PD, no explicit immune compartments, and no spatial tumor heterogeneity. More advanced virtual twins often integrate multi-scale physiology (cellular to organ), mechanistic immune–tumor interplay, microenvironmental features, and realistic PK (distribution, permeability, TMDD).

In addition, no online filtering/regression was applied to fit each patient's evolving labs/imaging as patient generated patient data within the model did not have this feature. A real twin would ingest electronic health records (EHRs), labs, vitals, imaging-derived tumor measurements, and patient reported outcomes (PROs) in real time, with data governance and provenance. Also, real in person twins require bias/fairness analysis, and sometimes regulatory clearance. Furthermore, there was no handling of measurement noise/delays. The recommendation policy in this study is a simple rule-based switch (continue vs. switch to a single 2L option vs. BSC). It is not a formal decision-optimization (e.g., model predictive control or reinforcement learning balancing efficacy, toxicity, and patient preferences). No interim-futility, no adaptive randomization, no CI/uncertainty reporting, and no bootstrap/posterior intervals were utilized for endpoints. Also, there were no security/PHI controls, deployment infrastructure, monitoring, or fail-safes for clinical use.

Another main limitation was external validation to prior clinical trial controls. After obtaining a functional trial simulation, a majority of the experiments were spent achieving acceptable trial summary statistics. For Arm A (Gemcitabine + nab-paclitaxel; first-line metastatic PDAC; MPACT trial), the published (approximate) for ORR was ~23%; mPFS was ~5.5 months; while mOS was ~8.5 months. The 12-month OS was in the mid-30% range; Grade 3/4 AEs roughly high-30s to 40%; with discontinuation around the high teens. The final_g25p notebook was ORR 21%, mPFS 4.7 mo, mOS 9.3 mo, OS-12 43%, G3+ 31%, Drop 17%. PFS was somewhat low (4.7 vs ~5.5 mo). OS-12 and mOS were a bit higher than expected for control; G3+ rate was somewhat low; DCR 82% was likely higher than many reports for GnP (DCR definitions vary, but 82% was on the high side). For Arm G (nal-IRI + 5-FU/LV; 2L; NAPOLI-1 doublet): The published (approximate) was mOS ~6.1 mo; mPFS ~3.1 mo; response rate modest (single-digit to teens depending on criteria); 12-month OS around mid-20% range.
final_g25p was ORR 3%, DCR 41%, mPFS 1.8 mo, mOS 5.6 mo, OS-12 15%, G3+ 18%, Drop 10%. PFS was short (1.8 vs ~3.1 mo) and 12-month OS too low vs typical reports.

Arm G Safety profile was simplified (per-cycle G3+ probability), so the G3+ rate may not reflect true 2L chemo toxicity patterns. Arms J vs K (Olaparib maintenance vs placebo; POLO trial, gBRCA-mt, post-platinum) were farther off for the current study than in literature. The remaining arms Arms B (magrolimab combo), C (MRTX1133 combo), D (PEGPH20 combo), E (pembro + mitazalimab combo), H/I (daraxonrasib ± chemo + mitazalimab) also were attempted to external studies, with some success in endpoint performance.
No confidence intervals, no p-values, no multiplicity control, and no calibration report that shows simultaneous fit to multiple endpoints (ORR/PFS/OS/G3+/dropout) against reference data were provided. Future studies can address some of these calibration issues by running repeated simulations to produce confidence intervals, tightening calibration of A, G, and J/K to their respective trials, and porting selective mechanistic components from the prior QSP trial (e.g., neutrophil-driven toxicity or dose modification) into final_g25p while preserved the digital twin feedback loop. The paragraphs in this section were assisted by gpt-5 high.

---

# Section: Conclusions

The final_g25p notebook delivered a working digital-twin simulation with a bidirectional feedback loop, per-patient decision logs, time-series data streams, and arm-level clinical endpoints. Key digital twin mechanisms defined by the author were verified throughout the trial iteration process: I) Generates a continuous stream of patient data, II) Analyzes the patient data, III) Returns back treatment recommendations to the patients, and IV) After patients are treated sends their updated recordings back to the digital twin. The current trial is biologically simpler and computationally lighter than the author's prior QSP study and has some improved face-validity for some endpoints (e.g., Arm A). Compared to the QSP study, the digital twin sacrifices mechanistic fidelity (immune, TMDD, spatial diffusion, lesion-level RECIST, dose modifications, interim-futility) for a compact, easy-to-run twin that demonstrates the end-to-end "sense–analyze–recommend–act–learn" loop. For clinical/external validation, at least the control arms (A, G, K) need closer calibration to known trials (MPACT, NAPOLI-1, POLO), and the model should report uncertainty and reproduce key comparators across multiple seeds/runs. Several investigational arms have no definitive clinical benchmarks, so no absolute performance claims can be made.

This virtual trial is modeling what would be an ambitious Phase II "umbrella" or "platform" trial design, where multiple treatment hypotheses are tested simultaneously to identify promising signals for further development in Phase III trials. The sample size of 100 patients per arm is typical for Phase II trials testing efficacy signals. Multiple experimental arms testing 10 different regimens simultaneously is characteristic of exploratory Phase II platform trials endpoints which focus on efficacy signals (ORR, PFS, OS) rather than dose-finding or definitive superiority. Biomarker stratification used BRCA and KRAS mutations for patient selection, common in Phase II precision oncology trials. Novel combinations of experimental drugs (MRTX1133, Daraxonrasib, Mitazalimab) based on three prior studies combined with standard therapies. Overall, the model saw an increase in trial summary performance over notebook iterations using AI, and exhibited core digital twin functionals with generated patient data.

The current study was effective at addressing the FDA "Assessing the Credibility of Computational Modeling and Simulation in Medical Device Submissions" and ASME V&V 40 Computational Modeling standard with high cost efficiency achieved through AI generations of text protocols, Python models, and multiple model log outputs used in visualizations. These tests performed by the author helped to answer questions regarding a) Verification: how input uncertainty propagates to output uncertainty, b) Validation: how suitable the model is for its intended purpose, c) Uncertainty Quantification: how robust the model was to biological and clinical assumptions regarding changes in key parameters, and d) Applicability: how credible the model was in regards to assumptions against its intended use. Overall AI performance scores for compliance related tests were found to be 81.9/100 for Verifications and 85.75% for the Validations.

---

# Data Availability: Zenodo

**Final Files: .ipynb, .py, .csv, .docx, .pdf**
1. final_g25p_Ref2d3USER_Apply4d...
2. Text_final_g25p_Ref2d3USER_Ap...
3. _adaptation_log
4. _adaptation_summary
5. _digital_twin_calibrated_final
6. _km_data_by_arm
7. _patient_logs
8. _waterfall_plot_data

**Prompt 01: .ipynb, .docx, .pdf**
9. B1_Final_Trial_Code
10. ABCD Code Review 02Sep25

**Prompt 02: .docx, .pdf**
11. 02_QspTWIN_Top12
12. C1_Final_Protocol

**Prompt 03: .ipynb, .docx, .pdf**
13. B1_Final_Trial_Code
14. 05_QspTWIN_Simulation_gpt5

**Prompt 04: .ipynb, .docx, .pdf**
15. 06c_QspTWIN_Simulation_ops41
16. Combined_06c_QspTWIN_Simulati...

**Prompt 05: .ipynb**
17. ops41_Combined_06c_QspTWIN_S...

**Prompt 06: .ipynb**
18. fixg25p_gpt5_ops41_Combined_06c...
19. fixg25p3_gpt5_ops41_Combined_06...
20. ops41_Combined_06c_QspTWIN_S...

**Prompt 07: .ipynb**
21. fixg25p_gpt5_ops41_Combined_06c...
22. fixg25p2_1SurvivalHR_ops41_Comb...
23. fixg25p3_gpt5_ops41_Combined_06...
24. fixops41_gpt5_ops41_Combined_06...
25. ops41_Combined_06c_QspTWIN_Si...

**Prompt 08: .ipynb**
26. B1_Final_Trial_Code
27. fix_ops41_g25p3_gpt5_ops41_Com...

**Prompt 09: .ipynb**
28. 1KPatient_transferB1_g25p_T02_TP...

**Prompt 10: .ipynb, docx, .pdf**
29. VectorizationJITParallel_1KPatient_t...
30. D1_VVUQ_Report

**Prompt 11: .ipynb**
31. 100Arms_VectorizationJITParallel_1...
32. Apply4c_VV40_100Arms_Vectoriza...

**Prompt 12: .ipynb**
33. Apply4d_VV40_100Arms_Vectoriza...

**Prompt 13: .ipynb**
34. g25p_Ref2d3USER_Apply4d_VV40...

**Prompt 14: .ipynb, .docx, .pdf**
35. 05_QspTWIN_Simulation_gpt5
36. final_g25p_Ref2d3USER_Apply4d_...

---

# ASME V&V 40 / FDA Standards

**Model Verification & Numerical Checks**
37. V-01 Stability of Integrator, 4
38. V-02 Stochastic Reproducibility, 5
39. V-03 Zero-Efficacy Test, 2
40. V-04 Zero-Growth Test, 2
41. V-06 Toxicity Model Logic, 2

**Model Validation & Sensitivity Analysis**
42. S-01 Drug Potency, 2
43. S-02 Drug Sensitivity, 2
44. S-03 Drug Clearance, 2
45. S-04 Tumor Aggressiveness, 2
46. S-05 Primary Resistance Rate, 2
47. S-06 Global Efficacy Tuning, 2
48. S-07 Toxicity and Dropout, 2
49. S-08 Survival Post-Progression, 2
50. S-09 Survival Biomarker Effect, 2

**Uncertainty Quantification**
51. UQ-01 Patient Sensitivity, 2
52. UQ-02 Patient Age, 2
53. UQ-03 Ensemble Simulation, 10

**Applicability Assessment**
54. A-01 Population Drift, 2
55. A-02 Alternative Dosing, 2
56. A-03 Progression (RECIST), 2
57. A-04 Simulation Horizon, 2

Final Files: .ipynb, .py, .csv. 55 Tests

**Standards 1-4: .ipynb, .py, .png**
58. Standard 1: Prompts 01-03
59. Standard 2: Prompts 04-07
60. Standard 3: Prompts 08-10
61. Standard 4: Prompts 11-14

**Visualizations: .ipynb, .py, .png**
62. Digital_Twin_Diagrams, 3
63. Digital_Twin_Outcomes, 5
64. Model_Verification_&_Numerical_Checks, 3
65. Model_Validation_&_Sensitivity_Analysis, 4
66. Uncertainty_Quantification, 4
67. Applicability_Assessment, 2

---

# Acknowledgments

The author would like to acknowledge OpenAI for providing access to ChatGPT and GPT, Google for providing access to Gemini, Anthropic for providing access to Claude, and xAI for providing access to Grok.

# Ethical Disclosures

The author of the article declares no competing interests.

# Rights and Permissions

This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (CC BY 4.0), which permits unrestricted use, distribution, and reproduction in any medium, provided the original author(s) and source are properly credited, a link to the Creative Commons license is provided, and any modifications made are indicated. To view a copy of this license, visit https://creativecommons.org/licenses/by/4.0/.

# About This Study

Kawchak K. Accelerating FDA Compliance and Cost Efficiency of in silico Clinical Trials via AI Digital Twin Pancreatic Cancer Simulation. Zenodo. 2025; 10.5281/zenodo.17239510.
