## output-final-patient

Stage 8 narrative, run from [`prompt-final-patient.md`](prompt-final-patient.md), which is
[`../sub-prompts/prompt-8-final-patient.md`](../sub-prompts/prompt-8-final-patient.md)
filed verbatim. This is the last stage of the eight.

### What was produced

The polished source set: `main.tex`, `patientstyle.sty`, `references.bib`, thirteen
sections, an Overleaf archive, and this narrative. There is no `publication/`
subdirectory, as the master prompt requires. Twenty commits, pushed on write.

### Compile result

```
pdflatex main -> bibtex main -> pdflatex main -> pdflatex main
Output written on main.pdf (88 pages, 492339 bytes).
0 errors   0 overfull boxes   0 undefined citations   0 undefined references
```

### The defects Stage 7 left, listed before they were fixed

The sub-prompt asks this stage to begin by listing every defect found in Stage 7 and then
to fix each one. The list was produced by three instruments rather than by reading: a
page-ink scanner that renders every page and measures the trailing gap, a cross-reference
resolver that checks every `\S` against the actual contents, and the compile log.

| # | Defect | Measured extent |
|:--|:--|:--|
| 1 | Figures set inline strand the space they cannot fit into | 41 of 83 pages with a trailing gap over 3 cm, worst 21.6 cm |
| 2 | Unbreakable tables run off the foot of a page | 2 pages, worst 143 pt of content past the bottom margin |
| 3 | A heading is the last thing on its page | 2 pages, each overfilling as a result |
| 4 | Two pairs of figures appear out of numeric order | figures 20 and 21, figures 24 and 25 |
| 5 | The contents spills two entries onto a fourth page | that page 21 cm empty |
| 6 | The paper is short of the parent protocol | 129,078 visible characters against 155,222, 83 percent |
| 7 | Captions drift out of the balance band as text moves | 10 of 30 outside the band after the section edits |
| 8 | Cross-references point at the wrong subsection | 11, once the new subsections renumbered three sections |

### Fix 1, the float carrier

Every figure-plus-caption is wrapped in a `pafloat`, a `figure` float placed `!tb`. Running
text closes the page and the figure heads the next one, or takes a float page when it
cannot share. Float parameters allow a float page only when the floats would fill 94
percent of it; `placeins` is loaded and `main.tex` clears the page between sections, so no
figure leaves the section that discusses it.

Three variants were built and measured before the third was kept.

| Placement | Pages | Pages with a gap over 3 cm | Worst gap |
|:--|:--|:--|:--|
| Inline, as Stage 7 | 83 | 41 | 21.6 cm |
| `!tp` | 75 | 23 | 21.9 cm |
| `!t`, later `!tb` | 73 | 22 | 21.5 cm |

`!tp` was rejected because the `!` makes LaTeX ignore `\floatpagefraction`, so a tall float
takes a float page in preference to the head of the next text page, and the text page it
would have headed stays empty. `!tb` keeps top placement first and allows the foot of a
page when the top is taken.

**The spacing invariant survives.** `pafig` drops its leading `\vskip 14pt` and
`\figcaption` its trailing `\vskip 13pt` when inside a float, because `\textfloatsep` and
`\floatsep` already set the float off from the text, and `\needspace` is suppressed where
it has no meaning. The rigid `\vskip 26pt` that pairs with the source's `\vspace{-0.7cm}`
is untouched, so the frame-to-caption distance is **6.1 pt for all thirty figures**,
floating or inline, whatever precedes or follows them.

### Fix 2, every table breakable

A `tabularx` is one unbreakable box. Where a heading was immediately followed by one,
`\@nobreak` prevented a break between them, the box did not fit, and the page overfilled
rather than moving the table: on page 25 of the Stage 7 layout a table row printed past
the bottom margin.

