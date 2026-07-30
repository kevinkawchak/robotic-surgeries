## prompt-patient

Your main goal is to generate a new Phase 1 PDAC clinical trial Patient Robot Advocacy paper that is a proponent for relieving:
1) Patient concerns with surgical robots based on the existing protocol from robotic-surgeries/blob/main/patient-robot-advocacy/inputs/phase-1-trial-protocol.zip (also use this protocol as the paper template, but make visual changes that suit this paper type that help patients visually, especially the cover page).
2) Build your context based on the Top 5 Gemini and Top 16 ChatGPT patient advocacy complete markdown files from robotic-surgeries/tree/main/patient-robot-advocacy/research (implement BibTeX entries where relevant).
3) Adapt new machine readable diagrams based on the trial protocol context and other relevant diagrams throughout robotic-surgeries/tree/main/patient-robot-advocacy/inputs (Don’t generate Excalidraw diagrams, but Excalidraw diagram code context can be utilized). A total of 30 diagrams of different types from (i-v) need to be generated according to paper context and paper page.
i) Mermaid-type Diagrams
ii) PlantUML-type Diagrams
iii) D2-type Diagrams
iv) Diagrams (Python)-type Diagrams
v) Graphviz-type Diagrams
a. Figures must be numbered sequentially from 1-30 in captions.
b. Each caption line has a similar number of centered characters; with no more than 3 lines of caption text.
c. Every new diagram must use \vspace{-0.7cm} between its own caption. (This spacing must also be the same distance for each diagram, no matter what is below it in the paper). Double check that every diagram and caption whitespacing is the same for each diagram.
d. The number of diagrams per type should not be based on equal numbers of diagrams per type, but based on using the correct diagram for its purpose regarding paper context and location in the paper.
e. Each diagram needs to use the robotic-surgeries/blob/main/patient-robot-advocacy/inputs/phase-1-trial-protocol.zip color scheme, but now also use up to three grayscale colors per diagram (light, medium, medium-dark), and also use up to two additional lighter shades of {protoblue}{HTML}{00417A} per diagram. Use black fill boxes sparingly.)
f. Each diagram must be a unique perspective for patient advocacy, and generated and committed in real time to GitHub as the output progresses, and not all committed at the same time at the end of processing. 

Output all files to directories and subdirectories under robotic-surgeries/tree/main/patient-robot-advocacy. Use robotic-surgeries/blob/main/patient-robot-advocacy/template/trial-protocol-template.zip as the template regarding setting up sub-prompts, directories and subdirectories. Utilize machine readable diagrams where relevant, but do not copy them directly (as patient advocacy context must be added). Update diagram type directories to i)-v) above (instead of just Mermaid), and other new paper specific adaptations.

Your new paper will have approximately the same number of text characters as the trial protocol and use the following inputs. 
A) robotic-surgeries/blob/main/patient-robot-advocacy/inputs/patient-priority-physical-ai.zip context serves as the reminder that the cancer patient, not the doctor, the nurse, the trial sponsor, the IRB, or the regulator, is the priority participant in any United States oncology clinical trial. Note that updated author legislation should be used for Bill citations: H. R. 9510 v5 (10.5281/zenodo.20619762)(and relevant sources throughout robotic-surgeries/blob/main/patient-robot-advocacy/references/references.bib.)
B) robotic-surgeries/blob/main/patient-robot-advocacy/inputs/cancer-patient-journey.zip is a simulation that presents the first fully autonomous, single-patient journey through a regulated Physical
AI oncology clinical trial (note that this study was for NSCLC, which should be distinguished from the current PDAC trial).
C) robotic-surgeries/blob/main/patient-robot-advocacy/inputs/patient-robot-instructions.tex which provides 10 sets of patient instructions for interacting with robots in their upcoming appointments. It is important to adapt this information to the current Phase 1 PDAC protocol.
D) robotic-surgeries/blob/main/patient-robot-advocacy/inputs/phase-1-six-platform-diagrams.zip provides a large assortment of machine readable diagrams based on types i)-v) above. Do not generate any excalidraw diagrams. Do not directly copy any of the diagrams, as 30 new comprehensive diagrams (with some being full page or dashboards) need to implement patient advocacy context.
E) robotic-surgeries/blob/main/patient-robot-advocacy/references/references.bib use these additional up to date author references, where relevant. 

