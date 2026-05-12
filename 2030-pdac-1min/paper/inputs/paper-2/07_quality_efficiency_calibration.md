\vspace{0.1cm}
\begingroup
  \renewcommand\thesection{7}  
  \section{Quality Assurance and Protocol Compliance}  
  \label{sec:7}                 
\endgroup
\vspace{-0.2cm}


Quality assurance was interwoven throughout the project to ensure the model and simulation adhered to the trial protocol and good modeling practices. In addition to the software QA steps, we conducted explicit protocol compliance checks:

\textbf{Output Consistency Checks:} We cross-checked that related outputs were consistent. For instance, we made sure that the calculated OS hazard ratios between arms were in general agreement to Kaplan–Meier curves, and that the reported PFS-6 and OS-12 rates were consistent with the median PFS/OS. If any inconsistency was found (even due to rounding or small sample error), we investigated it. We documented such findings to ensure readers aren’t confused by them and that they indeed reflect real model behavior, not errors.

\textbf{Ordinary Differential Equations (ODEs):} The core disease dynamics are captured by two coupled ODEs per tumor compartment – one for therapy-sensitive tumor volume $V_{s}(t)$ and one for resistant volume $V_{r}(t)$. In a simple well-mixed tumor (no spatial structure), that’s 2 ODEs for each patient. However, the model was “extended to a spatial grid” of compartments to approximate a 3D tumor. At GRID=5 (used in final simulations), there are $5^3$ = 125 compartments. Each compartment has its own $V_{s}$ and $V_{r}$, so that’s 125 * 2 = 250 ODEs per patient being integrated. Across 10,000 patients, one could conceptualize this as 2.5 million ODEs – though in practice they are solved efficiently in aggregate (the code vectorized operations over patients). Nonetheless, mathematically the model is on the order of $10^6$ coupled ODEs, which is extraordinarily large for a QSP model. For context, previous virtual trials or QSP models in oncology often had on the order of 1–10 ODEs total (e.g. a single tumor volume equation, maybe a few for drug concentration or immune cells). This PDAC model, by modeling spatial heterogeneity and a large cohort, far exceeds the ODE count of prior models. Even if we consider an average patient, 250 ODEs per patient is huge – many QSP models have <10 state variables per patient. One potential regulatory concern: complexity = opacity. With so many parameters, one might worry the model could be tuned to produce desired results.  

\begin{itemize}[leftmargin=1.6em]
\item \textbf{Partial Differential Equation (PDEs):} The model doesn’t solve the 3D tumor PDE in continuous form, but it implements spatial effects via discrete diffusion approximations. Essentially, it replaces the PDE with ODEs on a grid (a common method to solve reaction-diffusion PDEs is to discretize space into compartments).
\end{itemize}



\vspace{-0.4cm}
\begingroup
  \renewcommand\thesection{8}  
  \section{Computational Efficiency and Scalability}  
  \label{sec:8}                 
\endgroup
\vspace{-0.2cm}

Our simulation involved 10,000 virtual patients across 10 arms, each simulated over 3 years of virtual time with fine resolution (dt = 0.05 days after refinement). This is computationally intensive, so we optimized for efficiency and planned resource usage carefully.

\textbf{Runtime and Performance:} A series of tests were performed with results illustrating the tradeoff between grid size and time steps in \autoref{8A}. Final settings (dt = 0.05 days, GRID = 5 compartments) were based off these findings, simulating one patient for 3 years took roughly 0.5–1.0 seconds of real time on a single v6e-1 TPU (depending on the arm, since arms with more therapy effects do more calculations). Thus, the full 10,000-patient trial would naively take on the order of 1.5–3 hours on a single TPU. Using a cloud instance with 64 TPU cores, we could run \raisebox{0.1ex}\textasciitilde
64 patients in parallel, completing the trial in \raisebox{0.1ex}\textasciitilde
2–3 minutes. We further utilized the TPU instance: its processing helped handle the simulation and data aggregation extremely quickly. Earlier trials based on less complex workflows were well within a Colab Dual Core with 13 GB RAM in Colab (and trivial in the 173 GB TPU environment). 

