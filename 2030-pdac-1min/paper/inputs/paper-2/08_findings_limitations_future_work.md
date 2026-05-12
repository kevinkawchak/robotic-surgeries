\vspace{0.05cm}
\begingroup
  \renewcommand\thesection{10}  
  \section{Key Findings and Comparative Insights}  
  \label{sec:10}                 
\endgroup
\vspace{-0.25cm}

\textbf{Most Effective Strategies:} The standout regimens were those that target specific tumor vulnerabilities or combine synergistic modalities in a tolerable way. In particular, KRAS-mutant targeted therapy showed great promise: Arm C (KRAS G12D inhibitor + chemo) drastically improved outcomes in KRAS G12D patients (ORR \raisebox{0.1ex}\textasciitilde70\% vs \raisebox{0.1ex}\textasciitilde20–25\% on chemo historically, with a meaningful OS extension). Likewise, Arm H/I for KRAS G12C – a previously untargetable subset – turned a dismal prognosis into one with over half of patients alive at 1 year. These findings underscore that precision oncology (targeting driver mutations) can yield big gains even in PDAC, echoing successes seen in other cancers (e.g. lung cancer EGFR or ALK inhibitors). The model provides quantitative support for investing in trials of KRAS-targeted agents in PDAC subgroups. Additionally, maintenance therapy in biomarker-selected patients (Arm J for BRCA mutants) was validated as a strategy: it not only prolonged PFS but likely improves OS. This reinforces current clinical practice of maintenance PARP in BRCA-mutant PDAC and suggests it could even be more beneficial than seen in the POLO trial if applied optimally (our model didn’t include the confounding of crossover, thereby revealing a possible OS gain).

\textbf{Role of Chemotherapy:} The simulations indicate that chemotherapy's role can sometimes be substituted or minimized. For example, in KRAS G12C patients, dropping chemo (Arm I) did not hurt survival relative to keeping chemo (Arm H) – it mainly reduced toxicity and slightly lowered ORR. This hints that in certain biomarker-selected groups, one might spare patients the added chemo toxicity without compromising long-term outcomes. However, in broader populations, chemo still provided most of the tumor kill (Arm A vs any single immunotherapy arm – e.g., PD-1 alone did nothing; chemo drove the outcomes). Chemo-based control arms (Arm A, Arm G) largely defined the floor of outcomes, and any improvement came on top of chemo’s effect. Even in combinations, chemo contributed to initial tumor shrinkage (e.g., Arm H vs I ORR difference was small but present), which can be important for rapid symptom relief in PDAC. So, while exciting new agents are emerging, the model suggests we aren’t yet at a point to eliminate chemo in most patients except possibly small subgroups.

\textbf{Immunotherapy Dilemmas:} Checkpoint inhibitor monotherapy (PD-1) was ineffective (modeled ORR ~0\%, no survival benefit), which matches clinical reality in PDAC. Dual immunotherapy plus chemo (Arm E) paradoxically performed worse than chemo due to toxicity, illustrating that more is not better if toxicity is unmanageable. However, immunotherapy when targeted appropriately or combined rationally, it helped. PD-1 plus CD40 (Arm I) in a subset with a KRAS-directed therapy (essentially, the KRAS inhibitor causing tumor antigen release) led to durable disease control in some patients. And CD47 (magrolimab) added a bit of benefit to chemo (Arm B), though modest. The key insight is that immunotherapy in PDAC likely requires combination with other synergistic treatments and careful patient selection. Throwing multiple immunotherapies blindly (Arm E) failed, but tailoring them in the right context (Arm I for an immunogenic subset, Arm B for CD47\_high tumors) showed some value. The model essentially mirrors current PDAC trial thinking: single-agent immunotherapy doesn’t work, and even combos need either a primed immune microenvironment or a less toxic regimen to succeed.









