


\begingroup
  \renewcommand\thesection{13}  
  \section{Deliverables and Impact}  
  \label{sec:13}                 
\endgroup

Finally, we summarize the key deliverables from this project here and in Data availability:

\begin{itemize}[leftmargin=1.6em]
\item \textbf{Comprehensive Playbook (this paper)}: A structured report detailing the trial design, model implementation, V\&V summarization, and results. It serves as both a record of what was done (for internal knowledge management or audits) and a communication tool for external stakeholders (e.g. to include in a regulatory submission or share with a pharma partner considering a similar approach). By numbering sections according to requirements and including all results and interpretations, it ensures transparency and traceability from objectives to outcomes.  
\item \textbf{Initial Protocol (Part A):} The original trial design document (text format) capturing the clinical context and intent. It describes the trial arms A-E and G-K, patient population, inclusion/exclusion criteria, dosing schedules, and endpoint definitions. Essentially, this is the written Phase II protocol that served as the starting blueprint for the model. It’s included to provide the clinical reference for all modeling decisions. 
\item \textbf{Verified QSP Model Code (Part B):} The Python code and notebooks that implement the trial simulation. The impact of this deliverable is that anyone can reproduce the virtual trial or even modify parameters/arms using Python 3.12 to test new ideas, fostering confidence in the model’s effectiveness and reusability. (.ipynb, .py, csv for each trial run) 
\item \textbf{Reverse-Engineered Model Spec (Part C):} A human-readable document that describes the model in plain language, generated from the code. This is useful for team members or external reviewers who prefer not to read code. It enhances understanding and trust, as it reads like a protocol describing each arm’s mechanism and the equations in words. Future conversions back to code should primarily utilize Part B, accompanied by author notes taken from Part C.
\item \textbf{VVUQ Report (Part D) summarized here:} A compilation of all verification, validation, and uncertainty quantification activities. It demonstrates that the model was built rigorously. The impact is to satisfy governance requirements (anyone auditing the model development can see we tested numerical stability, explored uncertainties, etc.) and to identify the model’s domain of validity.
\item \textbf{Simulation Output Data:} All raw and processed data from the virtual trial runs have been included as supplementary files as CSV files. This includes patient-level outcomes and arm-level summaries. This data can be mined further by statisticians or used to perform additional analyses (for example, subgroup outcomes or correlations between toxicity and efficacy). By delivering the data, we allow others to verify our summary statistics and derive new insights.
\item \textbf{Key Prompts (Part E):} We included pivotal prompts used on the study to a) Import patient arms and archetypes from a prior article b) Obtain Part A text based clinical trial c) Improve performance of the code based trial d) Expand to the Part B code with multi-mechanism toxicity e) Obtain the Part C text based trial instructions from Part B. 
\item \textbf{Figures and Plots:} A collection of figures (Kaplan–Meier curves, waterfall plots of tumor shrinkage, bar charts of ORR, etc.) were generated. Where individual patient data from log files were incorporated, AI utilized sampling from patients for dashboards included in this playbook. Visualizing the results makes the impact more tangible – for instance, seeing the separation of survival curves drives home how much better Arm H was than Arm G, and how toxicity succinctly shows how toxic Arm E was relative to others.  
\end{itemize}

In sum, the project deliverables provide a 360-degree view of the virtual trial and ensure that its insights can be acted upon. The in silico findings have already influenced our pipeline decisions. By sharing this playbook with the broader team and stakeholders, we enabled data-driven prioritization: resources can be focused on the most promising strategies (KRAS and BRCA targeted combos) and away from likely dead-ends (toxic immunotherapy overloads). This illustrates the real impact of the QSP virtual trial – it’s not just an academic exercise, but a tool that informs practical decisions, potentially saving time and cost by avoiding unfruitful paths and highlighting high-yield opportunities.



\begingroup
  \renewcommand\thesection{14}  
  \section{Financial Assessments}  
  \label{sec:14}                 
\endgroup

\begin{figure}[H]
    \renewcommand\thefigure{14A}
    \centering \hspace{0.4cm}
    \includegraphics[width=0.875\linewidth]{images/Figure_14A.png}
    % \vspace{0.05cm}
    \caption{(A) Industry QSP simulation estimated trial cost vs prospective real trials\\(B) ROI from avoiding the larger cost; (C) Cost distribution of QSP trials vs. in-person trials}
    \label{14A}
