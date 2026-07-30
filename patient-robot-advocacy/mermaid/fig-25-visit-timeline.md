## Figure 25. Your calendar: every visit, how long it takes, and what it is for

**Type:** mermaid-type - `gantt`
**Paper section:** § 9, Your Visits, Your Data, Your Robot Instructions
**Patient concern answered:** ChatGPT concern 16 (practical, financial, and post-trial
burdens) and the scheduling half of concern 7. The Schedule of Activities in the parent
protocol is a matrix of crosses. A participant planning work, travel, and caregiving needs
a calendar with durations, not a matrix with crosses.

**Why a mermaid-type Gantt.** Duration and overlap are the two facts a matrix cannot show.
The participant's real question is "how many days of my life does this take, and when",
and a Gantt answers it directly.

```mermaid
%%{init: {'theme':'base','themeVariables':{'fontSize':'11px','primaryColor':'#DCE8F1','primaryTextColor':'#111111','lineColor':'#6C757D','sectionBkgColor':'#E9ECEF','altSectionBkgColor':'#FFFFFF','gridColor':'#CED4DA','todayLineColor':'#00417A','taskBkgColor':'#DCE8F1','taskBorderColor':'#00417A','activeTaskBkgColor':'#00417A','activeTaskBorderColor':'#000000','doneTaskBkgColor':'#CED4DA','doneTaskBorderColor':'#6C757D','critBkgColor':'#3C7DB2','critBorderColor':'#00417A'}}}%%
gantt
    title Participant calendar, screening through the 24-month endpoint
    dateFormat YYYY-MM-DD
    axisFormat %b %Y
    todayMarker off

    section Screening (up to 28 days)
    Consent conversation, no procedures      :done, c1, 2026-09-01, 2d
    Staging imaging and CA 19-9              :done, c2, 2026-09-03, 5d
    KRAS G12 confirmation on tissue          :done, c3, 2026-09-08, 7d
    Eligibility review and enrollment        :done, c4, 2026-09-15, 3d

    section Baseline and surgery
    Baseline day, Phase 0 sign-off shown     :active, b1, 2026-09-28, 1d
    Robotic Whipple, day 0                   :crit, s1, 2026-09-29, 1d
    Inpatient acute window, days 1 to 7      :active, a1, 2026-09-30, 7d

    section Early recovery
    ISGPS fistula grading                    :f1, 2026-10-01, 6d
    Daraxonrasib restart advisory window     :f2, 2026-10-06, 15d
    Day 30 safety visit, Clavien-Dindo       :crit, f3, 2026-10-29, 1d

    section Confirmatory
    Day 90 pathology and mortality review    :crit, g1, 2026-12-28, 1d
    RECIST imaging, day 90                   :g2, 2026-12-28, 2d

    section Long-term follow-up (every 12 weeks)
    Visit at week 24                         :h1, 2027-03-22, 1d
    Visit at week 36                         :h2, 2027-06-14, 1d
    Visit at week 48                         :h3, 2027-09-06, 1d
    Visit at week 60                         :h4, 2027-11-29, 1d
    Visit at week 72                         :h5, 2028-02-21, 1d
    Visit at week 84                         :h6, 2028-05-15, 1d
    24-month overall-survival endpoint       :crit, h7, 2028-09-25, 1d
```

## The burden, totalled

| Phase | Visits | Days in hospital | Days at a clinic | Notes for planning |
|:--|:--|:--|:--|:--|
| Screening | 4 | 0 | about 4 | imaging and tissue work; no study procedure before consent |
| Baseline and surgery | 2 | 8 to 10 | 1 | the single inpatient stay of the study |
| Early recovery | 3 | 0 | 3 | the restart advisory is a conversation, not a procedure |
| Confirmatory | 2 | 0 | 2 | day 90 carries the two results most people want |
| Long-term | 7 | 0 | 7 | one half-day every 12 weeks for 24 months |
| **Total** | **18** | **8 to 10** | **about 17** | roughly 27 days of contact over 24 months |

Dates above are illustrative and anchored to a September 2026 first visit; the intervals,
not the calendar dates, are what the protocol fixes.

## Palette used

| Token | Hex | Applied to |
|:--|:--|:--|
| Corporate Blue | `#00417A` | active bars, task borders, the axis emphasis |
| `pablue1` lighter blue | `#3C7DB2` | the four critical milestones: surgery, day 30, day 90, 24-month |
| `pablue2` lighter blue | `#DCE8F1` | ordinary task bars |
| `pagraym` medium | `#CED4DA` | completed screening bars and gridlines |
| `pagrayl` light | `#E9ECEF` | alternating section bands |
| Professional Gray | `#6C757D` | section labels and bar outlines |

Three-gray budget: two used. Lighter-blue budget: two used. Black fill: none.

## TikZ rendering notes for `full-patient`

- Horizontal time axis 15 cm wide spanning September 2026 to September 2028, with month
  ticks in `protogray` 0.4pt and quarter labels in `\tiny\sffamily`.
- Five section bands as full-width rectangles alternating `pagrayl` and white, drawn first
  so every bar sits above its band.
- Bars are 3.6 mm tall with 2.2 mm of clear space between rows; a one-day task is drawn at
  a 1.4 mm minimum width so it stays visible at this compression.
- Task labels are `\tiny\sffamily` anchored `east` in the 4.6 cm label gutter at the left,
  never inside the bar, so no label can overlap a bar.
- The four critical milestones additionally carry a 0.5pt `protoblue` vertical drop line to
  the axis, labelled beneath in `\tiny\sffamily\bfseries`.
- No curved connectors in this figure, so no looseness declaration is required.