\begin{figure}[H]
    \renewcommand\thefigure{10A}
    \centering
    \includegraphics[width=1\linewidth]{images/Figure_10A.png}
    \vspace{0.05cm}
    \caption{Top panel: HRs of treatment versus control in patient subgroups. Bottom panels: BRCA-mutant PARP inhibitor patients (PFS values suboptimal vs. POLO); and PEGPH20 in HA-high patients}
    \label{10A}
\end{figure}



\textbf{Stroma Targeting and Microenvironment:} Our results reinforced that targeting the stromal barrier alone (PEGPH20) yields limited benefit as depicted in \autoref{10A}: improved drug delivery translated to a higher response rate but not extended survival. This aligns with the failure of HALO-301 and suggests that without addressing underlying tumor aggressiveness or immune evasion, simply making chemo reach the tumor better is not sufficient. The stroma, however, remains important in that it affects how other therapies work (we modeled reduced chemo efficacy in HA\_high tumors). So a finding is: patient stratification by stroma could identify who won’t benefit from chemo-heavy regimens (since $HA_{high}$ patients did worse on Arm A in our model, and even with PEGPH20 they didn’t achieve longer OS). It might be more fruitful to focus on treatments that can penetrate or bypass stroma inherently (like T cells or small molecules) rather than add a stroma degrader with extra toxicity.

\textbf{Limits of Aggression:} Perhaps one of the most important insights is the demonstration of diminishing returns when combining too many therapies. Arm E was instructive: even though each component (chemo, PD-1, CD40) had rationale, together they became counterproductive. This suggests an optimal “sweet spot” in combination complexity. The best arms (H, I, C, J) had at most 2–3 active agents and targeted a specific vulnerability. Arm E had 3 agents without specific biomarker targeting and failed. So, a takeaway is: focus on smart combinations, not maximal combinations. Use biomarkers to guide combos (as in H/I/J/C) and avoid piling on drugs without a clear strategy (as E did).

\textbf{Comparative Efficacy vs Toxicity:} We compiled an overview of each arm’s benefit–risk profile:

\begin{itemize}[leftmargin=1.6em]
\item \textbf{Arm C:} High efficacy in a subset; added targeted therapy toxicity was minimal (targeted drugs are generally well-tolerated compared to chemo). Benefit clearly outweighs risk for KRAS G12D patients – likely worth pursuing clinically (\autoref{10B}).
\item \textbf{Arm H:} Very high efficacy in a small subset, but toxicity was high (three drugs including chemo). Still, the OS gain (~12.8 vs 5.4 mo in control) is so large that it might justify the toxicity, especially if mitigated by aggressive supportive care. This arm (or a variant of it) could be trialed in KRAS G12C PDAC, with careful monitoring.
\item \textbf{Arm I:} Similar efficacy to H but much lower toxicity (no chemo). The model suggests this might achieve similar outcomes with far better patient experience – a strong case to test a chemo-free regimen in KRAS G12C patients, particularly those who are frail (who might not tolerate Arm H).
\item \textbf{Arm J:} Clear efficacy (maintains remission in BRCA-mutant patients) with relatively low toxicity (PARP inhibitors have some side effects like fatigue, but our model’s drop-out was only ~5\%). Benefit >> risk, so this supports current practice and perhaps combining maintenance PARP with other maintenance strategies in future.
\item \textbf{Arm B:} Slight efficacy gain; toxicity roughly equal to Arm A (magrolimab’s added anemia risk was small in our model – Arm B had similarly high Grade 3+ AE incidence and only slightly higher drop-out than Arm A). Essentially neutral risk–benefit – if the drug is available and cost is not an issue, one might add it, but our model doesn’t show a big advantage. It might not justify an expensive new drug for only a few percent absolute improvement in 1-year survival.
\item \textbf{Arm D:} Higher ORR but no survival gain, plus added toxicity (\raisebox{0.1ex}\textasciitilde99.7\% of patients had Grade \raisebox{0.25ex}{\scalebox{0.7}{$\geq$}}3 AEs in Arm D vs \raisebox{0.1ex}\textasciitilde84\% in Arm A). Risk \raisebox{0.1ex}\textasciitilde benefit (short-term gain offset by side effects). Likely not worth pursuing PEGPH20 further – consistent with its clinical discontinuation.
\item \textbf{Arm E:} Some initial responses but net harm (worse OS due to toxicity). Risk >> benefit. Should not proceed unless fundamentally redesigned (e.g. lower doses or patient selection to improve tolerability).
\item \textbf{Arm G/K:} Baseline arms, showing poor outcomes with existing therapy or no therapy – highlighting the unmet need. No benefit in these arms (by design, they are controls), but they provide context for improvements seen in experimental arms.
\end{itemize}

