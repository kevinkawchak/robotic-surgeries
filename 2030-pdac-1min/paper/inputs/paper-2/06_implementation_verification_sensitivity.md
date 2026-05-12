\begingroup
  \renewcommand\thesection{4}  
  \section{Model Implementation and Reverse-Engineering}  
  \label{sec:4}                 
\endgroup
\vspace{-0.3cm}

\textbf{Implementation (Part B):} The mechanistic model was implemented in Python (primarily via a Jupyter Notebook) as Part B of the project. Uniquely, a large language model (LLM) was leveraged to accelerate this coding process: we provided the written trial protocol (Part A) as input, and the LLM produced an initial draft of the simulation code. This included defining state variables, parameterizing them as per the protocol, and even writing ODE integration loops. We then reviewed and refined this code for accuracy, edge cases, and readability. The final code was modular, with clearly separated sections for initialization (patient generation), treatment application (dose schedules, turning on/off mechanisms per arm), ODE integration (we used a fixed-step solver for transparency), and output calculations (ORR, PFS, OS). The time integration was performed with a sufficiently small step (ultimately dt = 0.1–0.5 days), ensuring numerical stability. 

\textbf{Reverse-Engineered Spec (Part C):} To verify that the implemented code faithfully matches the intended trial design, an LLM was also used in reverse: after coding, we prompted the LLM to convert the Python code back into a descriptive text (Part C). This produced a human-readable “model specification” that could be compared section-by-section with the original trial protocol. For example, if the protocol said “Arm C: add KRAS G12D inhibitor continuously at 1 mg/kg,” the Part C text described how the code implements Arm C (e.g. “for patients with KRAS G12D = 1, a targeted therapy kill term is applied with efficacy corresponding to MRTX-1133’s profile”). We cross-checked each arm: the reverse-engineered text matched the protocol on all essential points, confirming that no arm was miscoded or omitted. This LLM-assisted verification caught a few minor inconsistencies early (for example, an initial code version missed applying the CD40 effect in Arm E; the Part C text revealed the omission, which was then fixed). The final Part C document serves as a readable “user manual” of the model, describing all ODEs and assumptions in plain language for any stakeholder who doesn’t read code.

\textbf{Model Stack:} \autoref{2A} illustrates the trial workflow: Part A (clinical design) → Part B (LLM-assisted code) → Part C (code-to-text validation) → Part D (this analysis). Additionally, the model stack includes the computational environment and tools: we used Python 3.12 with libraries for ODE solving and data analysis (NumPy/Pandas for handling the 10,000-patient data, matplotlib for plotting). The simulation was run in Google Colab cloud environments (initial development on a low cost dual-core CPU instance with 13 GB RAM, then more complex trial runs on a TPU instance with 173 GB RAM). No local machine was needed or used at any point. The AI/LLM integration did not stop at code generation – an AI agent was also used during simulation execution and analysis (next sections) as a “co-pilot” to enhance quality control and insight generation.

