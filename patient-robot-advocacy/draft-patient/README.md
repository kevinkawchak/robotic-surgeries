# draft-patient - Stage 6, the bracketed LaTeX scaffold (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Stage](https://img.shields.io/badge/Stage-6%20of%208-00417A.svg)](../sub-prompts/prompt-6-draft-patient.md)
[![Paper](https://img.shields.io/badge/Paper-Draft%201.0-00417A.svg)](main.tex)
[![Sections](https://img.shields.io/badge/Sections-13-00417A.svg)](sections)
[![Figure slots](https://img.shields.io/badge/Figure%20slots-30-00417A.svg)](sections)
[![Compiles](https://img.shields.io/badge/pdfLaTeX-compiles-brightgreen.svg)](main.tex)
[![Overleaf](https://img.shields.io/badge/Overleaf-ready%20zip-6C757D.svg)](draft-patient-LaTeX.zip)
[![Raster](https://img.shields.io/badge/Raster%20images-none-6C757D.svg)](.)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

Stage 6 of the eight-stage build, run from
[`../sub-prompts/prompt-6-draft-patient.md`](../sub-prompts/prompt-6-draft-patient.md).
This is the first compilable LaTeX skeleton of *Patient Robot Advocacy: A Phase 1,
First-in-Human, PDAC Clinical Trial Protocol of a LLM-Directed Robotic Whipple with
Daraxonrasib (RMC-6236)*, Draft 1.0.

Everything the [`../full-patient/`](../full-patient) stage must populate is marked with a
`\draftinstr{...}` bracketed instruction that **names the exact repository file** supplying
the material, so Stage 7 has no discretion about where its content comes from.

## Files

| File | What it is |
|:--|:--|
| [`main.tex`](main.tex) | Patient-advocacy cover page, keywords, clickable table of contents, one `\input` per section, `\clearpage` between sections |
| [`patientstyle.sty`](patientstyle.sty) | Palette, body typography, table columns, the five diagram vocabularies, the `pafig` frame, `\figcaption`, the cover furniture |
| [`references.bib`](references.bib) | 51 entries merged from three bibliographies into one format |
| [`sections/`](sections) | Thirteen `.tex` files, one per paper section, Rule 6 |
| [`draft-patient-LaTeX.zip`](draft-patient-LaTeX.zip) | Overleaf-ready bundle of all of the above |
| [`prompt-draft-patient.md`](prompt-draft-patient.md) | The Stage 6 sub-prompt, filed verbatim |
| [`output-draft-patient.md`](output-draft-patient.md) | The Stage 6 narrative, decisions, and verification results |

## The thirteen sections and their figure slots

| File | \S | Section | Figures |
|:--|:--|:--|:--|
| [`sec-00-front.tex`](sections/sec-00-front.tex) | 1 | Statement of Patient Commitment | 1, 2 |
| [`sec-01-summary.tex`](sections/sec-01-summary.tex) | 2 | Plain-Language Protocol Summary | 3, 4 |
| [`sec-02-concerns.tex`](sections/sec-02-concerns.tex) | 3 | The Documented Patient Concerns | 5, 6, 7, 8, 9 |
| [`sec-03-objectives.tex`](sections/sec-03-objectives.tex) | 4 | Objectives and Patient-Facing Endpoints | 10, 11 |
| [`sec-04-design.tex`](sections/sec-04-design.tex) | 5 | Study Design Explained | 12, 13 |
| [`sec-05-population.tex`](sections/sec-05-population.tex) | 6 | Who Can Join, and Who Decides | 14, 15, 16 |
| [`sec-06-intervention.tex`](sections/sec-06-intervention.tex) | 7 | What Happens in the Operating Room | 17, 18, 19, 20, 21 |
| [`sec-07-discontinuation.tex`](sections/sec-07-discontinuation.tex) | 8 | Stopping, Withdrawing, Changing Your Mind | 22, 23 |
| [`sec-08-assessments.tex`](sections/sec-08-assessments.tex) | 9 | Your Visits, Your Data, Your Robot Instructions | 24, 25, 26 |
| [`sec-09-evidence.tex`](sections/sec-09-evidence.tex) | 10 | The Numbers Behind the Reassurance | 27, 28 |
| [`sec-10-accountability.tex`](sections/sec-10-accountability.tex) | 11 | Accountability, Oversight, and Who Answers | 29 |
| [`sec-11-rights.tex`](sections/sec-11-rights.tex) | 12 | Patient Rights, Costs, and H. R. 9510 v5 | 30 |
| [`sec-12-references-backmatter.tex`](sections/sec-12-references-backmatter.tex) | 13 | References and Back Matter | none |

## The cover page, and how it differs from the parent protocol's

The colour scheme is unchanged: Corporate Blue `#00417A`, Professional Gray `#6C757D`,
Classic White. The furniture is not.

| Parent protocol cover | This cover | Why |
|:--|:--|:--|
| Centred `\LARGE` title in accent colour | Full-width Corporate Blue banner, white text, with a `pablue1` underscore rule | A patient picking the document up should see one object, not a wall of centred text |
| Version and date line | Four rounded badges: Draft 1.0, repository v1.0.0, 30 figures, 21 concerns answered | Badges are scannable; a version line is not |
| Regulatory basis line | Three-panel strip: who is in control, what could go wrong, what this costs me | The three questions the surveyed literature says patients actually ask, answered before any regulatory text |
| Single italic disclaimer block | Independence statement, then a separately labelled Disclaimer paragraph | The master prompt requires both, and separating them makes each readable |
| Keywords, then the table of contents | Same, with the paper DOI and the repository URL stated above the keywords | Both v1.0 and v1.0.0 are named on the cover, as required |

## The `pafig` spacing invariant

Every figure in every stage is written as exactly three source lines:

```latex
\end{pafig}
\vspace{-0.7cm}
\figcaption{Figure NN. ...}
```

`pafig` opens with a fixed `\addvspace{0.60\baselineskip}` and closes with a fixed
`\addvspace{0.10\baselineskip}`; `\figcaption` opens with `\nopagebreak` and closes with a
fixed `\addvspace{0.80\baselineskip}`. Because all three are fixed, the whitespace
signature is identical for all thirty figures regardless of what follows them. Verified in
this stage: 30 `pafig` environments, 30 `\vspace{-0.7cm}` lines, 30 `\figcaption` calls, and
figure numbers 1 to 30 with no gaps and no duplicates.

## The palette budget

Eleven colour tokens and no twelfth, declared once in `patientstyle.sty`:

| Token | Hex | Role |
|:--|:--|:--|
| `protoblue` | `#00417A` | Patient guarantees, end goals, the investigational system |
| `protogray` | `#6C757D` | Process, oversight, non-investigational context |
| `protowhite` | `#FFFFFF` | Inputs, context, every figure background |
| `protoblack` | `#000000` | Strokes and body text |
| `pagrayl` | `#E9ECEF` | Grayscale, light |
| `pagraym` | `#CED4DA` | Grayscale, medium |
| `pagrayd` | `#9AA1A8` | Grayscale, medium-dark |
| `pablue1` | `#3C7DB2` | Lighter shade 1 of Corporate Blue |
| `pablue2` | `#DCE8F1` | Lighter shade 2 of Corporate Blue |
| `padark` | `#222222` | Emphasis fill, used sparingly |
| `orcidgreen` | `#A6CE39` | Reserved for the ORCID iD mark only |

Per figure: at most three grayscale fills, at most two lighter blues, black fill sparingly.

## Table discipline

Every fixed-width column is declared `>{\raggedright\arraybackslash}p{...}` through the
`L`, `C`, and `R` column types, and every table is a `tabularx` at `\textwidth` with one
`Y` column absorbing the remainder, so no table is narrower or wider than the body measure
and no cell shows a large interword gap. `\tabcolsep` is 5pt and `\arraystretch` is 1.18,
inherited from the parent protocol.

## Files from other directories used here

| Source | Used for | Where |
|:--|:--|:--|
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `protostyle.sty` | the base palette, typography, table columns, widow and orphan penalties, the PNG-free ORCID mark | `patientstyle.sty` |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `main.tex` | the cover structure and the one-`\input`-per-section pattern | `main.tex` |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `references.bib` | the BibTeX format every entry is normalised to | `references.bib` |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/*` | every clinical fact each `\draftinstr` points Stage 7 at | all thirteen sections |
| [`../inputs/phase-1-six-platform-diagrams.zip`](../inputs) `dxstyle.sty` | the five TikZ diagram vocabularies and the vector pictograms, adapted to the restricted palette | `patientstyle.sty` |
| [`../inputs/patient-priority-physical-ai.zip`](../inputs) | the patient-as-priority premise | `sec-00-front`, `sec-11-rights` |
| [`../inputs/cancer-patient-journey.zip`](../inputs) | the journey structure, NSCLC, distinguished from PDAC | `sec-01-summary`, `sec-06-intervention` |
| [`../inputs/patient-robot-instructions.tex`](../inputs) | the ten robot-type sheets, re-scoped | `sec-08-assessments` |
| [`../mermaid/`](../mermaid) | nine figure sources and their TikZ rendering notes | figures 1, 3, 7, 10, 14, 19, 23, 25, 27 |
| [`../plantuml/`](../plantuml) | five figure sources | figures 8, 12, 15, 18, 22 |
| [`../d2/`](../d2) | seven figure sources | figures 4, 5, 11, 16, 21, 26, 29 |
| [`../diagrams-python/`](../diagrams-python) | four figure sources | figures 9, 17, 24, 30 |
| [`../graphviz/`](../graphviz) | five figure sources | figures 2, 6, 13, 20, 28 |
| [`../research/research-a.md`](../research) | the Gemini concern families | `sec-02-concerns` |
| [`../research/research-b.md`](../research) | the sixteen ChatGPT concerns and thirteen BibTeX entries | `sec-02-concerns`, `references.bib` |
| [`../references/references.bib`](../references) | the author works and the H. R. 9510 v5 citation | `references.bib` |

## Compiling

On Overleaf with pdfLaTeX, or locally:

```
pdflatex main -> bibtex main -> pdflatex main -> pdflatex main
```

Verified locally on TeX Live 2023 with pdfTeX: no errors, no missing citations, no
undefined references.

## License

Released under CC BY 4.0; reproduced U.S. Government regulatory text is used under
17 U.S.C. § 105. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
