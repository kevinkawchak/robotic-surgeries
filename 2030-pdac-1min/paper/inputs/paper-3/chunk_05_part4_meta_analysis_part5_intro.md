
\begin{minipage}{\textwidth}
% --- Title ---
\begin{center}
    \Large\textbf{Meta-Analysis Comparisons: o3ph, ops4}
\end{center}

\vspace{0.1cm}

\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=0.95\linewidth]{images/S58b.VIS.01.P44b-01.png}
    \captionof{figure}{Forest Plot of 2 Experimental Arms vs.\ Field}
    \label{MAImage1}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{1) FOLFIRINOX 2) NAPOLI-1 3) Arm A\\[3pt]Top Real World Trials Top in OS HR}
        \end{quote}
    \end{tcolorbox}
\end{minipage}
\hfill
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S58b.VIS.01.P44b-07.png} 
    \captionof{figure}{Toxicity vs.\ Survival Benefit}
    \label{MAImage2}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{1) Arm D 2) MPACT 3) Arm A\\[3pt]Virtual Doublet less Toxic than Field}
        \end{quote}
    \end{tcolorbox}
\end{minipage}

\vspace{0.4cm}

% Additional two image blocks go below
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \hspace*{0.55cm}\includegraphics[width=0.825\linewidth]{images/S58b.VIS.01.P44b-18.png}
    \captionof{figure}{Radar Plot of 2 Arms vs. FOLFIRINOX}
    \label{MAImage3}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{FOLFIRINOX best in OS Benefit\\[3pt]100K Patient Triplet/Doublet in 3 Areas}
        \end{quote}
    \end{tcolorbox}
\end{minipage}
\hfill
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S58b.VIS.01.P44b-20.png}
    \captionof{figure}{FOLFIRINOX, NAPOLI-1, MPACT, Study Timeline}
    \label{MAImage4}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-30pt, right=-30pt] 
        \begin{quote}
        \centering
        \textbf{Precision Era: KRAS G12C Inhibitors\\[3pt]Conversational AI Trials at Scale}
        \end{quote}
    \end{tcolorbox}
\end{minipage}

\vspace{0.35cm}

\section{Part IV: Meta-Analysis}

\subsection{100K Triplicate, Virtual, In-Person Trials}
\hspace{1.3em} Regarding the above charts, the forest plot \autoref{MAImage1} between Arm D (Daraxonrasib + Mitazalimab) and Arm A (Daraxonrasib + Mitazalimab + liposomal Irinotecan) from this study vs.\ other well-known clinical trials.\ Arm D finished last with an OS HR of 0.76, the MPACT trial was fourth, while Arm A finished third (HR 0.69). NAPOLI-1 was second with HR 0.67, while FOLFIRINOX was first at HR 0.57. \autoref{MAImage2} now incorporates toxicity with OS, with Arm D being the least toxic, with acceptable OS benefit.\ The radar plot in \autoref{MAImage3} illustrates FOLFIRINOX OS Benefit at 100, while Patient Fitness was approximately equal vs.\ the two Arms. Arm D reached top scores in Low Toxicity and Clinical Feasibility, further adding to its potential viability. The timeline in \autoref{MAImage4} depicts the advancements in PDAC drugs being compared: with FOLFIRINOX in 2011, MPACT in 2013, NAPOLI-1 in 2014, and the 100K Virtual Trial in 2025.  


\end{minipage}







\begin{minipage}{\textwidth}
\vspace{-0.9cm}
\renewcommand{\arraystretch}{1.61}
\setlength{\tabcolsep}{0pt}
\begin{table}[H]
\centering
\begin{tabular}{p{17.8cm}}
\toprule
\centering
\vspace{-0.55cm}
\textbf{Meta-Analysis: Triplicate vs.\ Virtual vs.\ On-Site Trials} \\
\vspace{0.055cm}
\midrule
\raggedright
\fontsize{7.25pt}{8.15pt}\selectfont

\vspace*{0.15cm}

\textbf{Table 1: Comparative Clinical and Methodological Metrics of In-Silico PDAC Trials}
\\

\vspace*{0.1cm}

