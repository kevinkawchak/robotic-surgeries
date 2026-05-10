# Visualization Outputs

Static and interactive renderings produced from the run artifacts. The PNG and
HTML files are mirrored from the upstream `viz/` folder; the ASCII chart files
are generated directly from the metric and iteration outputs.

## Files

| Filename                       | Type   | Notes                                            |
|--------------------------------|--------|--------------------------------------------------|
| metrics_dashboard.html         | html   | self-contained Plotly dashboard                  |
| metrics_summary.png            | png    | static metrics summary chart                     |
| per_arm_contribution.png       | png    | per-arm contribution chart                       |
| xyz_path_4arm.txt              | text   | 4-arm per-second xyz path overlay                |
| composite_bar_chart.txt        | ASCII  | composite score per iteration bar chart          |
| composite_histogram.txt        | ASCII  | robot vs human composite histogram               |
| per_arm_resection_chart.txt    | ASCII  | per-arm resection volume mean (mm^3)             |
| wall_clock_chart.txt           | ASCII  | wall-clock seconds per iteration bar chart       |

## Rendering Notes

The PNG files are placeholder bytes when matplotlib is not present in the
local environment; in this run only the upstream pre-rendered artifacts were
copied into outputs/viz to avoid overwriting committed renders. The ASCII
charts are generated and serve as the primary visualization for paper
publication.
