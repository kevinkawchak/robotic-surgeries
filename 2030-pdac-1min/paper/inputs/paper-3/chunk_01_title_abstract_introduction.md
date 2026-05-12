\documentclass{article}
% \documentclass[tikz,border=10pt]{standalone}

\usepackage{PRIMEarxiv}

\usepackage[utf8]{inputenc} % allow utf-8 input
\usepackage[T1]{fontenc}    % use 8-bit T1 fonts
\usepackage{url}            % simple URL typesetting
\usepackage{array}
\usepackage{booktabs}       % professional-quality tables
\usepackage{caption}
\usepackage{amsmath}
\usepackage{placeins}
\captionsetup{width=\textwidth}
\usepackage{float}
\usepackage{amsfonts}       % blackboard math symbols
\usepackage{nicefrac}       % compact symbols for 1/2, etc.
\usepackage{microtype}      % microtypography
\usepackage{lipsum}
\usepackage{fancyhdr}       % header
\usepackage{graphicx}       % graphics
\graphicspath{{media/}}     % organize your images and other figures under media/ folder
\usepackage[colorlinks=true, linkcolor=black, citecolor=black, filecolor=black, urlcolor=black]{hyperref}
\usepackage{cleveref}
\usepackage{orcidlink}
\usepackage{pgfplots}
\usepackage{pgfplotstable}
\usepackage[dvipsnames,table,xcdraw]{xcolor}
\usepackage{tikz}
\usepackage{tabularx}
\usepackage{makecell}
\usepackage{listings}
\usepackage{longtable}
\usepackage{pgf}
\usepackage{pgf-pie}
\usepackage{colortbl}
\usepackage{enumitem}
\usetikzlibrary{positioning}
\usepackage[x11names]{xcolor}
\usepackage{tcolorbox}
\usepackage{xcolor}
\usepackage{mdframed}
\usepackage{textcomp}
\usepackage{fancybox}
% \usetikzlibrary{positioning, shapes.geometric}
% \usetikzlibrary{arrows.meta}
\usetikzlibrary{calc} 
\usetikzlibrary{backgrounds}
\usetikzlibrary{decorations.pathmorphing, decorations.markings}
\usepackage[justification=centering]{caption}
% \usepackage[left=1.81in, right=1.05in, top=1in, bottom=1in]{geometry}
\setcounter{errorcontextlines}{999}
\usepackage{amssymb}
\setcounter{tocdepth}{3} % Include sections, subsections, subsubsections in ToC


% Experiment
\usetikzlibrary{arrows.meta,positioning,calc}
\usetikzlibrary{shapes.geometric, arrows}
\tikzstyle{startstop} = [rectangle, rounded corners, minimum width=3cm, minimum height=1cm,text centered, draw=black, fill=red!30]
\tikzstyle{process} = [rectangle, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=orange!30]
\tikzstyle{decision} = [diamond, minimum width=3cm, minimum height=1cm, text centered, draw=black, fill=green!30]
\tikzstyle{arrow} = [thick,->,>=stealth]

\usetikzlibrary{mindmap,trees}

\usepackage{circuitikz}



\setlength{\tabcolsep}{18pt} % Gap before text starts
\renewcommand{\arraystretch}{1.5} % Cell Height scaling
\setlength{\arrayrulewidth}{0.5mm} % Table Border Thickness


%Header
\pagestyle{fancy}
\thispagestyle{empty}
\rhead{ \textit{ }} 



%% Title
\title{ChatGPT 100,000 Patient 24-Month \textit{In Silico} Phase III\\5-Arm Pancreatic Cancer Clinical Trial Triplicate}
% \title{ChatGPT 100,000 Patient 24-Month \textit{In Silico} Triplicate\\Phase III 5-Arm Daraxonrasib, Mitazalimab, Irinotecan Pancreatic Cancer Clinical Trials, ICH E3‑Compliant}
% \title{ChatGPT 100,000 Patient 24-Month \textit{In‑Silico} Phase III 5-Arm Pancreatic Cancer Clinical Trials (ICH E3‑Compliant)}

