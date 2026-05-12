\begingroup
  \renewcommand\thesection{2}  
  \section{Mechanistic QSP Model Construction}  
  \label{sec:2}                 
\endgroup
% \vspace{-0.1cm}

\textbf{Model Overview:} A detailed quantitative systems pharmacology (QSP) model of PDAC was constructed to represent tumor biology and drug mechanisms in each trial arm. The model explicitly captures tumor–microenvironment interactions and multi-modal treatment effects, rather than relying on empirical response probabilities. It integrates diverse mechanistic pathways relevant to PDAC: tumor cell proliferation, drug-induced cytotoxicity, oncogene-driven growth, immune activation/suppression, and stromal barrier effects. Importantly, the model was designed to be modular: each therapy’s mechanism can be toggled on or off per arm, enabling combination regimens to be simulated by superimposing the relevant modules. This extensible architecture allowed us to incorporate multiple pathways simultaneously (DNA damage response for chemotherapy, KRAS-driven signaling for targeted therapy, T-cell mediated killing for immunotherapies, myeloid immunosuppression via CD47, stromal hindrance via hyaluronan, etc.), going beyond traditional single-pathway QSP models. By including all major PDAC treatment modalities in one system, natural synergy and antagonism could emerge (for example, cytotoxic chemo making tumor cells more immunogenic and thus more susceptible to immune clearance). The mechanistic breadth aligns with modern QSP standards and permits exploration of dynamics that real trials cannot directly observe (e.g. tumor regrowth patterns after therapy). Notably, the model’s baseline predictions for standard treatments were calibrated to approximate clinical reality.\\
\vspace{-0.15cm}

\textbf{State Variables and Equations:} The core disease model tracks tumor growth in two compartments: therapy-sensitive tumor cells and therapy-resistant tumor cells (intrinsically resistant from the start). Key differential equations governing tumor volume dynamics (in a single well-mixed tumor compartment, later extended to a spatial grid) are:
\\
\vspace{-0.15cm}

$V_{s}$(t) = volume of therapy-sensitive tumor cells (susceptible to chemo and other treatments)
$V_{r}$(t) = volume of therapy-resistant tumor cells (insensitive to certain therapies, e.g. chemo-resistant clone)\\
\vspace{-0.15cm}

\[
\begin{aligned}
\frac{dV_s}{dt} &= r_s V_s\!\left(1-\frac{V_s+V_r}{K}\right)
- k_{\text{chemo}}(t)\,V_s - k_{\text{immune}}(t)\,V_s - k_{\text{target}}(t)\,V_s,\\[6pt]
\frac{dV_r}{dt} &= r_r V_r\!\left(1-\frac{V_s+V_r}{K}\right)
- k_{\text{immune}}(t)\,V_r - k_{\text{target}}(t)\,V_r
\normalsize \text{ [if target affects resistant cells]}
\end{aligned}
\]
\end{minipage}




\begin{figure}[H]
    \renewcommand\thefigure{2A}
    \centering \hspace{-0.5cm}
    \includegraphics[width=.48\linewidth]{images/Figure_2A.png}
    \vspace{0.05cm}
    \caption{AI-assisted modeling workflow shows Part A (design) through Part C (protocol),\\highlighting where AI/LLM was used in code generation, validation, and review}
    \label{2A}
\end{figure}
\vspace{-0.6cm}