{\renewcommand{\arraystretch}{1.05}
\begin{tabular}{p{0.6cm} p{2.1cm}@{\hspace{2mm}}p{3.1cm}@{\hspace{2mm}}p{3.1cm}@{\hspace{2mm}}p{4.0cm}@{\hspace{2mm}}p{4.0cm}}
\textbf{R} & \textbf{C1: Metric / Parameter} & \textbf{C2: 100K Triplicate (Control Arm E)} & \textbf{C3: 100K Triplicate (Triplet Arm A)} & \textbf{C4: Comparator In-Silico Study 1 (Digital Twin, 2024)} & \textbf{C5: Comparator In-Silico Study 2 (AI Simulation, 2023)} \\
R1 & Patient Population Size (N) & 20,000 & 20,000 & $\sim$861 (matched to real trial cohort) & 30 (virtual patients) \\
R2 & Patient Profile Summary & "Fitter" profile; $>$95\% ECOG 0--1 (underrepresentation of ECOG 2 vs RWD) & Same fitter profile as Control (ECOG 0/1 $\sim$97\%) & Mirrors real trial patients (each digital twin uses a real patient's clinical and molecular data) & Small virtual cohort; limited diversity (focused on average PDAC biology in simulation) \\
R3 & Modeling Architecture & Exponential survival model (Weibull k=1.0) & Exponential survival model with synergy factor (Weibull k=1.0) & AI-driven "digital twin" model (multi-omic data + trial outcomes; FarrSight algorithm) & Knowledge-based AI simulation (aiHumanoid DeepNEU v8.1 database, $\sim$72k relationships) \\
R4 & Median Overall Survival (OS) & 6.1 months & 8.7 months & $\sim$6.7 mo (control) / $\sim$8.5 mo (experimental) (accurately recreated from actual trial) & N/R (not reported; efficacy described via effect size, not median OS) \\
R5 & OS Hazard Ratio (HR vs. Control) & 1.00 (Reference arm) & $\sim$0.69 (Triplet vs Control) & $\sim$0.72 (in simulated trial, exp vs control) (targeting the actual HR) & N/R (no direct HR; reported p-values for endpoints, no HR given) \\
R6 & Median Progression-Free Survival (PFS) & 3.1 months & N/R (not reported for Arm A) & $\sim$3.7 mo (control) / $\sim$5.5 mo (exp) (recreated from trial) & N/R \\
R7 & PFS Hazard Ratio (HR vs. Control) & 1.00 (Reference) & N/R & $\sim$0.69 (exp vs control) (from actual trial) & N/R \\
R8 & Grade $\geq$3 Adverse Events (\%) & 76.5\% & 94.0\% & N/R (not explicitly reported; presumably matched actual trial's $\sim$43\% vs 27\% for combo vs ctrl) & N/R (qualitative: "increased bone marrow toxicity" noted) \\
R9 & Defined Patient Archetypes & 7 archetypes (ARCH-01 to ARCH-07) covering age, fitness, genomics & 7 archetypes (same as Control) & N/R (no fixed archetypes; each twin is individualized to a real patient) & N/R (no defined archetypes; all virtual patients treated as one group) \\
R10 & Key Subgroup Finding & N/A (Control arm, no targeted therapy) & Enhanced benefit in ARCH-05 (KRAS G12C mutant subgroup) & N/R (study validated outcomes; any subgroup effect would mirror the real trial if present) & p53 increase observed with treatment (target engagement); no patient subgroups analyzed \\
R11 & Source (URL / Report) & Source: Report & Source: Report & Asghar et al. 2024 (Digital Twin); Von Hoff et al. 2013 for actual PDAC trial & Danter et al. 2023 (medRxiv preprint) \\
\end{tabular}}

\vspace*{0.2cm}

\textbf{Table 2: Comparative Clinical Metrics -- Virtual Trial vs. Key Real-World PDAC Trials}
\\

\vspace*{0.1cm}

{\renewcommand{\arraystretch}{1.0}
\begin{tabular}{p{0.6cm} p{2.2cm}@{\hspace{2mm}}p{2.3cm}@{\hspace{2mm}}p{2.3cm}@{\hspace{2mm}}p{3.5cm}@{\hspace{2mm}}p{2.85cm}@{\hspace{2mm}}p{3.0cm}}
\textbf{R} & \textbf{C1: Metric / Parameter} & \textbf{C2: 100K Triplicate (Triplet Arm A)} & \textbf{C3: 100K Triplicate (Doublet Arm D)} & \textbf{C4: Phase III -- MPACT (Gemcitabine + Nab-Paclitaxel)} & \textbf{C5: Phase III -- NAPOLI-1 (nal-IRI + 5-FU/LV)} & \textbf{C6: Phase III -- PRODIGE 4 (FOLFIRINOX)} \\
R1 & Study / Regimen & Triplet (Dara + Mita + nal-IRI) & Doublet (Dara + Mita) & Gemcitabine + nab-Paclitaxel (Gem+Nab-P) & nal-IRI + 5-FU/LV (NAPOLI combo) & FOLFIRINOX (Oxali+Iri+5FU+Leucovorin) \\
R2 & Patient Population Size (N) & 20,000 (simulated) & 20,000 (simulated) & 861 (431 vs 430 per arm) & 417 (117 combo, 149 control, 151 monotherapy) & 342 (171 vs 171 per arm) \\
R3 & Baseline ECOG PS 0--1 (\%) & $>$95\% (modelled; failed RWD validation) & $>$95\% (similarly fit cohort) & $\sim$93\% (KPS $\geq$80; $\sim$7\% were PS2) & $\sim$100\% (KPS $\geq$70 eligibility; trial patients all PS 0--1) & 100\% (ECOG 0--1 required) \\
R4 & Median Overall Survival (OS) & 8.7 months & $\sim$8.0 months \textit{(Calculated)} & 8.5 months (combination arm) & 6.2 months (combo arm; 2nd line) & 11.1 months (FOLFIRINOX arm) \\
R5 & OS Hazard Ratio (HR vs. SoC) & $\sim$0.69 (vs Arm E control) & $\sim$0.76 (vs Arm E) \textit{(Calculated)} & 0.72 (vs gemcitabine) & 0.67 (vs 5-FU/LV) & 0.57 (vs gemcitabine) \\
R6 & Median Progression-Free Survival (PFS) & N/R & N/R & 5.5 months & 3.1 months & 6.4 months \\
R7 & PFS Hazard Ratio (HR vs. SoC) & N/R & N/R & 0.69 (vs gem) & 0.56 (vs 5-FU) & 0.47 (vs gem) \\
R8 & Grade $\geq$3 Adverse Events (\%) & 94.0\% & N/R & 84\% ($\geq$G3 in combo arm; any-event incidence) & 79\% ($\geq$G3 in combo arm, est.) -- e.g., neutropenia 27\% & $\sim$75\% ($\geq$G3 in FOLFIRINOX arm, est.) -- neutropenia 45\% \\
R9 & Objective Response Rate (ORR) (\%) & N/R & N/R & 23\% (vs 7\% gem) & 7.7\% (vs 0.8\% 5-FU) & 31.6\% (vs 9.4\% gem) \\
R10 & Source (URL / Report) & Source: Report & Source: Report & NEJM 2013 (MPACT) & Lancet 2016 (NAPOLI-1) & NEJM 2011 (FOLFIRINOX) \\
\end{tabular}}

\vspace*{0.2cm}

\textbf{Table 3: Pooled Clinical Metrics and Head-to-Head Efficacy--Toxicity Scoring}
\\

\vspace*{0.1cm}

{\renewcommand{\arraystretch}{1.0}
\begin{tabular}{p{0.6cm} p{1.4cm}@{\hspace{2mm}}p{1.35cm}@{\hspace{2mm}}p{1.8cm}@{\hspace{2mm}}p{0.7cm}@{\hspace{2mm}}p{1.5cm}@{\hspace{2mm}}p{1.8cm}@{\hspace{2mm}}p{1.8cm}@{\hspace{2mm}}p{1.7cm}@{\hspace{2mm}}p{1.4cm}@{\hspace{2mm}}p{1.9cm}}
\textbf{R} & \textbf{C1: Study ID} & \textbf{C2: Study Type} & \textbf{C3: Trial Arm (Regimen)} & \textbf{C4: N} & \textbf{C5: Median OS (mo)} & \textbf{C6: OS vs Control ($\Delta$ mo)} & \textbf{C7: Grade $\geq$3 AEs (\%)} & \textbf{C8: AEs vs Control ($\Delta$ \%)} & \textbf{C9: Source URL} & \textbf{C10: Calculated ETS} \\
R1 & 100K-Sim & Virtual & \textbf{Triplet (Arm A)} -- Dara+Mita+nal-IRI & 20000 & 8.7 & +2.6 & 94.0 & +17.5 & Source: Report & --0.69 (negative) \\
R2 & 100K-Sim & Virtual & Control (Arm E) -- nal-IRI + 5-FU & 20000 & 6.1 & 0.0 (Reference) & 76.5 & 0.0 & Source: Report & N/A \\
R3 & 100K-Sim & Virtual & \textbf{Doublet (Arm D)} -- Dara+Mita & 20000 & $\sim$8.0 \textit{(Calc.)} & +1.9 \textit{(Calc.)} & N/R & N/A & Source: Report & N/A (toxicity N/R) \\
R4 & MPACT & Real-World & \textbf{Gem+nab-P} (Exp) & 431 & 8.5 & +1.8 & $\sim$84.0 & +13.6 (43.2 vs 29.6\%) & Von Hoff et al. 2013 & $\sim$0.00 (baseline) \\
R5 & MPACT & Real-World & Gemcitabine (Control) & 430 & 6.7 & 0.0 & $\sim$70.4 & 0.0 & Von Hoff et al. 2013 & N/A \\
R6 & NAPOLI-1 & Real-World & \textbf{nal-IRI + 5-FU} (Exp) & 117 & 6.2 & +1.9 & $\sim$76.0 (est.) & +30 (est., vs $\sim$46\% 5FU) & Wang-Gillam et al. 2016 & (negative)* \\
R7 & NAPOLI-1 & Real-World & 5-FU/LV (Control) & 149 & 4.2 & 0.0 & $\sim$46.0 (est.) & 0.0 & Wang-Gillam et al. 2016 & N/A \\
R8 & PRODIGE4 (ACCORD11) & Real-World & \textbf{FOLFIRINOX} (Exp) & 171 & 11.1 & +4.3 & $\sim$75.0 (est.) & +25 (est., vs $\sim$50\% gem) & Conroy et al. 2011 & +0.36 (slightly +) \\
R9 & PRODIGE4 (ACCORD11) & Real-World & Gemcitabine (Control) & 171 & 6.8 & 0.0 & $\sim$50.0 (est.) & 0.0 & Conroy et al. 2011 & N/A \\
\end{tabular}}

\end{tabular}
\vspace{-0.2cm}
\midrule
\vspace{-0.2cm}
\caption{Meta-Analysis Served as Input for Financial Assessment, o3ph. Ref: S58}
\bottomrule
\label{MATables}
\end{table}
\end{minipage}












\begin{minipage}{\textwidth}
% --- Title ---
\begin{center}
    \Large\textbf{Financial Assessment and Value Proposition: o3ph, ops4}
\end{center}

\vspace{0.1cm}

\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S59b.VIS.01.P45b-11.png}
    \captionof{figure}{Total Project Cost Financial Estimates}
    \label{FAImage1}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{Phase II/III Trials: Site/FTE Costs\\[3pt]\$36K Triplicate: One User, AI Compute}
        \end{quote}
    \end{tcolorbox}
\end{minipage}
\hfill
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S59b.VIS.01.P45b-13.png} 
    \captionof{figure}{Time-to-Decision: 100K Triplicate vs.Field}
    \label{FAImage2}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{One Month AI Turnaround Time\\[3pt]Bests: Virtual Trials, Aids Trial Decisions}
        \end{quote}
    \end{tcolorbox}
