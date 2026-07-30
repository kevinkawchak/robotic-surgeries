## Figure 1. The seven commitments made to you, from first conversation to day 90

**Type:** mermaid-type - `flowchart TD`
**Paper section:** § 1, Statement of Patient Commitment
**Patient concern answered:** Gemini family 1 (loss of the human element and surgeon
control) and ChatGPT concern 14 (loss of personal care and surgeon-patient trust). A
protocol opens with a Statement of Compliance addressed to regulators. This figure opens
the patient paper with the seven things the same protocol commits to the participant, each
one anchored to the protocol clause that makes it enforceable rather than aspirational.

**Why a mermaid-type flowchart.** The seven commitments are not a list; they are a sequence
in time, and each one becomes checkable at a specific moment. A flowchart top-down is the
only idiom that shows both the order and the gate that closes behind each promise.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontSize':'12px','primaryColor':'#FFFFFF','primaryTextColor':'#111111','lineColor':'#6C757D','secondaryColor':'#E9ECEF','tertiaryColor':'#DCE8F1'}}}%%
flowchart TD
    P(["You, the participant"]):::goal

    C1["<b>1. Nothing starts without you</b><br/>Consent signed before any<br/>study procedure - 21 CFR § 50.20"]:::commit
    C2["<b>2. The robot is proven before you</b><br/>Phase 0 gate: &ge; 1000 simulations,<br/>&ge; 2 frameworks, USL &ge; 7.0"]:::commit
    C3["<b>3. You are never the untested dose</b><br/>3+3 escalation, sentinel stagger,<br/>DL1 cleared before DL2 opens"]:::commit
    C4["<b>4. A human approves every motion</b><br/>Class II collaborative device,<br/>continuous oversight, no free running"]:::commit
    C5["<b>5. Stopping is faster than harm</b><br/>&le; 3 ms cross-arm e-stop,<br/>&le; 500 ms system-wide guarantee"]:::commit
    C6["<b>6. Your record cannot be edited</b><br/>Hash-chained audit trail,<br/>21 CFR part 11, seed and commit bound"]:::commit
    C7["<b>7. Leaving costs you nothing</b><br/>Withdraw at any time, standard<br/>care continues, § 8 governs data"]:::commit

    G1{{"Consent<br/>on file?"}}:::gate
    G2{{"Gate<br/>passed?"}}:::gate
    G3{{"Cohort<br/>cleared?"}}:::gate

    D30["Day 30 - primary safety window<br/>Clavien-Dindo grading complete"]:::mid
    D90["Day 90 - R0 pathology and<br/>90-day mortality reported to you"]:::goal

    P --> C1 --> G1
    G1 -- "no: nothing proceeds" --> STOP["No study activity<br/>occurs at all"]:::halt
    G1 -- yes --> C2 --> G2
    G2 -- "no: enrollment held" --> STOP
    G2 -- yes --> C3 --> G3
    G3 -- "no: cohort pauses" --> STOP
    G3 -- yes --> C4 --> C5 --> C6 --> C7
    C7 --> D30 --> D90

    classDef goal fill:#00417A,stroke:#000000,stroke-width:1.4px,color:#FFFFFF
    classDef commit fill:#FFFFFF,stroke:#00417A,stroke-width:1.1px,color:#111111
    classDef gate fill:#CED4DA,stroke:#000000,stroke-width:1px,color:#111111
    classDef mid fill:#6C757D,stroke:#000000,stroke-width:1.1px,color:#FFFFFF
    classDef halt fill:#222222,stroke:#000000,stroke-width:1.2px,color:#FFFFFF
```

## Palette used

| Token | Hex | Applied to |
|:--|:--|:--|
| Corporate Blue | `#00417A` | the participant node, the day-90 outcome node, commitment strokes |
| Professional Gray | `#6C757D` | the day-30 safety-window node and every edge |
| Classic White | `#FFFFFF` | the seven commitment fills |
| `pagraym` medium | `#CED4DA` | the three gate diamonds |
| `padark` (sparing) | `#222222` | the single halt node, used once |

Three-gray budget: one used (`#CED4DA`). Lighter-blue budget: none used. Black fill: one
node.

## TikZ rendering notes for `full-patient`

Draw with the `mm*` vocabulary of `patientstyle.sty`.

- `P` as `mmgoal` at `(0,0)`, `text width=34mm`.
- `C1` to `C7` as `mmin` in a single column at `x=0`, `y = -2.0, -4.4, -6.8, -9.2, -11.6,
  -14.0, -16.4`, `text width=52mm`, so 24 mm of vertical pitch leaves at least 9 mm of
  clear space between ranks.
- `G1`, `G2`, `G3` as `mmdec` at `x=5.6`, aligned with `C1`, `C2`, `C3`.
- `STOP` as `mmdark` at `(10.4,-4.4)`, reached by three `mmedged` edges that enter from the
  east of each diamond; route the second and third with
  `to[out=0,in=180,looseness=0.8]` so they do not overlap the first.
- `D30` as `mmstep` and `D90` as `mmgoal` at `y = -18.8` and `-21.0`.
- Bold the commitment number with `\textbf{}` and set the clause reference in
  `\scriptsize`.
