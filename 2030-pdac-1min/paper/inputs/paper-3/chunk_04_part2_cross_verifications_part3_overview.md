\begin{minipage}{\textwidth}
\vspace{-0.5cm}
% --- Title ---
\begin{center}
    \Large\textbf{Multi-Model Cross-Verifications of Trials, ops4}
\end{center}

\vspace{0.1cm}

% Additional two image blocks go below
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S49.VIS.02.P39-04.png}
    \captionof{figure}{Inter-Arm Consistency Scores by Category}
    \label{CVImage3}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{8.95-9.45 Arm Averages Patterns\\[3pt]as Judged across Five AI Models}
        \end{quote}
    \end{tcolorbox}
\end{minipage}
\hfill
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S49.VIS.02.P39-10.png}
    \captionof{figure}{Waterfall Chart of Metric Categories}
    \label{CVImage4}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{8.65 Overall Trial Reproducibility Score\\[3pt]Starts at 10, with Category Decrements}
        \end{quote}
    \end{tcolorbox}
\end{minipage}


\begin{minipage}[t]{0.49\textwidth}
    \centering
    \hspace*{0.7cm}\includegraphics[width=0.88\linewidth]{images/S48.VIS.01.P38-05.png}
    \captionof{figure}{Inter-Model Consistencies for mPFS by Archetype}
    \label{CVImage1}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{Higher Model Consistency is Better\\[3pt]g25p: Most Consistent Across Archetypes}
        \end{quote}
    \end{tcolorbox}
\end{minipage}
\hfill
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=0.9\linewidth]{images/S48.VIS.01.P38-03.png} 
    \captionof{figure}{Pairwise Model Agreement for Row Consistencies}
    \label{CVImage2}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{Larger r Values Indicate Higher\\[3pt] Correlations with AI Models. grk4=o3pr}
        \end{quote}
    \end{tcolorbox}
\end{minipage}

\vspace{0.8cm}

\raggedright
\section{Part II: Cross-Verifications}

\subsection{Patient Trial vs. Patient Trial} 

\hspace{1.3em} Five AI models were used for cross-verifying the three in silico trials. The bar chart in \autoref{CVImage3} illustrates consistency across arms, with control Arm E being most consistent, likely due to more straightforward processing. The waterfall plot in \autoref{CVImage4} provides a final reproducibility score across the three trial 100,000 patient trials of 8.65. \autoref{CVImage1} illustrates mPFS by archetype row consistencies across the five models. g25p was most consistent across the 7 archetypes (4 scores \raisebox{0.25ex}{\scalebox{0.7}{$\geq$}}9.5), while ops4 had lower but more consistent scores. \autoref{CVImage2} shows pairwise model agreement, with two r=1.0 correlations between grk4 and o3pr and several other scores above r=0.9. These results indicate that consistencies for more than one AI software manufacturer have coincided for at least this task.     

\end{minipage}














\begin{minipage}{\textwidth}
\vspace{-0.5cm}
% --- Title ---
\begin{center}
    \Large\textbf{Multi-Model Meta-Verifications: Logs vs.\ Trials, ops4}
\end{center}

\vspace{0.1cm}

% Additional two image blocks go below
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S56.VIS.02.P42-04.png}
    \captionof{figure}{Measurement Reliability Profiles across Arms}
    \label{MVImage3}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{High Score, Overlapping Radar Preferred\\[3pt]High Arm Consistency for each Metric}
        \end{quote}
    \end{tcolorbox}
\end{minipage}
\hfill
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S56.VIS.02.P42-10.png}
    \captionof{figure}{Trial Value Distributions}
    \label{MVImage4}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{10/10 Scores for Baseline KRAS/Cohorts\\[3pt]8.8-10 Overall Range shows Consistency}
        \end{quote}
    \end{tcolorbox}
\end{minipage}

\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S55.VIS.01.P41-08.png}
    \captionof{figure}{Inter-Model Agreement for Calculated Values}
    \label{MVImage1}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{Multiple Models had Exact Agreement\\[3pt]grk4-g25p, grk4-o3pr, g25p-o3pr}
        \end{quote}
    \end{tcolorbox}
