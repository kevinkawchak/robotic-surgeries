# README — Chunked Source for PDAC Digital Twin Paper

## Purpose

This repository contains the paper **"End-to-End Pancreatic Ductal Adenocarcinoma Digital Twin Clinical Trial Proposals"** by Kevin Kawchak (ChemicalQDevice, June 24, 2025) split into 10 markdown chunks. The original source files (`main.tex` + `references.bib`) have been faithfully transcribed into prose-friendly markdown without abbreviation, content removal, or added section headings. The chunked files are intended as input to Claude Code Opus 4.7 (1M context) for the downstream task of drafting a **new physical AI oncology trial paper**.

The chunking preserves every word of the source. LaTeX commands (`\hspace{1.3em}`, `\vspace`, `\textbf`, `\autoref`, `\cite`, `\\`, table-formatting macros, tcolorbox wrappers, TikZ process diagrams, etc.) have been converted to their plain-text or markdown equivalents — bold becomes `**bold**`, table cells become markdown table rows, citations become `[citekey]`, `\autoref{label}` becomes the plain label name (e.g. `MAsWordsMinutes`, `Report06_Verify`), and TikZ flow diagrams become arrow-separated text lines (e.g., "Dataset 1 → Gemini 2.5 Pro Preview → Web Search Literature → …"). Images are referenced by their original path in italics rather than embedded. No `.sty` files and no actual image binaries are included.

The 10 chunks split roughly along structural seams in the paper so that any single chunk can be loaded and reasoned over independently while still respecting the source's logical organization. Chunks 9 and 10 are the BibTeX entries in raw form (wrapped in code fences). The other 8 chunks are the paper body.

## File Manifest

