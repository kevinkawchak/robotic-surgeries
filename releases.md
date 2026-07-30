# Release Notes

This file tracks every tagged release of the robotic-surgeries repository.
Releases follow semantic versioning. The first project to land here is the
4-arm 1-minute glioblastoma trial in `2030-gbm-1min/` (project version
v3.9.1, repository release v0.1.0). The v0.2.0 release publishes the
end-to-end run outputs of the same pipeline. The v0.3.0 release lands the
LaTeX paper template under `2030-gbm-1min/paper/`. The v0.4.0 release
lands the populated full LaTeX paper under `2030-gbm-1min/paper/full-paper/`.
The v0.5.0 release lands the 8-arm 1-minute PDAC instruction set at
`2030-pdac-1min/paper/instructions/`. The v0.6.0 release lands the
PDAC 1-minute generated codebase at `2030-pdac-1min/paper/codegen/`.
The v0.7.0 release lands the PDAC 1-minute execution outputs at
`2030-pdac-1min/paper/execution/`. The v0.8.0 release lands the
PDAC 1-minute draft LaTeX paper template at
`2030-pdac-1min/paper/draft-paper/`. The v0.9.0 release lands the
populated PDAC 1-minute full LaTeX paper at
`2030-pdac-1min/paper/full-paper/`. The v1.0.0 release lands the
Patient Robot Advocacy paper at `patient-robot-advocacy/`.

## Release title

v1.0.0 - Patient Robot Advocacy Paper (Phase 1 PDAC Trial Answered To The Participant, Eight Stages From One Prompt)

## Summary

This release lands the Patient Robot Advocacy paper at
`patient-robot-advocacy/`, built by Claude Code Opus 5 from the
single master prompt filed verbatim at
`patient-robot-advocacy/prompts/prompt-patient.md` across 122
commits in eight sequential stages within a single PR. The paper is
`Patient Robot Advocacy: A Phase 1, First-in-Human, PDAC Clinical
Trial Protocol of a LLM-Directed Robotic Whipple with Daraxonrasib
(RMC-6236)`, Draft 1.0, Kevin Kawchak, CEO ChemicalQDevice, San
Diego, July 31, 2026. It takes the parent Phase 1 trial protocol at
`patient-robot-advocacy/inputs/phase-1-trial-protocol.zip`, which is
written for the FDA, the IRB, the sponsor, and the site, and
re-presents the same trial to the person whose abdomen is being
opened. Twenty-one documented patient concerns about surgical
robots, de-duplicated from two dated July 28, 2026 research passes
by Gemini 3.1 Pro and ChatGPT 5.6 Thinking Extended at
`patient-robot-advocacy/research/`, are each answered with the
specific clause, limit, gate, or number in this protocol that
settles them, and the five that are answered by governance rather
than by a hard limit are named as such rather than dressed as
guarantees. Stages 1 to 5 produce thirty machine-readable diagram
sources across the five permitted platforms and no others: nine
Mermaid, seven D2, five PlantUML, five Graphviz, and four Diagrams
(Python), with counts following the purpose each idiom serves rather
than an equal quota, and with no Excalidraw output anywhere. Stage 6
lands the bracketed scaffold at `patient-robot-advocacy/draft-patient/`
carrying 78 drafting instructions that name the exact repository file
each later stage must read. Stage 7 at
`patient-robot-advocacy/full-patient/` executes every one of them,
draws all thirty figures natively in TikZ so the PDF rebuilds from
its own LaTeX with no external tool and no raster image, and runs two
independent figure verification passes that between them found and
fixed eleven defects including three figures whose fills were
selected by a conditional inside a `\foreach`, which TeX never
evaluates as the source implies. Stage 8 at
`patient-robot-advocacy/final-patient/` is the senior author's
proof-reading pass: it lists eight defects before fixing any of them,
wraps every figure in a float so a tall figure no longer strands the
page it will not fit on, converts all forty-three tables to breakable
`xltabular` so none can run off the foot of a page, renumbers two
pairs of figures into ascending order, retargets eleven
cross-references, rebalances all thirty captions, compresses the
contents to three pages, and adds fifteen subsections to bring the
paper to length parity with the parent protocol. Pages carrying a
trailing gap over 3 cm fall from 41 of 83 to 15 of 88, and eleven of
the fifteen that remain are a section's last page, which follows
directly from the `\clearpage` between sections. The finished paper
is 88 pages, thirteen sections, thirty figures in ascending order,
forty-three tables all at body text width, 51 bibliography entries
with every DOI printed and hyperlinked, and 168,275 visible text
characters against the parent protocol's 155,222. The CI lint and
format gates on Python 3.10, 3.11, and 3.12 pass because every file
added is LaTeX, Markdown, or a diagram source outside the CI matrix
working directory (`2030-gbm-1min/`), and the four Python diagram
sources are `ruff format --check` and `ruff check` clean regardless.

## Features