\end{figure}



 

\begin{figure}[H]
    \renewcommand\thefigure{14B}
    \centering
    \includegraphics[width=0.825\linewidth]{images/Figure_14B.png}
    % \vspace{0.05cm}
    \caption{(A) Current study cost estimate and ROI vs Phase II, III trials; (B) Time to trial results\\favored by current study; (C) Per-patient cost reduction factor. Key Findings: Virtual trials are \\ \raisebox{0.1ex}\textasciitilde300× cheaper than Phase II, \raisebox{0.1ex}\textasciitilde1000× cheaper than Phase III, with 24-40× faster results}
    \label{14B}
\end{figure}







\begin{minipage}{\textwidth}
% \vspace{-0.5cm}

\raggedright
\section{Data availability} % Use section* for an unnumbered section
\linespread{0.95}\selectfont
% --- Column 1 ---
\begin{minipage}[t]{0.32\textwidth}
\normalsize
\begin{enumerate}[leftmargin=1.6em]
\item A1\_Initial\_Protocol.pdf
\item B1\_Final\_Trial\_Code.csv
\item B1\_Final\_Trial\_Code.ipynb
\item B1\_Final\_Trial\_Code.py
\item B2\_Trial\_Sequence
    \begin{enumerate}
    \item B2\_Draft\_1
        \begin{enumerate}
        \item B2\_Draft\_1.csv
        \item B2\_Draft\_1.ipynb
        \item B2\_Draft\_1.py
        \end{enumerate}
    \item B2\_Draft\_2
        \begin{enumerate}
        \item B2\_Draft\_2.csv
        \item B2\_Draft\_2.ipynb
        \item B2\_Draft\_2.py
        \end{enumerate}
    \item B2\_Draft\_3
        \begin{enumerate}
        \item B2\_Draft\_3.csv
        \item B2\_Draft\_3.ipynb
        \item B2\_Draft\_3.py
        \end{enumerate}
    \item B2\_Neg\_Control
        \begin{enumerate}
        \item B2\_Neg\_Control.csv
        \item B2\_Neg\_Control.ipynb
        \item B2\_Neg\_Control.py
        \end{enumerate}
    \item B2a\_Prior\_Files
        \begin{enumerate}
        \item 2 .pdfs, 1 .ipynb files
        \end{enumerate}
    \end{enumerate}
\item B3\_Final\_Triplicate
    \begin{enumerate}
    \item B3\_Final\_1
        \begin{enumerate}
        \item B3\_Final\_1.csv
        \item B3\_Final\_1.ipynb
        \item B3\_Final\_1.py
        \end{enumerate}
    \item B3\_Final\_2
        \begin{enumerate}
        \item B3\_Final\_2.csv
        \item B3\_Final\_2.ipynb
        \item B3\_Final\_2.py
        \end{enumerate}
    \item B3\_Final\_3 
        \begin{enumerate}
        \item B3\_Final\_3.csv
        \item B3\_Final\_3.ipynb
        \item B3\_Final\_3.py
        \end{enumerate}
    \end{enumerate}
    \vspace{-0.5cm}
\item[] \item[] \hspace{-0.525cm} \textbf{Numerical Stability}
\item B4\_Verify\_Time\_Step
    \begin{enumerate}
    \item B4\_dt\_005
        \begin{enumerate}
        \item B4\_dt\_005.csv
        \item B4\_dt\_005.ipynb
        \item B4\_dt\_005.py
        \end{enumerate}
    \item B4\_dt\_010
        \begin{enumerate}
        \item B4\_dt\_010.csv
        \item B4\_dt\_010.ipynb
        \item B4\_dt\_010.py
        \end{enumerate}
    \item B4\_dt\_025
        \begin{enumerate}
        \item B4\_dt\_025.csv
        \item B4\_dt\_025.ipynb
        \item B4\_dt\_025.py
        \end{enumerate}
    \item B4\_dt\_045
        \begin{enumerate}
        \item B4\_dt\_045.csv
        \item B4\_dt\_045.ipynb
        \item B4\_dt\_045.py
        \end{enumerate}