\end{minipage}

\vspace{0.4cm}

% Additional two image blocks go below
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S59b.VIS.01.P45b-18.png}
    \captionof{figure}{Risk-Time Matrix Estimates, Log Scale}
    \label{FAImage3}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{100K Triplicate: Lowest \$, Uncertainty\\[3pt]Aids Slow/Expensive Human Trials}
        \end{quote}
    \end{tcolorbox}
\end{minipage}
\hfill
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S59b.VIS.01.P45b-20.png}
    \captionof{figure}{Ambitious AI Virtual Trial Forecasts}
    \label{FAImage4}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{Assumes \$19.96M Arm A Cost Savings if\\[3pt]Actual Trial Did Not Perform Favorably}
        \end{quote}
    \end{tcolorbox}
\end{minipage}

\vspace{0.65cm}

\section{Part V: External Study Value Proposition}

\subsection{Estimates vs.\ Single Virtual, QSP Trials}

\hspace{1.3em} \autoref{FAImage1} estimates the cost of a single 60 hour x 4 week user at \$150/hr vs.\ other virtual trials, a Phase II trial, and a Phase III trial (logarithmic scale). The triplicate was roughly \$36,000, while virtual trials trended upwards to \$600,000 for a QSP Model, and in-person trials went up to \$100 Million. Time-to-decision represented in \autoref{FAImage2} illustrated the speed of the 100K patient triplicate at 1 month, while in-person trials ranged from 2.5-5.0 years. The risk-time matrix in \autoref{FAImage3} again illustrated fast time to decision by the 100K triplicate, further emphasized with the lowest uncertainty. Lastly, \autoref{FAImage4} depicts potential cost savings up to \$19.96M to avoid an Arm A failure. Based on prior figures \autoref{MAImage2} and \autoref{MAImage3}, it is believed that Arm D (Daraxonrasib + Mitazalimab) would be a more appropriate candidate due to toxicity benefits and clinical feasibility. Burn rate reduction of \$2.36M, cost reduction of 99.9997\%, and ROI of 55,000\% could also be realized as a result of learning from the outcomes of this trial to assist future in-person trial drug selection. 

\end{minipage}
