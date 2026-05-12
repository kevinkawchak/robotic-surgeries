# Section 3: Results: Digital Twin Simulation Notebook

```
Simulating 38 cycles for 1000 patients...

============================================================
DIGITAL TWIN BI-DIRECTIONAL FEEDBACK LOOP ACTIVE
============================================================

Cycle Progress:
Cycle   0/38 [........................................] Month  0.0 | Alive: 1000 | Progressed:    0
Cycle   2/38 [##......................................] Month  1.9 | Alive:  945 | Progressed:  219
Cycle   4/38 [####....................................] Month  3.7 | Alive:  849 | Progressed:  405
Cycle   6/38 [######..................................] Month  5.6 | Alive:  763 | Progressed:  514
Cycle   8/38 [########................................] Month  7.5 | Alive:  656 | Progressed:  591
Cycle  10/38 [##########..............................] Month  9.3 | Alive:  551 | Progressed:  626
Cycle  12/38 [############............................] Month 11.2 | Alive:  481 | Progressed:  648
Cycle  14/38 [##############..........................] Month 13.1 | Alive:  420 | Progressed:  674
Cycle  16/38 [################........................] Month 14.9 | Alive:  337 | Progressed:  826
Cycle  18/38 [##################......................] Month 16.8 | Alive:  274 | Progressed:  866
Cycle  20/38 [#####################...................] Month 18.7 | Alive:  214 | Progressed:  872
Cycle  22/38 [#######################.................] Month 20.5 | Alive:  157 | Progressed:  893
Cycle  24/38 [#########################...............] Month 22.4 | Alive:  118 | Progressed:  895
Cycle  26/38 [###########################.............] Month 24.3 | Alive:   92 | Progressed:  897
Cycle  28/38 [#############################...........] Month 26.1 | Alive:   74 | Progressed:  897
Cycle  30/38 [###############################.........] Month 28.0 | Alive:   52 | Progressed:  897
Cycle  32/38 [#################################.......] Month 29.9 | Alive:   40 | Progressed:  897
Cycle  34/38 [###################################.....] Month 31.7 | Alive:   32 | Progressed:  897
Cycle  36/38 [#####################################...] Month 33.6 | Alive:   27 | Progressed:  897


Simulation complete!

Compiling results...

Main results saved to pdac_digital_twin_calibrated_final.csv
Sample patient logs saved to patient_logs/ directory

Generating specialized outputs for analysis...
[X] Adaptation log saved to adaptation_log.csv
[X] Kaplan-Meier data (by arm) saved to km_data_by_arm.csv
[X] Waterfall plot data saved to waterfall_plot_data.csv

============================================================
TRIAL SUMMARY STATISTICS
============================================================
Arm   N      ORR%   DCR% | mPFS (HR)    PFS-6 | mOS (HR)     OS-12 | Safety (G3+/Drop%)
--- ----- ------ ------ | ------------ ----- | ------------ ----- | ------------------
A   100    21.0%  82.0% |  4.7 (1.00)  42.0% |  9.3 (1.00)  43.0% | 31.0% / 17.0%     
B   100    31.0%  85.0% |  6.3 (0.80)  51.0% | 10.7 (0.96)  48.0% | 44.0% / 19.0%     
C   100    44.0%  96.0% |  7.5 (0.63)  57.0% | 13.1 (0.67)  54.0% | 39.0% / 21.0%     
D   100    19.0%  82.0% |  3.8 (1.15)  33.0% |  9.8 (1.07)  40.0% | 26.0% / 17.0%     
E   100    44.0%  95.0% |  5.6 (0.83)  45.0% | 11.2 (0.83)  48.0% | 41.0% / 26.0%     
G   100     3.0%  41.0% |  1.8 (1.00)   9.0% |  5.6 (1.00)  15.0% | 18.0% / 10.0%     
H   100    47.0%  93.0% |  7.5 (0.31)  55.0% | 12.1 (0.34)  55.0% | 36.0% / 21.0%     
I   100    17.0%  79.0% |  3.1 (0.49)  29.0% |  8.4 (0.58)  35.0% | 22.0% / 12.0%     
J   100    39.0%  97.0% | 10.3 (0.00)  67.0% | 21.5 (0.38)  85.0% | 47.0% / 18.0%     
K   100     0.0%   0.0% |  1.0 (1.00)   0.0% | 14.0 (1.00)  58.0% | 14.0% /  5.0%     

[X] Treatment adaptation summary saved to adaptation_summary.csv

============================================================
DIGITAL TWIN TRIAL SIMULATION COMPLETE
============================================================

All outputs saved. Main results in 'pdac_digital_twin_calibrated_final.csv'

Total simulation runtime: 13.12 seconds (0.22 minutes)

The digital twin successfully:
  [X] Generated continuous patient data with calibrated parameters
  [X] Analyzed patient states each cycle
  [X] Provided personalized treatment recommendations
  [X] Adapted therapy based on response and toxicity
  [X] Reported ORR, PFS, and OS values
```

Cycles Indicate Patient Progress over Time, Summary Provides Final Outcomes for Each Arm
