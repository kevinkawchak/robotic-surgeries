## Figure 19. One operative step, message by message: who proposes, who approves, who acts

**Type:** mermaid-type - `sequenceDiagram`
**Paper section:** § 7, What Happens in the Operating Room
**Patient concern answered:** ChatGPT concern 2 (who is actually controlling the
operation), concern 3 (human override and rescue capability), and concern 9 (overreliance
on AI and automation bias); Gemini family 1. This is the single most frequently raised
concern in every surveyed source, and it is the one that a paragraph answers worst. A
sequence diagram answers it exactly, because it shows that no message from the model
reaches an actuator without passing through a human.

**Why a mermaid-type sequence.** The question is about ordering and authority between
five participants over a few hundred milliseconds. Nothing else expresses "the model never
talks to the motor" as unambiguously as a lifeline that has no arrow to the motor.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontSize':'11px','primaryColor':'#DCE8F1','primaryTextColor':'#111111','primaryBorderColor':'#00417A','lineColor':'#6C757D','actorBkg':'#DCE8F1','actorBorder':'#00417A','actorTextColor':'#111111','noteBkgColor':'#E9ECEF','noteBorderColor':'#6C757D','signalColor':'#00417A','signalTextColor':'#111111'}}}%%
sequenceDiagram
    autonumber
    participant S as Sensor stack<br/>(640 channels, 10 kHz)
    participant L as On-premises LLM<br/>(advisory only)
    participant G as Safety gate<br/>(deterministic)
    participant H as Operating surgeon<br/>(sole authority)
    participant R as Robot arms<br/>(8, force-capped)

    S->>L: current field state, force vector, vessel proximity
    activate L
    L->>L: propose next step (no actuation path exists)
    L-->>G: candidate motion plan + confidence + rationale
    deactivate L
    activate G
    G->>G: check tip force &le; 3 N per arm, &le; 18 N cumulative
    G->>G: check no-fly envelope around SMV and portal vein
    alt any limit violated
        G--xL: plan rejected, reason logged, not shown as executable
        G->>H: rejection notice with the violated limit named
    else all limits satisfied
        G->>H: plan presented for approval, with confidence and rationale
    end
    deactivate G
    activate H
    H->>H: accept, modify, or decline (declining needs no justification)
    H->>R: approved motion command, signed by the surgeon
    deactivate H
    activate R
    R->>R: execute within the envelope, 10 kHz heartbeat maintained
    R-->>S: resulting state
    deactivate R
    Note over G,H: The surgeon may press stop at any instant. Cross-arm<br/>halt completes in &le; 3 ms; system-wide in &le; 500 ms.
    Note over L,R: There is no arrow from the model to the arms.<br/>That absence is the safety argument.
```

## What the diagram asserts, and where the protocol says it

| Assertion in the figure | Protocol basis |
|:--|:--|
| The model is advisory and has no actuation path | Class II collaborative device classification, continuous human oversight |
| A deterministic gate sits between advice and approval | per-arm tip force at most 3 N, cumulative at most 18 N, vascular no-fly gating |
| A rejected plan is never presented as executable | safety-gate design; rejection is logged with the violated limit named |
| The surgeon may decline without justification | operator authority is unconditional under the oversight model |
| Stopping is bounded, not best-effort | at most 3 ms cross-arm, at most 500 ms system-wide |
| Every message is recorded | hash-chained audit trail under 21 CFR part 11 |

## Palette used

| Token | Hex | Applied to |
|:--|:--|:--|
| Corporate Blue | `#00417A` | actor borders, message arrows, activation bars |
| `pablue2` lighter blue | `#DCE8F1` | actor header boxes |
| `pagrayl` light | `#E9ECEF` | the two note boxes |
| Professional Gray | `#6C757D` | lifelines, note borders, return arrows |
| Classic White | `#FFFFFF` | the figure field |

Three-gray budget: one used. Lighter-blue budget: one used. Black fill: none.

## TikZ rendering notes for `full-patient`

- Five `mmactor` headers at `x = 0, 3.6, 7.2, 10.8, 14.4`, `y = 0`, `text width=24mm`.
- Lifelines are `mmlife` dashed rules from `y = -0.6` down to `y = -12.6`.
- Activation bars are `mmact` rectangles, 2.6 mm wide, centred on the lifeline, spanning
  exactly the messages they enclose.
- Messages are `mmmsg` solid for calls and `mmret` dashed for returns, labelled
  `\tiny\sffamily` **above** the arrow, never on it; self-messages are drawn as a 4 mm
  right-hand loop with `to[out=20,in=-20,looseness=6]`.
- The `alt` fragment is a `protogray` 0.5pt rectangle with a corner tab reading `alt`, and
  a dashed divider between the two branches.
- The two notes are `umlnote`-style boxes spanning the named lifelines, placed at
  `y = -11.2` and `y = -12.2` so they do not collide with the last message.