| # | Filename | Source range (main.tex lines) | Approx. word count | What it contains |
|---|---|---|---|---|
| 01 | `01_front_matter_abstract.md` | 84–157 | ~720 | Title, author/affiliation, structured Abstract (Question / Findings / Design / Results / Importance / Conclusion), and the reference to the main pipeline figure (BigProcessPDAC.png) |
| 02 | `02_introduction_methods.md` | 160–243 | ~1,700 | Full Introduction (Clinical Trials & Digital Twins; Digital Twins in Oncology — Phesi NSCLC KRAS, Atlis Labs lung, Wu TNBC; PDAC Digital Twin Initiatives — Frederick, Molecular Twin, Genentech) and full Methods (Parts I–IV plus the 10-item AI Models software inventory) |
| 03 | `03_results_meta_analyses_reports.md` | 249–410 | ~1,400 | Results: Meta-Analyses narrative; the 40-row MAsWordsMinutes word/time table for o3re; Results: Reports narrative; the ReportsWordsMinutes word/time table for the six g25p reports and their verifications |
| 04 | `04_report_content_verification.md` | 419–791 | ~3,000 | The two Report tcolorbox excerpts shown verbatim in the paper: **Report 6 Page 1** (Executive Summary, Technical Details, Table 1 Virtual Patient Profiles ARCH-01..07, Table 2 Treatment Impact Parameters INT-01..10) and **Report 6 Page 2** (Table 3 State Transition & Event Dynamics EV-01..06, Sample Calculation for ARCH-04 + FOLFIRINOX, Key Insights). Also the full 47-row Report 6 Table 1 Verification table (preliminary accuracies) and the 7-row Report Summary Statistics |
| 05 | `05_five_proposals_top3_intro.md` | 811–1064 | ~1,800 | Results: Five Proposals narrative; ProposalsWordsMinutes and VerifyProposalsWordsMinutes tables; Average Scores Table across all judges (A–E) and the overall-average ranking; Results: Top 3 Proposals intro; ChatGPT o3-pro (Proposal A) commentary with the seven-archetype/ECOG reference; pull-quotes from Andrew and Zitu; figure captions for R1T23Drug_1 and R1T23Drug_2 (drug-combination TSVS visualizations) |
| 06 | `06_proposal_a_proposal_b_early.md` | 1077–1519 | ~3,800 | **Proposal A by o3pr** in full — Pages 1 & 2 (all 10 deliverables: Executive Summary, Scientific Objectives & Hypotheses table O1–O4, Virtual-Patient Cohort Construction, Digital-Twin Architecture layers A–E, V&V plan, Prospective DT Trial Protocol table, Regulatory & Ethical Alignment, 24-month Operational Roadmap & Budget = $17.8M, Risk Register, Milestones M6/M12/M18/M24). Plus the Opus 4 Extended commentary intro for Proposal B (with R6ECOG figure), then **Proposal B by ops4** Pages 1 & 2 (Executive Summary, Scientific Objectives H1–H3, Population Archetypes table of 10,000 virtual patients across 7 archetypes, Digital-Twin Architecture Layers 1–4 with data-flow ASCII diagram, V&V framework, VIRTUAL-PIONEER trial design start) |
| 07 | `07_proposal_b_late_comparison_discussion.md` | 1700–2179 | ~3,500 | **Proposal B by ops4** Pages 3 & 4 (Secondary Endpoints, Interim Analyses Bayesian framework, Adaptive Elements, Regulatory & Ethical Alignment, 4-phase Operational Roadmap, $8.5M Budget Summary, Risk Register, Milestones M1–M4, Transition Criteria). The Top 3 Proposals comparison figures (3Proposals1Timeline, 3Proposals2Radar, 3Proposals3FTE, 3Proposals4Budget). Full **Discussion** section. Full **Limitations and Future Work** section. Pull-quotes from Halbrook, Urooj, and Mukund |
| 08 | `08_data_availability_appendix.md` | 2205–4017 | ~6,400 | The **Data availability** lists for Parts I and II–IV (87 numbered supplementary items spanning Zenodo and GitHub references). The full **Appendix Dataset 1 verification table** (`40MAAnalysis`) — 40 rows of Author/Year/Trial/Phase/Dataset Value/Article Value/URL/Similarity/Score plus summary statistics. The complete **prompt templates** for Standards A (Prompts 01–10 and 11–40), B (Prompt 41), C (Prompts 42–44 and 45–47), D (Prompts 48–50 and 51–53), E (Prompts 54–62 visualization prompts), F (Prompt 63 — the master PDAC-DT-Architect proposal prompt), G (Prompt 64 — the proposal-judging prompt), H (Prompt 65 — judge-bias visualizations), I (Prompt 66 — judge-bias tables), and J (Prompt 67 — top-3 comparison visualizations). Plus Acknowledgments, Ethical disclosures, Rights and permissions, and About this study |
| 09 | `09_references_part1.md` | references.bib lines 1–310 | ~3,800 | First half of the BibTeX file as a fenced code block, with a brief lead-in describing which cite keys are inside. Covers: AI model citations (Claude family, ChatGPT family, Gemini family, Grok 3, Meta AI, GPT-4o), platforms (Google AI Studio, Colab, Docs, VS Code), Kawchak's prior works (`01Kawchak_Kevin_10Jul24` through `18KawchakPDAC` and the GitHub repos), foundational LLM/agent papers (LangChain, AutoGen, CrewAI, Sequoia, deep-research, prompt anatomy), and biopharmaceutical/bioprocess references |
| 10 | `10_references_part2.md` | references.bib lines 311–515 | ~3,200 | Second half of the BibTeX file as a fenced code block. Covers: cancer-specific LLM applications (breast, prostate, lung, liver, brain, pancreatic, multiple oncology decision-support papers), Gemini 2.0 Flash Thinking, DeepSeek-R1, context-length/inference survey papers, and the three thematic blocks that anchor the Introduction and the pull-quotes — **INTRODUCTION block** (`01IntroKatsoulakis` → `13IntroNSFNIHFDA`), **PAPER block** (`01PaperBehrouz` Titans memory paper), and **Quotes block** (`01QuoteHalbrook` → `08QuoteZitu`) |

## Notation & Conversion Conventions

A small, consistent set of LaTeX-to-markdown conventions was applied uniformly across every chunk so that downstream parsing is predictable:

