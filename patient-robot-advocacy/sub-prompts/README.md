# sub-prompts - Process A output (Patient Robot Advocacy, v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Sub-prompts](https://img.shields.io/badge/Sub--prompts-8-00417A.svg)](.)
[![Stages](https://img.shields.io/badge/Stages-5%20diagram%20%2B%20draft%20%2B%20full%20%2B%20final-6C757D.svg)](.)
[![Figures](https://img.shields.io/badge/Figures-30-00417A.svg)](.)
[![Paper](https://img.shields.io/badge/Paper-Patient%20Robot%20Advocacy-00417A.svg)](../final-patient)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

This folder is the output of **Process A**. From the single master prompt filed verbatim
in [`../prompts/prompt-patient.md`](../prompts/prompt-patient.md), Claude Code Opus 5
generated the eight sub-prompts that **Process B** then runs in sequence to grow the
Patient Robot Advocacy paper from machine-readable diagram sources, through a bracketed
draft, to a fully populated paper, to a polished final source set.

Where the upstream workflow in
[`../template/trial-protocol-template.zip`](../template/trial-protocol-template.zip) had
four sub-prompts and one diagram directory (`mermaid/`), this build has **eight**
sub-prompts and **five** diagram directories, one for each permitted diagram type. No
Excalidraw stage exists: the master prompt excludes Excalidraw output, and the Excalidraw
material in `../inputs/phase-1-six-platform-diagrams.zip` is used only as context.

## The eight sub-prompts

| # | Sub-prompt | Runs in stage | Figures produced | Adapted from (trial-protocol-template) |
|:--|:--|:--|:--|:--|
| 1 | [`prompt-1-mermaid.md`](prompt-1-mermaid.md) | [`../mermaid/`](../mermaid) | 1, 3, 7, 10, 14, 19, 23, 25, 27 | `sub-prompts/prompt-1-mermaid.md` |
| 2 | [`prompt-2-plantuml.md`](prompt-2-plantuml.md) | [`../plantuml/`](../plantuml) | 8, 12, 15, 18, 22 | new (diagram-type split) |
| 3 | [`prompt-3-d2.md`](prompt-3-d2.md) | [`../d2/`](../d2) | 4, 5, 11, 16, 21, 26, 29 | new (diagram-type split) |
| 4 | [`prompt-4-diagrams-python.md`](prompt-4-diagrams-python.md) | [`../diagrams-python/`](../diagrams-python) | 9, 17, 24, 30 | new (diagram-type split) |
| 5 | [`prompt-5-graphviz.md`](prompt-5-graphviz.md) | [`../graphviz/`](../graphviz) | 2, 6, 13, 20, 28 | new (diagram-type split) |
| 6 | [`prompt-6-draft-patient.md`](prompt-6-draft-patient.md) | [`../draft-patient/`](../draft-patient) | 30 slots scaffolded | `sub-prompts/prompt-2-draft-protocol.md` |
| 7 | [`prompt-7-full-patient.md`](prompt-7-full-patient.md) | [`../full-patient/`](../full-patient) | 30 drawn | `sub-prompts/prompt-3-full-protocol.md` |
| 8 | [`prompt-8-final-patient.md`](prompt-8-final-patient.md) | [`../final-patient/`](../final-patient) | 30 polished | `sub-prompts/prompt-4-final-protocol.md` |

## Why the diagram types split the way they do

The master prompt requires that the number of diagrams per type follow the purpose of the
diagram and its location in the paper, not an equal quota. The split below is the result.

| Type | Count | Chosen because the patient's question is |
|:--|:--|:--|
| Mermaid-type | 9 | "What happens, in what order, and who decides?" - decisions in time |
| D2-type | 7 | "How much of this is there, and how does it group?" - containment and true grids |
| PlantUML-type | 5 | "What exactly do you guarantee?" - formal notation with defined semantics |
| Graphviz-type | 5 | "What depends on what, and can you prove it?" - pure graph structure |
| Diagrams (Python)-type | 4 | "Where does this physically live?" - infrastructure, air gaps, data paths |

## Shared conventions asserted by every sub-prompt

1. **Palette, per diagram.** Corporate Blue `#00417A`, Professional Gray `#6C757D`,
   Classic White, black strokes and text; at most three grayscale fills (`#E9ECEF` light,
   `#CED4DA` medium, `#9AA1A8` medium-dark); at most two lighter shades of `#00417A`
   (`#3C7DB2`, `#DCE8F1`); black fill (`#222222`) used sparingly.
2. **Numbering.** Figures are numbered 1 to 30 across the whole paper. Each diagram stage
   owns a subset of those numbers and never renumbers.
3. **Spacing.** `\vspace{-0.7cm}` sits between every figure and its own caption, identical
   for all thirty figures.
4. **Captions.** At most three lines, manually broken, with balanced character counts.
5. **Originality.** No figure is copied from `../inputs/phase-1-six-platform-diagrams.zip`
   or `../inputs/phase-1-trial-protocol.zip`; each is a new composition whose subject is a
   patient concern.
6. **No raster.** No PNG and no JPG anywhere in the build.
7. **Real-time commits.** One commit per distinguishable file, pushed on write, inside one
   continuously updated pull request.

## Files from other directories used here

| Source | Used by | For |
|:--|:--|:--|
| [`../prompts/prompt-patient.md`](../prompts/prompt-patient.md) | all eight | the master prompt these were generated from |
| [`../template/trial-protocol-template.zip`](../template/trial-protocol-template.zip) | 1, 6, 7, 8 | the four-stage workflow, directory layout, and commit discipline |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs/phase-1-trial-protocol.zip) | all eight | the clinical protocol being advocated for, and the LaTeX style base |
| [`../inputs/phase-1-six-platform-diagrams.zip`](../inputs/phase-1-six-platform-diagrams.zip) | 1 to 5 | the five diagram vocabularies, as context only |
| [`../inputs/patient-priority-physical-ai.zip`](../inputs/patient-priority-physical-ai.zip) | 2, 5, 6, 7, 8 | the patient-as-priority premise and the bill framing |
| [`../inputs/cancer-patient-journey.zip`](../inputs/cancer-patient-journey.zip) | 1, 4 | the autonomous single-patient journey, NSCLC, distinguished from PDAC |
| [`../inputs/patient-robot-instructions.tex`](../inputs/patient-robot-instructions.tex) | 2, 3 | the ten robot-type instruction sheets, re-scoped to PDAC |
| [`../research/research-a.md`](../research/research-a.md) | 1, 3, 5 | the Gemini concern families |
| [`../research/research-b.md`](../research/research-b.md) | 1 to 5 | the sixteen ChatGPT concerns and the thirteen sources |
| [`../references/references.bib`](../references/references.bib) | 5, 6, 7, 8 | the up-to-date author references, including H. R. 9510 v5 |

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