This kind of analysis helps prioritize. The playbook would recommend focusing on regimens like C, H, I, J for further development, and de-prioritizing or reworking B, D, E.



\begin{figure}[H]
    \renewcommand\thefigure{10B}
    \centering
    \includegraphics[width=1\linewidth]{images/Figure_10B.png}
    \vspace{0.05cm}
    \caption{Waterfall plots of best tumor shrinkage for control (left, Arm A) vs targeted (right, Arm C). Bottom: KRAS G12C+ Inhibitor therapy is best in ORR/DCR (early G12C trials similar performance)}
    \label{10B}
\end{figure}


\begin{figure}[H]
    \renewcommand\thefigure{10C}
    \centering
    \includegraphics[width=0.97\linewidth]{images/Figure_10C.png}
    \vspace{0.05cm}
    \caption{Comparative efficacy radar: left forest plot shows hazard ratios for patient archetypes.\\Right radar plot compares ORR, median PFS/OS, and toxicity for standard chemo vs. combinations}
    \label{10C}
\end{figure}



\begin{figure}[H]
    \renewcommand\thefigure{10D}
    \centering
    \includegraphics[width=1\linewidth]{images/Figure_10D.png}
    \vspace{0.05cm}
    \caption{(A) Waterfall in Arm C stratified by KRAS G12D mutation; (B) Violin plot of OS favors baseline immune high infiltration; (C) Maximum tumor reduction vs OS (Pearson r \raisebox{0.25ex}{\scalebox{0.75}{$\approx$}} –0.93)}
    \label{10D}
\end{figure}




\textbf{Another insight:} The combination of targeted + immunotherapy (Arm I) did very well, implying that tumor antigen release by targeted therapy plus immune activation is a powerful combo. This is akin to the concept of immunogenic cell death – kill tumor cells and at the same time ramp up the immune system (CD40 agonist to stimulate T cells). This might be generalizable beyond KRAS G12C. Our platform could test similar “targeted + immuno” ideas in other contexts (e.g. combining a PARP inhibitor with PD-1 in BRCA patients). This showcases the ability of the QSP model to also inspire new combinations.


\vspace{-0.3cm}
\begingroup
  \renewcommand\thesection{11}  
  \section{Limitations and QSP Trial Conclusions}  
  \label{sec:11}                 
\endgroup
\vspace{-0.3cm}

While the virtual trial provided rich insights, it’s important to acknowledge its limitations and the lessons learned:

\begin{itemize}[leftmargin=1.6em]
\item \textbf{Model Assumptions:} We assumed no acquired resistance, fully compliant patients, and ideal pharmacodynamics for novel agents. These assumptions likely made some outcomes optimistic (especially long-term durability of responses). We communicated these assumptions, and in interpreting results we always considered how breaking these assumptions would affect outcomes (e.g. if resistance emerges, Arm H/I’s long OS would drop). The lesson is that model-based predictions are only as good as the assumptions – and including stakeholders in reviewing those assumptions was crucial. In our case, clinicians immediately questioned the lack of acquired resistance, prompting us to add that to future model plans.
\item \textbf{Data Gaps:} For experimental components (like CD47 or CD40 agents in PDAC), we had to generate patients, which introduces uncertainty. We mitigated it by doing sensitivity analyses (seeing that our conclusions didn’t hinge on exact assumed potency, as noted). The learning here is to perform UQ around any poorly-known parameters and be cautious in over-interpreting results that depend on them. We clearly flagged where data was thin (e.g. “magrolimab effect may be overestimated since clinical PDAC data is lacking”).
\item \textbf{Numerical Stability vs. Convenience:} A key lesson was the importance of numerical stability. Initially, we were comfortable with dt = 0.5 days for faster simulation, but the AI assistant uncovered that this introduced subtle inaccuracies (inflating ORRs). Based on that, we re-ran with dt = 0.05 days and got corrected, more realistic results. This was a valuable reminder that even if convergence tests suggest a plateau, using the finest feasible resolution is safest when seeking high accuracy. It did cost more computing time, but ultimately it improved model fidelity (Arm A’s ORR dropping from 50\% to 15\% after this fix fundamentally changed our interpretation of some arms). Thus, we learned not to cut corners on resolution when it can materially affect outcomes.
\item \textbf{Biology vs. Artifacts:} Some initial results that looked interesting turned out to be artifacts of the model rather than true biology – for example, Arm A’s very high ORR was an artifact. Once corrected, the story changed: Arm A became a more realistic baseline (and some arms like B went from looking like “no OS improvement” to a slight improvement in relative terms). However, some end points such as mPFS and Grade 3 AEs remained suboptimal throughout code iterations, as apparent in final trial summaries. The take-home is that one must distinguish genuine biological insights from model quirks. Our layered verification (both numerical and biological calibration) helped us filter out those artifacts before drawing conclusions. 
\item \textbf{Generality:} Our results apply to the specific scenario modeled (metastatic PDAC trial with certain drugs). One limitation is the generality of these findings – e.g. the success of Arm C (KRAS G12D inhibition, shown in \autoref{10D}) assumes a drug as effective as MRTX-1133; if real drugs are weaker, outcomes would differ. We framed our findings in a comparative way intentionally – focusing on which strategies outperform others, rather than the exact percentages. The lesson is that QSP virtual trials are best at comparative effectiveness and scenario exploration, not absolute prediction. We conveyed that nuance to stakeholders (e.g. we said “Arm H could in principle improve survival vs current therapy, if the drugs work as modeled,” making it clear this is conditional and illustrative).
\item \textbf{Stakeholder Communication:} We learned the importance of communicating these complex results in understandable terms. We iteratively improved our presentation – adding interpretive text (“this could translate to X months benefit in a trial”) and visual aids (Kaplan–Meier curves, bar charts for ORR/toxicity) that we included in this report. This made the findings accessible. A lesson was that the QSP model’s value is only realized if the end-users (clinicians, decision-makers) can grasp the insights, so significant effort went into translating model-speak into clinical-speak. The retrospective nature helped because we could refine our messaging after seeing initial confusion.
\item \textbf{AI Integration:} Using AI (LLMs) was a novel aspect. It accelerated coding and documentation, but we also encountered its limits (the AI was limited in the number of parameters being modified at one time). We found that AI was excellent for first drafts and tedious tasks (like converting code to text), but human oversight was essential for prompting additional fixes. The lesson is that AI can enhance productivity, but it’s not a replacement for expert review – rather, it’s a tool that needs guidance. When we followed up on the AI’s recommendations (like testing more dt values), we gained unexpected insights. So being receptive to the AI “suggestions” (even though they were not always explicit – in one case the AI simply flagged a discrepancy, which we interpreted as a suggestion to investigate) proved beneficial.
\end{itemize}

In conclusion, the virtual trial yielded valuable insights but also highlighted the importance of rigorous validation and clear communication. The limitations noted are not detriments but rather guideposts for improving future models and for tempering conclusions with appropriate caution. A virtual trial is a powerful tool to explore “what-if” scenarios, but it must be continually cross-checked with reality and presented with its assumptions front and center. We believe this retrospective analysis has illustrated both the potential and the current boundaries of QSP-driven virtual trials in oncology.  


\vspace{-0.2cm}
\begingroup
  \renewcommand\thesection{12}  
  \section{Future Work and Model Extensions}  
  \label{sec:12}                 