\end{minipage}
\hfill
\begin{minipage}[t]{0.49\textwidth}
    \centering
    \includegraphics[width=1\linewidth]{images/S55.VIS.01.P41-10.png} 
    \captionof{figure}{Table Specific Deviations by Model}
    \label{MVImage2}
    \vspace{0.15cm}
    \begin{tcolorbox}[colback=gray!10, colframe=black, boxrule=0.7pt, arc=4pt, width=7.9cm, top=7pt, bottom=7pt, left=-15pt, right=-15pt] 
        \begin{quote}
        \centering
        \textbf{No Deviations are Preferred. Largest:\\[3pt] Table 3 (grk3) +1, Table 2-R1 (ops4) -0.9}
        \end{quote}
    \end{tcolorbox}
\end{minipage}


\vspace{0.8cm}

\subsection{Log vs. Report Table vs. Trial}

\hspace{1.3em} These diagrams illustrate meta-verifications using multiple AI models for the three trials vs.\ individual log files. The radar plot in \autoref{MVImage3} illustrates close consistencies across multiple dimensions for each of the five arms. The ridge plot in \autoref{MVImage4} illustrates high scores for metrics, with Baseline KRAS have the highest score (10) and narrowest distribution. \autoref{MVImage1} generated by ops4 illustrates three exact agreements (<0.01) amongst AI models. \autoref{MVImage2} highlights specific table-model combinations that had the highest deviation from median scores, with one table by grk3 (+1) and one table by ops4 (-0.9) having largest deviations.


\end{minipage}









\begin{minipage}{\textwidth}



\begin{minipage}{\textwidth}
\vspace{-0.75cm}
\renewcommand{\arraystretch}{1.61}
\setlength{\tabcolsep}{0pt}
\begin{table}[H]
\centering
\begin{tabular}{p{17.8cm}}
\toprule
\centering
\vspace{-0.55cm}
\textbf{Virtual Trials Overview} \\
\vspace{0.055cm}
\midrule
\raggedright
\fontsize{7.75pt}{8.75pt}\selectfont

\vspace*{0.15cm}

\textbf{Table 01: 3 Virtual Trials - Overview} \\

\vspace*{0.1cm}

