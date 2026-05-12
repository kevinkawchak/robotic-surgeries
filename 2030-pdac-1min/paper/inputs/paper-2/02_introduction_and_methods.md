

\begin{minipage}{\textwidth}
\begingroup
  \renewcommand\thesection{A}  
  \section{Introduction}  
  \label{sec:A}                 
\endgroup
\vspace{-0.05cm}

\hspace{1.3em} In 2013, Natpara submitted a Quantitative Systems Pharmacology inquiry to the U.S. Food and Drug Administration regarding how alternative dosing strategies could reduce an adverse event \cite{01IntroCucurull, 02IntroPeterson}. Five years later, effective QSP Model-Informed Drug Development (MIDD) has increased in popularity, with 60 QSP submissions in 2020 \cite{01IntroCucurull}. QSP has been utilized to de-risk decisions for accelerating timelines and increasing return on investments. The increased biological complexities of QSP over simplified empirical models has led to additional FDA attention to continue model technique innovations \cite{01IntroCucurull, 03IntroGalluppi, 04IntroMadabushi}. In addition, QSP models have been advantageous in patient stratification on the basis of pharmacodynamic biomarkers and clinical endpoints, combination therapies describing therapeutic interventions at the cellular level, and novel drugs regarding large numbers of targets and mechanisms \cite{01IntroCucurull}. Additionally, QSP informed initiatives led by FDA Project Optimus in 2021 have been used to aid dose and schedule selection to improve safety and effectiveness \cite{05IntroVenkatakrishnan, 06IntroMurphy}. \\
\vspace{-0.25cm}

\hspace{1.3em} QSP models of increasing complexity by Wang et al. targeted immuno-oncology by utilizing data from multiplex digital pathology and genomic analysis, as published in 2024 \cite{07IntroWang}. These approaches offered better perspectives regarding the tumor immune microenvironment "to predict effectiveness of immune checkpoint inhibitors in combination with other therapies in multiple cancer types". Additionally, spatially resolved agent-based models "track whole patient-scale dynamics and recapitulate the emergent spatial heterogeneity in the tumor" \cite{08IntroGong}. The cost and time associated with developing these intricate models is typically high due to complex biologies. For instance, PDAC cancer has dense desmoplastic stroma, poor perfusion, high interstitial pressure, and immunosuppressive microenvironments \cite{09IntroHartupee}. Initiatives led by Flatiron Health have aimed to "generate real-world evidence from over 4 million patient journeys with industry-leading real-world data" in regards to oncology data curation \cite{11IntroFlatiron}. With the end goals of pancreatic cancer models to save money due to years of failed Phase III trials \cite{18IntroWang}, an opportunity was realized for capable conversational AI models to re-imagine the QSP model developing process, streamline VVUQ, and add interpretability to complex code through rapid text based protocol generations.\\
\vspace{-0.25cm}

\hspace{1.3em} Several 2025 developments have attributed large language models (LLMs) as having utility to clinical trials. For instance, Yang et al. detailed LLMs as clinical trial simulation productivity tools such as coding, report writing, and search assimilation \cite{21IntroYang}. The use of LLMs for QSP published by Androulakis et al. in the same year as "facilitating interdisciplinary collaboration, lowering barriers to entry, and democratizing QSP workflows" \cite{19IntroAndroulakis, 20IntroAndroulakis}. Goryanin, et al.\ in 2025 found that some LLMs could summarize QSP model structure, simulate outcomes, and propose perturbation experiments useful for refining workflows and scenario testing \cite{22IntroGoryanin}. Based on these recent developments, to the author's best knowledge, no end-to-end QSP oncology clinical trial with supporting documentation using conversational AI has been achieved at the time of publication.\\
\vspace{-0.25cm}

\begingroup
  \renewcommand\thesection{B}  
  \section{Methods}  
  \label{sec:B}                 
\endgroup
\vspace{-0.05cm}

\hspace{1.3em} QSP Arms were partially based on a Daraxonrasib + Mitazalimab + liposomal Irinotecan drug combination proposal that had a top therapeutic synergy and viability score, combined with baseline characteristics, archetypes, and timelines from Proposal A and B of a recent study \cite{18KawchakPDAC}. Additional trial structure, patient cohort specifics, and patient log file structures were derived from an author's empirical model \cite{19KawchakSimPDAC}, which was included in Prompt 01 using ChatGPT o3-pro Research. Further adaptations through iterative prompting to the resulting plain text trial instructions that were obtained, further optimized across AI manufacturers, and eventually converted into Python for deterministic results. Modifications to Temperature and Top-P hyperparameters in Gemini 2.5 Pro, additional adverse events processing components, and PDE diffusion grid incorporations aided the Part B final trial summary performance. As the code increased in size to over 1,300 lines, only Gemini could be utilized to make effective code revisions - with improvements seen based on narrower inquiries to optimize parameters or end results. Part B was then converted into the Part C plain text protocol using ChatGPT 5 Pro Research.\\
\vspace{-0.25cm}

\hspace{1.3em} Results were obtained and reported primarily on the final trial summaries at the bottom of Python scripts. Patient log files could only be utilized with ChatGPT to gain additional insights and create visualization templates. VVUQ experiments were run in stages, as findings progressively assisted the Part B final trial summary performance. AI recommended variable changes based on either mechanistic (dt, grid size) or biological (Emax, EC50, etc.) based parameters. These findings were used to obtain the optimized Part B dt = 0.05, grid size = 5 settings. In-depth VVUQ sections requiring additional tables, interpretations, and oncology-specific modeling notes are included in supplementary D1\_VVUQ\_Report. External study comparisons to prior trials were primarily based on AI searches while processing prompts. The author composed the abstract, introduction, and methods, prompted AI, and made corrections.\\
\vspace{-0.25cm}

\hspace{1.3em} Large portions of the study required the author to read scripts, playbooks, and verification documents and then submit prompts to AI for new revisions. The term "we" in this trial refers to the author and AI, and AI-in-the-Loop quality assurance.\ All visualizations were obtained by Opus 4.1 Extended by processing text instructions into Python scripts, which were executed in Google Colab \cite{GoogleColab}, viewed in VS Code\cite{Visual_Studio_Code}, and are included in F1\_Trial\_Charts. Initial attempts to convert Python into R or Julia languages were not successful, likely due to clinical trial, biological, and mathematic complexities at scale.\\
\vspace{-0.25cm}

\hspace{1.3em} AI software were based on unmodified chat-based inference LLMs. MacOS 14.5 (23F79), Chrome Version 138.0.7204.169. \\
\vspace{-0.25cm}

\begin{enumerate}[leftmargin=1.75em]
    \item \textbf{ChatGPT:} OpenAI ChatGPT 5 Research (Deep Research), ChatGPT website pro chat interface \cite{ChatGPT5DR}
    \item \textbf{Gemini:} Google Gemini 2.5 Pro, Google AI Studio.\ Settings: Temp=1, Thinking mode=On, Thinking budget=32768, Off=(Structured output, Code execution, Function calling, Grounding with Google Search, URL context), Off=(Safety settings), Output length=65536, Top P=0.95. (Alternate: Temp=0.2, Top P=0.95) \cite{Google_AI_Studio}
    \item \textbf{Opus:} Claude Opus 4.1 Extended, Claude website professional plan chat interface \cite{Opus41}
    \item \textbf{Other:} OpenAI ChatGPT o3-pro Research was accessed in earlier project stages through the ChatGPT website pro chat interface \cite{ChatGPTo3}. xAI Grok 3 was accessed through the Grok website chat interface for small coding tasks \cite{Grok3}
\end{enumerate}
\end{minipage}