\textbf{Scale of Parameters and Variables:} The attached simulation notebook defines dozens of parameters governing tumor biology, drug actions, and patient variability. \autoref{T1} in the playbook catalogs the major ones, which include tumor growth rates ($r_{s}$, $r_{r}$), initial resistant fraction ($f_{res}$), carrying capacity (K), kill rate terms for each therapy ($k_{chemo}$, $k_{target}$, $k_{immune}$ as functions of drug dose), and toxicity-related thresholds. From the code, we see global settings like MAX\_DAYS (simulation horizon) and numerical parameters like time-step and GRID\_SIZE (spatial resolution) which are adjustable. There are pharmacodynamic parameters for each drug – e.g., Emax and EC50 for gemcitabine, nab-paclitaxel, MRTX-1133, 5-FU, nanoliposomal irinotecan (Nal-IRI), CD47 mAb (magrolimab), PARP inhibitor (olaparib), etc.. In the snippet we see 8 drugs’ Emax/EC50 pairs defined, so that’s 16 parameters just for drug PK/PD effects. There are also immune parameters (T-cell activation and suppression rates, baseline immune cell levels), PD-1 binding kinetics ($k_{on}$, $k_{off}$, $k_{in}$), neutrophil dynamics (production/death rates for toxicity modeling), and probabilities of Grade 3+ AEs per cycle for targeted and IO therapies. Furthermore, the virtual population is defined by distributions for patient attributes: age, weight, baseline tumor burden, etc., across 7 archetype subgroups – each of those distributions has parameters (mean, SD) in the code. In total, counting distinct symbols, there are on the order of 50–100 adjustable parameters in this simulation. This includes \raisebox{0.1ex}\textasciitilde20 core biophysical parameters (rates, Emax, etc.), \raisebox{0.1ex}\textasciitilde10 toxicity and PK parameters, \raisebox{0.1ex}\textasciitilde5–10 defining initial conditions and variability (like fraction of patients with KRAS G12D, which is set \raisebox{0.1ex}\textasciitilde35\%), and numerous binary flags (mutation present or not, etc.) for each virtual patient. The state variables themselves are also numerous: each patient has at least 2 dynamic state variables (sensitive and resistant tumor volume) per compartment, plus possibly a neutrophil count state for toxicity and an ongoing tally of cumulative hazard for survival. With 125 compartments (GRID=5) and 10k patients, that’s 2.5 million tumor volume states being updated each time-step (though handled vectorized). Clearly, the model’s dimensionality is high. 






\begingroup
  \renewcommand\thesection{5}  
  \section{Verification and Validation of QSP Clinical Trial}  
  \label{sec:5}                 
\endgroup
\vspace{-0.325cm}

To ensure the model’s outputs are numerically correct and stable, we performed extensive verification tests varying the simulation resolution parameters: the integration time-step (dt) and the spatial grid granularity (GRID\_SIZE). The goal was to confirm that results (e.g. tumor response rates, survival outcomes) converge as dt and grid size are refined, and that the chosen settings are adequate for accuracy. We ran a subset of the trial with progressively smaller dt values and compared ORR and disease control rate (DCR) for each arm. At very fine steps (dt = 0.05 or 0.1 days), results stabilized – for instance, Arms A–I all showed \raisebox{0.1ex}\textasciitilde0\% ORR at those fine steps (reflecting that with a sufficiently accurate integration, no responses occurred in those arms under the test scenario). However, at coarser steps we saw artificial efficacy appearing: by dt = 0.25 days some arms showed non-zero ORR (e.g. Arm A \raisebox{0.1ex}\textasciitilde5\%), and at dt = 0.45 days Arm A’s ORR jumped to \raisebox{0.1ex}\textasciitilde27\%. At an extremely coarse dt = 0.50 days, it rose slightly further (31.5\%). This indicated that integration error at large dt was inflating apparent treatment effect – essentially a numerical artifact where the solver’s imprecision allowed tumor kill to be overestimated. Importantly, the inflation plateaued between 0.45 and 0.50 (Arm C’s ORR was \raisebox{0.1ex}\textasciitilde70\% at both), suggesting an asymptote. We interpreted that beyond dt \raisebox{0.25ex}{\scalebox{0.75}{$\approx$}}0.4 days, the solver was too inaccurate, but below dt \raisebox{0.25ex}{\scalebox{0.75}{$\approx$}} 0.1 days it was stable. In practice, we often used dt = 0.05 days for safety during verification runs. An AI agent assisted in this process by noticing the anomaly at coarse dt and suggesting the intermediate tests at 0.3-0.5 days – automating what a human numerical analyst would do. This saved time and ensured we identified the threshold of instability. 

