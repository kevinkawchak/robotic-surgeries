# diagrams-python - Stage 4, Diagrams (Python)-type sources (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Stage](https://img.shields.io/badge/Stage-4%20of%208-00417A.svg)](../sub-prompts/prompt-4-diagrams-python.md)
[![Figures](https://img.shields.io/badge/Figures-4%20of%2030-00417A.svg)](.)
[![Type](https://img.shields.io/badge/Type-Diagrams%20(Python)--type-6C757D.svg)](.)
[![Lint](https://img.shields.io/badge/ruff%20format%20%2B%20check-passing-brightgreen.svg)](.)
[![Import](https://img.shields.io/badge/Import-guarded%2C%20runs%20anywhere-6C757D.svg)](.)
[![Raster](https://img.shields.io/badge/Raster%20images-none-6C757D.svg)](.)
[![Release](https://img.shields.io/badge/Release-v1.0.0-orange.svg)](../../releases.md)

Stage 4 of the eight-stage build, run from
[`../sub-prompts/prompt-4-diagrams-python.md`](../sub-prompts/prompt-4-diagrams-python.md).
Four of the paper's thirty figures are Diagrams (Python)-type, the smallest share, and
deliberately so: this idiom is unbeatable for one narrow question and wrong for every
other. The question is **where does this physically live**.

## The four figures

| File | Fig | Construct | § | Patient concern answered |
|:--|:--|:--|:--|:--|
| [`fig_09_concern_locations.py`](fig_09_concern_locations.py) | 9 | clustered node map | 3 | all twenty-one, by giving each a physical address |
| [`fig_17_operating_room_stack.py`](fig_17_operating_room_stack.py) | 17 | deployment, full page | 7 | cybersecurity and network reach; who is controlling |
| [`fig_24_data_pipeline.py`](fig_24_data_pipeline.py) | 24 | pipeline with access overlay | 9 | privacy, recording, and secondary use |
| [`fig_30_post_trial_continuity.py`](fig_30_post_trial_continuity.py) | 30 | lifecycle across three time zones | 12 | cost, and post-trial burden |

## The argument each figure makes by an absence

Three of the four figures make their central claim not with a node but with a **missing
edge**, which is a property this idiom has and the other four do not.

| Figure | The absent edge | What its absence asserts |
|:--|:--|:--|
| 9 | on-premises model to the network boundary | during a procedure there is no route out of the building |
| 17 | the same edge, drawn and struck through | three things cross the boundary before a procedure and nothing crosses during it |
| 24 | any principal to the de-identified store for commercial training | data is not used to train commercial models without a separate consent |
| 30 | device support past study closure | an obligation that ends is drawn ending, rather than quietly omitted |

## Code discipline

Every file is a runnable, import-guarded `mingrammer/diagrams` script.

| Property | Why |
|:--|:--|
| `from __future__ import annotations` | the file parses on Python 3.10, 3.11, and 3.12 alike |
| Imports inside `build()` behind `try` / `except ImportError` | the file is importable and lint-clean on a machine with no `diagrams` package, and returns without side effects |
| `Diagram(..., show=False, outformat="svg")` | nothing is opened, and no PNG or JPG can be produced |
| Palette as module-level constants | one definition per colour, referenced everywhere, so a palette audit is a grep |
| Protocol limits as a module-level dict | the numbers printed on the tiles are the numbers in the protocol, in one place |
| 4-space indent, double quotes, no wildcard imports | `ruff format --check` and `ruff check` both pass |
| No file above 100 characters per line except two long f-strings inside string literals | keeps the source readable in a side-by-side diff |

Verified locally with `ruff format --check .` and `ruff check .`, both passing on all four
files. The repository CI (`lint-and-format` on Python 3.10, 3.11, and 3.12) runs against
`2030-gbm-1min` only, so these files are outside its scope; they are held to the same
standard anyway.

## Palette budget, verified per figure

| Fig | Grayscale fills used (max 3) | Lighter blues used (max 2) | Black strokes |
|:--|:--|:--|:--|
| 9 | 2 | 1 | 1 edge |
| 17 | 2 | 1 | 4 edges |
| 24 | 2 | 1 | 1 edge |
| 30 | 2 | 1 | 3 edges |

Black is used for strokes on the halt path and on obligations that end, never as a node
fill, which keeps the sparing-use rule satisfied while letting the most consequential edges
read first.

## Files from other directories used here

| Source | Used by | For |
|:--|:--|:--|
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-06-intervention.tex` | 9, 17 | the eight-arm platform, the 10 kHz heartbeat bus, force caps, on-premises inference |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-08-assessments.tex` | 24 | the assessment and telemetry capture set |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-10-oversight.tex` | 9, 24 | the hash-chained audit trail and 21 CFR part 11 controls |
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `sections/sec-11-additional.tex` | 30 | the post-trial and cost provisions this figure expands |
| [`../inputs/cancer-patient-journey.zip`](../inputs) | 17, 24 | the autonomous single-patient journey stack, NSCLC, re-scoped to PDAC and stated as such in the module docstring |
| [`../inputs/phase-1-six-platform-diagrams.zip`](../inputs) `dxstyle.sty` | all four | the `dg*` vocabulary and the twenty vector pictograms, as context only |
| [`../research/research-a.md`](../research) | 9, 30 | Gemini families 4 and 6 |
| [`../research/research-b.md`](../research) | all four | concerns 1, 2, 10, 11, 13, 16 |
| [`../references/references.bib`](../references) | 30 | `hr9510billv5` and `natlpaiplatf` for the post-trial provisions |

## Rendering these sources outside LaTeX

`pip install diagrams graphviz` then `python fig_NN_*.py` writes an SVG next to the script.
Without the package, each script imports cleanly and `build()` returns immediately. The
paper does not invoke Python: it redraws each figure natively in TikZ using the `dg*`
vocabulary and the vector pictograms, following the rendering notes in the docstring.

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