\vspace{-0.2cm}

\author{
  Kevin Kawchak \orcidlink{0009-0007-5457-8667} \\
  Chief Executive Officer \\
  ChemicalQDevice \\
  San Diego, CA\\
  July 24, 2025\\
  \vspace{-0.24cm}
  kevink@chemicalqdevice.com \\
}

\begin{document}
\maketitle

\centering
\large \textbf{Abstract} \normalsize  
\vspace*{0.075cm} \par
\raggedright


{\newlength{\labelwidth}
\settowidth{\labelwidth}{\textbf{Impacts:}\hspace{0.3cm}} % Sets the width to the longest label plus a 1em space

\noindent\makebox[\labelwidth][l]{\textbf{Inquiry:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright Is it possible for ChatGPT to simulate three reproducible 100,000 patient pancreatic ductal adenocarcinoma (PDAC) Phase III clinical trial reports? If so, can the results be internally and externally validated, cross-verified using other AI models, and be compared both clinically and financially to other trials?}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Concept:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright 5 arms based on the Daraxonrasib + Mitazalimab + liposomal Irinotecan drug combination, baseline characteristics, and patient archetypes were identified from a prior study: doi.org/10.5281/zenodo.15735068. Six artificial intelligence models were then implemented to address the clinical trial pipeline: o3ph: ChatGPT o3-pro Research, g25p: Google Gemini 2.5 Pro, grk4: Grok 4, grk3: Grok 3 Think, o3pr: ChatGPT o3-pro, and ops4: Opus 4 Extended. o3ph generated the ICH E3‑aligned trial reports, log files, plus internal, and external validations. g25p, grk4, grk3, o3pr, and ops 4 provided cross verifications that highlighted trial-to-trial and model-to-model correlations. g25p utilized 24 generations in the study to produce a virtual trials overview, while o3ph provided a meta-analysis of pooled and scored data versus relevant virtual and on-site trials. o3ph also provided a financial assessment and value proposition of USD estimates against Phase II and Phase III studies. ops4 provided visualizations written in Python for the majority of the sections.}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Results:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright 100,000 individual patients generated from three separate o3ph conversations followed multiplicative hazard ratios and per-arm monthly hazards set in the prompt. Key variables were independent of each other, which yielded distributions of uncensored results. Log file cumulative effects of the censored 100,000 patients yielded expected results in OS by Arm (A > D > E), \raisebox{0.25ex}{\scalebox{0.7}{$\geq$}}G3 AE (A > D > E), and PFS (A > D > E). Baseline characteristics by metric across trials were in close alignment, and internal validations between log files and trial reports exhibited similar performance. External validation vs.\ a Flatiron Health dataset for OS passed, while ECOG validation saw higher differences. These deviations, along with a KRAS-mutant labeling issue were high, but consistent in magnitude across the three trials.}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Outputs:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright In order to consolidate trial information, validations, and cross-verifications, g25p processed 24 of these relevant outputs to create a virtual trials overview. The core trial information, technical specifications, reproducibility, and validation findings provided a concise output needed for subsequent comparisons to trials. The method used to pool the current study with prior studies was accomplished by o3ph utilizing the virtual trials overview alongside online clinical trial data to produce a 9,574 word meta-analysis. Results focused on PRODIGE-4 and NAPOLI-1 trials that were top two in OS, while Arm A was third. However, the Arm D doublet of Daraxonrasib + Mitazalimab was less toxic than the other trials, and was found to be more clinically feasible than FOLFIRINOX in PRODIGE-4.}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Impacts:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright The financial assessment and value proposition performed by o3ph and visualized by ops4 placed an estimated price of \$36,330 on the current study (1 user at \$150/hr working 60 hrs/wk). Estimates for other virtual trials ranged from \$120,000-\$600,000, while a real Phase II trial was \$20.0M, and the Phase III trial estimate was \$100.0M. Time-to-decision was fastest for the 100K Triplicate at 1 month, while other studies ranged from 4.5 months to 5.0 years. The AI's main financial decision was that Arm A (Daraxonrasib + Mitazalimab + liposomal Irinotecan) was not a strong enough candidate, and the results from the current study were estimated to save \$19.96M to avoid a clinical trial failure. In addition, a \$2.36M burn rate reduction was anticipated, with an overall cost reduction of 99.9997\% vs.\ a Phase III trial per patient.}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Outcome:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright The main benefit was that reproducibility was observed across a single trial or multiple trials, while individual patients likely varied based on raw exponential sampling. The o3ph feat was primarily in providing a trial report that was replicable between the other trials performed in separate conversations. Similarly, the g25p model's processing of 24 outputs to create a virtual trials overview could not me accomplished by any other model due to token limitations. The overview served to inform the final meta-analysis and financial assessment by o3ph, providing tangible comparisons and planning tools for upcoming studies. All work was performed by one user in a 30 day window.}}

