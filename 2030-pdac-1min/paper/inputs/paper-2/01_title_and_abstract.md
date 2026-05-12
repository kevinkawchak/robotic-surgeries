%% Title
\title{QSP Metastatic Pancreatic Cancer AI Clinical Trial Simulation\\From Protocol to Prediction: Code, VVUQ, and Playbook}



\vspace{-0.2cm}

\author{
  Kevin Kawchak \orcidlink{0009-0007-5457-8667} \\
  Chief Executive Officer \\
  ChemicalQDevice \\
  San Diego, CA\\
  August 29, 2025\\
  \vspace{-0.24cm}
  kevink@chemicalqdevice.com \\
}

\begin{document}
\maketitle

\centering
\large \textbf{Abstract} \normalsize  
\vspace*{0.075cm} \par
\raggedright

% \begin{minipage}{\textwidth}
{\newlength{\labelwidth}
\settowidth{\labelwidth}{\textbf{Impacts:}\hspace{0.3cm}} % Sets the width to the longest label plus a 1em space

\noindent\makebox[\labelwidth][l]{\textbf{Question:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright Is it plausible for artificial intelligence to generate QSP (quantitative systems pharmacology) pancreatic cancer clinical trial protocols, Python scripts, VVUQ (verification, validation, and uncertainty quantification), and playbook?}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Concepts:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright Two prior author studies consisting of drug arms, baseline characteristics, and patient archetypes were incorporated into the initial text trial protocol. The protocol was then further optimized and converted into Python by ChatGPT 5 Pro Research (ChatGPT). Additional trial attributes and mathematical functions were added; followed by hyperparameter optimizations, increased adverse events functionality, and fine-tuning of time steps and tumor grid size primarily by Gemini 2.5 Pro (Gemini). Sensitivity analyses to biological parameters were then conducted; yielding the final model code with optimized parameters and further comparisons to established trials including POLO, NAPOLI-1, and MPACT. The code was then converted back into a plain text protocol by ChatGPT for interpretability regarding non-technical staff, and serving as a platform for future developments.}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Results:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright Verifications of several mechanistic variables revealed numerically stable objective response rates (ORRs), with results assisting the finalization of time step dt = 0.05 and tumor volume grid size = 5. Uncertainty quantification of biological sensitive vs. resistant clone parameters also aided in robust ORRs for a combination therapy. Additional sensitivity analysis was performed regarding a KRAS inhibitor whose Emax potency increased by up to threefold, limiting ORR error to 11\%. In effect, both numerical stability and biological credibility were demonstrated by the QSP pancreatic cancer simulation. Efforts to ground the control arms to external standards for this model had some success with mOS, ORR\%, and DCR\% performing more optimally; while mPFS, and Grade 3+ Adverse Events experienced less optimal results based on external validations.}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Outputs:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright Initial text based protocols were iteratively refined by ChatGPT based on the author's prior empirical trial, known requirements for QSP trials, and additional biological incorporations. Code trials were generated based on iterative prompting to optimize parameters and variables. The 10 arm, 7 archetype, 10,000 patient trial with up to 250 ordinary differential equations (ODEs) per patient was aimed towards rapid drug prototyping a Phase II trial in real time. Each trial run yielded a Python script, notebook, and a patient log file. These generated materials were then used throughout the study to build the QSP playbook, VVUQ documentation, and visualization text instructions. The instructions were then converted into Python scripts by Opus 4.1 Extended (Opus), further optimized by the author, and then executed in Google Colab.}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Impacts:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright Financial assessments were established between industry QSP virtual trial costs at \$2M vs historical Phase II and Phase III trials. The current study was performed by the author at a theoretical cost of \$36,304 based on a \$150/hr rate at 60 hr/wk for 4 weeks. A QSP cost reduction of up to 99.6\% was found; supported by a 23 month time reduction and +27,500\% ROI vs. a typical \$10.2M Phase II trial. Due to the larger patient cohorts and low resource requirements, the current QSP study was \$3.6/patient vs. an in-person trial of \$59,500/patient, a 16,528x difference. These financial propositions would most likely be realized by preventing no-go arms from proceeding to in-person trials, such as Arm E; which had a low mOS at 6.6 month, a high Grade 3+ AEs at 92.5\%, and second highest Drop \% at 14.2\%.}

\vspace{0.1cm}\par

\noindent\makebox[\labelwidth][l]{\textbf{Outcome:}}%
\parbox[t]{\dimexpr\textwidth-\labelwidth}{\raggedright Arm C, an oncogene-targeted therapy, was the most recommended drug combination by AI due to its high ORR at 70.8\% and mOS as 11.9 (HR = 0.50). Arms H and I derived from the previous empirical trial were consistently top drug combinations due to competitive response rates and survival. AI models proved pivotal for specialized tasks as ChatGPT was the domain expert that automated text production, Gemini generated trial code solutions at scale, and Opus converted text instructions into effective Python dashboards. Ultimately, as trial code character numbers and complexity rose, models were able to address smaller challenges in the code to obtain useful updates. The numerical stability and sensitivity analyses throughout the VVUQ process can be considered among the study's most impactful results, while endpoints were more challenging to align with external control arms. This may be due to an estimated 2.5 million tumor volume states being updated at each time-step, adding complexity for further AI modifications.}}
% \end{minipage}
\normalsize


\renewcommand{\contentsname}{Table of Contents} % Change title
\tableofcontents
\newpage

% \keywords{QSP Trial \and LLM \and Pancreatic Cancer \and Python

