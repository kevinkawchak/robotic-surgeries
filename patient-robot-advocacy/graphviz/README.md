# graphviz - Stage 5, Graphviz-type diagram sources (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Stage](https://img.shields.io/badge/Stage-5%20of%208-00417A.svg)](../sub-prompts/prompt-5-graphviz.md)
[![Figures](https://img.shields.io/badge/Figures-5%20of%2030-00417A.svg)](.)
[![Type](https://img.shields.io/badge/Type-Graphviz--type-6C757D.svg)](.)
[![Constructs](https://img.shields.io/badge/Constructs-DAG%20%7C%20bipartite%20%7C%20decision%20tree%20%7C%20fault%20tree%20%7C%20provenance-6C757D.svg)](.)
[![Invariants](https://img.shields.io/badge/Graph%20invariants-stated%20%2B%20verified-brightgreen.svg)](.)
[![Raster](https://img.shields.io/badge/Raster%20images-none-6C757D.svg)](.)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

Stage 5 of the eight-stage build, and the last of the diagram stages, run from
[`../sub-prompts/prompt-5-graphviz.md`](../sub-prompts/prompt-5-graphviz.md). Five of the
paper's thirty figures are Graphviz-type. Graphviz is used wherever the patient's question
is **what depends on what, and can you prove it**: pure graph structure with a stated
invariant and no narrative sugar.

## The five figures

| File | Fig | Construct | § | Patient concern answered |
|:--|:--|:--|:--|:--|
| [`fig-02-accountability-dag.dot`](fig-02-accountability-dag.dot) | 2 | rooted DAG | 1 | who is to blame; responsibility if harmed |
| [`fig-06-concern-to-clause.dot`](fig-06-concern-to-clause.dot) | 6 | bipartite map, full page | 3 | all twenty-one, wired to their answering clause |
| [`fig-13-escalation-decision-tree.dot`](fig-13-escalation-decision-tree.dot) | 13 | decision tree with record leaves | 5 | experimental risk; being among the first |
| [`fig-21-hazard-barrier-fault-tree.dot`](fig-21-hazard-barrier-fault-tree.dot) | 21 | fault tree, AND and OR gates | 7 | malfunction and unintended actions |
| [`fig-28-evidence-provenance.dot`](fig-28-evidence-provenance.dot) | 28 | provenance DAG, record nodes | 10 | hype; cancer-control effectiveness |

## Graph invariants, stated in the source and verified

The master prompt requires graph discipline. Each file states its invariant in the header
comment block so [`../final-patient/`](../final-patient) can re-verify it, and each is
verified here.

| Fig | Invariant | Why it is the argument | Verified |
|:--|:--|:--|:--|
| 2 | Acyclic | No body in the chart can be its own reviewer. A cycle would be exactly the accountability failure the concern describes. | yes, topological sort succeeds |
| 6 | Bipartite | No edge joins two concerns and no edge joins two clauses. A concern answered with another concern is not answered. | yes, two-colouring succeeds; 24 edges, all cross-partition |
| 13 | Tree | Exactly one path from the root to each leaf, so the dose rule is auditable rather than interpretable. | yes, every non-root node has exactly one structural parent |
| 20 | Terminating, typed gates | Every path ends in a basic event; every gate declares AND or OR. An OR gate with one input is a single point of failure and is drawn as one. | yes, 10 basic events, 5 typed gates, 0 dangling |
| 28 | Acyclic, no unsourced value | A value node with no incoming edge would be a number with no source. There are none. | yes, 9 values, 9 sourced |

## What each figure refuses to soften

| Figure | The uncomfortable thing it draws anyway |
|:--|:--|
| 2 | Only three obligations point back at the participant. The chart does not pretend the participant sits above the FDA; it shows what the participant is actually owed. |
| 6 | Three of the twenty-four edges are dashed, meaning governance or disclosure only. Concerns 18, 20, and 21 have no hard limit behind them. |
| 13 | The tree includes a `Study pause, DSMB convenes` terminal. A dose-escalation figure that had no stopping leaf would be a marketing diagram. |
| 20 | Barrier 5 is filled medium-dark gray and labelled `SINGLE BARRIER ONLY`: registration drift beyond 2 mm is caught by the deterministic gate alone. The figure names it as a gap. |
| 28 | Two of the nine quoted values are class S, author simulation rather than human data. The rule node states that, in black, at the foot of the figure. |

## Graphviz idiom respected

Times labels, thin black strokes, plain ellipses for ordinary nodes, ruled record boxes for
structured nodes, dashed `subgraph cluster_*` with a corner title, `rankdir` declared,
`rank=same` used to lock ranks, `dir=back` on the fault tree so the arrows read from cause
to effect in the conventional direction, and `constraint=false` on the three back-reference
edges of Figure 2 so they do not distort the rank assignment.

## Palette budget, verified per figure

| Fig | Grayscale fills used (max 3) | Lighter blues used (max 2) | Black fill nodes |
|:--|:--|:--|:--|
| 2 | 2 | 2 | 1 (the terminal obligation) |
| 6 | 2 | 2 | 0 |
| 13 | 2 | 2 | 1 (the study-pause terminal) |
| 20 | 3 | 1 | 1 (the top event) |
| 28 | 2 | 2 | 1 (the provenance rule) |

Figure 21 is the only figure in the paper that uses all three grayscale fills, and it does
so to grade barrier strength: light for an intact barrier annotation, medium for an OR gate,
medium-dark for the single-barrier gap. Each black fill marks the one node in its figure a
reader should carry away.

## Files from other directories used here

| Source | Used by | For |
|:--|:--|:--|
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-00-compliance.tex` | 2 | the compliance spine and the oversight bodies |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-04-design.tex` | 13 | the 3+3 rule and the staggered sentinel enrollment |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-06-intervention.tex` | 20 | force caps, no-fly gating, heartbeat bus, e-stop budgets |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-09-statistics.tex` | 28 | the analysis populations and the quoted comparator values |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-10-oversight.tex` | 2 | the DSMB, the Physical AI Safety Review Committee, and the IRB route |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `references.bib` | 28 | `Siegel2025`, `DutchCohort2025`, and the citation-key format |
| [`../inputs/patient-priority-physical-ai.zip`](../inputs) | 2 | the premise that inverts the root of the accountability chart |
| [`../inputs/phase-1-six-platform-diagrams.zip`](../inputs) `dxstyle.sty` | all five | the `gv*` vocabulary, as context only |
| [`../research/research-a.md`](../research) | 2, 6, 20 | Gemini families 2, 3, and 5 |
| [`../research/research-b.md`](../research) | 6, 13, 28 | the sixteen numbered concerns and their thirteen sources |
| [`../references/references.bib`](../references) | 28 | `pdac060s2030`, `onpremwhippl`, and the author-work provenance targets |

## Rendering these sources outside LaTeX

Each `.dot` file is valid DOT. `dot -Tsvg fig-NN-*.dot -o out.svg` renders Figures 2, 13,
20, and 28; Figure 6 is a `graph` rather than a `digraph` and renders the same way. The
paper does not invoke Graphviz: it redraws each figure natively in TikZ using the `gv*`
vocabulary, following the `// TikZ:` comment block at the head of each file.

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