\normalsize


\renewcommand{\contentsname}{Table of Contents} % Change title
\tableofcontents
\newpage

% \keywords{Pancreatic Cancer \and ChatGPT \and In Silico Trial}







\begin{minipage}{\textwidth}

\vspace{-1cm}

\begin{figure}[H]
    % \hspace*{2.2cm}
    \centering
    \includegraphics[width=0.75\linewidth]{images/MainDiagramSimPDAC}
    \vspace{0.05cm}
    \caption{PDAC 100K Patient In Silico Clinical Trial Pipeline}
    \label{MainProcessTriplicate}
\end{figure}
% \vspace{-0.2cm}
\end{minipage}







\begin{minipage}{\textwidth}
\section{Introduction} 


\subsection{LLMs Benefit In Silico Studies}

\hspace{1.3em} In 2025, clinical trial based datasets have been produced by combining oncology high context conversational AI reports and meta-analyses \cite{18KawchakPDAC, 17KawchakGlioblastoma, 16KawchakLung}. Output lengths of 10,000 words or more consistently exceeded the lengths of full-length articles, with AI composing multiple relevant sections in less than an hour. AI informed in silico clinical trial proposals containing patient, drug, and financial information were generated using several readily available models, including o3pr, ops4, g25p, and o3ch \cite{18KawchakPDAC}. Proposal verification, validation \& uncertainty quantification plans, as well as trial protocol and no-go criteria were included using AI by Kawchak K. Visualizations in Python yielding multiple chart types were best generated using ops4 or son4, although publication ready images required additional screening. Clinical trial data represented by risk of bias, forest plots, heatmaps, budgets, and financial timelines have been generated effectively. Meta-prompting using an AI model to generate, refine, or interpret prompts has been an effective tool to improve the output quality of subsequent generations. This method was particularly effective when large datasets needed to be implemented, but were not fully understood by the user. 


\hspace{1.3em}  For instance, meta-prompts were used with g25p on a 408,081 word dataset to determine a more optimized prompt for processing the large dataset. The g25p 1M token context length has enabled workflows that other leading AI models could not achieve. Verifications using the same prompt across multiple separate models was another effective technique to gain a consensus by Kawchak K. Five models were utilized to judge five virtual clinical trial proposals in best of 10 scoring, to yield a consensus on PDAC digital twin proposals \cite{18KawchakPDAC}. Criteria were based on deliverable completion, citation ability, trial impact, and funding probability, with the overall score being highest for o3pr at 9.09. Additional analysis of the three top proposals yielded trial timelines, a 6-part ROI analysis, FTE allocation, and budget comparisons. For small tasks, models such as 4och \cite{10Kawchak_mAbInContext_2024, 09Kawchak_mAbBioprocess_2024, 08kawchak2024Paclitaxel} and grk3 \cite{18KawchakPDAC, 17KawchakGlioblastoma} were effectively utilized for fast insights regarding well known information. 

% \vspace{-0.14cm}
\subsection{In Silico Studies, Local Trials}

