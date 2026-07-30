# template - the workflow this build is modelled on (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Template](https://img.shields.io/badge/Template-trial--protocol--template-00417A.svg)](trial-protocol-template.zip)
[![Stages](https://img.shields.io/badge/Template%20stages-4-6C757D.svg)](.)
[![This build](https://img.shields.io/badge/This%20build%20stages-8-00417A.svg)](../sub-prompts)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

[`trial-protocol-template.zip`](trial-protocol-template.zip) is the completed
`trial-protocol` build from the author's `physical-ai-oncology-trials` repository. It is
the **process template** for this build: it defines the directory layout, the sub-prompt
convention, the per-file commit discipline, and the staged growth of a LaTeX document from
diagram sources to a polished final source set.

## What the template contains

```
trial-protocol-template/
  README.md              build hub with badges, pipeline, milestone table, directory map
  prompts/               prompt-protocol.md (master, verbatim) + output-protocol.md
  sub-prompts/           prompt-1-mermaid .. prompt-4-final-protocol (Process A output)
  mermaid/               25 Mermaid figure files + README + output-mermaid.md
  draft-protocol/        main.tex, protostyle.sty, references.bib, sections/, zip,
                         prompt-draft-protocol.md, output-draft-protocol.md, README
  full-protocol/         the same set, fully rendered
  final-protocol/        the same set, polished, plus publication/
  template/              the single-column paper template the protocol recolored
  nih-protocol/          the NIH-FDA IND/IDE protocol template, 10 markdown chunks
  research/              four dated 2026 background markdowns
```

## What this build keeps

| Template convention | Kept as |
|:--|:--|
| Master prompt filed verbatim under `prompts/` | [`../prompts/prompt-patient.md`](../prompts/prompt-patient.md) |
| Process A generates sub-prompts, Process B runs them | [`../sub-prompts/`](../sub-prompts), eight of them |
| One diagram stage before any LaTeX stage | five diagram stages, one per permitted type |
| Three LaTeX stages: draft, full, final | [`../draft-patient/`](../draft-patient), [`../full-patient/`](../full-patient), [`../final-patient/`](../final-patient) |
| Each LaTeX stage carries `main.tex`, a `.sty`, a `.bib`, `sections/`, and a zip | identical |
| Each stage files its own `prompt-*.md` and writes a paired `output-*.md` | identical |
| One commit per distinguishable file, pushed in real time | identical |
| Second-to-last commit of a stage fixes all errors; last commit does repository updates | identical |
| Corporate Blue `#00417A` plus Professional Gray `#6C757D` plus Classic White | identical, extended by three grays and two lighter blues |

## What this build changes

| Change | Reason |
|:--|:--|
| `mermaid/` becomes five directories: [`../mermaid/`](../mermaid), [`../plantuml/`](../plantuml), [`../d2/`](../d2), [`../diagrams-python/`](../diagrams-python), [`../graphviz/`](../graphviz) | the master prompt requires five diagram types, chosen by purpose rather than by quota |
| Four sub-prompts become eight | one per diagram type plus one per LaTeX stage |
| `draft-protocol` / `full-protocol` / `final-protocol` become `draft-patient` / `full-patient` / `final-patient` | the deliverable is a patient advocacy paper, not a protocol |
| No `publication/` subdirectory under `final-patient/` | explicitly excluded by the master prompt |
| No `nih-protocol/` directory | the NIH-FDA section order is inherited through [`../inputs/phase-1-trial-protocol.zip`](../inputs), which already applied it |
| The template's own `template/` subdirectory is not reproduced | [`../inputs/phase-1-trial-protocol.zip`](../inputs) is the paper template for this build |
| Thirteen `sections/*.tex` files instead of the template's six-section paper layout | one `.tex` per paper section, per Rule 6 |
| A patient-advocacy cover page replaces the protocol cover page | the master prompt asks for visual changes that help patients, especially on the cover |
| Figures numbered 1 to 30 continuously across five type directories | the template restarted numbering per platform; this paper does not |

## Directory-by-directory correspondence

| Template directory | This build | Note |
|:--|:--|:--|
| `prompts/` | [`../prompts/`](../prompts) | same convention, `prompt-patient.md` and `output-patient.md` |
| `sub-prompts/` | [`../sub-prompts/`](../sub-prompts) | four becomes eight |
| `mermaid/` | [`../mermaid/`](../mermaid) + four siblings | one directory per diagram type |
| `draft-protocol/` | [`../draft-patient/`](../draft-patient) | bracketed scaffold, thirteen sections |
| `full-protocol/` | [`../full-patient/`](../full-patient) | populated, thirty TikZ figures |
| `final-protocol/` | [`../final-patient/`](../final-patient) | polished, no `publication/` |
| `research/` | [`../research/`](../research) | two dated markdowns instead of four |
| `inputs/` | [`../inputs/`](../inputs) | five author sources |
| n/a | [`../references/`](../references) | new: the author's up-to-date bibliography |

## Files from other directories used here

| Source | Used for |
|:--|:--|
| [`../prompts/prompt-patient.md`](../prompts/prompt-patient.md) | the master prompt that named this template |
| [`../sub-prompts/`](../sub-prompts) | the eight sub-prompts generated from this template's four |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) | the paper template, which the process template wraps |

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
