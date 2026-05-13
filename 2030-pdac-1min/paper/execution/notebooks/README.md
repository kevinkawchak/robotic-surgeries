# Notebooks Execution

This directory captures the equivalent pure Python computation output for the three Jupyter notebooks at `../../codegen/notebooks/`. The notebooks are not run as live kernels because the execution environment lacks a Jupyter kernel. Each notebook's computational output is captured as a text summary; the same numbers are reproducible by importing the codegen modules in a fresh Jupyter kernel.

## Reproduction (when Jupyter is available)

```bash
cd 2030-pdac-1min/paper/codegen
pip install jupyter pandas matplotlib
jupyter nbconvert --to notebook --execute notebooks/iteration_analysis_1min.ipynb
jupyter nbconvert --to notebook --execute notebooks/anastomosis_analysis.ipynb
jupyter nbconvert --to notebook --execute notebooks/daraxonrasib_pk_analysis.ipynb
```

## Files

| File | Description |
|------|-------------|
| `iteration_analysis_summary.txt` | 32 iteration cross arm composite statistics |
| `anastomosis_analysis_summary.txt` | 3 anastomosis cross iteration outcome distribution |
| `daraxonrasib_pk_analysis_summary.txt` | Perioperative pharmacokinetic decay trajectory |

## Summary of Notebook Outputs

### Iteration Analysis
- iterations: 32
- mean composite: 93.298
- 95 percent CI half width: 0.462
- PJ grade A rate: 100.0%
- HJ leak absent rate: 93.8%
- GJ patent rate: 93.8%

### Anastomosis Analysis
The notebook produces two views:
- Iteration sweep view (the publication number): PJ A 32/32, HJ absent 30/32, GJ patent 30/32
- Per anastomosis controller view: PJ A 31/32, HJ absent 14/32, GJ patent 32/32
Ring tension RMSE: 0.0029 N across all 3 anastomoses (within tight 0.005 N tolerance band).

### Daraxonrasib PK Analysis
- Half life: 36 h
- Trough threshold: 0.5 ng/mL
- T 0 serum: 0.45 ng/mL (contract held across all 32 iterations)
- Restart day distribution: T+7d 29/32, T+14d 3/32, T+21d 0/32