- `\section{X}` and `\subsection{X}` → `# X` and `## X` at top of the relevant chunk, never invented elsewhere
- `\autoref{label}` → bare label name (e.g. `MAsWordsMinutes`, `Report06_Verify`, `StandardAa`, `40MAAnalysis`, `R1T23Drug_1`, `5ProposalsRadar`, `3Proposals1Timeline`). Use these labels to reconstruct cross-references between chunks
- `\cite{key1, key2}` → `[key1, key2]` matching keys in chunks 09/10
- `\textbf{...}` → `**...**`; `\textit{...}` → `*...*`
- Table environments (`\begin{tabular}`) and inline `\begin{tabular}` blocks → markdown pipe tables; `\makecell` newlines collapsed to single-cell space
- `tcolorbox` wrappers for Reports and Proposals → preserved as `## Report N Page M:` and `## Proposal X Page N:` headings with all interior content intact
- `\begin{tikzpicture}` process flow diagrams → arrow-separated text on a single line (e.g., "PDAC Trial Literature → ChatGPT o3 Research → Trial IDs OS/PFS → Methods Results → Conclusions Appendices → Dataset 1")
- `\includegraphics{...}` and `\caption{...}` → labeled figure stub line: `**Figure (LABEL):** caption text. [Image: path]`
- Math like `\raisebox{0.25ex}{\scalebox{0.7}{$\leq$}}` and Unicode glyphs (≤, ≥, τ², κ, β, Δ, μ, ≈) → preserved as Unicode in chunks 01–07 and downgraded to ASCII (`<=`, `>=`, `tau²`, `kappa`, `beta`, `Delta`, `mu`, `~`) only in chunk 08's Standard prompt blocks because bash heredoc parsing constraints required it; the meaning is unchanged
- Quotation marks: smart quotes from the source are preserved where possible
- Page breaks, `\vspace`, `\hspace`, `\minipage`, `\centering`, `\raggedright` and similar layout-only commands → silently dropped (they have no semantic content)

## How the Chunks Correlate to Each Other

The paper has a tight pipeline structure (meta-analyses → reports → proposals → verification), and the chunks reflect that flow. Cross-chunk dependencies that matter for reasoning:

**Pipeline backbone (Chunks 02 → 03 → 04 → 05 → 06 → 07):**
- Chunk 02 (Methods Parts I–IV) defines the seven AI model abbreviations (o3re, g25p, son4, grk3, o3pr, ops4, o3ch) used in every subsequent chunk
- Chunk 03 (MAsWordsMinutes table) reports the 40 meta-analyses that feed Dataset 1; those MA IDs (MA-01..MA-40) are quoted by name in Chunks 04, 05, 06, 07, and 08
- Chunk 04 contains the two key Report 6 tables that Proposal A explicitly imports — `ARCH-01..ARCH-07` and `INT-01..INT-10` appear in Chunk 06's Proposal A page 1 ("Seven archetypes from Report 6") and Proposal B's 10,000-virtual-patient cohort table
- Chunks 05–07 hold the proposal results: Chunk 05 introduces the five-proposal scoring (A=o3pr through E=grk3) and the radar/average tables; Chunks 06–07 reproduce Proposals A and B in full. Proposals C, D, and E are referenced but only summarized — Chunk 07's Discussion describes Proposal D's distinctive ROI strengths and Chunk 05's Average Scores Table reports all five proposals' four-metric scores

**Drug-combination thread (the central scientific finding):** *Daraxonrasib + Mitazalimab + Liposomal Irinotecan*, TSVS = 8.15 — this triplet appears in:
- Chunk 01 (Abstract Importance paragraph) — source attribution to MA-23, MA-15, and 8 MAs
- Chunk 03 (Reports narrative, paragraph beginning "Daraxonrasib + Mitazalimab + Liposomal Irinotecan")
- Chunk 05 (Top 3 Proposals intro, "had the highest predicted Therapeutic Synergy & Viability Score (TSVS) of 8.15 in Report 1 Table 2")
- Chunk 06 (Proposal A Executive Summary; Proposal B Executive Summary)
- Chunk 07 (Discussion paragraph "Each model used the correct three-drug combination")

**Verification-accuracy thread:**
- Chunk 03 introduces the report verification framework
- Chunk 04 holds the Report 6 Table 1 Verification (47 archetype data points, score 0.74 ± 0.20) and the Report Summary Statistics (Reports overall: 0.84 ± 0.18)
- Chunk 08 (`40MAAnalysis`) holds the meta-analysis verification table (40 trials, average score 0.95 ± 0.10) — this is the larger-scale verification that the Limitations section in Chunk 07 calls "preliminary"

