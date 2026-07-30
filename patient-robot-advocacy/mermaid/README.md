# mermaid - Stage 1, mermaid-type diagram sources (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Stage](https://img.shields.io/badge/Stage-1%20of%208-00417A.svg)](../sub-prompts/prompt-1-mermaid.md)
[![Figures](https://img.shields.io/badge/Figures-9%20of%2030-00417A.svg)](.)
[![Type](https://img.shields.io/badge/Type-mermaid--type-6C757D.svg)](.)
[![Constructs](https://img.shields.io/badge/Constructs-flowchart%20%7C%20sequence%20%7C%20state%20%7C%20gantt%20%7C%20quadrant%20%7C%20xychart%20%7C%20pie-6C757D.svg)](.)
[![Raster](https://img.shields.io/badge/Raster%20images-none-6C757D.svg)](.)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

Stage 1 of the eight-stage build, run from
[`../sub-prompts/prompt-1-mermaid.md`](../sub-prompts/prompt-1-mermaid.md). Nine of the
paper's thirty figures are mermaid-type, more than any other type, because more of the
patient's questions are about **what happens, in what order, and who decides** than about
anything else.

## The nine figures

| File | Fig | Construct | § | Patient concern answered |
|:--|:--|:--|:--|:--|
| [`fig-01-seven-commitments.md`](fig-01-seven-commitments.md) | 1 | `flowchart TD` | 1 | loss of the human element; surgeon-patient trust |
| [`fig-03-journey-schema.md`](fig-03-journey-schema.md) | 3 | `flowchart LR`, full page | 2 | treatment choice; unknown and experimental risks |
| [`fig-07-concern-quadrant.md`](fig-07-concern-quadrant.md) | 7 | `quadrantChart` | 3 | all twenty-one, ranked honestly on two axes |
| [`fig-10-endpoint-meaning.md`](fig-10-endpoint-meaning.md) | 10 | `flowchart TD`, three ranks | 4 | cancer-control effectiveness; hype |
| [`fig-14-eligibility-self-selection.md`](fig-14-eligibility-self-selection.md) | 14 | `flowchart TD`, two decision columns | 6 | bias and applicability; treatment choice |
| [`fig-19-advise-approve-execute.md`](fig-19-advise-approve-execute.md) | 19 | `sequenceDiagram` | 7 | who is controlling; override; automation bias |
| [`fig-23-consent-lifecycle.md`](fig-23-consent-lifecycle.md) | 23 | `stateDiagram-v2`, composite | 8 | software change and versioning; withdrawal |
| [`fig-25-visit-timeline.md`](fig-25-visit-timeline.md) | 25 | `gantt` | 9 | practical and post-trial burden |
| [`fig-27-reassurance-dashboard.md`](fig-27-reassurance-dashboard.md) | 27 | `xychart` + `pie` + tables, full page | 10 | effectiveness; hype; safety and malfunction |

Figure numbers 2, 4, 5, 6, 8, 9, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22, 24, 26, 28, 29,
and 30 belong to the four sibling stages. Numbering is continuous across the whole paper
and is never restarted per type.

## File format

Every file carries the same seven parts, in this order:

1. `## Figure NN. <title>` heading.
2. Type, paper section, and the patient concern answered, with the source of that concern.
3. A short "why this diagram type" paragraph justifying the choice against the four
   alternatives.
4. The fenced ` ```mermaid ` block, valid Mermaid, with the palette declared in the
   `%%{init}%%` directive so the source renders correctly outside LaTeX.
5. A prose or tabular reading aid where the figure carries an argument that needs one.
6. A **Palette used** table naming every colour and confirming the per-diagram budget:
   at most three grayscale fills, at most two lighter blues, black fill sparingly.
7. **TikZ rendering notes** telling [`../full-patient/`](../full-patient) exactly how to
   draw the figure with the `mm*` vocabulary of `patientstyle.sty`, including coordinates,
   text widths, minimum clear space, and an explicit `looseness` for every curved
   connector.

## Palette budget, verified per figure

| Fig | Grayscale fills used (max 3) | Lighter blues used (max 2) | Black fill nodes |
|:--|:--|:--|:--|
| 1 | 1 | 0 | 1 |
| 3 | 1 | 1 | 0 |
| 7 | 2 | 1 | 0 |
| 10 | 1 | 2 | 0 |
| 14 | 2 | 2 | 0 |
| 19 | 1 | 1 | 0 |
| 23 | 2 | 1 | 0 |
| 25 | 2 | 2 | 0 |
| 27 | 2 | 2 | 0 |

## Files from other directories used here

| Source | Used by | For |
|:--|:--|:--|
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-01-summary.tex` | 3, 25 | the trial schema and the Schedule of Activities the calendar re-expresses |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-03-objectives.tex` | 10 | the objective and endpoint set |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-05-population.tex` | 14 | inclusion and exclusion criteria, § 5.1, § 5.2, § 5.4 |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-06-intervention.tex` | 19, 27 | force caps, no-fly gating, e-stop budget, heartbeat bus |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-07-discontinuation.tex` | 23 | withdrawal routes and data disposition |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `protostyle.sty` | all nine | the `mm*` vocabulary and the base palette |
| [`../inputs/cancer-patient-journey.zip`](../inputs) | 3 | the autonomous single-patient journey structure, NSCLC, re-scoped to PDAC |
| [`../inputs/phase-1-six-platform-diagrams.zip`](../inputs) `dxstyle.sty` | all nine | the quantitative primitives `\vbarcol`, `\donutseg`, `\ciband`, `\legkey`, as vocabulary only |
| [`../research/research-a.md`](../research) | 1, 7, 19 | the Gemini concern families |
| [`../research/research-b.md`](../research) | 7, 10, 14, 19, 23, 25, 27 | the sixteen numbered concerns and their citations |
| [`../references/references.bib`](../references) | 27 | `pdac060s2030`, `paipredict4x`, `rasolute302` for the quantitative panels |

## What is deliberately not here

No Excalidraw source. The master prompt excludes Excalidraw output; the Excalidraw section
of [`../inputs/phase-1-six-platform-diagrams.zip`](../inputs) was read for context only. No
PNG, no JPG, and no rendered SVG: the sources are text, and the paper renders them as
vector TikZ.

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
