## Figure 3. Your journey through the trial, annotated with every point where you decide

**Type:** mermaid-type - `flowchart LR` (full page, landscape reading)
**Paper section:** § 2, Plain-Language Protocol Summary
**Patient concern answered:** ChatGPT concern 8 (randomization and treatment choice) and
concern 7 (unknown and experimental risks). The parent protocol's schema shows the trial
flowing through the participant. This figure inverts it: the same schema, redrawn so that
every node the participant controls is filled Corporate Blue and every node the sponsor
controls is gray, which makes the balance of control visible at a glance rather than
arguable.

**Distinguished from the NSCLC journey.** The structure is adapted from the author's
autonomous single-patient journey simulation, which was **non-small cell lung cancer**.
This journey is **PDAC**: the operation is a pancreaticoduodenectomy rather than a
lobectomy, the drug is daraxonrasib rather than a checkpoint inhibitor, the dominant
early complication is a pancreatic fistula rather than a prolonged air leak, and the
survival baseline is far lower.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontSize':'11px','primaryColor':'#FFFFFF','primaryTextColor':'#111111','lineColor':'#6C757D'}}}%%
flowchart LR
    subgraph S1["Screening - up to 28 days"]
      direction TB
      A1["Referral and<br/>eligibility review"]:::spon
      A2["KRAS G12 confirmation<br/>on tissue"]:::spon
      A3["Staging: resectable or<br/>borderline resectable"]:::spon
      A4(["<b>You decide</b><br/>consent, or decline<br/>with no consequence"]):::you
      A1 --> A2 --> A3 --> A4
    end

    subgraph S2["Baseline - day -1"]
      direction TB
      B1["Phase 0 simulation sign-off<br/>&ge; 1000 runs, &ge; 2 frameworks"]:::spon
      B2["USL &ge; 7.0 and safety<br/>matrix verified"]:::spon
      B3(["<b>You decide</b><br/>Physical AI opt-out<br/>still open at this point"]):::you
      B1 --> B2 --> B3
    end

    subgraph S3["Surgery - day 0"]
      direction TB
      C1["Eight-arm robotic Whipple<br/>under continuous oversight"]:::key
      C2["Force caps &le; 3 N per arm,<br/>&le; 18 N cumulative"]:::spon
      C3["Vascular no-fly gating<br/>on SMV and portal vein"]:::spon
      C1 --> C2 --> C3
    end

    subgraph S4["Acute - days 1 to 7"]
      direction TB
      D1["ISGPS fistula grading"]:::spon
      D2["Daraxonrasib restart advisory<br/>T+7, T+14, or T+21"]:::spon
      D3(["<b>You decide</b><br/>accept or decline<br/>the advised restart"]):::you
      D1 --> D2 --> D3
    end

    subgraph S5["Follow-up"]
      direction TB
      E1["Day 30 - Clavien-Dindo,<br/>primary safety window"]:::spon
      E2["Day 90 - R0 pathology,<br/>90-day mortality"]:::spon
      E3["Every 12 weeks to<br/>24-month overall survival"]:::spon
      E4(["<b>You decide</b><br/>withdraw at any visit,<br/>care continues"]):::you
      E1 --> E2 --> E3 --> E4
    end

    S1 --> S2 --> S3 --> S4 --> S5
    A4 -. "declining ends it here" .-> OUT["Standard-of-care pathway,<br/>unchanged and available"]:::gray
    B3 -. "opting out of Physical AI" .-> OUT
    E4 -. "withdrawal at any time" .-> OUT

    classDef you fill:#00417A,stroke:#000000,stroke-width:1.4px,color:#FFFFFF
    classDef key fill:#3C7DB2,stroke:#00417A,stroke-width:1.2px,color:#FFFFFF
    classDef spon fill:#FFFFFF,stroke:#6C757D,stroke-width:1px,color:#111111
    classDef gray fill:#E9ECEF,stroke:#6C757D,stroke-width:1px,color:#111111
```

## Palette used

| Token | Hex | Applied to |
|:--|:--|:--|
| Corporate Blue | `#00417A` | the four decision nodes that belong to the participant |
| `pablue1` lighter blue | `#3C7DB2` | the operation itself, the one investigational act |
| Professional Gray | `#6C757D` | sponsor-node strokes, lane borders, and every edge |
| Classic White | `#FFFFFF` | sponsor-controlled steps |
| `pagrayl` light | `#E9ECEF` | the standard-of-care exit node |

Three-gray budget: one used. Lighter-blue budget: one used. Black fill: none.

## TikZ rendering notes for `full-patient`

Full-page figure. Draw with `mm*` plus `mmlane` for the five phase lanes.

- Five lanes left to right at `x = 0, 4.6, 9.2, 13.4, 18.0`, each an `mmlane` fitted over
  its members with an `mmlanetitle` anchored `south west` on the lane's `north west`.
- Inside a lane, stack members top to bottom with 2.1 cm pitch; `text width=30mm` for
  sponsor nodes and `34mm` for the participant nodes so the bold "You decide" line does
  not wrap awkwardly.
- Participant nodes are `mmgoal`; the operation node uses a local
  `fill=pablue1,draw=protoblue`; sponsor nodes are `mmin` with `draw=protogray`.
- Lane-to-lane edges leave the lane's east and enter the next lane's west with
  `mmedgeb`, at the vertical midpoint of the lane, so no edge crosses a member box.
- The three dotted exits to `OUT` are `mmedged` routed **below** all lanes at `y = -11.2`
  using `-| ` right-angle routing, never diagonally through a lane.
- `OUT` sits centred beneath the lanes at `(11.0,-12.4)` as an `mmin` with `fill=pagrayl`.