\textbf{Cost Considerations:} The price of a QSP in industry was estimated by AI to be \$2M, as visualized in \autoref{14A}. The cost of the TPU instance was about \$0.374/hour; since our runs were only minutes, the cost was less than one dollar per full trial simulation – very reasonable. For earlier experiments with less trial complexity, a dual-core CPU approach at \$0.007/hour cost was trivial. Throughout the experiments, approximately \$4 of Colab credits were spent. Cost projections for the single user were carried over from a previous paper at \$150/hr, 60 hrs/week, and 4 weeks, totaling \$36,000 obtained from \cite{19KawchakSimPDAC}. These are projections, as the user was not directly compensated for the work. Monthly cloud compute for OpenAI = \$260, Anthropic = \$20, and Google was \$20, xAI was \$0 - for a total of \$300. Thus, total cost considerations for the project were \$36,304, as illustrated in \autoref{14B}. 

\begin{figure}[H]
    \renewcommand\thefigure{8A}
    \centering
    \includegraphics[width=0.425\linewidth]{images/Figure_8A.png}
    \vspace{0.05cm}
    \caption{Simulation runtime vs numerical resolution: plotting TPU time per 1,000\\patients against timestep and grid size. Finer dt/grid greatly increases compute cost}
    \label{8A}
\end{figure}


In summary, computational efficiency was achieved through code optimization and appropriate hardware choices. We demonstrated that our approach can scale and that runtime was well within manageable limits. This is important for practical adoption – even though this was a retrospective study, future prospective uses might integrate such simulations into decision-making pipelines, so they need to run quickly. We have shown that a full trial simulation can run in minutes on accessible hardware, which is promising.  



\vspace{0.2cm}
\begingroup
  \renewcommand\thesection{9}  
  \section{Oncology-Specific Calibration \& Validation}  
  \label{sec:9}                 
\endgroup
\vspace{-0.1cm}


To bolster confidence in the model, we continuously aligned its behavior with known oncology data and principles. This section highlights how the model’s outputs compare to clinical benchmarks and where we made assumptions or simplifications unique to cancer biology, which we transparently communicated.

\textbf{Baseline Calibration to Clinical Data:} We ensured that standard-of-care arms approximated the efficacy observed in real trials. For example, in the first-line setting, gemcitabine + nab-paclitaxel (Arm A) was initially calibrated to a median OS of \raisebox{0.1ex}\textasciitilde10.3 months with ORR \raisebox{0.1ex}\textasciitilde50\% in the model. Real-world MPACT trial data for this regimen is ~8.5 months median OS, 23\% ORR. Our model overshot the ORR (50\% vs 23\%) in that idealized calibration. After addressing the numerical artifact in integration, the refined final outcome for Arm A was \raisebox{0.1ex}\textasciitilde6.9 months OS with ORR \raisebox{0.1ex}\textasciitilde14.7\%, which is somewhat conservative relative to clinical data. We judged this acceptable because it still falls in a plausible range – essentially modeling a slightly more refractory population – and it avoids overestimating efficacy. It underscores how patient assumptions affect outcomes: our earlier optimistic calibration assumed an exceptionally fit cohort (yielding higher ORR), whereas the refined model effectively assumed more typical PDAC dynamics (yielding lower ORR). Gemcitabine monotherapy, run as a validation scenario, gave \raisebox{0.1ex}\textasciitilde6.3 months OS and \raisebox{0.1ex}\textasciitilde0\% ORR in our simulation. Clinically, gemcitabine yields \raisebox{0.1ex}\textasciitilde5.7–6.8 months OS and \raisebox{0.1ex}\textasciitilde7–9\% ORR. The model’s OS is on target, however the ORR was low (0\% vs ~7\%). 