\end{enumerate}
\end{enumerate}
\end{minipage}
% --- Spacer ---
\hfill
% --- Column 2 ---
\begin{minipage}[t]{0.32\textwidth}
\normalsize
\begin{enumerate}[leftmargin=1.6em]
\setcounter{enumi}{6} % Continue numbering from column 1
\item B4\_Verify\_Time\_Step (cont.)
    \begin{enumerate}
    \item B4\_dt\_050
        \begin{enumerate}
        \item B4\_dt\_050.csv
        \item B4\_dt\_050.ipynb
        \item B4\_dt\_050.py
        \end{enumerate}
    \item B4\_dt\_055
        \begin{enumerate}
        \item B4\_dt\_055.csv
        \item B4\_dt\_055.ipynb
        \item B4\_dt\_055.py
        \end{enumerate}
    \item B4\_dt\_060
        \begin{enumerate}
        \item B4\_dt\_060.csv
        \item B4\_dt\_060.ipynb
        \item B4\_dt\_060.py
        \end{enumerate}
    \end{enumerate}
\item B5\_Verify\_Grid\_Size
    \begin{enumerate}
    \item B5\_Grid\_Size\_2
        \begin{enumerate}
        \item B5\_Grid\_Size\_2.csv
        \item B5\_Grid\_Size\_2.ipynb
        \item B5\_Grid\_Size\_2.py
        \end{enumerate}
    \item B5\_Grid\_Size\_3
        \begin{enumerate}
        \item B5\_Grid\_Size\_3.csv
        \item B5\_Grid\_Size\_3.ipynb
        \item B5\_Grid\_Size\_3.py
        \end{enumerate}
    \item B5\_Grid\_Size\_4
        \begin{enumerate}
        \item B5\_Grid\_Size\_4.csv
        \item B5\_Grid\_Size\_4.ipynb
        \item B5\_Grid\_Size\_4.py
        \end{enumerate}
    \item B5\_Grid\_Size\_5
        \begin{enumerate}
        \item B5\_Grid\_Size\_5.csv
        \item B5\_Grid\_Size\_5.ipynb
        \item B5\_Grid\_Size\_5.py
        \end{enumerate}
    \item B5\_Grid\_Size\_6
        \begin{enumerate}
        \item B5\_Grid\_Size\_6.csv
        \item B5\_Grid\_Size\_6.ipynb
        \item B5\_Grid\_Size\_6.py
        \end{enumerate}
    \item B5\_Grid\_Size\_7
        \begin{enumerate}
        \item B5\_Grid\_Size\_7.csv
        \item B5\_Grid\_Size\_7.ipynb
        \item B5\_Grid\_Size\_7.py
        \end{enumerate}
    \end{enumerate}
    \vspace{-0.5cm}
\item[] \item[] \hspace{-0.525cm} \textbf{Sensitivity Analysis} 
\item B6\_Quantify\_Tumor\_Vol
    \begin{enumerate}
    \item B6\_dVol\_res\_003
        \begin{enumerate}
        \item B6\_dVol\_res\_003.csv
        \item B6\_dVol\_res\_003.ipynb
        \item B6\_dVol\_res\_003.py
        \end{enumerate}
    \item B6\_dVol\_res\_006
        \begin{enumerate}
        \item B6\_dVol\_res\_006.csv
        \item B6\_dVol\_res\_006.ipynb
        \item B6\_dVol\_res\_006.py
        \end{enumerate}
    \item B6\_dVol\_res\_009
        \begin{enumerate}
        \item B6\_dVol\_res\_009.csv
        \item B6\_dVol\_res\_009.ipynb
        \item B6\_dVol\_res\_009.py
    \end{enumerate}
\end{enumerate}
\end{enumerate}
\end{minipage}
% --- Spacer ---
\hfill
% --- Column 3 ---
\begin{minipage}[t]{0.32\textwidth}
\normalsize
\begin{enumerate}[leftmargin=3.2em]
\setcounter{enumi}{9} % Continue numbering from column 2
\item B7\_Quantify\_Emax\_Mrtx
    \begin{enumerate}
    \item B7\_Emax\_036
        \begin{enumerate}
        \item B7\_Emax\_036.csv
        \item B7\_Emax\_036.ipynb
        \item B7\_Emax\_036.py
        \end{enumerate}
    \item B7\_Emax\_072
        \begin{enumerate}
        \item B7\_Emax\_072.csv
        \item B7\_Emax\_072.ipynb
        \item B7\_Emax\_072.py
        \end{enumerate}
    \item B7\_Emax\_108
        \begin{enumerate}
        \item B7\_Emax\_108.csv
        \item B7\_Emax\_108.ipynb
        \item B7\_Emax\_108.py
        \end{enumerate}