Populate directories and subdirectories in robotic-surgeries/tree/main/patient-robot-advocacy in an analogous manner as robotic-surgeries/blob/main/patient-robot-advocacy/template/trial-protocol-template.zip (but using new draft-patient, full-patient, final-patient directories, and current inputs). Do not include a publication directory under final-patient. Adapt your own mermaid/plantuml/d2/python/graphviz/draft/full/final LaTeX file processing stages and corresponding directories, which are enabled by generating specific sub-prompts and executing the same sub-prompts that you generated. Each existing and newly generated directory in robotic-surgeries/tree/main/patient-robot-advocacy must have its own comprehensive README, and relevant badges.

“COVER PAGE” (vary in appearance to the patient advocacy theme, keeping the current color scheme)
Title: Patient Robot Advocacy: A Phase 1, First-in-Human, PDAC Clinical Trial Protocol of a LLM-Directed Robotic Whipple with Daraxonrasib (RMC-6236)
Draft 1.0
10.5281/zenodo.xxxxxxxx (with hyperlink , 0009-0007-5457-8667 (with hyperlink https://orcid.org/0009-0007-5457-8667)
CEO Kevin Kawchak, ChemicalQDevice, kevink@chemicalqdevice.com
Independent research paper and practical adoption guide. It is not medical or regulatory advice and is not endorsed by the FDA, NIH, HHS, an IRB, ICH, or any sponsor. All figures derive from the author’s repository sources and are illustrative unless tied to a cited reference.
Disclaimer: This work is independent and is not endorsed or sponsored by any trial sponsor, CRO, site, IRB, regulator, or medical society; and was adapted using Claude Code Opus 5.
San Diego
July 31, 2026
Note: Both the paper (v1.0)(https://doi.org/10.5281/zenodo.xxxxxxxx); and the repository (v1.0.0) (https://github.com/kevinkawchak/robotic-surgeries/tree/main/patient-robot-advocacy) should be stated with URLs, where appropriate.
“COVER PAGE”

Be sure quantitative data and tables from author sources is sufficient enough for patients to be convinced of the robotic Phase 1 clinical trial. Adapt from the existing Phase 1 protocol back matter.

Cite where relevant using the existing .bib from robotic-surgeries/blob/main/patient-robot-advocacy/inputs/phase-1-trial-protocol.zip. Add any new references from robotic-surgeries/tree/main/patient-robot-advocacy/research using the same exact bibtex format from the Phase 1 protocol. Make sure all references when compiled will have clickable URLs; and state the DOI text with corresponding clickable DOI URLs, where relevant; and that no links run off of the right side of the page.

Create an auto-commit / auto-PR process in real-time that allows for the user to monitor branch progress without any user intervention. Do not hold commits from GitHub, instead commit after current files are generated. This is an extensive process, so the ability to monitor your branch progress throughout your generation is important. A single last update by you provides changelog, versioning, and other updates provided below.

“SUB-PROMPT SCHEDULE”
Each of the following instructions refer to adapting to the robotic-surgeries/blob/main/patient-robot-advocacy/template/trial-protocol-template.zip processing workflow.
1. Each machine readable diagram must be high quality, comprehensive, professional, and professionally colored (each of the 30 diagrams has its own commit) (diagrams must be improved throughout the draft, full, final process). Don’t directly copy prior author diagrams from different works. There must be no overlap between different aspects within each figure. Every diagram must be new, comprehensive, and professionally relevant to this paper. No shortcuts, please. 
2. draft-patient: (the first paper files provides sets of bracketed text instructions that also identify exact robotic-surgeries/tree/main/patient-robot-advocacy repository files and directories for subsequent steps to process) (10+ commits) Adapt a table of contents, back matter and other supporting information
3. full-patient: (the second iteration paper needs to utilize the files and directories identified in draft-patient effectively to generate a full version). Optimize column widths for aesthetics based on the prior robotic-surgeries/blob/main/patient-robot-advocacy/inputs/phase-1-trial-protocol.zip author methods and the amount of text per column. Learn and verify twice that each figure a) has no text box and arrow overlaps, b) if curved arrows are present: correct amount of looseness is specified, and c) has proper spacings between boxes. Again LaTeX figures need to have the same complexity and completeness throughout. (10+ commits)
4. final-patient: (your context and formatting quality should reach maximum quality here. You need to spend time double verifying all diagrams, context, and formatting is improved from full-patient) (learn from and implement corrections you identify from full-patient). Learn and implement the author’s /clearpage, table formatting column widths, and other types of /vspace and /hspace formatting methods throughout all figures and text. Learn from and implement the author’s other corrections/proof reading techniques to create the polished final-patient source files with publication quality diagrams. (10+ commits)
“SUB-PROMPT SCHEDULE”

