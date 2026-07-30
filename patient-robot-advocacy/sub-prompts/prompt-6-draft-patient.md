## prompt-6-draft-patient

**Stage 6 of 8.** Output directory: [`../draft-patient/`](../draft-patient). Produces the
bracketed-instruction LaTeX scaffold of the Patient Robot Advocacy paper.

### Objective

Build the first complete, compilable LaTeX skeleton of *Patient Robot Advocacy: A Phase 1,
First-in-Human, PDAC Clinical Trial Protocol of a LLM-Directed Robotic Whipple with
Daraxonrasib (RMC-6236)*, Draft 1.0. Every part of the paper that Stage 7 must populate is
marked with a `\draftinstr{...}` bracketed instruction that **names the exact repository
file or directory** supplying the material, so Stage 7 has no discretion about where its
content comes from.

### Deliverables

| File | Content |
|:--|:--|
| `main.tex` | Patient-advocacy cover page, keywords, clickable table of contents, `\input` per section |
| `patientstyle.sty` | Palette, body typography, table columns, the five diagram vocabularies, `pafig`, `\figcaption` |
| `references.bib` | Protocol bibliography plus the thirteen new patient-perception entries, one format |
| `README.md` | Stage README with badges and a source-to-section map |
| `sections/sec-00-front.tex` … `sections/sec-12-references-backmatter.tex` | Thirteen section files |
| `draft-patient-LaTeX.zip` | Overleaf-ready bundle of all of the above |
| `prompt-draft-patient.md`, `output-draft-patient.md` | This prompt filed verbatim, plus the stage narrative |

### Section plan (one `.tex` per section, Rule 6)

| File | Section | Figures |
|:--|:--|:--|
| `sec-00-front.tex` | Statement of Patient Commitment | 1, 2 |
| `sec-01-summary.tex` | Plain-Language Protocol Summary | 3, 4 |
| `sec-02-concerns.tex` | The Documented Patient Concerns | 5, 6, 7, 8, 9 |
| `sec-03-objectives.tex` | Objectives and Patient-Facing Endpoints | 10, 11 |
| `sec-04-design.tex` | Study Design Explained | 12, 13 |
| `sec-05-population.tex` | Who Can Join, and Who Decides | 14, 15, 16 |
| `sec-06-intervention.tex` | What Happens in the Operating Room | 17, 18, 19, 20, 21 |
| `sec-07-discontinuation.tex` | Stopping, Withdrawing, Changing Your Mind | 22, 23 |
| `sec-08-assessments.tex` | Your Visits, Your Data, Your Robot Instructions | 24, 25, 26 |
| `sec-09-evidence.tex` | The Numbers Behind the Reassurance | 27, 28 |
| `sec-10-accountability.tex` | Accountability, Oversight, and Who Answers | 29 |
| `sec-11-rights.tex` | Patient Rights, Costs, and H. R. 9510 v5 | 30 |
| `sec-12-references-backmatter.tex` | References and back matter | none |

### Cover page (patient-advocacy variant, protocol colour scheme retained)

A full-width Corporate Blue banner carrying the title; a Draft 1.0 badge line; the DOI
`10.5281/zenodo.xxxxxxxx` hyperlinked to `https://doi.org/10.5281/zenodo.xxxxxxxx`; the
ORCID iD `0009-0007-5457-8667` hyperlinked to `https://orcid.org/0009-0007-5457-8667`; the
author block `CEO Kevin Kawchak, ChemicalQDevice, kevink@chemicalqdevice.com`; a
three-panel "What this paper answers for you" strip that no protocol cover page has; the
independence statement; the disclaimer naming Claude Code Opus 5; `San Diego`; and
`July 31, 2026`. Paper v1.0 and repository v1.0.0 URLs are both stated.

### Rules for this stage

1. Every `\draftinstr{...}` names its source file explicitly, for example
   `../research/research-b.md` or `../d2/fig-05-concern-families.d2`.
2. Every figure slot is present as a real `pafig` environment containing at minimum the
   frame and title node, so the scaffold compiles and paginates realistically. The
   `\vspace{-0.7cm}` before each `\figcaption` is present from this stage forward.
3. Every table is present with its final column specification, using
   `>{\raggedright\arraybackslash}p{...}` on every fixed-width column and totalling
   `\textwidth`.
4. Single dashes only; no em dash, en dash pair, or triple dash. `§` for every codified
   reference. No PNG, no JPG.
5. Commits: one for `main.tex`, one for `patientstyle.sty`, one for `references.bib`, one
   for `README.md`, and one for each of the thirteen section files. The second-to-last
   commit fixes all errors across all files; the last commit lands the zip and the stage
   `output-draft-patient.md`. That is 20 commits, exceeding the 10+ requirement.
6. The stage must compile with `pdflatex -> bibtex -> pdflatex -> pdflatex`.