\endgroup
\vspace{-0.2cm}


Building on this project, several future directions have been identified:

\begin{itemize}[leftmargin=1.6em]
\item \textbf{Acquired Resistance Module:} As noted, adding an acquired resistance mechanism is a priority. We plan to introduce a stochastic process during simulation where a fraction of sensitive tumor cells can become resistant each cycle, at rates informed by clinical data (e.g. resistance mutations emerging after a median of X months on therapy). This will allow us to model eventual relapse even in arms that initially perform well, providing more realistic long-term projections (e.g. turning those flat OS tails into gradually declining ones).
\item \textbf{Tumor-Immune Dynamics Expansion:} Explicitly modelling T cell and macrophage populations, and interactions like checkpoint inhibition kinetics and myeloid suppression would likely improve results. This could enable exploration of immunotherapy scheduling (e.g. induction chemo to release antigens, followed by delayed PD-1 blockade, etc.) and a deeper analysis of why certain patients might not respond. We would calibrate this to any PDAC immune data available (tumor-infiltrating lymphocyte counts, etc.).
Biomarker-Driven Patient Enrollment: In this virtual trial, each arm was run on an appropriate subset, but in reality, one might design trials that test multiple strategies in the same patient (adaptive trials) or require biomarker pre-selection. We could simulate an adaptive trial design where, say, KRAS G12C patients are adaptively randomized between Arm H and Arm I to see which is better – mimicking a head-to-head in that niche population. This would involve coding an “umbrella” trial logic atop our model. It could help address questions like, should chemo be added or omitted if a KRAS G12C drug is available? Our current results hint “omit chemo,” but a formal trial simulation could confirm significance and optimal decision rules.
\item \textbf{Cost-Effectiveness and Multi-Criteria Optimization:} While our model focused on efficacy and toxicity, a real decision might include drug costs or quality-of-life metrics. We can extend the analysis to incorporate a simple cost model (drug costs, hospitalization costs from toxicity) and even a quality-adjusted survival metric. This would allow assessing, for example, if Arm H’s small survival edge over Arm I is worth the presumably higher cost and worse quality of life (likely not, according to our current thinking). Such extensions move into the health economics realm, broadening the impact of the model for decision-makers.
\item \textbf{Other Indications and Generalizability:} The core model can be adapted to other indications (e.g. earlier-stage PDAC). We identified that by swapping out the tumor growth parameters and recalibrating drug effects, we could potentially simulate, say, a pancreatic adjuvant therapy trial that tests a similar immunotherapy combo. Exploring the model’s flexibility in this regard is future work – essentially testing how reusable the QSP modules are beyond this specific trial.  
\item \textbf{Mechanistic Detail Additions:} We plan to enrich certain mechanisms. One example is pharmacokinetics: currently drug effects are direct, but adding PK sub-models (e.g. gemcitabine clearance, peak/trough concentrations) could allow exploring dose adjustments or scheduling changes. Another example is a more detailed toxicity model that distinguishes types of toxicities (hematologic vs hepatic, etc.) and their timing – useful if considering supportive care interventions. These additions would make the model more granular and possibly reveal time-dependent effects (like needing to delay doses due to toxicity, which isn’t currently simulated explicitly beyond drop-out).
\item \textbf{Collaboration and Validation:} We aim to validate the model’s predictions with any emerging clinical trial data. For instance, if a trial of KRAS G12C inhibitor + chemo in PDAC reports results, we will compare those to our Arm H prediction. Any discrepancies will guide model refinement (maybe adjusting the immune effect or the cross-resistance assumptions). We also could collaborate with experimentalists: e.g. using the model to design a mouse study that could test a hypothesis (like “chemo-free combo is better for KRAS G12C – test this in a PDAC mouse model with KRAS G12C and see if immune response is durable”). This would further strengthen the model’s credibility and potentially feed back new data to improve it.
Overall, the future work will enhance the model’s realism, extend its applicability, and integrate it more tightly with the experimental/clinical workflow. 
\end{itemize}
