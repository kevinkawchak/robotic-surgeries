# d2 - Stage 3, D2-type diagram sources (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Stage](https://img.shields.io/badge/Stage-3%20of%208-00417A.svg)](../sub-prompts/prompt-3-d2.md)
[![Figures](https://img.shields.io/badge/Figures-7%20of%2030-00417A.svg)](.)
[![Type](https://img.shields.io/badge/Type-D2--type-6C757D.svg)](.)
[![Constructs](https://img.shields.io/badge/Constructs-grid%20%7C%20containers%20%7C%20sql__table%20%7C%20layers-6C757D.svg)](.)
[![Full page](https://img.shields.io/badge/Full--page%20figures-2-00417A.svg)](.)
[![Raster](https://img.shields.io/badge/Raster%20images-none-6C757D.svg)](.)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

Stage 3 of the eight-stage build, run from
[`../sub-prompts/prompt-3-d2.md`](../sub-prompts/prompt-3-d2.md). Seven of the paper's
thirty figures are D2-type, the second largest share, because a surprising amount of what a
patient needs is **quantity and grouping** rather than sequence: how many concerns are
there, how many visits, how many choices, how many of the ten robots will I actually meet.

## The seven figures

| File | Fig | Construct | § | Patient concern answered |
|:--|:--|:--|:--|:--|
| [`fig-04-soa-patient-grid.d2`](fig-04-soa-patient-grid.d2) | 4 | true grid, 8 by 13 | 2 | practical burden; what actually happens at each visit |
| [`fig-05-concern-families.d2`](fig-05-concern-families.d2) | 5 | nested containers | 3 | all twenty-one, by making the set finite |
| [`fig-11-endpoint-registry.d2`](fig-11-endpoint-registry.d2) | 11 | `sql_table` with relations | 4 | cancer-control effectiveness; hype |
| [`fig-16-five-choices-layers.d2`](fig-16-five-choices-layers.d2) | 16 | layers and steps | 6 | treatment choice; who is controlling |
| [`fig-20-force-nofly-envelope.d2`](fig-20-force-nofly-envelope.d2) | 20 | container with measurement grid | 7 | malfunction; vascular injury |
| [`fig-26-robot-instruction-cards.d2`](fig-26-robot-instruction-cards.d2) | 26 | card grid, 2 by 5, full page | 9 | who is controlling; practical burden |
| [`fig-29-responsibility-matrix.d2`](fig-29-responsibility-matrix.d2) | 29 | grid matrix, 7 by 10 | 11 | responsibility if something goes wrong; team experience |

## Containment discipline

The master prompt requires that containment carry meaning. In every figure of this stage,
nothing that belongs to the participant is drawn inside a container owned by the sponsor,
the site, or the regulator.

| Figure | What the containment asserts |
|:--|:--|
| 4 | The grid has no container hierarchy at all, because a schedule is flat. Inventing one would have implied ownership that does not exist. |
| 5 | Six disjoint concern families, jointly exhaustive of the surveyed literature. No concern appears in two containers, which is why the count is exactly twenty-one. |
| 11 | Endpoint records sit outside the analysis-population record they reference. A foreign key is a relation, not containment, and drawing it as containment would have implied that the endpoint definition depends on who is in the population. |
| 16 | Each layer contains one choice and its consequence, and layers accumulate rather than replace, so no later layer can silently withdraw an earlier choice. |
| 21 | The force limits and the no-fly geometry sit in two sibling containers inside one envelope, because either alone is insufficient: a force cap does not stop an arm entering a corridor, and a corridor does not cap force. |
| 26 | Ten sibling cards with no parent grouping, because the ten robot types are not a hierarchy and grouping them by likelihood would have buried the four that are not used. |
| 29 | The matrix has no containment; roles are columns, not containers, so no role can be shown as containing the participant. |

## Grid discipline, verified

| Requirement | Figures | Verified |
|:--|:--|:--|
| Declared rows and columns, no free-floating cells | 4, 21, 26, 29 | yes |
| No cell straddles two columns | 4, 21, 26, 29 | yes |
| No arrow crosses a cell boundary without a labelled port | 21 | yes, the two cross-container annotations are labelled |
| Header row and label column visually distinct from data cells | 4, 21, 29 | yes |
| Exactly one accountable party per row | 29 | yes, 9 of 9 rows |

## Palette budget, verified per figure

| Fig | Grayscale fills used (max 3) | Lighter blues used (max 2) | Black fill cells |
|:--|:--|:--|:--|
| 4 | 1 | 2 | 0 |
| 5 | 1 | 2 | 0 |
| 11 | 1 | 2 | 0 |
| 16 | 1 | 2 | 0 |
| 21 | 2 | 2 | 1 (the invariant strip) |
| 26 | 2 | 2 | 0 |
| 29 | 1 | 2 | 1 column (the "you call" column) |

The two black-fill uses are deliberate and both carry the single most actionable content in
their figure: the operative invariant in Figure 20, and the "who you call" column in
Figure 29.

## Files from other directories used here

| Source | Used by | For |
|:--|:--|:--|
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-01-summary.tex` | 4 | the Schedule of Activities matrix this figure re-expresses |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-03-objectives.tex` | 11 | the endpoint definitions and their timepoints |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-06-intervention.tex` | 21 | tip-force caps, cumulative cap, no-fly gating on the SMV and portal vein |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-09-statistics.tex` | 11 | the analysis populations |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-10-oversight.tex` | 29 | the oversight bodies and their authorities |
| [`../inputs/patient-robot-instructions.tex`](../inputs) | 26 | all ten instruction sheets, re-scoped to PDAC and stripped of raster images |
| [`../inputs/patient-priority-physical-ai.zip`](../inputs) | 16, 29 | the participant-held choices and the accountability premise |
| [`../inputs/phase-1-six-platform-diagrams.zip`](../inputs) `dxstyle.sty` | all seven | the `d2*` vocabulary, as context only |
| [`../research/research-a.md`](../research) | 5 | the six Gemini concern families that name the containers |
| [`../research/research-b.md`](../research) | 5, 11, 16, 26, 29 | the sixteen numbered concerns, de-duplicated into the twenty-one |
| [`../references/references.bib`](../references) | 26 | `h2pancrevvuq` and `humanoid4sit` for the humanoid and cobot cards |

## Rendering these sources outside LaTeX

Each `.d2` file is valid D2 and declares its palette through `d2-config.theme-overrides`,
so `d2 fig-NN-*.d2 out.svg` reproduces the intended appearance. The paper does not invoke
D2: it redraws each figure natively in TikZ using the `d2*` vocabulary, following the
`# TikZ:` comment block at the head of each file.

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
