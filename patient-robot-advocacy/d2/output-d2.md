## output-d2

Stage 3 narrative, run from [`../sub-prompts/prompt-3-d2.md`](../sub-prompts/prompt-3-d2.md).

### What was produced

Seven D2-type diagram sources, figures 4, 5, 11, 16, 20, 26, and 29 of the paper's thirty.
Two of the seven are full-page figures. One commit per file, pushed on write, plus a README
commit and this narrative.

### The organising idea of the stage

Stage 1 answers "what happens", Stage 2 answers "what is guaranteed", and Stage 3 answers
"how much of it is there, and how does it group". That third question is answered badly by
prose and worse by flowcharts. A patient who is told the concerns about surgical robots are
"well understood" has learned nothing; a patient shown twenty-one concerns in six disjoint
containers, each with a section number printed inside it, has learned that the set is
finite and addressed.

### Decisions made during the stage

1. **Figure 4 keeps the grid flat.** It was tempting to group the eight visit columns into
   phases. A schedule has no ownership hierarchy, and inventing containers would have
   implied one. The only structural addition is the totals row, which answers a question
   the parent protocol never asks: how many hours does this cost you.

2. **Figure 5 fixes the count at twenty-one and shows the fill key.** Six Gemini families
   plus sixteen ChatGPT concerns overlap on five items. De-duplicating gives twenty-one.
   The fill key then states the uncomfortable breakdown: seven answered by a hard numeric
   limit, nine by a procedural guarantee, five by governance or disclosure only. A figure
   that had coloured all twenty-one the same would have been dishonest.

3. **Figure 11 adds a row that no clinical protocol carries.** The `plain_meaning` row is
   the paper's editorial position expressed as a schema field: an endpoint that cannot be
   restated as a sentence about the participant has not yet been explained to them. Making
   it a required field of the record forces it to be filled for every endpoint, including
   the exploratory one.

4. **Figure 16 makes the accumulation visible.** Layers that replace each other would say
   the participant trades one choice for the next. Layers that accumulate say all five
   remain live, which is the actual protocol position, and the closing note draws the
   conclusion the layout implies: not one of the five is exercised on the day of surgery.

5. **Figure 20 pairs the two limits that are individually insufficient.** A force cap does
   not prevent an arm entering a vascular corridor, and a corridor does not cap the force
   applied inside permitted tissue. Drawing them as sibling containers inside one envelope
   makes the pairing structural rather than asserted.

6. **Figure 26 tells the participant what they will not meet.** Four of the ten robot types
   in the source instruction set are not used in this protocol. Listing them, greyed, with
   the reason, is more useful than silently dropping them, because a participant who has
   read about steerable needle robots elsewhere needs to know this study does not use one.

7. **Figure 29 enforces one accountable party per row.** The invariant is checked: nine
   rows, nine single A assignments. The concern in the literature is not that no one is
   responsible; it is that everyone is, which is the same thing. The far-right column, the
   only black fill in the figure, converts the matrix into an instruction.

### Verification performed

| Check | Result |
|:--|:--|
| Seven files present, figure numbers 4, 5, 11, 16, 21, 26, 29 | pass |
| Every file is valid D2 with a `d2-config.theme-overrides` palette block | pass |
| Every file carries a `# Figure NN.` header block and `# TikZ:` rendering notes | pass |
| Containment discipline table in the README, all seven rows | pass |
| Grid discipline, five requirements across four grid figures | pass |
| Figure 29 invariant, exactly one A per row | pass, 9 of 9 |
| Figure 5 concern count reconciles to twenty-one after de-duplication | pass |
| Figure 26 carries no raster image and no `\includegraphics` | pass |
| Every curved connector in the TikZ notes declares an explicit `looseness` | pass |
| Per-diagram palette budget respected | pass, maximum two grays and two lighter blues |
| No figure reproduces a figure from either input archive | pass |

### Commits in this stage

| # | Commit | File |
|:--|:--|:--|
| 1 | Figure 4, patient-facing Schedule of Activities grid | `fig-04-soa-patient-grid.d2` |
| 2 | Figure 5, twenty-one concerns in six containers | `fig-05-concern-families.d2` |
| 3 | Figure 11, endpoint registry as typed records | `fig-11-endpoint-registry.d2` |
| 4 | Figure 16, five choices as progressive layers | `fig-16-five-choices-layers.d2` |
| 5 | Figure 20, force caps and no-fly envelope | `fig-20-force-nofly-envelope.d2` |
| 6 | Figure 26, ten robot instruction cards | `fig-26-robot-instruction-cards.d2` |
| 7 | Figure 29, responsibility matrix | `fig-29-responsibility-matrix.d2` |
| 8 | Stage README | `README.md` |
| 9 | This narrative | `output-d2.md` |

### Handoff to Stage 4

[`../diagrams-python/`](../diagrams-python) takes figures 9, 17, 25, and 30. The boundary:
Stage 3 answers "how much of it is there"; Stage 4 answers "where does it physically live".
Figure 20 here bounds what the arms may do; Figure 17 there shows the room the arms are in,
the cabinet the model runs on, and the network cable that is not connected.