\end{enumerate}
\item B8\_Quantify\_Vol\_Resist
    \begin{enumerate}
    \item B8\_Vol\_Res\_005
        \begin{enumerate}
        \item 8\_Vol\_Res\_005.csv
        \item 8\_Vol\_Res\_005.ipynb
        \item 8\_Vol\_Res\_005.py
        \end{enumerate}
    \item B8\_Vol\_Res\_015
        \begin{enumerate}
        \item B8\_Vol\_Res\_015.csv
        \item B8\_Vol\_Res\_015.ipynb
        \item B8\_Vol\_Res\_015.py
        \end{enumerate}
    \item B8\_Vol\_Res\_030
        \begin{enumerate}
        \item B8\_Vol\_Res\_030.csv
        \item B8\_Vol\_Res\_030.ipynb
        \item B8\_Vol\_Res\_030.py
        \end{enumerate}
\end{enumerate}
\item B9\_Quantify\_EC50\_Mrtx
    \begin{enumerate}
    \item B9\_EC50\_100
        \begin{enumerate}
        \item B9\_EC50\_100.csv 
        \item B9\_EC50\_100.ipynb
        \item B9\_EC50\_100.py
        \end{enumerate}
    \item B9\_EC50\_050
        \begin{enumerate}
        \item B9\_EC50\_050.csv
        \item B9\_EC50\_050.ipynb
        \item B9\_EC50\_050.py
        \end{enumerate}
    \item B9\_EC50\_025 
        \begin{enumerate}
        \item B9\_EC50\_025.csv
        \item B9\_EC50\_025.ipynb
        \item B9\_EC50\_025.py
        \end{enumerate}
\end{enumerate}
\vspace{-0.025cm}
\item[] \hspace{-0.68cm} \textbf{Final Documentation}    
\item C1\_Final\_Protocol.pdf
\item D1\_VVUQ\_Report.pdf
\item E1\_Key\_Prompts.pdf
\item F1\_Trial\_Charts.ipynb
\item F1\_Trial\_Charts.py 
\item F1\_Trial\_Images
\end{enumerate}
\phantom{11i} Source: Zenodo \cite{20KawchakQSPPDAC}
\end{minipage}

\end{minipage}








\raggedright
% \section{Appendix}










\newpage
\normalsize

%Bibliography
\bibliographystyle{unsrturl}  
\bibliography{references}  

\vspace{0.1cm}
\raggedright

\begin{minipage}{\textwidth}
\section{Acknowledgments} \normalsize 

\vspace{0.025cm}

The author would like to acknowledge OpenAI for providing access to ChatGPT, Google for providing access to Gemini, Anthropic for providing access to Claude, and xAI for providing access to Grok.

\vspace{0.1cm}

% \textbf{\large Ethical disclosures} \normalsize
\section{Ethical disclosures}

\vspace{0.025cm}
 
The author of the article declares no competing interests.

\vspace{0.1cm}

% \textbf{\large Rights and permissions} \normalsize
\section{\textbf{Rights and permissions}}

\vspace{0.025cm}

This article is distributed under the terms of the Creative Commons Attribution 4.0 International License (\href{https://creativecommons.org/licenses/by/4.0/}{CC BY 4.0}), which permits unrestricted use, distribution, and reproduction in any medium, provided the original author(s) and source are properly credited, a link to the Creative Commons license is provided, and any modifications made are indicated. To view a copy of this license, visit \url{https://creativecommons.org/licenses/by/4.0/}.

\vspace{0.1cm}

% \textbf{\large About this study} \normalsize
\section{About this study}

\vspace{0.025cm}

Kawchak K. QSP Metastatic Pancreatic Cancer AI Clinical Trial Simulation From Protocol to Prediction: Code, VVUQ, and Playbook. Zenodo. 2025; 10.5281/zenodo.17001137 \cite{20KawchakQSPPDAC}.
\end{minipage}
\end{document}