Every table of more than two rows is now an `xltabular` with `\endfirsthead`, `\endhead`,
`\endfoot`, and `\endlastfoot`, so it fills the page it starts on and continues overleaf
under a repeated header, with an italic continuation line at each break. Forty-three of
forty-three tables are breakable and the document contains zero unbreakable boxes.

Converting the tables also closed gaps on its own, because a table that could not fit had
been jumping whole pages: flagged pages fell from 22 to 17 on that change alone.

### Fix 3, no stranded headings

`\subsection` reserves itself plus three lines and `\subsubsection` plus two. A first
attempt reserved four and a half lines and three, which pushed too much and produced a
page carrying three lines of text and a 21.9 cm gap; the reservation was reduced until the
headings held and the gaps did not open.

### Fix 4, the figures renumbered into order

The operative-envelope figure was numbered 21 and appeared before the fault tree numbered
20; the calendar was numbered 25 and appeared before the data pipeline numbered 24. Both
figures were in the right subsection in each case, so the numbers moved rather than the
figures.

20 was exchanged with 21 and 24 with 25, and the swap was applied to:

- the thirty `\figcaption` lines,
- fifteen prose and table cross-references,
- six short-form `Fig 20`, `Fig 21`, `Fig 24` labels inside Figure 5's node text, which the
  first pass missed because the regex matched `Figure` and not `Fig`,
- the figure inventory in § 13.2 and the cover panel in `main.tex`,
- the four diagram source files, renamed so each still carries the number of the figure it
  draws, together with their directory READMEs, their stage narratives, and the hub
  README's per-type figure lists.

The per-type counts are unchanged, because each swap exchanges one figure each way.
[`../full-patient/`](../full-patient) is deliberately not renumbered: its PDF and archive
were built under the old numbering and are internally consistent, and its README carries a
note pointing here.

### Fix 5, the contents in three pages

`article.cls` opens every section entry with `\addvspace{1.0em}`, which over thirteen
sections and, after the section commits, 104 subsections put the last entries on a fourth
page that was then 21 cm empty. `\l@section` is redefined with a 0.18em lead and the
contents is set `\footnotesize` at `\linespread{0.92}`. It fits three pages with no entry
removed and no reduction of `tocdepth`.

### Fix 6, length parity with the parent protocol

Stage 7 reported 137,000 characters against 147,000. That comparison counted raw source
lines, which is generous to the paper, because the paper's tables carry more markup per
visible character than the protocol's. Measured like for like, with comments,
`tikzpicture` and `pafig` blocks, and LaTeX control sequences stripped from both, the
Stage 7 paper carried **129,078 visible characters against the protocol's 155,222**, which
is 83 percent and not 93.

Fifteen subsections were added across the thirteen sections. None is padding; each answers
a question the surveyed literature records participants asking, and each was placed where
the question arises rather than appended for length.

| § | Subsection added | What it does |
|:--|:--|:--|
| 1.2 | How to check a commitment, without taking anyone's word | Turns each of the seven commitments into an artefact to ask for, and names who holds it |
| 1.6 | What this paper does not promise | Draws the advocacy's boundary at the front instead of leaving it to § 10 |
| 2.2 | The words you will hear, defined once | Twenty terms in the sense this protocol uses them |
| 2.7 | How many people, and when your turn comes | Why 18, why the sentinel wait is not negotiable, what happens if you become ineligible while waiting |
| 3.8 | The five answered by governance alone, named | Names them, and separates the two that could become harder answers from the three that are structural |
| 4.7 | What each endpoint costs you to measure | Prices all nine in the participant's time, blood, and discomfort |
| 4.8 | Which endpoints are reported back to you, and when | Four individual, five cohort, with the schedule for each |
| 5.9 | Why there is no control group, and what replaces one | The external comparator as a floor rather than a target |
| 5.10 | What happens if the study is stopped while you are in it | The halt from the participant's side, before and after the operation |
| 6.7 | Second opinions, and how to get one that is worth having | The three documents that make the opinion about this study |
| 6.8 | Bringing someone with you, and who may decide | Why there is no legally authorised representative provision |
| 7.10 | The day of the operation, hour by hour | The operation as a day, each step marked study-specific or not |
| 7.11 | Who is in the room, and what each of them does | Five clinical roles unchanged, two added, and what the safety monitor may do |
| 7.12 | What is different from a conventional robotic Whipple | Ten aspects: four constraints added, nothing changed about the operation |
| 8.6 | Changing your mind is not a failure of the study | Removes the suggestion the word withdrawal carries |
| 9.8 | Missing a visit, and what actually happens | Four load-bearing visits, nine reschedulable, five declinable |
| 9.9 | The direct channel, and what it is not | The three things it cannot do |
| 10.8 | How to read a number in this paper, in four steps | Makes the provenance discipline usable rather than declared |
| 11.7 | What accountability does not mean here | Not punishment, not compensation, not fault |
| 12.5 | If you take one page to the consent conversation | Five questions, ten minutes, testing the five properties the paper establishes |
| 13 | How this paper may be reused | The two anticipated reuses and the correction route |