{\renewcommand{\arraystretch}{1.05}
\begin{tabular}{p{0.5cm}@{\hspace{2mm}}p{2cm}@{\hspace{2mm}}p{2cm}@{\hspace{2mm}}p{2.25cm}@{\hspace{2mm}}p{2cm}@{\hspace{2mm}}p{2.5cm}@{\hspace{2mm}}p{1.85cm}@{\hspace{2mm}}p{3.25cm}}
 & \textbf{C1: Study Title/ Identifier} & \textbf{C2: Primary Goal} & \textbf{C3: Trial Phase Equivalence} & \textbf{C4: Study Design} & \textbf{C5: Trial Arms} & \textbf{C6: Patient Population Size} & \textbf{C7: Patient Archetypes} \\
\textbf{R1: Details} & A Phase III Virtual Study of Triplet Daraxonrasib + Mitazalimab + liposomal Irinotecan vs Doublets vs Chemotherapy in Advanced Pancreatic Ductal Adenocarcinoma (PDAC-SIM-001) & To compare the efficacy and safety of a novel triplet therapy against doublet combinations and standard chemotherapy control in advanced PDAC. & \textbf{Phase:} III (Virtual Simulation) \textbf{Design:} Randomized, controlled, parallel-group, five-arm study. \textbf{Endpoints:} Co-primary endpoints of Overall Survival (OS) and Progression-Free Survival (PFS) with a 24-month data cutoff. & 5-arm in-silico simulation based on predefined patient archetypes and time-to-event models. Patients were randomized 1:1:1:1:1. & \textbf{Arm A:} Triplet (Daraxonrasib + Mitazalimab + liposomal Irinotecan) \textbf{Arm B:} Doublet (Mitazalimab + liposomal Irinotecan) \textbf{Arm C:} Doublet (Daraxonrasib + liposomal Irinotecan) \textbf{Arm D:} Doublet (Daraxonrasib + Mitazalimab) \textbf{Arm E:} Control (nal-IRI + 5-FU chemotherapy) & \textbf{Total:} 100,000 virtual patients per simulation run, conducted in triplicate. \textbf{Per Arm:} 20,000 patients. & \textbf{7\hspace{0.1cm}Predefined Archetypes:} ARCH-01: Young\_Fit\_Metastatic ARCH-02: Elderly\_Frail\_Metastatic ARCH-03: LAPC\_Standard\_Fitness ARCH-04: Young\_Fit\_BRCAm ARCH-05: Metastatic\_KRAS\_G12C ARCH-06: Metastatic\_High\_Stroma ARCH-07: Advanced\_Refractory\_PS1 \\
\end{tabular}}\\
\vspace*{0.1cm}
\textit{Source: Synthesized from trial reports S33.TRL.13.P30, S37.TRL.14.P30, S40.TRL.15.P30.}\\
\vspace*{0.2cm}
\textbf{Table 02: 3 Virtual Trials - Technical Specifications} \\
\vspace*{0.1cm}
{\renewcommand{\arraystretch}{1.05}
\begin{tabular}
{p{0.5cm}@{\hspace{2mm}}p{2.5cm}@{\hspace{2mm}}p{3cm}@{\hspace{2mm}}p{3.1cm}@{\hspace{2mm}}p{2.5cm}@{\hspace{2mm}}p{2.7cm}@{\hspace{2mm}}p{2.2cm}}
& \textbf{C1: Drug Combination(s)} & \textbf{C2: Patient Data Granularity} & \textbf{C3: Modeling Architecture} & \textbf{C4: Project Timeline} & \textbf{C5: Primary Endpoints} & \textbf{C6: Key AI Models Utilized} \\
\textbf{R1: Details} & \textbf{Core Triplet:} Daraxonrasib (KRAS G12C inhibitor) + Mitazalimab (immunotherapy) + liposomal Irinotecan. \textbf{Doublets \& Control:} Various combinations of the core agents and a standard chemotherapy control were tested across the 5 arms. & Virtual patients were generated with a rich set of features defined by seven archetypes. Key data points included: age, disease stage (metastatic vs. locally advanced), ECOG performance status (0, 1, 2), tumor genomics (KRAS mutation status, specifically G12C; germline BRCA mutation status), and baseline tumor markers (CA 19-9). & An exponential survival model (Weibull shape k=1.0) was used to simulate time-to-event outcomes. Baseline hazards for the control arm were set to achieve median PFS of 3.1 months and OS of 6.1 months. Multiplicative hazard ratios (HRs) for each drug and a synergy factor (0.90) for the triplet were applied to model treatment effects. & The virtual trial simulations and analyses were conducted with a report date of July-August 2025. A fixed random seed (20250624) was used across all three trials to ensure reproducibility of the simulation runs. & \textbf{Co-primary Endpoints:} 1. \textbf{Overall Survival (OS):} Time from randomization to death from any cause. 2. \textbf{Progression-Free Survival (PFS):} Time from randomization to disease progression or death. \textbf{Secondary Endpoints:} 12-month OS rates and incidence of Grade $\geq$3 adverse events. & \textbf{For Cross-Verification \& Meta-Verification:} 1. \textbf{grk4:} Grok 4 2. \textbf{grk3:} Grok 3 3. \textbf{ops4:} Opus 4 4. \textbf{g25p:} Gemini 2.5 Pro 5. \textbf{o3pr:} ChatGPT o3-pro \\
\end{tabular}}\\
\vspace*{0.1cm}
\textit{Source: Synthesized from trial reports S33, S37, S40 and verification files S43-S56.}\\
\vspace*{0.2cm}
\textbf{Table 04: Reproducibility and Validation Findings} \\
\vspace*{0.1cm}
{\renewcommand{\arraystretch}{1.05}
\begin{tabular}{p{1.2cm}@{\hspace{2mm}}p{7.9cm}@{\hspace{2mm}}p{8.2cm}}
& \textbf{C1: Validation (External Concordance)} & \textbf{C2: Reproducibility (Internal \& Cross-Model Consistency)} \\
\textbf{R1: Overall Survival (OS)} & \textbf{High Concordance:} The control arm (Arm E) from all three simulations demonstrated high external validity against Flatiron real-world data. OS\% at all measured time points (0-24 months) fell within the ±5\% pre-specified concordance threshold. The mean OS\% difference was ~1.5\% and the Pearson correlation was 0.999, both passing validation criteria (S35b, S38b, S41b). & \textbf{High Reproducibility:} Median OS values were extremely stable across the triplicate runs (e.g., Arm A mean OS of 8.73 mo, with a range of only 0.1 mo). Cross-trial consistency scores for Median OS and OS HR were high, averaging 8.98 and 9.08 respectively across the five AI models (S43-S47). This indicates the OS outcomes were highly reproducible. \\
\textbf{R2: Baseline Characteristics} & \textbf{Partial Concordance:} The simulated ECOG performance status distribution failed external validation. The absolute differences for ECOG 0, 1, and 2 vs. Flatiron data were ~5\%, ~14\%, and ~19\% respectively, all exceeding the ±5\% failure threshold (S35b, S38b, S41b). This indicates the simulated patient population was fitter than the real-world cohort. & \textbf{Exceptional Reproducibility:} Baseline characteristics were nearly identical across the three trials. Cross-trial consistency scores for all baseline metrics were $\geq$9.8 out of 10 across all AI models (S43-S47). The meta-verification analysis of the verification logs confirmed that discrepancies found were also highly consistent; for example, the KRAS-mutant deviation was found with a consistency score of 10.0 (S50-S54). \\
\textbf{R3: Cross-Model Verification \& Analysis} & Not Applicable. External validation was performed on the simulation output itself, not on the AI models' analysis. & \textbf{Strong Inter-Model Agreement:} The five AI models showed remarkable agreement in their analyses. Visualizations confirmed a "tight cluster" for grk4, g25p, and o3pr, with grk3 and ops4 as minor outliers (S55). Agreement was highest for baseline metrics and lowest for archetype-specific outcomes (S48). The analysis included programmatic generation of visualizations (e.g., 01\_heatmap\_consistency\_scores.py from S48) to quantify this agreement. \\
\textbf{R4: Overall Reproducibility Assessment} & The simulation's survival dynamics are externally valid, but the patient profile has limitations. & \textbf{Highly Robust:} The triplicate runs were highly consistent, with minimal variance in all primary and secondary endpoints. The AI-driven cross-trial verification process confirmed this stability with high consistency scores. Furthermore, meta-verification of the verification logs themselves also scored highly (mean scores >8.8), confirming the entire data generation and analysis pipeline is robust and reproducible (S50-S56). Analysis of visualization scripts (S49, S56) showed that percentage-based metrics (like AE rates) had higher consistency than time-to-event metrics (like median OS). \\
\end{tabular}}
\textit{Source: Synthesis of all verification (S35, S38, S41), external validation (S35b, S38b, S41b), cross-trial verification (S43-S47, S48, S49), and meta-verification (S50-S54, S55, S56) files.}

\end{tabular}
\vspace{-0.4cm}
\midrule
\vspace{-0.2cm}
\caption{Overview Served as Input for Meta-Analysis, g25p. Ref: S57}
\bottomrule
\label{VTOverviewTables}
\end{table}
\end{minipage}

\section{Part III: Virtual Trials Overview}

\subsection{Reproducibility: Validations, Cross-Model}
\hspace{1.3em} The g25p summary above is based on 24 prior generations as inputs, which includes the study design, patient population, and archetypes (Table 01). In addition, technical specifications between drug types, patient data granularity, modeling architecture, and key AI models utilized for cross-verifications are in Table 02. Reproducibility findings via the Flatiron dataset, internal validations, and consistencies are found in Table 04; setting up for comparisons to key in-person trials in the next steps.\\
\end{minipage}