We performed a spatial grid refinement test starting from a coarse grid (e.g. GRID\_SIZE = 2, meaning a very low-resolution tumor representation) up to GRID\_SIZE = 7 (high resolution), we found that outcomes also converged. At very low grid resolution, some arms’ efficacy was underestimated (e.g. with too few compartments the model can under-capture the effect of spatial heterogeneity). By GRID\_SIZE = 5, key metrics like ORR had stabilized for all arms (changes from 5 → 6 → 7 were <1\% absolute) – indicating that a 5×5×5 grid was sufficient. The final settings initially chosen were dt = 0.50 days and GRID = 5. All arms’ outcomes were verified to change negligibly with finer resolution, giving us high confidence in the numerical validity of the simulation. However, given the importance of numerical stability, we ultimately executed the definitive simulations with a finer time step: dt = 0.05 days (still using GRID = 5) as recommended by the AI assistant seen in \autoref{5A}. This eliminated any residual integration error in the final reported outcomes, at the cost of additional compute time. We confirmed that results at dt = 0.05 were effectively the same as those at dt = 0.1 (no further changes in ORR/PFS/OS), indicating full convergence. 



\vspace{-0.1cm}
\begin{figure}[H]
    \renewcommand\thefigure{5A}
    \centering
    \includegraphics[width=0.6\linewidth]{images/Figure_5A.png}
    \vspace{0.05cm}
    \caption{Numeric convergence: (a) effect of time-step (dt) on ORR for arms, showing\\ORR stabilizes at dt\raisebox{0.25ex}{\scalebox{0.7}{$\leq$}}0.1. (b) effect of spatial grid size on ORR, stabilizing by GRID=5}
    \label{5A}
\end{figure}
\vspace{-0.25cm}






\textbf{Biological Validation:} In addition to numerical convergence, we validated the model’s behavior against known clinical outcomes to ensure biological realism. For example, an arm with essentially no effective therapy – PD-1 checkpoint inhibitor monotherapy in PDAC – was expected to show \raisebox{0.1ex}\textasciitilde0\% tumor responses and very short survival. Indeed, in our test, Arm G (PD-1 only, representing a second-line ARCH-07 refractory scenario) yielded 0\% ORR and virtually all patients progressed quickly, recapitulating the dismal outcomes observed in reality for PD-1 monotherapy in PDAC. Conversely, Arm A (intense chemo) was expected to produce some responses and \raisebox{0.1ex}\textasciitilde8–11 months median OS; our model gave \raisebox{0.1ex}\textasciitilde15\% ORR and 6.9 months OS for Arm A’s population, which is slightly pessimistic relative to clinical benchmarks. These cross-checks increased confidence that the model wasn’t just numerically stable, but also biologically credible in its predictions. All verification results and plots were documented for transparency, and any discrepancies led to model adjustments or at least annotations (e.g. noting when a model assumption caused a divergence from clinical data).

In summary, by the end of verification we had (a) tuned the simulator for stable operation (no significant dependence on step size or grid), and (b) confirmed that it reproduces expected behavior in edge-case scenarios (e.g. ineffective treatment yields no response, known treatments match historical data). This establishes a solid foundation to proceed to analyzing the trial outcomes.  

\vspace{0.1cm}
\begingroup
  \renewcommand\thesection{6}  
  \section{Sensitivity Analysis, Uncertainty Quantification}  
  \label{sec:6}                 
\endgroup
\vspace{-0.35cm}

We next examined how sensitive the model outputs are to key uncertain parameters, as part of uncertainty quantification (UQ). The aim was to identify which assumptions most affect the trial results (“high-impact” parameters) and ensure that conclusions are robust to reasonable parameter variations. Two sensitivity studies are highlighted here: the intrinsic resistant fraction ($f_{res}$) and the KRAS inhibitor potency (Emax), as these were anticipated to strongly influence outcomes.

