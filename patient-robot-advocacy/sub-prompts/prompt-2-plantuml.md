## prompt-2-plantuml

**Stage 2 of 8.** Output directory: [`../plantuml/`](../plantuml). Produces the
**PlantUML-type** machine-readable diagram sources for the Patient Robot Advocacy paper.

### Objective

Author the PlantUML-type diagram sources. PlantUML is chosen wherever the patient's
question needs **formal notation with a defined semantics** - who the actors are, what
states a participant can be in, what a guaranteed latency budget actually guarantees, and
what the alternative branches of an activity are. A patient who is told "the surgeon can
always stop it" is reassured by a timing diagram in a way that prose cannot match.

### Figure allocation (5 of 30)

| Fig | PlantUML construct | Paper section | Patient-advocacy perspective |
|:--|:--|:--|:--|
| 8 | use case (`@startuml` actors + ellipses) | § 3 Concerns | Patient as the primary actor of every safeguard |
| 12 | state machine | § 5 Design | Participant status, screening to end of study |
| 15 | sequence with activation bars | § 6 Who joins | 24/7 booking and real-time sponsor response |
| 18 | timing diagram | § 7 Operating room | Emergency-stop latency budget, 3 ms to 500 ms |
| 22 | activity with swimlanes | § 8 Stopping | Withdrawal routes and what happens to your data |

### Rules for this stage

1. One file per figure, named `fig-NN-slug.puml`, with `NN` the paper-wide figure number
   (`08`, `12`, `15`, `18`, `22`). The file is valid PlantUML: it opens `@startuml` and
   closes `@enduml`, and carries the palette as `skinparam` declarations so the source is
   directly renderable outside LaTeX.
2. Immediately after `@startuml`, a `' Figure NN.` comment block states the title, the
   patient concern answered, and the paper section, followed by `' TikZ:` lines that tell
   the `full-patient` stage how to draw the figure with the `uml*` vocabulary of
   `patientstyle.sty`.
3. **Palette (hard limit, per diagram):** identical to Stage 1 - `protoblue #00417A`,
   `protogray #6C757D`, white, black strokes and text, at most three grayscale fills
   (`#E9ECEF`, `#CED4DA`, `#9AA1A8`), at most two lighter blues (`#3C7DB2`, `#DCE8F1`),
   and black fill only sparingly.
4. Formal notation is respected: stick actors for humans, folded notes for constraints,
   open triangles for generalisation, filled diamonds for composition, initial and final
   pseudostates on every state machine, and activation bars on every sequence lifeline.
5. Do not copy the PlantUML section of `../inputs/phase-1-six-platform-diagrams.zip`. That
   atlas draws the sponsor's system; these five figures draw the patient's guarantees.
6. No PNG, no JPG. One commit per figure file, pushed on write; a final commit lands
   `README.md` and `output-plantuml.md`.

### Sources to draw on

`../inputs/phase-1-trial-protocol.zip` § 6 (intervention, e-stop, force caps), § 7
(discontinuation), § 10 (oversight); `../research/research-b.md` concerns 2, 3, 4, 8, 10,
13, 16; `../inputs/patient-priority-physical-ai.zip` (H. R. 9501 self-selection and
H. R. 9505 real-time sponsor contact, cited here as H. R. 9510 v5);
`../inputs/patient-robot-instructions.tex` (what the patient is told to do and when).
