\begin{minipage}{\textwidth}
\begingroup
  \renewcommand\thesection{0}  
  \section{\textbf{QSP Simulation Playbook: Phase II PDAC Trial}}  
  \label{sec:0}                 
\endgroup
\vspace{-0.2cm}

\vspace{0.3cm}
This playbook documents an end-to-end retrospective analysis of a virtual Phase II clinical trial in metastatic pancreatic ductal adenocarcinoma (PDAC). The project (Parts A-C) – comprising the trial design, QSP model implementation, and reverse engineered model specification – was completed prior to this report. Here we consolidate those efforts and the subsequent verification and validation (Part D) into a comprehensive playbook. All sections map to key project objectives or requirements. This playbook reviews and validates a completed in silico trial, emphasizing lessons learned and how the project met its planned objectives. It is formatted as a structured report, with clear headings, tables of parameters, governing equations, and results summaries. \\
\vspace{-0.15cm}

\begingroup
  \renewcommand\thesection{1}  
  \section{Clinical Trial Definition and Scope}  
  \label{sec:1}                 
\endgroup
% \vspace{-0.1cm}

\textbf{Trial Design:} The in silico trial was defined to mirror a real Phase II clinical trial in metastatic PDAC, but with an expanded multi-arm scope. The virtual trial included 10 treatment arms A–K (Arms A-E first line therapies, Arms G-K second line therapies; Arm F for distinction between lines) with approximately 1,000 virtual patients per arm, covering a range of therapeutic strategies: standard chemotherapy, targeted inhibitors, stromal modulators, and immunotherapies. For example, Arm A represented intensive multi-drug chemotherapy (gemcitabine + nab-paclitaxel \cite{02PaperGem}, analogous to a FOLFIRINOX-like regimen \cite{01PaperFolfironox}), while experimental arms added novel agents: Arm C combined chemo with a KRAS G12D oncogene inhibitor, Arm H added anti–PD-1 checkpoint blockade to chemo, Arm I combined PD-1 blockade with a CD40 agonist (with or without chemo), etc. Each virtual patient’s tumor progression and treatment response were simulated over a 3-year follow-up, capturing standard oncology endpoints – objective response rate (ORR), progression-free survival (PFS), overall survival (OS) – as well as safety outcomes (e.g. frequency of severe Grade \raisebox{0.25ex}{\scalebox{0.7}{$\geq$}}3 adverse events and treatment drop-out rates).\\
\vspace{-0.15cm}

\textbf{Scope and Innovation:} This trial definition exceeded typical QSP scopes, which often examine only one experimental arm vs. control. Here, ten parallel arms were run under a unified model, effectively simulating multiple trial scenarios concurrently. The multi-arm design included context-specific control groups for biomarker-defined subpopulations (e.g. Arm A and Arm G served as controls for first-line and second-line settings, respectively). This broad scope enabled head-to-head comparisons across therapies that would be infeasible in a single real trial, providing comprehensive insights into comparative efficacy and safety. A structured trial protocol (Part A) was written as the “source of truth” for the design – including arms A–K, patient inclusion criteria, dosing schedules, and endpoint definitions – and served as a binding specification for model development. By numbering protocol sections to map onto modeling requirements, we ensured traceability from clinical intent to implementation. In summary, the trial was clearly defined in clinical terms and then expanded in silico to test numerous combination strategies in parallel. The ten patient arms (A-E, G-K) and seven archetypes (ARCH-01 to ARCH-07) are described in Part A. \\
\vspace{-0.15cm}