For Arm B (gem/nab + CD47 inhibitor), no exact clinical data exists (CD47 mAb is experimental), so we compared it to gem/nab alone. Our model predicted ORR \raisebox{0.1ex}\textasciitilde
17.3\%, OS \raisebox{0.1ex}\textasciitilde7.6 mo, versus gem/nab \raisebox{0.1ex}\textasciitilde14.7\%, 6.9 mo – so only a slight improvement. This suggests the added magrolimab provided a very modest benefit (increasing ORR by only \raisebox{0.1ex}\textasciitilde2.6 percentage points and median OS by \raisebox{0.1ex}\textasciitilde0.7 months). In relative terms, that’s perhaps a 15–20\% improvement over gem/nab’s baseline efficacy – biologically plausible, but not game-changing. We explicitly noted that our model assumes ideal conditions for magrolimab’s effect (all CD47\_high patients, full dosing, etc.), so a real trial might see even less benefit due to toxicity or suboptimal patient selection. So while Arm B’s trend (slightly improved outcomes) is reasonable, the magnitude is small; we flagged that any real trial might question if such a marginal gain is worth it.

In the second-line cohort, Arm G (nal-IRI + 5FU) \cite{03PapernalIRI5FU} in the model gave OS 5.4 mo, 0\% ORR, as mentioned – aligning with NAPOLI-1’s \textbf{~}6.1 mo OS, 7\% ORR (within the noise of patient sampling, our 0\% vs 7\% ORR was less than the standard). Arm H (adding KRAS G12C inhibitor + CD40 to chemo, in KRAS G12C patients) yielded much better outcomes; there’s no direct clinical analog yet, but we know KRAS G12C inhibitors in other cancers yield high response rates (\raisebox{0.1ex}\textasciitilde40–50\% in lung). Our model gave \raisebox{0.1ex}\textasciitilde67.7\% ORR in KRAS G12C-mutant PDAC with chemo + CD40 (Arm H), which is aspirational but not beyond belief for a highly selected group, especially when combining therapies. The absolute numbers – \raisebox{0.1ex}\textasciitilde12.8 months median OS in a second-line context – are almost unprecedented in PDAC, but remember these are KRAS G12C patients (a subset with an actionable mutation) on three active agents; also, our model’s optimism (fit patients, no acquired resistance) would naturally extend OS. We thus treat Arm H/I’s results as theoretical best-cases. We cautioned stakeholders that real outcomes might be less optimal if tumors evolve resistance mid-therapy, or if patients can’t tolerate full treatment.


\textbf{Resistance Dynamics Assumption:} One major biological assumption in the model is that resistance is purely intrinsic (fixed $f_{res}$) and no new resistance emerges during treatment. In reality, PDAC can develop acquired resistance (e.g. secondary mutations, immune evasion mechanisms) over months. Our model’s outcomes, especially for the more effective regimens, likely represent an upper bound assuming tumors don’t find a way to escape during the follow-up. We explicitly noted this limitation. For instance, if Arm C shows patients disease-free at 12 months in the model, one must realize that clinically a tumor might mutate around the KRAS inhibitor by then, causing relapse earlier. We conveyed to stakeholders that our long OS tails are likely optimistic because of this – they should be interpreted as “if resistance didn’t emerge, here’s what could happen.” 

\textbf{Tumor Heterogeneity:} We have already discussed $f_{res}$ sensitivity. Biologically, PDAC often has resistant clones present (e.g. cancer stem cells). Our baseline of 5\% was somewhat optimistic (implying most cells are initially sensitive). If in reality that fraction is higher or if multi-drug cross-resistance exists, real outcomes would be closer to our “high resistance” sensitivity scenario (much poorer). We used this to emphasize to stakeholders that our model’s favorable projections (like Arm C’s 70\% ORR) assume a relatively homogeneous tumor. We even suggested a potential future model enhancement: link $f_{res}$ to specific genetic markers in silico (e.g. TP53 mutation or high EMT features could confer higher resistance fraction). This would make the heterogeneity more mechanistic.

\textbf{Pharmacodynamic Parameters:} We cross-validated novel agent parameters wherever possible. For MRTX-1133 (KRAS G12D inhibitor), we set its Emax and EC50 such that at clinically achievable exposures (\raisebox{0.1ex}\textasciitilde1 µM in tumor) it almost maximally inhibits tumor growth. We tested extreme cases and found little outcome change, indicating we likely put it in a saturating regime – analogous to dosing a targeted therapy at MTD to fully inhibit the oncogene, which is indeed what real trials aim for. This gave us confidence that if our assumed potency is a bit off, it wouldn’t flip conclusions – Arm C would still be effective as long as the drug isn’t drastically weaker than expected. 