\textbf{Tumor Resistant Fraction ($f_{res}$):} We varied the initial fraction of resistant cells from the baseline 5\% up to 15\% and 30\% in the virtual patients, and re-simulated efficacy outcomes (\autoref{6A}). The impact was dramatic: for example, in Arm A (chemo control), ORR plummeted from \raisebox{0.1ex}\textasciitilde31.5\% at 5\% resistant to only ~5.7\% at 30\% resistant – a six-fold decrease in response rate as the resistant subclone size tripled. Many arms showed a similar pattern: Arms B, D, E, H, I all saw their ORRs drop by >50\% when moving from 5\% → 15\% → 30\% resistant. This is scientifically sensible: if a larger portion of the tumor is therapy-insensitive, far fewer patients achieve significant shrinkage. Notably, Arms C and J were somewhat less affected (their ORRs fell only modestly), suggesting that targeted therapy (Arm C) and PARP maintenance (Arm J) can overcome or avoid resistance mechanisms to a degree – likely because these strategies attack the tumor in ways not solely reliant on upfront sensitivity (e.g. Arm C targets a specific oncogene present in all cancer cells, including those that might be chemo-resistant). We flagged $f_{res}$ as a high-impact uncertainty: small changes in this parameter lead to large swings in outcomes, affecting conclusions about regimen efficacy. Practically, this means our optimistic results assume relatively homogeneous tumors; if real tumors have higher heterogeneity, the benefits of some combos might be overestimated. We communicated this to stakeholders and in documentation as a caveat. This analysis mirrors known oncology wisdom: initial tumor heterogeneity (e.g. pre-existing resistant cancer stem cells or clones) can strongly influence treatment success. It also provides a hypothesis for patient selection in trials – e.g. if one could identify patients with low pre-existing resistance (via a biomarker), they might realize the full benefit predicted in arms like C or H, whereas those with high resistance burden might not.
\vspace{-0.2cm}


\begin{figure}[H]
    \renewcommand\thefigure{6A}
    \centering
    \includegraphics[width=0.52\linewidth]{images/Figure_6A.png}
    \vspace{0.05cm}
    \caption{Sensitivity to resistance: ORR in Arm A (blue) and Arm C (green) as a function of initial resistant fraction $f_{res}$. As $f_{res}$ increases, ORR drops dramatically, confirming high-impact of tumor heterogeneity}
    \label{6A}
\end{figure}







\textbf{Targeted Therapy Potency (Emax):} We tested the sensitivity to the KRAS G12D inhibitor’s efficacy by scaling its Emax (the maximum fractional kill per day) to 50\% of baseline and 150\% of baseline, as shown in \autoref{6B}. The results showed minor changes in outcomes for Arm C: at half potency, Arm C’s ORR was still \raisebox{0.1ex}\textasciitilde66.4\% vs 70.3\% at baseline; at 1.5× potency, ORR \raisebox{0.1ex}\textasciitilde71.9\%. The disease control rate (DCR) and median OS likewise varied only a little. Thus, the model was not overly sensitive to the exact assumed potency of the KRAS inhibitor – we appear to have calibrated it in a regime where it’s near maximal effect already. This is reassuring: even if the real drug is a bit less effective than assumed, Arm C would likely still outperform chemo alone by a large margin. Similarly, making the KRAS inhibitor slightly more potent didn’t radically change outcomes, indicating a plateau. This suggests that our conclusions about Arm C’s benefit are robust unless the drug were dramatically weaker in reality (in which case, obviously, it would not work as well). We did analogous tests for the KRAS G12C inhibitor in Arms H/I with similar findings. In short, our model’s qualitative outcomes (e.g. Arm C is a big win) did not hinge on fine-tuned potency values – a good indication of robustness.



\begin{figure}[H]
    \renewcommand\thefigure{6B}
    \centering
    \includegraphics[width=.6\linewidth]{images/Figure_6B.png}
    \vspace{0.05cm}
    \caption{Heatmap showing ORR for Arm C extrapolated from two analyses. High resistance dramatically lowers ORR (top to bottom), but top row 5\% resistance shows only 6\% gain from 50\% to 150\% potency}
    \label{6B}
\end{figure}

\textbf{Note:} Additional studies regarding Resistant tumor volume derivatives and EC50 mrtx are available in supplementary folders B6 and B9. Additional UQ analyses on other parameters were conducted, but for brevity only the above are detailed.