\hspace{1.3em} In early 2024, Arcus Biosciences sponsored the PRISM-1 study, with Dr.\ Zev Wainberg, stating that "There is already a lot of data from randomized phase II and III trials on patients treated with gemcitabine/nab-paclitaxel. A synthetic arm is really very efficient since it reduces the number of patients needed for a study so the trial timeline is shorter and costs are reduced \cite{03IntroArcus}.” Later in 2024, Arcus Biosciences utilized data from a prior Phase 1B ARC-8 study which yielded a "37\% reduction in risk of death and a 5.9-month improvement in median overall survival" for patients treated with quemliclustat-based regimens when compared to a 122 patient Synthetic Control Arm® of patients treated with chemotherapy alone in a post-hoc analysis.  \cite{02IntroArcus}.
\vspace{0.1cm}

\hspace{1.3em} A 2024 \textit{Nature Cancer} article by researchers at Johns Hopkins and Cedars-Sinai Medical Center featured a Molecular Twin AI platform that integrated a dataset of 6,363 clinical and multi-omic molecular features to predict outcomes for pancreatic adenocarcinoma patients. "Our platform enables discovery of parsimonious biomarker panels and performance assessment of outcome prediction models learning from resource-intensive panels. This approach has considerable potential to impact clinical care and democratize precision cancer medicine worldwide \cite{04IntroOsipov}."  	
\vspace{0.1cm} 

\hspace{1.3em} In 2024, Asghar et al.\ published on the "Prediction of therapeutic response and cancer outcomes in solid tumours via in silico clinical trials." "For all 8 clinical studies, the digital twin model accurately simulated both trial arms, compared drug efficacy across arms and predicted which treatment was most active. "Blinded evaluation: Using data for paclitaxel, the model correctly predicted that nab-paclitaxel+gemcitabine response rates were higher than gemcitabine in metastatic pancreatic cancer (predicted LOR -0.090, p = <0.001) \cite{10IntroAsghar}." Toshimoto et al. in November 2024 published on an immune-oncology quantitative systems pharmacology (IO-QSP) model with custom tumor diameter, growth rate and immune cell proportions parameters. Two mechanisms of action were considered, with the authors "successfully reproducing the clinical responses of anti-PD-1 and/or combination therapy with anti-PD-1 and anti-CTLA-4". "The established IO-QSP models captured clinical responses of standard of care treatments and checkpoint inhibitors in both gastric and pancreatic cancers \cite{01IntroSayama}." 

\vspace{0.1cm}

\hspace{1.3em} The 2025 Phase III AVATAR Trial by Sarno et al.\ for personalized pancreatic cancer treatment featured whole‑exome sequencing + mouse/ PDO drug screens run. Avatar data selected matched therapy candidates; although only 10\% received matched drugs, that subgroup doubled median OS (19.3 mo vs 8.7 mo). "The study showed that personalized medicine did not improve survival as compared with standard of care in an intention-to-treat population \cite{07IntroSarno}." The Ko et al. April 2025 article on "Investigational Use of Real-World Data as a Hybrid Control in Pancreatic Ductal Adenocarcinoma From the Randomized Phase Ib/II MORPHEUS Trial" utilized a hybrid control arm and an experimental arm (atezolizumab + PEGylated recombinant human hyaluronidase (Atezo + PEGPH20)). HRs ranged from 1.02 to 1.06, and were comparable with the reported trial HR (HR 0.91; 95\% CI: 0.56, 1.49), with precision improvements experienced when using the hybrid control \cite{06IntroKo}." Pourmousa et al.\ in April 2025 detailed an AI methodology by researchers at UNC and MIT for pancreatic cancer that "evaluates predictive approaches to identify synergistic drug combinations using a dataset from the National Center for Advancing Translational Sciences (NCATS)." "Screening 496 combinations of 32 anticancer compounds against the PANC-1 cells experimentally determined the degree of synergism and antagonism." "Beyond highlighting the potential of ML, this work delivers 307 experimentally validated synergistic combinations, demonstrating its practical impact in treating pancreatic cancer." \cite{09IntroPourmousa}."

\end{minipage}












