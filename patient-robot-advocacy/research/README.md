# research - documented patient concerns (v1.0.0)

[![License](https://img.shields.io/badge/License-CC%20BY%204.0-yellow.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Concerns](https://img.shields.io/badge/Concerns-21%20documented-00417A.svg)](.)
[![Gemini](https://img.shields.io/badge/Gemini%203.1%20Pro-Top%205-6C757D.svg)](research-a.md)
[![ChatGPT](https://img.shields.io/badge/ChatGPT%205.6-Top%2016-6C757D.svg)](research-b.md)
[![BibTeX](https://img.shields.io/badge/New%20BibTeX%20entries-13-00417A.svg)](../references)
[![Date](https://img.shields.io/badge/Dated-July%2028%2C%202026-lightgrey.svg)](.)

Two dated 2026 research markdowns supply the evidence base for the paper's central claim:
that patient apprehension about surgical robots is specific, documented, and answerable
clause by clause, rather than a diffuse fear of technology.

## [Research A: July 28, 2026](research-a.md) - Gemini 3.1 Pro

**Prompt.** *What are the main concerns patients will having with surgical robots/Physical
AI oncology trials?*

Six concern families, of which the top five drive the paper's § 3 structure.

| # | Concern family | Answered in the paper by |
|:--|:--|:--|
| 1 | Loss of the human element and surgeon control | § 3.1, § 7.2; Figures 8, 19 |
| 2 | Surgical safety and technical failures | § 3.2, § 7.4; Figures 18, 20 |
| 3 | Misdiagnosis and algorithmic bias | § 3.3, § 10.3; Figures 6, 27 |
| 4 | Data privacy and cybersecurity | § 3.4, § 9.3; Figures 9, 24 |
| 5 | The accountability dilemma, "who is to blame?" | § 3.5, § 11; Figures 2, 29 |
| 6 | Increased costs | § 3.6, § 12.2; Figure 30 |

## [Research B: July 28, 2026](research-b.md) - ChatGPT 5.6 Thinking Extended

**Prompt 1.** *What are the main concerns patients will having with surgical robots/Physical
AI oncology trials?*

**Prompt 2.** Re-issued asking for full Markdown with bracketed citation numbers mapped to
twelve-character BibTeX labels in the exact format of the parent protocol's `Siegel2025`
entry.

Sixteen numbered concerns, each with the question the patient is likely to ask and what the
trial team should explain, plus ten minimum-information items for consent, plus thirteen
BibTeX entries.

| # | Concern | Answered in the paper by |
|:--|:--|:--|
| 1 | Safety, malfunction, unintended actions | § 3.2, § 7.4; Figures 18, 20 |
| 2 | Who is actually controlling the operation | § 3.1, § 7.3; Figure 19 |
| 3 | Human override and rescue capability | § 7.4; Figure 18 |
| 4 | Responsibility if something goes wrong | § 11.1; Figures 2, 29 |
| 5 | Surgeon and operating-team experience | § 11.2; Figure 29 |
| 6 | Cancer-control effectiveness | § 4.2, § 10.1; Figures 10, 27 |
| 7 | Unknown and experimental risks | § 5.1, § 10.2; Figures 12, 13 |
| 8 | Randomization and treatment choice | § 5.2; Figure 12 |
| 9 | Overreliance on AI and automation bias | § 7.3; Figure 19 |
| 10 | Privacy, recording, and secondary data use | § 9.3; Figure 24 |
| 11 | Cybersecurity and network dependence | § 9.4; Figures 9, 17 |
| 12 | Bias and applicability to the individual | § 6.3; Figure 14 |
| 13 | Software changes, versioning, drift | § 8.3; Figure 23 |
| 14 | Loss of personal care and surgeon trust | § 3.1; Figure 8 |
| 15 | Marketing, hype, unrealistic expectations | § 10.4; Figure 28 |
| 16 | Practical, financial, post-trial burdens | § 12.2; Figure 30 |

Six Gemini families plus sixteen ChatGPT concerns, de-duplicated on the overlapping items,
give the **twenty-one documented concerns** that § 3 enumerates and Figures 5, 6, and 7
render.

## The thirteen new BibTeX entries

Research B ends with thirteen entries in the parent protocol's format. All thirteen are
merged verbatim into the paper bibliography at
[`../final-patient/references.bib`](../final-patient), keeping the `doi` + `url` + `note`
triad so every reference compiles with a clickable URL.

| Key | Source | Cited in |
|:--|:--|:--|
| `WuSemiAI2026` | Surgical Endoscopy, patient perceptions of semi-autonomous RAS | § 3, § 5, § 8 |
| `TelesAI2026A` | JMIR Cancer, 330-patient attitude survey | § 3, § 10 |
| `Jauniaux2025` | J Robotic Surgery, systematic review of public perspectives | § 3, § 10 |
| `BrarRAS2024X` | J Robotic Surgery, public perceptions and misconceptions | § 3, § 10 |
| `LeeAuto2024X` | npj Digital Medicine, autonomy levels in cleared robots | § 4, § 7 |
| `FDARobot2022` | FDA, computer-assisted surgical systems | § 4, § 10 |
| `FDATrans2024` | FDA, Health Canada, MHRA transparency principles | § 8, § 9 |
| `FDACyber2026` | FDA, cybersecurity in medical devices | § 9 |
| `FDADiver2017` | FDA, age, race, and ethnicity reporting | § 6 |
| `FDARealW2025` | FDA, real-world AI device performance | § 8 |
| `NCIConsent24` | NCI, understanding informed consent forms | § 2, § 6 |
| `NCICosts2024` | NCI, who pays for clinical trials | § 12 |
| `NCITrial2024` | NCI, how clinical trials work | § 2, § 5 |

## Quantitative findings carried into the paper

| Finding | Source | Used in |
|:--|:--|:--|
| 56 percent of 50 previously operated patients would consider semi-autonomous robot-assisted surgery, conditional on which steps the robot controls | `WuSemiAI2026` | § 3.1, Figure 7 |
| Approximately half of 330 oncology patients expressed concern about AI in cancer care, led by loss of human interaction and medical errors | `TelesAI2026A` | § 3.1, Figure 27 |
| Expectation and experience diverge systematically in robotic surgery, with expectation set by marketing rather than evidence | `Jauniaux2025` | § 10.4, Figure 28 |
| Public misconception that the robot operates by itself is the single most common misconception | `BrarRAS2024X` | § 3.1, Figure 5 |
| No FDA-cleared surgical robot exceeds task-level autonomy under supervision | `LeeAuto2024X` | § 4.1, § 7.3 |

## Files from other directories used here

| Source | Used for |
|:--|:--|
| [`../inputs/phase-1-trial-protocol.zip`](../inputs) `references.bib` | the exact BibTeX field order the thirteen new entries follow |
| [`../references/references.bib`](../references) | the author works the concerns are answered with |

## License

Released under CC BY 4.0. Author: Kevin Kawchak, CEO ChemicalQDevice
([ORCID 0009-0007-5457-8667](https://orcid.org/0009-0007-5457-8667)).
