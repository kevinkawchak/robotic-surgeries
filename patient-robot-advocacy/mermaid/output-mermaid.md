## output-mermaid

Stage 1 narrative, run from
[`../sub-prompts/prompt-1-mermaid.md`](../sub-prompts/prompt-1-mermaid.md).

### What was produced

Nine mermaid-type diagram sources, figures 1, 3, 7, 10, 14, 19, 23, 25, and 27 of the
paper's thirty. Each is a separate file and each landed in its own commit, pushed on write.

### How the nine were chosen

The master prompt forbids an equal quota per diagram type and requires the choice to follow
the diagram's purpose and its location in the paper. Mermaid received the largest share
because the largest share of the patient's questions are ordering questions.

| Question shape | Count | Mermaid construct chosen |
|:--|:--|:--|
| What happens first, and what closes behind it | 3 | `flowchart` with gates |
| Who sends what to whom, and in which order | 1 | `sequenceDiagram` |
| What states can I be in, and how do I leave them | 1 | `stateDiagram-v2` |
| How long does this take, and when | 1 | `gantt` |
| How do these items rank on two independent axes | 1 | `quadrantChart` |
| How large are these quantities against each other | 2 | `xychart-beta`, `pie`, CI strip |

### Decisions made during the stage

1. **Figure 3 is a full page, and the parent protocol's schema is inverted.** The protocol
   draws the trial flowing through the participant. Redrawing it with participant-controlled
   nodes in Corporate Blue and sponsor-controlled nodes in white makes the balance of
   control a visual fact rather than a claim. Four of the fifteen nodes are the
   participant's; the figure does not pretend that is a majority.

2. **Figure 7 admits an honest gap.** Quadrant 4 collects the concerns that this protocol
   answers only by governance or disclosure - cancer-control effectiveness, accountability,
   the human relationship, and cost. A proponent's paper that placed every concern in
   quadrant 1 would not be credible, and the surveyed literature would contradict it.

3. **Figure 19 makes its argument by an absence.** There is no arrow from the on-premises
   model to the robot arms. The lifeline exists, the model exists, and no message connects
   them. That absence answers the single most common patient concern more convincingly than
   any label could.

4. **Figure 25 totals the burden.** The Schedule of Activities in the parent protocol is a
   matrix of crosses. Converting it to a calendar and then totalling it - about 18 visits,
   8 to 10 inpatient days, roughly 27 days of contact over 24 months - answers a question
   the protocol never asks.

5. **Figure 27 publishes the unfavourable numbers.** Panel B states that 8.2 percent of the
   1000 Phase 0 simulated procedures were halted by a safety mechanism. Panel D states that
   this study cannot move a survival curve. Both are kept because a dashboard that carried
   only favourable values would be the marketing the surveyed patients said they distrust.

6. **The NSCLC distinction is stated in the figure source, not only in the paper.** Figure 3
   adapts the structure of the author's autonomous single-patient journey, which was
   non-small cell lung cancer. The differences that matter to a PDAC patient - the
   operation, the drug, the dominant early complication, and the survival baseline - are
   named in the file itself so the distinction cannot be lost downstream.

### Palette compliance

Every figure was checked against the per-diagram budget: at most three grayscale fills, at
most two lighter shades of `#00417A`, and black fill used sparingly. The maximum grayscale
use in this stage is two; the maximum lighter-blue use is two; exactly one node across all
nine figures uses a black fill, the single halt node in Figure 1.

### Verification performed

| Check | Result |
|:--|:--|
| Nine files present, figure numbers 1, 3, 7, 10, 14, 19, 23, 25, 27 | pass |
| Every fenced block is valid Mermaid with an `%%{init}%%` palette directive | pass |
| Every file carries all seven required parts | pass |
| No figure reproduces a figure from either input archive | pass, checked against all 120 atlas figures and all 20 protocol figures |
| No PNG, no JPG, no rendered raster | pass |
| Every curved connector in the TikZ notes declares an explicit `looseness` | pass |
| Per-diagram palette budget respected | pass |

### Commits in this stage

| # | Commit | File |
|:--|:--|:--|
| 1 | Figure 1, the seven commitments | `fig-01-seven-commitments.md` |
| 2 | Figure 3, full-page journey schema | `fig-03-journey-schema.md` |
| 3 | Figure 7, concern quadrant | `fig-07-concern-quadrant.md` |
| 4 | Figure 10, endpoint to plain meaning | `fig-10-endpoint-meaning.md` |
| 5 | Figure 14, two-way eligibility gate | `fig-14-eligibility-self-selection.md` |
| 6 | Figure 19, advise-approve-execute sequence | `fig-19-advise-approve-execute.md` |
| 7 | Figure 23, consent lifecycle state machine | `fig-23-consent-lifecycle.md` |
| 8 | Figure 25, participant visit calendar | `fig-25-visit-timeline.md` |
| 9 | Figure 27, reassurance dashboard | `fig-27-reassurance-dashboard.md` |
| 10 | Stage README | `README.md` |
| 11 | This narrative | `output-mermaid.md` |

### Handoff to Stage 2

[`../plantuml/`](../plantuml) takes figures 8, 12, 15, 18, and 22. The boundary is
deliberate: where Stage 1 shows what happens, Stage 2 shows what is formally guaranteed.
Figure 19 here shows that the surgeon approves every motion; Figure 18 there shows, on a
timing axis, how long the surgeon has to intervene and how long the halt takes.