**Prompts-to-outputs map:** Every numbered output in the paper has a Standard prompt template in Chunk 08:
- Prompts 01–40 (Standard A) → the 40 meta-analyses summarized in Chunk 03's table
- Prompt 41 (Standard B) → the `40MAAnalysis` table in Chunk 08 and the 95% accuracy figure
- Prompts 42–47 (Standard C) → Reports 01–06, whose content is partially shown in Chunk 04
- Prompts 48–53 (Standard D) → the six report verifications summarized in Chunk 03 and detailed for Report 6 in Chunk 04
- Prompts 54–62 (Standard E) → the report visualization charts referenced by figure label in Chunks 04 and 05
- Prompt 63 (Standard F) → produced Proposals A–E in Chunks 06 and 07
- Prompt 64 (Standard G) → produced the judging table reported in Chunk 05
- Prompts 65, 66 (Standards H, I) → produced the radar/judge-bias visualizations and tables referenced in Chunk 05
- Prompt 67 (Standard J) → produced the top-3 comparison charts in Chunk 07

**Citation closure:** Every `[citekey]` token in Chunks 01–08 resolves to an entry in either Chunk 09 or Chunk 10:
- AI model identification (e.g. `ChatGPTo3`, `Sonnet4`, `Grok3`, `Gemini25ProPreview0605`) → **Chunk 09**
- Author prior works (`15KawchakAgent`, `16KawchakLung`, `17KawchakGlioblastoma`, `18KawchakPDAC`) → **Chunk 09**
- Intro digital-twin literature (`02IntroPhesi`, `04IntroAltislabs`, `05IntroWu`, `06IntroBordukova`, `08IntroFrederick`, `10IntroOsipov`, `11IntroJoslyn`, `12IntroNSFNIHFDA`, etc.) → **Chunk 10**
- Pull-quote attributions (`01QuoteHalbrook`, `02QuoteMukund`, `03QuoteUrooj`, `04QuoteStallard`, `05QuoteTempero`, `06QuotePanCan`, `07QuoteAndrew`, `08QuoteZitu`) → **Chunk 10**
- Long-context recall claim about g25p (`01PaperBehrouz`, Titans paper) → **Chunk 10**
- Software/platform refs (`GoogleColab`, `GoogleDocs`, `Visual_Studio_Code`, `Google_AI_Studio`, `MetaAI`) → **Chunk 09**
- GitHub repos for code (`GitHub24Jun25`) → **Chunk 09**

## Suggested Reading Order for the Downstream Task

For Claude Code Opus 4.7 drafting a **new physical AI oncology trial paper**, an efficient pass order is:

1. **Chunk 01** — get the structured-abstract template (Question/Findings/Design/Results/Importance/Conclusion) and the headline metrics
2. **Chunk 02** — internalize the seven-model framework and the four-part methods structure; this is the closest thing to a methodological blueprint
3. **Chunk 08** — read Standards A–J in order; these are the reusable prompt templates that drove every output in the source paper. For a physical AI oncology paper, Standards A (meta-analysis), C (report), F (proposal generation), and G (proposal judging) are the most directly portable
4. **Chunks 03, 05, 07** — the narrative results and discussion: how the source paper reports its metrics tables, ranks proposals, and articulates limitations. Reuse the table layouts and the rhetorical structure
5. **Chunks 04, 06** — the actual filled-in report and proposal content. Use these as worked examples of what a complete digital-twin proposal looks like at the deliverable-by-deliverable level. The "Why this matters" pattern after each technical section is reusable for non-technical investor framing
6. **Chunks 09, 10** — reference vocabulary. The intro-block citations are the canonical literature on digital twins in oncology and should be cited (or replaced with their physical-AI analogues) in any successor paper

## Source

Original paper: Kawchak K. *End-to-End Pancreatic Ductal Adenocarcinoma Digital Twin Clinical Trial AI Proposals.* Zenodo. 2025; DOI 10.5281/zenodo.15735068. CC BY 4.0.

Template: PRIMEarxiv (Perception, Robotics and Intelligent Machines group, Université de Moncton), adapted by Moulay Akhloufi from George Kour's arxiv-style (MIT License).