Here $r_{s}$ and $r_{r}$ are the net proliferation rates of sensitive and resistant cells, respectively (set to reflect PDAC tumor doubling time under no treatment). A logistic growth term (1 - $V_{s}$+$V_{r}$ K is included with a large carrying capacity K to prevent unbounded growth (in practice, patients die or tumors plateau before reaching K). Therapeutic killing terms appear as time-dependent kill rates $k_{drug}$(t) multiplying the tumor volume. \textbf{Chemotherapy} kill, $k_{chemo}$(t), is nonzero during drug administration periods and is applied \textbf{only to sensitive cells} (resistant cells are assumed impervious to chemo). \textbf{Targeted therapy} kill, $k_{target}$(t), represents tumor cell kill or growth arrest due to an oncogene inhibitor (e.g. KRAS G12D inhibitor MRTX-1133, or KRAS G12C inhibitor in second-line). This term is only active in arms where the drug is given and the tumor carries the target mutation; it was typically applied to the entire tumor volume in those patients (we assume the oncogene drives all tumor cells, though one could restrict it further). \textbf{Immune-mediated kill}, $k_{immune}$(t), represents cytotoxic T-cell and macrophage attack on tumor cells; it is modulated by immunotherapies (e.g. PD-1 blockade increases $k_{immune}$ by unleashing T cells, CD40 agonist increases it by priming T cells and antigen-presenting cells, and CD47 blockade increases macrophage-mediated phagocytosis). This term affects both sensitive and resistant cells (the immune system can, in principle, recognize and kill both subpopulations). All kill rates are functions of time, reflecting dosing schedules and drug PK/PD: for instance, $k_{chemo}$(t) might spike after each gemcitabine/nab-paclitaxel dose and decay with drug half-life, while $k_{immune}$(t) rises gradually upon PD-1/CD40 therapy and might persist as immune memory.

\textbf{Initial Conditions:} At t=0 (treatment initiation), each virtual patient’s tumor volume is initialized and partitioned into sensitive vs resistant cells. We denote the \textbf{intrinsic resistant fraction} as $f_{res}$ (a key parameter). Thus: 


$V_{s}(0)$ = (1 - $f_{res}$) $V_{0}$

$V_{r}(0)$ = $f_{res}$ $V_{0}$

where $V_{0}$ is the baseline tumor volume (e.g. normalized to 1.0, or set such that it corresponds to a typical PDAC tumor burden at trial entry). In our baseline, $f_{res}$ = 0.05 (5\% of cells are inherently drug-resistant), meaning most tumors start largely sensitive. Other state variables in the model include drug concentrations in the tumor (if PK is explicitly modeled) and immune cell levels; for simplicity, many immune effects were captured in the $k_{immune}(t)$ term rather than by a separate T-cell ODE. The model does track some patient-specific attributes (e.g. presence of certain mutations or high stroma marker) as static flags that determine eligibility for drug effects (e.g. KRAS G12D = 1 in Arm C patients, $HA_{high}$ = 1 in Arm D patients, etc.).



\begin{figure}[H]
    \renewcommand\thefigure{2B}
    \centering
    \includegraphics[width=.65\linewidth]{images/Figure_2B.png}
    \vspace{0.05cm}
    \caption{Modular QSP model architecture: block diagram of drug-specific modules\\(chemo, targeted, immune) feeding into tumor cell compartments and toxicity}
    \label{2B}
\end{figure}
\vspace{-0.2cm}




\textbf{Spatial Structure:} To capture drug delivery and microenvironment heterogeneity, the tumor was discretized into a 3D grid of compartments (with linear dimension GRID\_SIZE, e.g. 5×5×5 = 125 compartments at GRID=5; also referred to as grid size). This acts as a simple spatial model: compartments at the periphery have higher drug exposure and immune cell infiltration, whereas core compartments may be hypoperfused or protected by stroma. Diffusion of drug and movement of immune cells between compartments were modeled (e.g. via diffusion terms or reduced $k_{chemo}$ in inner compartments). A stromal barrier factor was implemented such that high hyaluronan-expressing tumors ($HA_{high}$) have elevated interstitial pressure and poor drug penetration – effectively reducing chemo concentration deeper in the tumor. Arm D (pegvorhyaluronidase enzyme) transiently reduces this barrier, improving intra-tumoral drug penetration. Although we do not present the full PDE here, conceptually the model’s structure can be visualized in \autoref{2B}.

\begin{itemize}[leftmargin=1.6em]
\item \textbf{Tumor compartments (sensitive/resistant):} arranged spatially to simulate gradients in drug and oxygen. These compartments grow and die by the equations above.
\item \textbf{Chemotherapy module:} periodic dosing input → distribution into tumor compartments (limited by stroma) → kills sensitive tumor cells (modeled by the $k_{chemo}$ term).
\item \textbf{Targeted therapy module:} continuous dosing (pills) or periodic IV → systemic concentration → kills tumor cells carrying the target mutation (modeled by the $k_{target}$ term affecting those cells in eligible patients).
\item \textbf{Immune module:} baseline immune surveillance provides a small $k_{immune}$ kill. PD-1 inhibitor (Arm H) removes immune “brakes,” increasing $k_{immune}$; CD40 agonist (Arms E, H, I) provides an “accelerator” to immune activation, further raising $k_{immune}$. CD47 blocker (Arm B) increases macrophage-mediated kill (this is effectively folded into $k_{immune}$ as well). The net immune kill term is thus higher in arms with immunotherapies, leading to improved tumor clearance unless counteracted by other factors (e.g. if a patient’s tumor is non-immunogenic, the model reflects a very low baseline $k_{immune}$, so even PD-1/CD40 yield little effect – such variability was embedded in the virtual population).
\item \textbf{Toxicity module:} All drugs contribute to a composite toxicity score (based on known dose-limiting toxicities). This influences a patient’s probability of dropping out of treatment. For example, overlapping toxicities from three drugs (Arm E) can trigger early discontinuation in the simulation, which then stops the corresponding kill terms. Toxicity does not directly feed back on tumor cells in the model (except by stopping treatment), but it is tracked to compute safety endpoints and drop-out events.
\end{itemize}

