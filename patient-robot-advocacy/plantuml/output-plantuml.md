## output-plantuml

Stage 2 narrative, run from
[`../sub-prompts/prompt-2-plantuml.md`](../sub-prompts/prompt-2-plantuml.md).

### What was produced

Five PlantUML-type diagram sources, figures 8, 12, 15, 18, and 22 of the paper's thirty.
One commit per file, pushed on write, plus a README commit and this narrative.

### The organising idea of the stage

Stage 1 answers "what happens". Stage 2 answers "what is guaranteed". The distinction is
not stylistic. A patient told that a surgeon supervises the robot has been told what
happens; a patient shown a guarded state machine, a timing budget, and a swimlaned
withdrawal path has been told what is guaranteed, by whom, and within what bound. Formal
notation is the right medium for the second kind of statement, because formal notation has
somewhere to put the guard.

### Decisions made during the stage

1. **Figure 8 changes only the actor.** Every one of the twelve use cases is already in the
   parent protocol, written as a sponsor obligation. Redrawing them with the participant as
   primary actor is the whole intervention. Ten of the twelve are exercised by the
   participant; the two that are not, pressing stop and issuing a version notice, require
   someone physically present or inside the build system, and neither can be exercised
   against the participant. The figure states that ratio rather than implying a cleaner one.

2. **Figure 12 keeps the `Cohort hold` state visible.** It would be tidier to fold the
   sentinel window into the transition guard. It is left as an explicit state because it is
   the clearest single piece of evidence that the design accepts delay in exchange for
   participant safety: a participant is never the second person at a new dose level before
   the first person's safety window has closed.

3. **Figure 15 notifies the treating oncologist on every branch.** The surveyed literature
   is consistent that the fear attached to a direct sponsor channel is displacement of the
   existing clinician relationship. Every branch of the `alt` fragment therefore carries a
   notification back to the treating oncologist, and the closing note says so explicitly.

4. **Figure 18 uses a logarithmic axis and a human comparison.** The three budgets span four
   orders of magnitude, from a 0.1 ms bus period to a 500 ms system-wide guarantee, and a
   linear axis would render the first two invisible. The blink comparison is included
   because a millisecond figure without a human referent is not reassurance, it is
   specification.

5. **Figure 22 does not pretend withdrawal is costless to the record.** Route C states that
   data already collected cannot be removed from the safety analysis, and route D states
   that aggregate safety data already reported to the FDA cannot be recalled. Both are true,
   both are unwelcome, and omitting them would have made the other two routes less
   believable.

### Verification performed

| Check | Result |
|:--|:--|
| Five files present, figure numbers 8, 12, 15, 18, 22 | pass |
| Every file opens `@startuml` and closes `@enduml` | pass |
| Every file carries a `' Figure NN.` header block and `' TikZ:` rendering notes | pass |
| Palette carried as `skinparam`, so the source renders standalone | pass |
| Formal-notation discipline table in the README, all eight rows | pass |
| Every guard in Figure 12 is a real condition, not a label | pass, 11 of 11 |
| Every curved connector in the TikZ notes declares an explicit `looseness` | pass |
| No figure reproduces a figure from either input archive | pass |
| Per-diagram palette budget respected | pass, maximum two grays and one lighter blue |
| No PNG, no JPG | pass |

### Commits in this stage

| # | Commit | File |
|:--|:--|:--|
| 1 | Figure 8, participant as primary actor | `fig-08-patient-actor-usecase.puml` |
| 2 | Figure 12, guarded participant state machine | `fig-12-participant-state-machine.puml` |
| 3 | Figure 15, booking and sponsor response | `fig-15-booking-sponsor-response.puml` |
| 4 | Figure 18, emergency-stop timing budget | `fig-18-estop-timing-budget.puml` |
| 5 | Figure 22, withdrawal activity with swimlanes | `fig-22-withdrawal-activity.puml` |
| 6 | Stage README | `README.md` |
| 7 | This narrative | `output-plantuml.md` |

### Handoff to Stage 3

[`../d2/`](../d2) takes figures 4, 5, 11, 16, 20, 26, and 29. The boundary: Stage 2 answers
"what is guaranteed"; Stage 3 answers "how much of it is there, and how does it group".
Figure 12 here shows the states a participant passes through; Figure 4 there shows every
assessment those states carry, as a true grid.