“RULES”
1. Commit only to the robotic-surgeries repository with an updated main README (but limit additions to 2 sections). All subdirectories need to have detailed READMEs. Do not commit to other repositories
2. Only Claude Code Opus 5 can be used throughout all of this single prompt and sub-prompts. Do not stall, ask questions, or go into plan mode
3. No png or jpg files are allowed
4. Use tables where relevant, make sure each table is the width of the body text, and column widths will yield professional formatted tables
5. Each README.md for each directory must be comprehensive and state which files from other directories were used and where
6. For each sub-prompt: 1 commit is required for each of the following (main.tex, .sty, .bib, and README); and 1 commit is required for each of the paper’s .tex sections (1 .tex file per section) that each correspond to main.tex (this is different than the paper template, with each section needing a .tex)
7. For each sub-prompt generation: the 2nd to last commit must fix all of your errors for all files. For the last commit, perform the remaining repository updates defined below
8. All commits and PRs must be submitted to GitHub in real-time the moment they are generated for user viewing. Do not hold commits and PRs from GitHub as they are completed
9. You have permission to commit, commit to main, merge, and create PRs in GitHub
10. Do not take shortcuts from sub-prompt to sub-prompt: every stage must be fully developed. All files generated from prompts must be present and working. Each set of LaTeX files must compile properly in Overleaf by the author
11. Don’t stop until all tasks are completed. The user will continue the session by using the phrase “Continue” if tokens are exhausted. This is a lengthy process
12. Leave DOI in the format: 10.5281/zenodo.xxxxxxxx (with Hyperlink: https://doi.org/10.5281/zenodo.xxxxxxxx).
13. All draft-patient, full-patient, and final-patient developments must have their own .tex outputs and tex zip file that will run properly by the author in Overleaf, as each is generated separately, and accessed in real time
14. You will be judged on how well you followed these rules and sub-prompt schedule after you finish by the author and professionals
15. Don’t take any shortcuts
“RULES”

For each LaTeX source: avoid large white empty spaces without text. Where large spacing between words exist throughout the body of text.: modify \raggedright spacing to make positioning between words look equally and properly spaced. Make sure text doesn’t run off the right side of the page anywhere. Include instructions to avoid lines with a single or two words. All tables need to use a similar format for each column width as in this example: The contents of every table cell must be properly left aligned using the example format:{>{\raggedright\arraybackslash}p{2cm}. Every width value must have a prepended \raggedright\arraybackslash to ensure no big gaps between words in tables. It is also important that tables match the exact width of the body of the text.

Avoid single lines separate from the main paragraph on the next page. Perform the final formatting steps that a senior author would take by correcting white space formatting and removing and/or adding relevant text to make each section and page look properly formatted and self standing by itself. (Don’t overcrowd the page with text, some white space formatting is ok). Make sure to correct all incorrect symbols such as SS into “§” where relevant. Use single dashes, but no em dashes, double dashes, or triple dashes throughout the paper.

Under robotic-surgeries/tree/main/patient-robot-advocacy/prompts: Create a prompt-patient.md that uses a “## prompt-patient” heading followed by only this entire prompt word-for-word. Make sure only a heading and this exact prompt text is included. Create a separate output-patient.md that uses a “## output-patient” heading followed by the entire output of this prompt (containing the Claude markdown output, not the code files). Be sure only the heading with the exact Claude Code output is included.

In later commits, update robotic-surgeries/blob/main/README.md repository structures, machine readable paper diagrams and toc, and other affected areas in the repository (this is the only repository that needs to be edited). Add a short 425 character (with spaces) summary for this update. Add 1 additional section towards the top of the README body that further details this version with diagrams (followed by the toc, repository structure, badges, etc.) Include tables where relevant throughout the main/README.

Include v1.0.0 on repository documentation headings and release notes. Be sure to fix and address errors that would cause failed checks for the single pull request (such as for lint and Python environment issues to avoid the following error during final checks): "3 failing checks
x Cl / lint-and-format (3.10) (pull...
x Cl / lint-and-format (3.11) (pull...
x Cl / lint-and-format (3.12) (pull..." Place the new release notes in releases.md under main using the format below. Update other relevant documentation such as project structures. Update the main Readme diagrams, repository structure, etc. where necessary. Update the CHANGELOG.md (v1.0.0).

"FORMAT"
Release title
v1.0.0 - [Fill in Title Here]

## Summary

## Features

## Contributors
@kevinkawchak
@claude
@google-gemini
@openai

## Notes
“FORMAT”