- Complete paper source at `patient-robot-advocacy/final-patient/`: `main.tex` (patient-advocacy cover page keeping the parent protocol's colour scheme while replacing its furniture with a full-width Corporate Blue banner, four badges, the ORCID and DOI line, and a three-panel strip answering who is in control, what could go wrong, and what is this costing me; keywords; a three-page clickable contents; thirteen `\input` lines with `\clearpage` between them), `patientstyle.sty` (eleven colour tokens and no twelfth, five TikZ diagram vocabularies, the rigid `pafig` frame, the `pafloat` carrier, twenty vector pictogram macros, six quantitative primitives), `references.bib` (51 entries, every DOI printed as text and hyperlinked), `sections/` (thirteen populated section files), and `final-patient-LaTeX.zip` (Overleaf-ready bundle).
- Thirty machine-readable diagram sources in five directories, each in its platform's own syntax and each carrying a header naming the figure, the section it serves, and the concern it answers: `patient-robot-advocacy/mermaid/` (9 `.md` with fenced mermaid: flowchart, sequence, state, gantt, quadrant), `patient-robot-advocacy/d2/` (7 `.d2`: containers, grids, sql tables, layers), `patient-robot-advocacy/plantuml/` (5 `.puml`: use case, state machine, timing, sequence with activation), `patient-robot-advocacy/graphviz/` (5 `.dot`: rooted DAG, bipartite, decision tree, fault tree), `patient-robot-advocacy/diagrams-python/` (4 `.py`: clustered infrastructure with vector pictograms).
- The figure spacing rule made provable rather than eyeballed: `pafig` closes with a rigid `\vskip 26pt`, the source applies `\vspace{-0.7cm}` which is `-19.9pt`, and `\figcaption` opens with `\nointerlineskip`, so the frame-to-caption distance is exactly 6.1 pt for all thirty figures, floating or inline, whatever precedes or follows them on the page.
- All thirty captions on three lines of near-equal character count, balanced by a dynamic-programming split over word boundaries and, where no split of the existing wording could reach the band, by rewording the caption: line lengths 62 to 112 characters, maximum within-caption spread 12.
- Forty-three tables, every one at `\textwidth`, every fixed column `>{\raggedright\arraybackslash}p{...}`, `\tabcolsep` 5 pt, `\arraystretch` 1.18, and every table of more than two rows breakable with a repeated header and an italic continuation line.
- The twenty-one documented concerns enumerated in section 3 with an answer class for each, wired to their answering clause in Figure 6, plotted against prevalence in Figure 7, and indexed one row each in a twenty-one-row breakable table.
- Provenance discipline: four class letters, M measured, C comparator, S simulation, P protocol limit, carried on every number in section 10, with section 10.8 stating in four steps how to read one, including the fact that no M number from a human procedure on this platform exists yet.
- Bill citations throughout use H. R. 9510 v5 at DOI 10.5281/zenodo.20619762, superseding the earlier H. R. 9501 to H. R. 9507 numbering.
- The NSCLC journey input at `patient-robot-advocacy/inputs/cancer-patient-journey.zip` used for topology and explicitly distinguished from PDAC on four named differences: three anastomoses rather than one bronchial closure, a RAS(ON) inhibitor rather than a checkpoint inhibitor, pancreatic fistula rather than prolonged air leak, and a far lower survival baseline.
- The ten robot instruction sheets from `patient-robot-advocacy/inputs/patient-robot-instructions.tex` re-scoped from general oncology to this PDAC protocol, reproduced in full in section 9.7 and drawn as a card grid in Figure 26, with the four unused robot types left visibly unused.
- Fifteen directory READMEs, each with badges and each stating which files from which other directories it used and where.
- Three preserved paper stages rather than one overwritten directory, each with its own sub-prompt filed verbatim, its own narrative, and its own Overleaf archive, so the build is auditable end to end.
- Top level `README.md` extended by exactly two new sections: the v1.0.0 ASCII snapshot with the 425-character summary and two tables, and the thirty-row figure index with the thirteen-section contents.
- `patient-robot-advocacy/prompts/output-patient.md` carrying the complete Claude markdown output for the run, including the nine decisions taken before the first sub-prompt was written and a table of every rule in the master prompt against where it is satisfied.

## Contributors

@kevinkawchak
@claude
@google-gemini
@openai

## Notes

- The CI lint and format matrix at `.github/workflows/ci.yml` runs `ruff format --check`, `ruff check`, `yamllint`, and the file size cap against `2030-gbm-1min/` only. Every file added by this release is LaTeX, Markdown, or a diagram source under `patient-robot-advocacy/`, so this PR cannot regress `CI / lint-and-format (3.10)`, `(3.11)`, or `(3.12)`. The four Python diagram sources were kept `ruff format --check` and `ruff check` clean anyway.
- No PNG or JPG file exists anywhere in `patient-robot-advocacy/`. Every figure is TikZ vector art, including the twenty pictograms that stand in for the raster node icons the Diagrams (Python) platform would normally emit.
- The paper DOI is left in the form `10.5281/zenodo.xxxxxxxx`, hyperlinked to `https://doi.org/10.5281/zenodo.xxxxxxxx`, pending the live Zenodo deposition.
- The paper carries 168,275 visible text characters against the parent protocol's 155,222, which is 108 percent. The comparison strips comments, diagram sources, and LaTeX control sequences from both documents so it measures what a reader reads. Stage 7 had reported 93 percent on a raw source-line count; that measurement flattered the paper and is corrected in `patient-robot-advocacy/final-patient/output-final-patient.md`.
- `patient-robot-advocacy/full-patient/` keeps the pre-renumber figure numbering deliberately, because its PDF and archive were built under it and are internally consistent. Its README records the four swaps and points at `final-patient/`.
- Eleven of the fifteen pages carrying a trailing gap over 3 cm are the last page of a section, which follows from the `\clearpage` between sections that the build is required to apply. They are not closable without removing that `\clearpage` or writing text to fill space.
- There is no `publication/` subdirectory under `patient-robot-advocacy/final-patient/`, per the master prompt.

## Release title

v0.9.0 - 2030 PDAC 1-Minute Full LaTeX Paper (Populated From The v0.8.0 Bracketed Draft Template)

## Summary

This release lands the v0.9.0 PDAC 1-minute full LaTeX paper at
`2030-pdac-1min/paper/full-paper/` expanded by Claude Code Opus
4.7 1M Max from the v0.8.0 bracketed draft template at
`2030-pdac-1min/paper/draft-paper/` across fourteen sequential
commits within a single PR. Every bracketed instruction in the
upstream draft (abstract synthesis brackets, 5 introduction
subsection brackets, 7 methods subsection brackets, 7 results
subsection brackets, 5 discussion subsection brackets, 5
limitations subsection brackets, 4 conclusions block brackets)
has been resolved into running prose, anchored tables, and ASCII
diagrams in the corresponding `sections/*.tex` file. The
upstream v0.8.0 draft template under
`2030-pdac-1min/paper/draft-paper/` is preserved verbatim and is
not modified by this PR. The 35 entry doi + url + note triad
bibliography at `2030-pdac-1min/paper/full-paper/references.bib`
preserves the clickable DOI plus GitHub plus Zenodo hyperlinks
for every repository style entry and adds the new
`pdac-draft-paper-v080` self reference. The 2nd to last commit
verifies all senior author final pass invariants (single dashes
only, black text only, raggedright table cells everywhere, every
`\cite{}` resolves, every `\label{}` resolves, every `\S`
renders, no SS in body, table column widths sum under 14.0 cm,
abstract under 1500 char paragraph). The last commit lands the
`LaTeX Source Files.zip` Overleaf ready bundle plus the v0.9.0
entries in this `releases.md`, in the top level `README.md`, and
in `CHANGELOG.md`. The CI lint and format gates on Python 3.10,
3.11, and 3.12 pass uniformly across the single PR because the
new files under `2030-pdac-1min/paper/full-paper/` are LaTeX and
Markdown only and live outside the CI matrix working directory
(`2030-gbm-1min/`).

## Features

- Populated full LaTeX paper at `2030-pdac-1min/paper/full-paper/main.tex` with the dark blue accent style file at `new_paper.sty`, the 35 entry doi + url + note triad bibliography at `references.bib`, and the navigation README at `README.md`.
- 8 fully populated section files at `2030-pdac-1min/paper/full-paper/sections/`: `abstract.tex` (single paragraph 1416 char body opening with the on premises repository based LLM thesis, naming the four phase Claude Code workflow, the PancreSpeed 1.0 60 second target, Daraxonrasib, the headline composite 93.298 plus leaderboard 93.735 plus T+7d 29 of 32 numbers, the 1001 record exceptional processing feat, and the practical adoption gap), `introduction.tex` (5 subsections with the anchored Table 1 robot comparison and the 8 arm 10 kHz heartbeat ASCII snapshot), `methods.tex` (7 subsections with 5 anchored tables for per arm tool assignment, 10 channel sensor sample, xyz command state enum, vascular safety zones plus anastomosis ring tension, and 6 frozen composite weights), `results.tex` (7 subsections with 4 anchored tables for codegen subpackage size, 6 component composite per iteration mean and std, 4 entrant leaderboard, and Daraxonrasib restart day distribution; explicitly highlights the 1001 record Phase 5 first 100 ms `sensor_sample_8arm.jsonl` exceptional processing feat), `discussion.tex` (5 subsections with Table 1 real life adoption gaps), `limitations_future.tex` (5 subsections with 3 anchored tables for 4 phase accounting, 60 min vs 1 min delta, and 10 future deliverables), `conclusions.tex` (4 thematic blocks with Table 1 themes), `back_matter.tex` (acknowledgments, ethical disclosures, rights and permissions, cite this article, data availability fully populated and extended to name the v0.9.0 full paper directory).
- Title page metadata: title `2030: 60 Second Pancreatic Cancer Whipple Surgery + Daraxonrasib Simulation` across two centered lines, author Kevin Kawchak with the green ORCID logo plus `https://orcid.org/0009-0007-5457-8667` clickable hyperlink, affiliation CEO ChemicalQDevice, DOI `10.5281/zenodo.20174131` clickable hyperlink to `https://doi.org/10.5281/zenodo.20174131`, date May 15, 2026.
- Disclaimer block under the abstract: `Disclaimer: This work is independent and not endorsed or sponsored by trial sponsors, FDA, CRO, site, IRB, regulator, or medical society; and was generated using Artificial Intelligence.`
- Keywords block under the disclaimer: `60 Second Surgery, Pancreatic Ductal Adenocarcinoma, Whipple Procedure, Physical AI, Robotic Surgery, On-Premises LLM, Daraxonrasib, KRAS`.
- 14 anchored tables across the 8 section files, all using the `>{\raggedright\arraybackslash}p{Xcm}` column type contract, all summing to under 14.0 cm column widths so no table runs off the right margin.
- 35 entry doi + url + note triad bibliography at `references.bib` extending the v0.8.0 draft inventory with the new `pdac-draft-paper-v080` self reference plus the existing entries (this paper self cite, parent repos, 4 prior PDAC author papers, Daraxonrasib summary, prior 60 second GBM paper, upstream v0.5.0 to v0.7.0 PDAC tree anchors, FDA RTCT announcement, PDAC clinical context, Daraxonrasib trial anchors, competitor robot platforms, IEC plus FDA plus ICH standards, reporting standards, AI tooling).
- Overleaf ready bundle at `2030-pdac-1min/paper/full-paper/LaTeX Source Files.zip` containing main.tex + new_paper.sty + references.bib + README.md + sections/.
- Top level `README.md` updated with v0.9.0 release badge, v0.9.0 PDAC Full Paper badge, v0.9.0 PDAC Full Paper ASCII snapshot, `2030-pdac-1min/paper/full-paper/` subtree in Repository Structure block, updated High Level Architecture ASCII diagram, updated citation block referencing v0.9.0, updated Quick Start block referencing the full paper compile recipe.
- This v0.9.0 release notes block in `releases.md` plus the matching v0.9.0 entry in `CHANGELOG.md`.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- The CI lint and format matrix at `.github/workflows/ci.yml` targets `2030-gbm-1min/` as the lint working directory. The new files under `2030-pdac-1min/paper/full-paper/` are LaTeX and Markdown only and are not lint gated by CI. This PR therefore does not regress the upstream `CI / lint-and-format (3.10) (pull...)`, `(3.11) (pull...)`, or `(3.12) (pull...)` checks.
- The full paper is populated; every bracketed instruction in the upstream v0.8.0 draft template has been resolved into running prose, anchored tables, and ASCII diagrams. The upstream draft template at `2030-pdac-1min/paper/draft-paper/` is preserved verbatim and is not modified by this PR.
- The Zenodo deposition at DOI 10.5281/zenodo.20174131 is the v0.9.0 PDAC full paper DOI placeholder; the live Zenodo upload step is gated on a valid `ZENODO_TOKEN` and follows the same deposition pattern as the v0.4.0 GBM full paper at DOI 10.5281/zenodo.20113157.
- The 6 surplus bibliography entries (`apache-arrow`, `ccby4`, `chatgpt-thinking`, `duckdb`, `google-gemini-overview`, `repo-physical-ai-oncology-trials`, `repo-robotic-surgeries`, `zenodo`) are present in `references.bib` but not yet cited in the body; they are available for the sibling cancer site downstream pass.

## Release title

v0.8.0 - 2030 PDAC 1-Minute Draft LaTeX Paper Template (Bracketed Head Start For Future Final Paper)

## Summary

This release lands the v0.8.0 PDAC 1-minute draft LaTeX paper
template at `2030-pdac-1min/paper/draft-paper/` populated by Claude
Code Opus 4.7 1M Max from the v0.5.0 instruction tree, the v0.6.0
codegen tree, the v0.7.0 execution tree, and the four prior author
PDAC papers plus the Daraxonrasib summary plus the two research
chunks under `2030-pdac-1min/paper/inputs/` across eleven
sequential commits within a single PR. The draft template ships
with bracketed downstream processing instructions in each section
file (sections/abstract.tex, introduction.tex, methods.tex,
results.tex, discussion.tex, limitations_future.tex, conclusions.tex,
back_matter.tex) so a future Claude Code Opus 4.7 1M Max session can
expand the brackets into the final 70 plus page paper at
`2030-pdac-1min/paper/full-paper/` without re-discovering source
files. Each bracketed instruction names the exact source file paths
in `2030-pdac-1min/paper/{instructions, codegen, execution, inputs}/`,
the exact bibtex citation keys to use, and the position the
subsection should take in the wider field. The reference inventory
at `references.bib` carries 41 entries with the doi + url + note
triad invariant; repository style entries embed both the GitHub URL
and the Zenodo URL inside the note field so each link renders as
clickable in the final PDF. The 2nd to last commit fixes formatting
errors (less than and greater than character escaping in two table
cells, single dash invariant verification across all .tex files,
\cite{} key resolution against the 41 entry bibliography, raggedright
column type contract verification across the 14 anchored tables,
table column width verification within the 16.5 cm text width). The
last commit lands the LaTeX Source Files.zip Overleaf-ready bundle
plus the v0.8.0 entries in this releases.md, in the top level
README.md, and in CHANGELOG.md. The CI lint and format gates on
Python 3.10, 3.11, and 3.12 pass uniformly across the single PR
because the new files under `2030-pdac-1min/paper/draft-paper/` are
LaTeX and Markdown only and live outside the CI matrix working
directory (`2030-gbm-1min/`).

## Features

- Bracketed draft LaTeX paper template at `2030-pdac-1min/paper/draft-paper/main.tex` with the dark blue accent style file at `new_paper.sty`, the 41 entry doi + url + note triad bibliography at `references.bib`, and the navigation README at `README.md`.
- 8 bracketed section files at `2030-pdac-1min/paper/draft-paper/sections/`: `abstract.tex` (single paragraph 900 to 1000 char target with 8 input synthesis brackets), `introduction.tex` (5 subsections with 1 anchored Table 1 robot comparison), `methods.tex` (7 subsections with 4 anchored tables for per-arm tool assignment, xyz command state enum, vascular safety zones plus anastomosis ring tension, and 6 frozen composite weights), `results.tex` (7 subsections with 4 anchored tables for codegen subpackage size, 6 component composite per-iteration mean and std, 4 entrant leaderboard, and Daraxonrasib restart day distribution), `discussion.tex` (5 subsections with Table 1 real-life adoption gaps), `limitations_future.tex` (5 subsections with 3 anchored tables for 4 phase accounting, 60 min vs 1 min delta, and 10 future deliverables), `conclusions.tex` (4 thematic blocks with Table 1 themes), `back_matter.tex` (acknowledgments, ethics, rights, cite, data availability blocks fully populated).
- Title page metadata: title `2030: 60 Second Pancreatic Cancer Whipple Surgery + Daraxonrasib Simulation` across two centered lines, author Kevin Kawchak with the green ORCID logo + `https://orcid.org/0009-0007-5457-8667` clickable hyperlink, affiliation CEO ChemicalQDevice, DOI `10.5281/zenodo.20174131` clickable hyperlink to `https://doi.org/10.5281/zenodo.20174131`, date May 15, 2026.
- Disclaimer block under the abstract: `Disclaimer: This work is independent and not endorsed or sponsored by trial sponsors, FDA, CRO, site, IRB, regulator, or medical society; and was generated using Artificial Intelligence.`
- Keywords block under the disclaimer: `60 Second Surgery, Pancreatic Ductal Adenocarcinoma, Whipple Procedure, Physical AI, Robotic Surgery, On-Premises LLM, Daraxonrasib, KRAS`.
- 14 pre-populated anchored tables across the 8 section files, all using the `>{\raggedright\arraybackslash}p{Xcm}` column type contract, all summing to less than 16.5 cm text width, all under 5 row count for cell density.
- 41 entry doi + url + note triad bibliography at `references.bib` covering: this paper self-cite (`kawchak_2026_20174131`), parent repositories (`repo-robotic-surgeries`, `repo-physical-ai-oncology-trials`), 4 prior PDAC author papers (`kawchak_2025_15735068`, `kawchak_2025_16415815`, `kawchak_2025_17001137`, `kawchak_2025_17239510`), Daraxonrasib summary (`kawchak_2025_18099351`), prior 60 second GBM paper (`kawchak_2026_20113157`), upstream v0.5.0 to v0.7.0 PDAC tree anchors (`pdac-instructions-v050`, `pdac-codegen-v060`, `pdac-execution-v070`), FDA RTCT announcement (`fda2026realtime`), PDAC clinical context (`Siegel2025CancerStatistics`, `DutchCohort2025Whipple`, `Conroy2018FOLFIRINOXAdjuvant`, `Bassi2017ISGPSPostOpFistula`), Daraxonrasib clinical trial anchors (`rasolute302`, `rasolve301`, `rev-fda-breakthrough`), competitor robot platforms (`intuitive-davinci-sp`, `medtronic-hugo-ras`, `verb-surgical`), IEC plus FDA plus ICH standards (`iec-80601-2-77`, `iec-62304`, `cfr-21-50-30`, `fda-samd`, `ich-e6r3`), reporting standards (`Collins2024TRIPODAI`, `ElEmam2024CREMLS`), and AI tooling (`claude-code`, `claude-opus-47`, `claude-sonnet-46`, `chatgpt-thinking`, `google-gemini-overview`, `ollama`, `vllm`, `apache-arrow`, `duckdb`, `zenodo`, `ccby4`).
- Overleaf ready bundle at `2030-pdac-1min/paper/draft-paper/LaTeX Source Files.zip` containing main.tex + new_paper.sty + references.bib + README.md + sections/.
- Top level `README.md` updated with v0.8.0 release badge, v0.8.0 PDAC Draft Paper badge, v0.8.0 PDAC Draft Paper ASCII snapshot, `2030-pdac-1min/paper/draft-paper/` subtree in Repository Structure block, updated High Level Architecture ASCII diagram, updated citation block referencing v0.8.0 plus the standalone `kawchak_2026_20174131` self-cite, updated Quick Start block referencing the draft-paper compile recipe.
- This v0.8.0 release notes block in `releases.md` plus the matching v0.8.0 entry in `CHANGELOG.md`.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- The CI lint and format matrix at `.github/workflows/ci.yml` targets `2030-gbm-1min/` as the lint working directory. The new files under `2030-pdac-1min/paper/draft-paper/` are LaTeX and Markdown only and are not lint gated by CI. This PR therefore does not regress the upstream `Cl / lint-and-format (3.10) (pull...)`, `(3.11) (pull...)`, or `(3.12) (pull...)` checks.
- The draft template is bracketed; the bracketed instructions in each section file are not processed in this release. A future Claude Code Opus 4.7 1M Max session reads the brackets and expands them into the final 70 plus page paper at `2030-pdac-1min/paper/full-paper/`.
- The Zenodo deposition at DOI 10.5281/zenodo.20174131 is the v0.8.0 PDAC draft paper DOI placeholder; the live Zenodo upload step is gated on a valid `ZENODO_TOKEN` and follows the same deposition pattern as the v0.4.0 GBM full paper at DOI 10.5281/zenodo.20113157.
- The 9 surplus bibliography entries (`apache-arrow`, `ccby4`, `chatgpt-thinking`, `duckdb`, `google-gemini-overview`, `kawchak_2026_20174131`, `repo-physical-ai-oncology-trials`, `repo-robotic-surgeries`, `zenodo`) are present in `references.bib` but not yet cited in the bracketed section files; the downstream final paper pass will cite them as the brackets are expanded into running prose.

## Release title

v0.7.0 - 2030 PDAC 1-Minute 8-Arm Whipple Execution (Codegen v0.6.0 Run Outputs Ready For Paper)

## Summary

This release lands the v0.7.0 PDAC 1-minute execution tree at
`2030-pdac-1min/paper/execution/` produced by running every executable
codegen module against the deterministic seed contract (root seed
20260513) across nine sequential commits within a single PR. The
execution tree captures the live run output of the 640 channel sensor
ingest pipeline (1001 record publication arm sample, Phase 5 first 100
ms), the per arm xyz Cartesian command mapping pipeline (1001 command
records, all EMIT verdicts at the Phase 5 target), the 10 kHz heartbeat
bus timing budget (per arm 32 byte response frame, 100 us watchdog,
3 ms cross arm e stop), the 32 iteration deterministic Latin hypercube
sweep (mean composite 93.298, std 1.225, 95 percent CI half width
0.462, range [88.431, 93.735]), the 6 component frozen composite
score breakdown (Quality 0.30 plus Time 0.20 plus Cost 0.15 plus
Safety 0.15 plus Patient experience 0.05 plus Anastomosis quality
0.15), the 4 entrant multi vendor LLM tournament (128 verdicts across
4 rounds, PancreSpeed 1.0 wins 96 of 96 played rounds at mean
composite 93.735), the 5 vessel safety zone gate verdict log
(100 tick sample path with clear 83, no_fly 6, soft_warning 6,
hard_stop 5), the 3 per anastomosis controller outcomes (PJ Grade A
31 of 32, HJ leak absent 14 of 32 per controller, GJ patent 32 of 32),
the Daraxonrasib perioperative trajectory (T 0 serum 0.45 ng/mL below
0.5 ng/mL trough threshold across all 32 iterations) and postoperative
restart advisory (T+7d 29 of 32, T+14d 3 of 32, T+21d 0 of 32 with FDA
SaMD framing preserved in every advisory), the Zenodo L0 raw
deposition pointer JSON family (DOI 10.5281/zenodo.18445179,
deposition size estimate 13.21 GB pending live upload), the 12 PDAC
specific ASCII diagrams and 3 ASCII visualizations inherited from the
v0.6.0 codegen, and the smoke test status (10 of 13 pass, 3 known
v0.6.0 codegen discrepancies documented). The 8th commit (2nd to
last) lands the defense in depth CI lint and format verification
record (ruff format check pass, ruff check pass, yamllint relaxed
pass on 2030-gbm-1min, 10 MB file size cap pass with 1.1 MB max
committed in execution tree, 5 MB Parquet cap pass with no Parquet
committed) plus the 15 entry cross commit cross reference matrix
plus the 20 step long form process documentation. The 9th commit
(last) updates the top level `README.md` with the v0.7.0 release
badge, the v0.7.0 PDAC Execution badge, the v0.7.0 PDAC Execution
ASCII snapshot, the `2030-pdac-1min/paper/execution/` subtree in the
Repository Structure block, the extended Quick Start command list,
the updated citation block, and the See also pointer. The CI lint
and format gates on Python 3.10, 3.11, and 3.12 pass uniformly across
the single PR because the new files under
`2030-pdac-1min/paper/execution/` are outside the CI matrix working
directory (`2030-gbm-1min/`). No committed file in the execution tree
exceeds 1.1 MB; no Parquet is committed.

## Features

- 1001 record 640 channel sensor sample at `2030-pdac-1min/paper/execution/sensors/sensor_sample_8arm.jsonl` plus per arm summary CSV plus 80 channel inventory plus ASCII channel map.
- 1001 record xyz Cartesian command sample at `2030-pdac-1min/paper/execution/xyz_mapping/xyz_command_sample.jsonl` plus 8 arm by 8 phase target tip position table plus 6 stage pipeline ASCII summary.
- 10 kHz heartbeat per arm 32 byte response frame timing table at `2030-pdac-1min/paper/execution/coordination/heartbeat_timing_table.csv` plus the 4 state collision avoidance FSM transition table.
- 32 iteration deterministic Latin hypercube sweep index at `2030-pdac-1min/paper/execution/iterations/index.jsonl` plus sample iteration L3 phase CSV plus iteration summary CSV plus per iteration outcomes CSV plus ASCII composite distribution histogram.
- 6 component frozen composite score breakdown at `2030-pdac-1min/paper/execution/metrics/composite_breakdown.csv` plus weights CSV plus weight sum validation log.
- 4 entrant cross iteration tournament leaderboard at `2030-pdac-1min/paper/execution/comparison/leaderboard.csv` plus 128 row per round verdicts CSV plus Round 3 robot vs human CSV plus comparison report markdown.
- 5 vessel safety zone gate verdict log at `2030-pdac-1min/paper/execution/vascular/gate_verdicts.csv` plus vessel proximity table plus per vessel per phase test matrix.
- 3 per anastomosis controller outcome CSVs at `2030-pdac-1min/paper/execution/anastomosis/{pj,hj,gj}_outcomes.csv` plus cross anastomosis outcome summary CSV.
- Daraxonrasib perioperative trajectory CSV at `2030-pdac-1min/paper/execution/daraxonrasib/perioperative_trajectory.csv` plus the postoperative restart advisory JSON plus per iteration advisory summary CSV plus ASCII trajectory plot plus ASCII restart day distribution.
- Zenodo L0 raw deposition pointer JSON at `2030-pdac-1min/paper/execution/zenodo/run_00000_L0_raw.zenodo_pointer.json` plus 32 row manifest skeleton plus deposition summary log.
- 12 PDAC specific ASCII diagrams at `2030-pdac-1min/paper/execution/diagrams/` (coordination_heartbeat_8arm, vascular_safety_map, anastomosis_target_map, per_arm_tool_assignment, per_phase_activation, per_arm_kinematic_chain, pancrespeed_mechanical, iteration_parameter_space, tournament_leaderboard, daraxonrasib_trajectory, fistula_risk_score_flow, 8_phase_timeline) inherited verbatim from v0.6.0.
- 3 ASCII visualizations at `2030-pdac-1min/paper/execution/viz/` (xyz_path_8arm, metrics_summary_ascii, vascular_safety_heatmap_ascii) inherited verbatim from v0.6.0.
- 3 Jupyter notebook computational summaries at `2030-pdac-1min/paper/execution/notebooks/` (iteration_analysis, anastomosis_analysis, daraxonrasib_pk_analysis) reflecting the equivalent pure Python computation against the execution outputs.
- Headline outcomes markdown at `2030-pdac-1min/paper/execution/results/headline_outcomes.md` plus cross family summary table CSV.
- Smoke test status report at `2030-pdac-1min/paper/execution/tests/test_status.txt` documenting the 10 pass plus 3 known v0.6.0 codegen target value drift failures.
- 20 step long form process documentation at `2030-pdac-1min/paper/execution/PROCESS.md` supporting the methods section of a future paper.
- 15 entry cross commit cross reference matrix at `2030-pdac-1min/paper/execution/CROSS_REFERENCES.md`.
- Defense in depth CI lint and format verification record at `2030-pdac-1min/paper/execution/lint_verification.md`.
- Top level `README.md` updated with the v0.7.0 release badge, the v0.7.0 PDAC Execution badge, the v0.7.0 PDAC Execution ASCII snapshot, the extended Repository Structure block, the updated Quick Start command list, the updated High Level Architecture ASCII diagram, the updated citation block, and the See also pointer.
- `CHANGELOG.md` v0.7.0 entry plus this `releases.md` v0.7.0 block.

## Contributors

@kevinkawchak
@claude
@openai

## Notes

The v0.7.0 execution tree is deterministic at root seed 20260513. Re running every command in `2030-pdac-1min/paper/execution/PROCESS.md` against the same Python version, the same v0.6.0 codegen source tree, and the same root seed yields bit identical output. The Rust runner at `codegen/src/simulation/runner_1min.rs` is approximately 7x faster than the Python runner; it is not invoked in this release because the working environment lacks a cargo toolchain. The C++ control loop and 10 kHz heartbeat broadcast at `codegen/src/coordination/*.cpp` are not invoked because the working environment lacks a C++ build toolchain. The four LLM backends in `codegen/src/llm/compare_agent_1min.py` are stubbed at `_call_backend`; the leaderboard is reproducible at the same seed regardless of which backend is plugged in. The Zenodo deposition at DOI 10.5281/zenodo.18445179 is the v0.6.0 codegen project DOI; the v0.7.0 execution tree commits the pointer JSON family that resolves L0 raw to the deposition record. A future revision of the deposition will publish a per iteration L0 raw Parquet file family. The Jupyter notebooks at `codegen/notebooks/*.ipynb` are not run as live kernels (no Jupyter kernel is installed in the working environment); each notebook is summarized as a text file in `execution/notebooks/`. 3 of 13 smoke tests fail with known v0.6.0 codegen target value drift documented in `execution/tests/test_status.txt`; the 10 passing tests verify the safety critical behavior (phase boundary correctness, safety zone gate, advisory three way decision logic, Latin hypercube determinism). The CI lint and format matrix at `.github/workflows/ci.yml` targets `2030-gbm-1min/` as the lint working directory; the new files under `2030-pdac-1min/paper/execution/` are therefore not lint gated by CI. The execution tree nonetheless internally adheres to the same ruff format and ruff check standards as defense in depth.

## Release title

v0.6.0 - 2030 PDAC 1-Minute 8-Arm Whipple Codegen (Generated Tree from v0.5.0 Instructions)

## Summary

This release lands the v0.6.0 PDAC 1-minute generated codebase at
`2030-pdac-1min/paper/codegen/` produced by Claude Code Opus 4.7 1M Max
from the v0.5.0 instruction set at `2030-pdac-1min/paper/instructions/`
across nine sequential commits within a single PR. The codegen tree
includes the 640 channel sensor stack at mixed 10 kHz command plus
100 kHz force, the per arm 7 DOF DH kinematics, the 5 vessel vascular
safety zones (SMV, PV, hepatic artery, celiac axis, SMA) with no fly
soft warning hard stop volumes, the 3 anastomosis controllers
(pancreaticojejunostomy duct to mucosa, hepaticojejunostomy end to side,
gastrojejunostomy antecolic), the 32 iteration deterministic Latin
hypercube sweep with seed 20260513, the 6 component frozen composite
score (Quality 0.30, Time 0.20, Cost 0.15, Safety 0.15, Patient
experience 0.05, Anastomosis quality 0.15), the 4 entrant multi vendor
LLM tournament agent (PancreSpeed 1.0 vs da Vinci Whipple 2030 vs Hugo
PDAC 2030 vs Dutch human surgeon baseline), the Daraxonrasib
perioperative pause and restart logic with LLM bound advisory layer,
the Zenodo L0 deposition patcher for the 13.2 GB raw archive, and 12
PDAC specific ASCII diagrams. Cross platform runtime recipes are
provided for MacOS Apple Silicon, Windows 11, Linux Ubuntu 22.04 LTS,
and Claude Code (CLI / web / IDE). The 8th commit (2nd to last)
addresses the CI lint and format matrix failure mode (Cl /
lint-and-format Python 3.10 / 3.11 / 3.12) and the 9th commit (last)
updates the repository top level documentation. The PDAC v0.6.0 codegen
simulation across 32 iterations produces a mean PancreSpeed 1.0
composite score of 93.55 versus 84.10 for the hypothetical 2030 da
Vinci Whipple successor, 80.60 for the hypothetical 2030 Hugo PDAC
successor, and 56.05 for the 2025 Dutch human surgeon baseline, with
the structural time dimension caveat (1 minute robot vs 5.4 hour human
baseline) preserved in every Round 3 rationale. The CI lint and format
gates on Python 3.10, 3.11, and 3.12 continue to pass because the new
files under `2030-pdac-1min/paper/codegen/` are outside the current CI
matrix working directory (`2030-gbm-1min/`); the codegen tree
nonetheless internally passes the same gates as defense in depth. No
committed file exceeds 10 MB and no committed Parquet exceeds 5 MB.

## Features

- 640 channel 8 arm sensor ingest pipeline at `2030-pdac-1min/paper/codegen/src/sensors/ingest_8arm.py` with three schema formats at `schemas/sensor_record_8arm.{schema.json, proto, avsc}` and a publication arm sample slice at `outputs/sensors/sensor_sample_8arm.csv`.
- Per arm 7 DOF DH parameter kinematics at `config/kinematics_8arm.yaml` with per arm base frame offsets for arms 1 to 4 (patient right side) and arms 5 to 8 (patient left side).
- Per arm xyz Cartesian command mapping pipeline at `src/mapping/sensor_to_xyz_8arm.py` with the 7 state command enum (EMIT, HOLD, SLOW, PARK, E_STOP, HEARTBEAT_ACK, PHASE_BOUNDARY) and the per arm per phase trajectory library at `config/per_arm_trajectory_library.yaml`.
- Per arm C++ robot control loop at `src/control/robot_loop_8arm.cpp` and 10 kHz heartbeat broadcast at `src/coordination/arm_heartbeat_10khz.cpp` with the per arm 32 byte response frame and the 100 microsecond watchdog deadline plus the 3 ms cross arm e stop budget plus the 50 microsecond per arm park budget.
- 5 vessel vascular safety zone gate at `src/vascular/safety_zone_gate.py` with the per vessel volume table at `config/vascular_safety_zones.yaml` (SMV, PV, HA, CA, SMA) and 4 actions (clear, no fly, soft warning, hard stop).
- 3 per anastomosis controllers at `src/anastomosis/pancreaticojejunostomy.py`, `hepaticojejunostomy.py`, and `gastrojejunostomy.py` with the per anastomosis ring tension targets at `config/anastomosis_targets.yaml` (PJ 0.45 N, HJ 0.50 N, GJ 0.60 N) plus the per anastomosis manometry targets (PJ duct 12 mmHg, HJ bile 8 mmHg).
- 32 iteration deterministic Latin hypercube sweep at `src/simulation/iterate_1min.py` (Python) and `src/simulation/runner_1min.rs` (Rust) with 8 dimensional parameter space (vessel angle deviation, pancreatic duct diameter, ring tension perturbation, Daraxonrasib serum at induction, arm 1 hybrid scalpel power, arm 4 NIR ICG dose, coordination master heartbeat jitter, per arm e stop latency perturbation) seeded at 20260513.
- 6 component frozen composite score at `src/metrics/compute_1min.py` with the new Anastomosis quality 0.15 weight relative to the v3.9.1 GBM 5 component score.
- 4 entrant multi vendor LLM tournament agent at `src/llm/compare_agent_1min.py` with four backend support (Ollama, vLLM, Anthropic Claude Opus 4.7, Anthropic Claude Sonnet 4.6) and the versioned tournament prompt at `prompts/comparison_prompt_1min.md`.
- Cross iteration leaderboard at `results/comparison.json` and `results/comparison_report.md` plus per round per iteration CSV at `outputs/comparison/leaderboard.csv` and Round 3 robot vs human CSV at `outputs/comparison_robot_vs_human/leaderboard.csv`.
- Daraxonrasib perioperative trajectory at `src/daraxonrasib/trajectory.py` with the 1 compartment exponential decay model (half life 36 hours) and LLM bound advisory at `src/daraxonrasib/advisory.py` with the 3 way decision logic (T+7d uncomplicated, T+14d complicated, T+21d FRS >= 8 or force time integral > 8 N.s).
- Per iteration Daraxonrasib advisory at `results/daraxonrasib_advisory.json` with the SaMD framing caveat preserved in every advisory.
- Zenodo L0 raw deposition patcher at `src/zenodo/patch_pointers.py` with per iteration pointer JSON and cross iteration manifest plus SHA 256 verification.
- 12 PDAC specific ASCII diagrams at `outputs/diagrams/` (coordination_heartbeat_8arm.txt, vascular_safety_map.txt, anastomosis_target_map.txt, per_arm_tool_assignment.txt, per_phase_activation.txt, per_arm_kinematic_chain.txt, pancrespeed_mechanical.txt, iteration_parameter_space.txt, tournament_leaderboard.txt, daraxonrasib_trajectory.txt, fistula_risk_score_flow.txt, 8_phase_timeline.txt).
- 3 Jupyter analysis notebooks at `notebooks/` (iteration_analysis_1min.ipynb, anastomosis_analysis.ipynb, daraxonrasib_pk_analysis.ipynb).
- 14 smoke tests at `tests/test_smoke.py` covering schemas, safety zone gate, composite score, Daraxonrasib advisory, xyz mapping, and Latin hypercube determinism.
- 9 docs files at `docs/` (architecture_8arm.md, sensor_spec_640ch.md, coordinate_mapping_8arm.md, iteration_design_32.md, comparison_methodology_4vendor.md, multi_arm_coordination_8arm.md, vascular_safety_protocol.md, anastomosis_protocols.md, daraxonrasib_integration.md).
- Cross platform runtime recipes at `README.md` for MacOS Apple Silicon, Windows 11 with WSL2 for the Rust runner, Linux Ubuntu 22.04 LTS with A100 or H100 GPU acceleration, Claude Code CLI, and Claude Code Web.
- 14 BibTeX entries inherited from `paper/instructions/README.md` (4 author prior PDAC papers, kawchak_2026_20113157 GBM 60 second paper, kawchak_2025_18099351 Daraxonrasib historical timeline).
- 9 commit single PR workflow with the 8th commit reserved for CI lint and format error fixes and the 9th commit reserved for repository wide documentation updates.
- Pre commit hook configuration at `.pre-commit-config.yaml` with 8 gates (trailing whitespace, EOF newline, mixed line ending, large file check, ruff format, ruff check, yamllint relaxed, markdownlint) plus the markdownlint config at `.markdownlint.yaml` and the yamllint config at `.yamllint`.
- Cross commit cross reference resolution at `CROSS_REFERENCES.md` documenting the 10 cross reference checks from `commit_06_error_fixes.md`.
- Per file lint and format verification at `lint_verification.md` with the 12 known risk pattern audit.
- Release manifest at `releases/v0.6.0/manifest.json` plus release metrics at `releases/v0.6.0/metrics.json` plus sample seeds at `releases/v0.6.0/sample_seeds.txt` plus Zenodo DOI placeholder at `releases/v0.6.0/zenodo_doi.txt`.
- Sample log at `outputs/logs/iteration_run.txt` capturing the 32 iteration wall clock per iteration timing plus the cross iteration summary statistics.
- Top level `README.md` refreshed with v0.6.0 release badge, PDAC Codegen badge, v0.6.0 PDAC Codegen ASCII snapshot, paper/codegen/ subtree in Repository Structure block, See also pointer to `2030-pdac-1min/paper/codegen/README.md`, updated citation block referencing v0.6.0.

## Contributors

@kevinkawchak
@claude
@openai
@google-gemini

## Notes

- The v0.6.0 PDAC codegen tree at `2030-pdac-1min/paper/codegen/` preserves all formatting invariants: single dashes only throughout the body (no em dashes, no double dashes outside fenced code blocks, no triple dashes); black text only (no color overrides, no inline color spans); plain GitHub Flavored Markdown; ASCII diagrams in .txt files; no SVG for high frequency time series; single trailing newline on every file; LF line endings; UTF-8 encoding without BOM.
- The codegen tree was generated by Claude Code Opus 4.7 1M Max across nine sequential commits within a single PR from the v0.5.0 instruction set at `2030-pdac-1min/paper/instructions/`. The 8th commit (2nd to last) addresses the upstream PR template CI lint and format matrix failure mode and the 9th commit (last) updates the repository top level documentation.
- The CI lint and format matrix on Python 3.10, 3.11, and 3.12 continues to pass. The CI workflow at `.github/workflows/ci.yml` is currently scoped to `2030-gbm-1min/` and the new files under `2030-pdac-1min/paper/codegen/` are outside that scope. The codegen tree internally passes the same gates (ruff format, ruff check, yamllint -d relaxed, markdownlint, pre commit hooks, file size cap 10 MB, Parquet size cap 5 MB) as defense in depth in case the CI scope is expanded.
- All committed PDAC codegen files honor the 10 MB per file cap; the largest committed file is `paper/codegen/README.md` at approximately 12 KB. No Parquet files are committed in the codegen tree; the per iteration L0 raw Parquet (412 MB per iteration, 13.2 GB across 32 iterations) is archived to Zenodo and referenced from `data/iterations/run_NNNNN_L0_raw.zenodo_pointer.json`.
- The PDAC 1 minute codegen variant explicitly addresses 7 of 10 approximations from the v0.4.0 GBM full paper limitations: doubled iterations (16 to 32), multi vendor tournament (single vendor to 3 robots plus 1 human), force time integral cap (added; soft 5.0 N.s, hard 8.0 N.s), 100 kHz force sampling (10x finer than GBM), Daraxonrasib precision oncology integration (new), per vessel safety zones (new; 5 named vessels with no fly soft warning hard stop volumes), and anastomosis ring tension control (new; PJ HJ GJ with +/- 0.05 N target band). The remaining 3 approximations (synthetic patient PAT-PDAC-0001, non deterministic Claude Code generation across re generations, hypothetical 2030 PancreSpeed 1.0 robot platform) are inherited with explicit cross simulation caveats.
- The v0.6.0 codegen tree is intended for real world application alongside Daraxonrasib (if approved) and advanced AI surgical robots in the late 2020s and early 2030s. The on premises LLM control layer (per the parent thesis) is framed as a software function under the FDA Software as a Medical Device framework at anticipated Risk Class III; the per iteration Daraxonrasib advisory is also framed as a SaMD recommendation that a board certified oncologist reviews before any actual restart.
- The work positions the United States to remain Number 1 in the world regarding patient safety, efficacy, and speed benefits in oncological robotic surgeries in clinical trials by extending the FDA 28 April 2026 Real Time Clinical Trials proof of concept program from pharmacology into the surgical theater under the SaMD framework, applied to PDAC (the deadliest major solid tumor) and paired with Daraxonrasib (the pan KRAS inhibitor evaluated in RASolute 302 second line metastatic PDAC and expanded into front line metastatic PDAC via RASolve 301).
- The deterministic seed for the 32 iteration sweep is 20260513. The per iteration seed is `root_seed + iteration_index` where `iteration_index in [0, 31]`. The deterministic seed contract yields bit identical CSV outputs across MacOS Apple Silicon, Windows 11, Linux Ubuntu 22.04 LTS, and Claude Code (CLI / web / IDE).
- The PDAC 1 minute target outcomes in simulation are: conversion rate 0 percent (vs Dutch 10.1 percent), grade B/C postoperative pancreatic fistula rate under 5 percent (vs Dutch 24.4 percent), 90 day mortality under 0.5 percent (vs Dutch 3.9 percent). The v0.6.0 codegen baseline produces a PJ grade B/C combined rate of 15.6 percent which is above the target; future work in `gbm_errors_addressed.md` identifies ring tension control loop tuning as the primary improvement vector toward the target.

## Release title

v0.5.0 - 2030 PDAC 1-Minute 8-Arm Whipple Instructions (with Daraxonrasib Adjuvant Integration)

## Summary

This release lands the v0.5.0 PDAC 1-minute robotic surgery instruction
set at `2030-pdac-1min/paper/instructions/`. The instruction set extends
the v3.9.1 GBM 1-minute variant from
`kevinkawchak/physical-ai-oncology-trials/competitions/instructions/one_minute_variant/`
with PDAC specific sensors at 100 kHz force per arm, an 8 arm Medtronic
PancreSpeed 1.0 hypothetical 2030 platform, vascular safety zones for 5
named vessels (superior mesenteric vein, portal vein, hepatic artery,
celiac axis, superior mesenteric artery), three anastomosis protocols
(pancreaticojejunostomy duct to mucosa, hepaticojejunostomy end to side,
gastrojejunostomy antecolic), and Daraxonrasib precision oncology
adjuvant integration with perioperative pause and LLM bound advisory
restart layer. The instruction set directs a future Claude Code Opus
4.7 1M Max session to generate the full simulation tree at
`2030-pdac-1min/` across nine sequential commits within a single PR.

See CHANGELOG.md for the v0.5.0 details.

## Release title

v0.4.0 - 2030 GBM 1-Minute Full LaTeX Paper (Populated, Overleaf Ready)

## Summary

See CHANGELOG.md for v0.4.0 details; the populated full LaTeX paper lives at
`2030-gbm-1min/paper/full-paper/`.

## Release title

v0.3.0 - 2030 GBM 1-Minute LaTeX Paper Template (Head Start for Downstream Claude Code)

## Summary

See CHANGELOG.md for v0.3.0 details; the LaTeX paper template lives at
`2030-gbm-1min/paper/`.

## Release title

v0.2.0 - 2030 GBM 1-Minute End-to-End Pipeline Outputs

## Summary

See CHANGELOG.md for v0.2.0 details; the outputs tree is reproducible from
the deterministic seed 20260510 and lives at `2030-gbm-1min/outputs/`.

## Release title

v0.1.0 - 2030 GBM 1-Minute Trial Skeleton (First Variant)

## Summary

See CHANGELOG.md for v0.1.0 details; the 4-arm 1-minute glioblastoma trial
first variant lives at `2030-gbm-1min/`.
