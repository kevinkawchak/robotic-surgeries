## Figure 23. Your consent is a state, not a signature: every transition you can trigger

**Type:** mermaid-type - `stateDiagram-v2` with a nested composite state
**Paper section:** § 8, Stopping, Withdrawing, Changing Your Mind
**Patient concern answered:** ChatGPT concern 13 (software changes, versioning, and
performance drift) and concern 8 (treatment choice), plus the withdrawal half of concern
16. A consent form implies a one-time act. In a Physical AI trial the thing consented to
can change while the participant is still enrolled, so consent has to be modelled as a
state machine with a re-consent transition, and the patient should be shown that machine.

**Why a mermaid-type state diagram.** Only a state machine can express that withdrawal is
reachable from every state, that re-consent is forced by an external event the participant
did not cause, and that two different terminal states exist with different data
consequences.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontSize':'11px','primaryColor':'#FFFFFF','primaryTextColor':'#111111','lineColor':'#6C757D'}}}%%
stateDiagram-v2
    direction TB
    [*] --> Informed

    Informed: <b>Informed</b><br/>§ 3 of this paper read,<br/>questions answered,<br/>no signature yet
    Consented: <b>Consented</b><br/>21 CFR § 50.20 satisfied,<br/>software version frozen<br/>and recorded

    state Enrolled {
        direction TB
        Screening: <b>Screening</b><br/>day -28 to -1
        Baseline: <b>Baseline</b><br/>day -1, Phase 0 sign-off,<br/>opt-out still open
        Operative: <b>Operative</b><br/>day 0
        Acute: <b>Acute</b><br/>days 1 to 7, restart advisory
        Followup: <b>Follow-up</b><br/>day 30, day 90, q12wk to 24 months
        Screening --> Baseline
        Baseline --> Operative
        Operative --> Acute
        Acute --> Followup
    }

    ReConsent: <b>Re-consent required</b><br/>software version changed,<br/>new risk identified, or<br/>protocol amended
    Withdrawn: <b>Withdrawn by you</b><br/>no reason required,<br/>standard care continues
    Completed: <b>Completed</b><br/>24-month endpoint reached

    Informed --> Consented: you sign
    Informed --> [*]: you decline, nothing recorded beyond the screening log
    Consented --> Enrolled: first study procedure
    Enrolled --> ReConsent: version or protocol change (not your doing)
    ReConsent --> Enrolled: you re-consent
    ReConsent --> Withdrawn: you decline the change
    Enrolled --> Withdrawn: you withdraw, any time, any visit
    Enrolled --> Completed: 24-month follow-up complete
    Withdrawn --> [*]
    Completed --> [*]

    note right of Withdrawn
        Data already collected stays in the
        safety analysis; nothing new is collected.
        You choose whether banked specimens
        are destroyed or retained.
    end note

    note left of ReConsent
        You did not cause this transition.
        Until you act, no study procedure
        proceeds under the changed version.
    end note
```

## The two transitions the parent protocol does not draw

| Transition | Why it matters to the participant |
|:--|:--|
| `Enrolled --> ReConsent` | An AI-enabled device can be updated. If the version that operates on the participant is not the version they consented to, the consent is stale. This protocol freezes the version at consent and forces a re-consent on any change, so the participant is never operated on by software they have not been told about. |
| `ReConsent --> Withdrawn` | Declining a change must be a real option, not a formality. Declining ends participation and returns the participant to standard care with no penalty and no loss of any care they were already receiving. |

## Palette used

| Token | Hex | Applied to |
|:--|:--|:--|
| Corporate Blue | `#00417A` | the `Consented` and `Completed` states, initial and final marks |
| `pablue2` lighter blue | `#DCE8F1` | the five nested `Enrolled` substates |
| `pagraym` medium | `#CED4DA` | the `ReConsent` state, the transition the participant did not cause |
| `pagrayl` light | `#E9ECEF` | the two note boxes and the `Informed` state |
| Professional Gray | `#6C757D` | the `Enrolled` composite border and every transition arrow |
| Classic White | `#FFFFFF` | the field and the `Withdrawn` state |

Three-gray budget: two used. Lighter-blue budget: one used. Black fill: none.

## TikZ rendering notes for `full-patient`

- `umlinit` filled disc at `(0,1.4)`; `umlfinal` ringed discs at `(-5.4,-13.0)` and
  `(5.4,-13.0)`.
- `Informed` and `Consented` as `umlstate` at `(0,0)` and `(0,-2.2)`, `text width=32mm`.
- The `Enrolled` composite is a `umlpkg` rounded rectangle fitted over five `umlstate`
  substates stacked at `y = -4.8` to `-10.4` with 1.4 cm pitch and `text width=30mm`;
  the composite's own title tab sits `north west`.
- `ReConsent` at `(6.4,-6.6)`, `Withdrawn` at `(-6.4,-9.4)`, `Completed` at `(0,-12.0)`.
- Every transition is `umlarrow` with a `\tiny\sffamily` label placed in a white-filled
  `mmlabel` node at the arrow midpoint so the label never sits on the line.
- The two long transitions out of the composite use
  `to[out=0,in=90,looseness=0.9]` and `to[out=180,in=90,looseness=0.9]`; they leave the
  composite border, not a substate, so no arrow crosses a substate box.
- Notes are `umlnote` boxes with a 0.5pt dashed leader to their anchor state.
