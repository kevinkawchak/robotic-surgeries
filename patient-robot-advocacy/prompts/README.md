# prompts - the master prompt and its output (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Prompt](https://img.shields.io/badge/Master%20prompt-verbatim-00417A.svg)](prompt-patient.md)
[![Output](https://img.shields.io/badge/Output-narrative-6C757D.svg)](output-patient.md)
[![Model](https://img.shields.io/badge/Model-Claude%20Code%20Opus%205-00417A.svg)](.)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

Two files, and only two.

| File | Contents |
|:--|:--|
| [`prompt-patient.md`](prompt-patient.md) | a `## prompt-patient` heading followed by the entire master prompt, word for word, and nothing else |
| [`output-patient.md`](output-patient.md) | an `## output-patient` heading followed by the entire Claude Code markdown output of that prompt, and nothing else |

`output-patient.md` records the assistant's narrative output only. It does not reproduce
any generated source file; those live in their own directories.

## What the master prompt asks for

| Requirement | Where it is satisfied |
|:--|:--|
| A Phase 1 PDAC Patient Robot Advocacy paper relieving patient concerns with surgical robots | [`../final-patient/`](../final-patient) |
| Context from the Top 5 Gemini and Top 16 ChatGPT concern markdowns | [`../research/`](../research), § 3 of the paper |
| 30 machine-readable diagrams across five types, numbered 1 to 30 | [`../mermaid/`](../mermaid), [`../plantuml/`](../plantuml), [`../d2/`](../d2), [`../diagrams-python/`](../diagrams-python), [`../graphviz/`](../graphviz) |
| The `trial-protocol-template` workflow, adapted | [`../sub-prompts/`](../sub-prompts), [`../template/`](../template) |
| draft, full, final stages, each with its own compilable `.tex` and zip | [`../draft-patient/`](../draft-patient), [`../full-patient/`](../full-patient), [`../final-patient/`](../final-patient) |
| A patient-advocacy cover page keeping the protocol colour scheme | `main.tex` of each paper stage |
| Real-time commits and one continuously updated pull request | one commit per distinguishable file, pushed on write |
| v1.0.0 documentation, changelog, and release notes | root [`README.md`](../../README.md), [`CHANGELOG.md`](../../CHANGELOG.md), [`releases.md`](../../releases.md) |

## Process A and Process B

**Process A** read the master prompt and wrote the eight sub-prompts in
[`../sub-prompts/`](../sub-prompts). **Process B** executed those eight sub-prompts in
order:

| Order | Sub-prompt | Stage directory |
|:--|:--|:--|
| 1 | `prompt-1-mermaid.md` | [`../mermaid/`](../mermaid) |
| 2 | `prompt-2-plantuml.md` | [`../plantuml/`](../plantuml) |
| 3 | `prompt-3-d2.md` | [`../d2/`](../d2) |
| 4 | `prompt-4-diagrams-python.md` | [`../diagrams-python/`](../diagrams-python) |
| 5 | `prompt-5-graphviz.md` | [`../graphviz/`](../graphviz) |
| 6 | `prompt-6-draft-patient.md` | [`../draft-patient/`](../draft-patient) |
| 7 | `prompt-7-full-patient.md` | [`../full-patient/`](../full-patient) |
| 8 | `prompt-8-final-patient.md` | [`../final-patient/`](../final-patient) |

Each LaTeX stage also files its own sub-prompt verbatim as `prompt-<stage>.md` and writes a
paired `output-<stage>.md`, exactly as the process template did.

## Files from other directories used here

| Source | Used for |
|:--|:--|
| [`../template/trial-protocol-template.zip`](../template) | the `prompts/` plus `sub-prompts/` convention this directory follows |
| [`../sub-prompts/`](../sub-prompts) | the eight sub-prompts Process A wrote from `prompt-patient.md` |

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