The paper now carries **168,275 visible characters, 108 percent of the parent protocol**,
which is the approximate parity the master prompt asks for.

### Fix 7, captions rebalanced

All thirty are three lines. Ten fell outside the band after the section edits. A
dynamic-programming split over word boundaries fixed five. For the other five no split of
the existing wording could reach a spread of 12 or less, so those five captions were
reworded: figures 10, 12, 14, 17, and 24. All thirty are now in band, with line lengths
between 62 and 112 characters and a maximum within-caption spread of 12.

### Fix 8, cross-references retargeted

Adding subsections renumbered three sections internally. Section 1 gained 1.2 in the
middle, section 2 gained 2.2 and 2.7, section 3 gained 3.8, and section 12 gained 12.5
before the closing argument. Every `\S` reference in the paper was resolved against the
generated contents, and eleven were retargeted.

| Reference | Was | Is | Why |
|:--|:--|:--|:--|
| The escalation route, six uses | § 11.5 | § 11.6 | § 11.5 is the audit trail; the escalation route is § 11.6. The three references that meant the audit trail were left alone |
| The governance-only five | § 3.7 | § 3.8 | § 3.7 scores completeness; § 3.8 names the five |
| What protects a DL3 participant | § 6.2 | § 5.6 | Stopping rules, not eligibility |
| Criteria re-checked when a slot opens | § 7.1 | § 6.2 | Inclusion and exclusion, not the operating room |
| What the site owes a participant who becomes ineligible while waiting | § 8.1 | § 6.4 | The booking channel notifies the oncologist on the ineligible branch |
| Which routes can remove analysed data | § 8.3 | § 8.1 | The four routes and their data consequences |
| A companion's signature | § 11.4 | § 11.6 | Reportable deviation, not team experience |
| The operative-time difference | § 7.7 | § 10.2 | The learning-curve figures, not conversion to open |

All 59 distinct subsection references now resolve. The three `\S` uses that do not resolve
to a subsection are 21 CFR § 50.20, 21 CFR § 50.25, and 17 U.S.C. § 105, which are
citations.

### White space, measured

The measurement renders every page at 50 dpi, ignores the running-footer band, and reports
the distance from the last row carrying ink to the bottom of the text block.

| | full-patient | final-patient |
|:--|:--|:--|
| Pages | 83 | 88 |
| Pages with a trailing gap over 3 cm | 41 | 15 |
| Worst gap | 21.6 cm | 20.3 cm |
| Of those, the last page of a section | not separated | 11 of 15 |
| Mid-section gaps | not separated | 4, at 3.9, 3.9, 5.3, and 7.8 cm |
| Content printed past the bottom margin | 2 pages | 0 |