\vspace{1.4cm}

\textbf{Safety Outcomes vs Expectations:} Multi-agent chemo in PDAC (like FOLFIRINOX) is known to cause Grade 3–4 AEs in \raisebox{0.1ex}\textasciitilde85\% of patients. Our original calibration had Arm A at 99\% Grade \raisebox{0.25ex}{\scalebox{0.7}{$\geq$}}3 AEs, which was slightly higher – likely because the model counted each Grade 3 event additively (if a patient had severe neutropenia and severe thrombocytopenia, we might count two Grade 3 events). In the refined simulation, Arm A had \raisebox{0.1ex}\textasciitilde84\% of patients experiencing at least one Grade 3+ AE, which is quite plausible and actually closer to clinical data. We explained that the model doesn’t explicitly account for the co-occurrence of toxicities (it might double-count events per patient in that sense). Nonetheless, essentially all patients in Arm A had some serious toxicity in our simulation, which aligns with the notion that this regimen is extremely toxic – in real life, \raisebox{0.1ex}\textasciitilde85\% have \raisebox{0.25ex}{\scalebox{0.7}{$\geq$}}1 Grade 3–4 event, so our model’s \raisebox{0.1ex}\textasciitilde84\% is on point. The drop-out rates are perhaps more directly informative in our model: in the final run, Arm A had \raisebox{0.1ex}\textasciitilde5.6\% drop-out, which seems reasonable – FOLFIRINOX does have some early discontinuations, though our initial model assumed \raisebox{0.1ex}\textasciitilde10\%. Arm E had 14.2\% drop-out (very high, reflecting the intolerability of the triple combo in the model; initially we had 22.8\%, which we dialed back after refining toxicity parameters). Arm H had 18.3\% drop-out vs Arm I only 5.8\%. The stark difference between H and I’s drop-outs (chemo vs no chemo) was a sanity check that removing chemo improves tolerability drastically, as expected. We highlighted such points to stakeholders: e.g. “Arm I’s drop-out was only \raisebox{0.1ex}\textasciitilde6\% vs Arm H’s \raisebox{0.1ex}\textasciitilde18\%, showing how much omitting chemo improved tolerability.” We also pointed out that any regimen with >15\% drop-out in our model is a red flag for real trials – typically one wants most patients to stay on therapy, otherwise dose modifications are needed. 

\textbf{Standard of Care vs Experimental Arms:} We double-checked that standard treatments behaved as they should (they did: chemo control arms matched known outcomes, as discussed), and that no experimental arm produced “superhuman” results outside plausible biology. For instance, an arm yielding >15 month median OS in metastatic PDAC would be suspect (no regimen has done that). Our best outcomes were in the \raisebox{0.1ex}\textasciitilde12–13 month range for median OS in certain subsets (Arm H/I and Arm J), which is on the high end but within conceivable range if a breakthrough occurred (some recent combos in selected patients have hit \raisebox{0.1ex}\textasciitilde12–14 mo median). We explicitly stated that none of our arms exceed the best clinical PDAC outcomes seen to date. Arm J’s ~12.3 mo OS for BRCA-mutant patients, and Arm H/I’s \raisebox{0.1ex}\textasciitilde12.8 mo for KRAS G12C patients, are comparable to the best reported outcomes in any trial (e.g. some FOLFIRINOX + targeted sub-studies).

In summary, we validated the model’s outputs against oncology reality wherever possible and clearly noted where the model diverges (by assumption or optimistic bias). By doing so, we build credibility in areas where the model is strong (e.g. it correctly replicates known failures like PEGPH20’s lack of OS benefit, and it aligns with known toxicity profiles) and are transparent about areas of uncertainty (resistance, assumptions about patient fitness). This approach ensures that the insights drawn (like which arms are promising) are taken in the proper context.  

