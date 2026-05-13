# PR Workflow (Nine Commit Single PR)

This file fixes the nine commit single PR workflow for the future generated PDAC 1 minute simulation tree at 2030-pdac-1min/. The future Claude Code Opus 4.7 1M Max session reads this file to author the nine commit sequence and to enforce the 2nd to last commit error fix pattern and the last commit repository update pattern.

## Why Nine Commits Instead of Seven

The v3.9.1 GBM 1 minute variant used a seven commit single PR workflow. The PDAC 1 minute variant extends this to nine commits because the PDAC scenario adds two new dimensions (the 5 vessel safety zones and the 3 anastomosis events plus Daraxonrasib integration) that did not exist in the GBM variant. The nine commit pattern preserves the 7 plus 2 working memory budget per commit established in the GBM variant while accommodating the additional PDAC dimensions.

## Nine Commit Sequence

The nine commit sequence for the future generated code at 2030-pdac-1min/ is reproduced below. The first commit emits the project skeleton; commits 2 through 5 emit the per dimension implementation (sensors, xyz, iterations, competition); commits 6 and 7 emit the PDAC specific dimensions (vascular safety + anastomosis + Daraxonrasib); commit 8 fixes errors; commit 9 updates the repository.

| Commit | Focus | Files emitted | Commit message prefix |
|--------|-------|----------------|-----------------------|
| 1 | Project overview, docs, configs | README.md, LICENSE.txt, pyproject.toml, docker-compose.yml, .gitignore, docs/*.md, config/project.yaml | v0.5.0 commit 1/9: project skeleton and docs |
| 2 | Sensors | schemas/sensor_record_8arm.*, src/sensors/ingest_8arm.py, data/sensor_sample_8arm.{jsonl, csv}, outputs/sensors/* | v0.5.0 commit 2/9: 640 channel sensor stack |
| 3 | XYZ mapping | schemas/xyz_command_8arm.*, src/mapping/sensor_to_xyz_8arm.py, config/kinematics_8arm.yaml, src/control/robot_loop_8arm.cpp, src/coordination/arm_heartbeat_10khz.cpp | v0.5.0 commit 3/9: 8 arm xyz mapping and heartbeat |
| 4 | Iterations | src/simulation/iterate_1min.py, src/simulation/runner_1min.rs, config/iterations.yaml, src/metrics/compute_1min.py, data/iterations/ run_NNNNN_*.parquet | v0.5.0 commit 4/9: 32 iteration sweep |
| 5 | Competition | src/llm/compare_agent_1min.py, prompts/comparison_prompt_1min.md, results/comparison.json, results/comparison_report.{md, pdf}, outputs/comparison/*, outputs/comparison_robot_vs_human/* | v0.5.0 commit 5/9: 4 entrant tournament |
| 6 | Vascular safety + Anastomosis | src/vascular/safety_zone_gate.py, src/anastomosis/*.py, config/vascular_safety_zones.yaml, config/anastomosis_targets.yaml, schemas/anastomosis_event.schema.json | v0.5.0 commit 6/9: vascular safety + 3 anastomoses |
| 7 | Daraxonrasib + Zenodo + viz + notebooks | src/daraxonrasib/*.py, schemas/daraxonrasib_event.schema.json, src/zenodo/patch_pointers.py, viz/*.{html, txt, png}, notebooks/*.ipynb, prompts/daraxonrasib_advisory_prompt.md | v0.5.0 commit 7/9: Daraxonrasib + Zenodo + viz |
| 8 (2nd to last) | Error fixes | Cross commit lint, format, cross reference fixes; per file ruff format, ruff check, yamllint, markdownlint fixes; pre commit hook fixes; file size cap fixes; Parquet size cap fixes | v0.5.0 commit 8/9: error fixes for CI lint matrix 3.10/3.11/3.12 |
| 9 (last) | Repository updates | Top level README.md, releases.md (v0.5.0 block per the FORMAT), CHANGELOG.md (v0.5.0 block), 2030-pdac-1min/README.md updates, repository structure diagram updates | v0.5.0 commit 9/9: repository updates and v0.5.0 release notes |

## 2nd to Last Commit (Error Fixes)

The 8th commit (2nd to last) explicitly addresses the CI lint and format matrix failure mode noted in the upstream PR template: 3 failing checks (Cl / lint-and-format (3.10) (pull...), (3.11) (pull...), (3.12) (pull...)). The 8th commit runs the pre commit hook configuration from ci_compliance_checklist.md across every committed file in 2030-pdac-1min/ and emits per file lint and format fixes.

The 8th commit also performs the following cross commit checks:

1. Every per arm xyz command record in data/xyz_command_sample_8arm.jsonl resolves to a valid command_enum value.
2. Every per anastomosis event in run_NNNNN_L4_anastomosis.parquet has a valid realized grade.
3. Every per iteration L0 pointer in run_NNNNN_L0_raw.zenodo_pointer.json has a valid SHA 256 manifest entry.
4. Every per arm tip force violation in run_NNNNN_events.parquet has a valid resolution field.
5. Every per round LLM tournament verdict in results/comparison.json preserves the structural time dimension caveat in the rationale.
6. Every committed file is under 10 MB.
7. Every committed Parquet is under 5 MB.
8. Every ruff format, ruff check, yamllint -d relaxed, and markdownlint pass returns exit code 0.

## Last Commit (Repository Updates)

The 9th commit (last) updates the repository top level documentation per the FORMAT in the parent README.

1. Top level README.md: add v0.5.0 release badge, add PDAC variant badge, add PDAC ASCII pipeline diagram, add PDAC subtree to Repository Structure block, update See also block.
2. releases.md: prepend a v0.5.0 release notes block per the FORMAT (Release title / Summary / Features / Contributors / Notes).
3. CHANGELOG.md: prepend a v0.5.0 entry (Added / Changed / Fixed / Notes).
4. 2030-pdac-1min/README.md: update Repository Tree block with the PDAC subdirectory contents.
5. references.md: add the seven BibTeX entries (paper-1, paper-2, paper-3, paper-4, kawchak_2026_20113157, kawchak_2025_18099351, plus the parent repository BibTeX entry).

## Cross References

- ci_compliance_checklist.md fixes the lint and format gates that the 8th commit enforces.
- commit_06_error_fixes.md fixes the 8th commit detailed error review.
- commit_07_repository_updates.md fixes the 9th commit detailed repository updates.
- README.md (this directory) fixes the nine commit plan for this PR.
