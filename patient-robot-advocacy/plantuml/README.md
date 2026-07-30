# plantuml - Stage 2, PlantUML-type diagram sources (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Stage](https://img.shields.io/badge/Stage-2%20of%208-00417A.svg)](../sub-prompts/prompt-2-plantuml.md)
[![Figures](https://img.shields.io/badge/Figures-5%20of%2030-00417A.svg)](.)
[![Type](https://img.shields.io/badge/Type-PlantUML--type-6C757D.svg)](.)
[![Constructs](https://img.shields.io/badge/Constructs-use%20case%20%7C%20state%20%7C%20sequence%20%7C%20timing%20%7C%20activity-6C757D.svg)](.)
[![Raster](https://img.shields.io/badge/Raster%20images-none-6C757D.svg)](.)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

Stage 2 of the eight-stage build, run from
[`../sub-prompts/prompt-2-plantuml.md`](../sub-prompts/prompt-2-plantuml.md). Five of the
paper's thirty figures are PlantUML-type. PlantUML is used wherever the patient's question
needs **formal notation with a defined semantics**: not what happens, but what is
guaranteed, under what guard, within what budget.

## The five figures

| File | Fig | Construct | § | Patient concern answered |
|:--|:--|:--|:--|:--|
| [`fig-08-patient-actor-usecase.puml`](fig-08-patient-actor-usecase.puml) | 8 | use case | 3 | loss of the human element; surgeon-patient trust |
| [`fig-12-participant-state-machine.puml`](fig-12-participant-state-machine.puml) | 12 | state machine with guards | 5 | unknown and experimental risks; treatment choice |
| [`fig-15-booking-sponsor-response.puml`](fig-15-booking-sponsor-response.puml) | 15 | sequence with activation bars | 6 | practical burdens; access and choice |
| [`fig-18-estop-timing-budget.puml`](fig-18-estop-timing-budget.puml) | 18 | timing diagram | 7 | human override and rescue capability |
| [`fig-22-withdrawal-activity.puml`](fig-22-withdrawal-activity.puml) | 22 | activity with swimlanes | 8 | privacy and secondary data use; post-trial burden |

## Why these five, and not others

| Figure | The alternative that was rejected, and why |
|:--|:--|
| 8 | A Mermaid flowchart of safeguards would show the safeguards but not who may invoke them. A use case diagram's entire premise is actor-to-capability, so reassigning the primary actor from sponsor to participant is a substantive claim rather than a relabelling. |
| 12 | A Mermaid state diagram shows the states. Only PlantUML notation carries the **guard** on each transition, and the guards are where the protection lives: `[sentinel window closed]`, `[no DLT declared]`, `[USL >= 7.0 verified]`. |
| 15 | A D2 sequence would show ordering. Only activation bars show **blocking**, which is the point: the participant is never the party left waiting without a stated service level. |
| 18 | Every other permitted type treats time as an ordering. A timing diagram treats it as a metric axis, and the claim being made here is quantitative: 0.1 ms bus period, 3 ms cross-arm halt, 500 ms system-wide guarantee. |
| 22 | A Graphviz decision tree would branch correctly but could not assign responsibility. Swimlanes answer "who does this" and "what happens to my record" in one figure. |

## Formal-notation discipline, verified

| Requirement | Figures | Verified |
|:--|:--|:--|
| Stick actors for humans, never boxes | 8, 15 | yes |
| Initial and final pseudostates present | 12, 22 | yes |
| Every transition carries a guard or a trigger | 12 | yes, 11 of 11 |
| Activation bars on every sequence lifeline | 15 | yes, 5 of 5 |
| `<<include>>` and `<<extend>>` used with correct direction | 8 | yes |
| Fork and join bars balanced | 22 | yes |
| Timing diagram uses a metric, not ordinal, axis | 18 | yes, logarithmic milliseconds |
| Folded notes carry constraints, not decoration | all five | yes |

## Palette budget, verified per figure

| Fig | Grayscale fills used (max 3) | Lighter blues used (max 2) | Black fill nodes |
|:--|:--|:--|:--|
| 8 | 1 | 1 | 0 |
| 12 | 2 | 1 | 0 |
| 15 | 1 | 1 | 0 |
| 18 | 2 | 1 | 0 |
| 22 | 2 | 1 | 2 (fork and join bars only) |

Corporate Blue `#00417A`, Professional Gray `#6C757D`, and Classic White are outside the
budget and are used in every figure. The grayscale fills are `#E9ECEF` light, `#CED4DA`
medium, and `#9AA1A8` medium-dark; the lighter blues are `#3C7DB2` and `#DCE8F1`.

## Files from other directories used here

| Source | Used by | For |
|:--|:--|:--|
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-04-design.tex` | 12 | the 3+3 escalation rule and the staggered sentinel enrollment |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-05-population.tex` | 12, 15 | § 5.1, § 5.2, and the § 5.4 minimal data set |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-06-intervention.tex` | 18 | the 10 kHz heartbeat bus, the 3 ms cross-arm and 500 ms system-wide e-stop budgets |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-07-discontinuation.tex` | 22 | the withdrawal routes and their data consequences |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-10-oversight.tex` | 8, 22 | the oversight bodies and the hash-chained record |
| [`../inputs/phase-1-six-platform-diagrams.zip`](../inputs) `dxstyle.sty` | all five | the `uml*` vocabulary and the `\umlactor` and `\umlcomp` macros, as context only |
| [`../inputs/patient-priority-physical-ai.zip`](../inputs) | 8, 15 | the patient-as-primary-actor premise and the direct sponsor channel |
| [`../inputs/patient-robot-instructions.tex`](../inputs) | 15 | what the participant is told to do before an appointment |
| [`../research/research-b.md`](../research) | all five | concerns 1, 3, 7, 8, 10, 14, 16 and their citations |
| [`../references/references.bib`](../references) | 15 | `hr9510billv5`, the legislation citation for the direct channel |

## Rendering these sources outside LaTeX

Each `.puml` file is valid PlantUML and carries its palette as `skinparam` declarations, so
`plantuml -tsvg fig-NN-*.puml` reproduces the intended appearance without editing. The
paper itself does not invoke PlantUML: it redraws each figure natively in TikZ using the
`uml*` vocabulary, following the `' TikZ:` comment block at the head of each file.

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