The eleven section-end gaps are a direct consequence of the `\clearpage` between sections
that the sub-prompt requires the stage to learn and apply: a thirteen-section document
whose sections each start on a fresh page will end up to thirteen of them part way down a
page. They are not closable without removing the `\clearpage`, and closing them by adding
text would mean writing text to fill space, which is the opposite of what the length work
above did.

Float pages were also examined. Top-aligning them was tried and rejected: a figure centred
on an otherwise empty page reads as deliberate, while the same figure pushed to the top
reads as a broken page. The default centred glue is kept and the reason is recorded in the
style file so it is not re-litigated.

### Third figure verification

The sub-prompt requires a third pass over all thirty figures, after Stage 7's two.

**a) No box overlap, no arrow through a box, no label on a line.** All thirty were
re-checked in the float context, and the four figures Stage 7 had to rebuild were rendered
and read: Figure 6, the bipartite concern graph that had been legible only at 0.57 scale;
Figure 7, the quadrant chart whose labels had collided in four places; Figure 12, the
guarded state machine whose sentinel note had overlapped a guard; and Figure 19, the
sequence diagram whose `alt` fragment guards had sat on the messages. All four are clean.
No figure is clipped by its frame and none is scaled below 1.

**b) Curved connectors.** 122 of 122 `to[out=,in=]` connectors declare an explicit
`looseness`.

**c) Clear space between boxes.** No figure exceeds 0.84 of the text height, measured by
instrumenting `pafig` to report the fitted box height at compile time, so no figure is
compressed by the frame and the pitches set in Stage 7 hold at scale 1.

**Order.** The thirty figures appear in ascending order, 1 to 30, with no gaps and no
duplicates, verified from the document order of the `\figcaption` lines rather than from
the source file names.

### Compliance audits

| Audit | Result |
|:--|:--|
| `pafig` environments, `\vspace{-0.7cm}` lines, `\figcaption` calls, `pafloat` wrappers | 30, 30, 30, 30 |
| Figure numbers in document order | 1 to 30, ascending, no gaps, no duplicates |
| Malformed figure and caption pairs | 0 |
| Captions outside the balance band | 0 of 30 |
| Curved connectors declaring `looseness` | 122 of 122 |
| Tables at `\textwidth` | 43 of 43 |
| Unbreakable tables | 0 of 43 |
| Fixed columns without `\raggedright\arraybackslash` | 0 |
| Unresolvable subsection cross-references | 0 |
| Em dashes, en dashes, or prose double dashes | 0 |
| `SS` used where `§` was meant | 0 |
| `\includegraphics`, PNG, or JPG | 0 |
| Colour tokens outside the permitted set | 0, ten used in the sections |
| Surviving `\draftinstr` | 0 |
| Overfull boxes, undefined citations, undefined references | 0, 0, 0 |

### Commits in this stage

| # | Commit | File |
|:--|:--|:--|
| 1 | Style file with the pagination machinery | `patientstyle.sty`, `prompt-final-patient.md` |
| 2 | Bibliography carried forward | `references.bib` |
| 3 | Cover and section order | `main.tex` |
| 4 to 16 | Thirteen sections, one commit each | `sections/*.tex` |
| 17 | Pagination pass and the third figure verification | all files |
| 18 | Stage README | `README.md` |
| 19 | Fix all errors | `sections/*.tex`, `README.md` |
| 20 | Overleaf zip and this narrative | `final-patient-LaTeX.zip`, `output-final-patient.md` |

### What remains open

Three things are worth naming rather than leaving for a reader to find.

The eleven section-end gaps described above are structural and are not defects.

`../full-patient/` carries the old figure numbering. It is a closed stage and its artefacts
are internally consistent; its README says so and points here.

The paper is 108 percent of the parent protocol rather than exactly 100. The excess is
concentrated in sections 1, 2, and 7, where the participant-facing material has no
counterpart in a protocol written for a regulator, and trimming it to hit a character count
exactly would remove the parts of the paper that justify its existence.
