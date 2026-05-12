# Mechanism Ablation v2

Pairwise comparisons that change one institutional mechanism at a time where the catalog permits a close proxy.

## Run Configuration

- runs per pair/case: 60
- cases per run: 48
- base seed: 20260501
- mechanisms: 25
- stress cases: 8
- legislative input: simulation-campaign-v21-paper.csv

Positive deltas improve higher-better metrics. Negative deltas improve lower-better diagnostics such as partisan alignment, shadow abuse, conflict, and administrative cost.

## Weighted Mechanism Summary

| Mechanism | Base -> Variant | Directional | Legal | Rights | Shadow | Conflict | Lower-court compliance | LC resistance | Enforcement | Gov. noncomp. | Emerg. opp. | Emerg. downstream | Precedent durability | Admin cost |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.016 | 0.026 | -0.025 | -0.222 | -0.042 | 0.022 | -0.010 | 0.007 | -0.040 | -0.170 | -0.061 | 0.088 | 0.039 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.015 | 0.010 | -0.017 | -0.216 | -0.045 | 0.025 | -0.012 | 0.010 | -0.039 | -0.155 | -0.082 | 0.048 | 0.041 |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.015 | -0.016 | -0.001 | -0.312 | -0.043 | 0.031 | -0.016 | 0.017 | -0.032 | -0.226 | -0.112 | 0.009 | 0.082 |
| Automatic merits follow-up | `current-us-like` -> `automatic-merits-follow-up` | 0.011 | -0.016 | -0.006 | -0.300 | -0.045 | 0.031 | -0.016 | 0.016 | -0.034 | -0.205 | -0.111 | 0.005 | 0.095 |
| Mandatory written emergency reasoning | `current-us-like` -> `mandatory-written-emergency-reasoning` | 0.010 | 0.016 | -0.021 | -0.246 | -0.040 | 0.022 | -0.011 | 0.009 | -0.035 | -0.182 | -0.063 | 0.064 | 0.080 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | 0.009 | 0.009 | -0.017 | -0.212 | -0.041 | 0.021 | -0.011 | 0.009 | -0.031 | -0.155 | -0.080 | 0.047 | 0.070 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.009 | 0.004 | -0.015 | -0.211 | -0.036 | 0.020 | -0.010 | 0.010 | -0.026 | -0.155 | -0.077 | 0.039 | 0.065 |
| Emergency integrity bundle | `current-us-like` -> `emergency-integrity-package` | 0.008 | -0.018 | 0.001 | -0.299 | -0.040 | 0.029 | -0.016 | 0.017 | -0.030 | -0.205 | -0.111 | 0.006 | 0.121 |
| Strong recusal enforcement | `current-us-like` -> `strong-recusal-enforcement` | 0.007 | 0.006 | -0.018 | -0.216 | -0.041 | 0.024 | -0.012 | 0.010 | -0.039 | -0.156 | -0.080 | 0.041 | 0.086 |
| Constitutional remand | `nonpartisan-commission` -> `constitutional-remand` | 0.003 | 0.035 | -0.001 | -0.000 | 0.001 | 0.019 | -0.036 | 0.020 | -0.001 | 0.000 | -0.001 | 0.064 | 0.094 |
| Public-interest litigation filter | `nonpartisan-commission` -> `public-interest-litigation-filter` | 0.002 | 0.007 | 0.007 | -0.002 | -0.004 | 0.003 | -0.001 | 0.000 | -0.004 | -0.000 | -0.002 | 0.014 | 0.024 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.000 | 0.002 | -0.011 | -0.005 | 0.013 | 0.003 | -0.001 | 0.001 | -0.006 | -0.000 | -0.004 | -0.001 | -0.002 |
| Remand and override-window bundle | `term-limited-balanced` -> `remand-override-window-package` | -0.002 | 0.043 | -0.006 | -0.031 | 0.001 | 0.018 | -0.035 | 0.020 | -0.000 | -0.026 | 0.018 | 0.083 | 0.147 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.003 | 0.002 | 0.001 | 0.000 | 0.000 | 0.001 | -0.001 | 0.000 | -0.006 | 0.000 | 0.001 | 0.009 | 0.038 |
| Jurisdiction-stripping constraints | `term-limited-balanced` -> `jurisdiction-stripping-constraints` | -0.003 | -0.004 | -0.001 | 0.002 | 0.015 | -0.001 | 0.000 | 0.030 | 0.015 | -0.000 | 0.002 | 0.001 | 0.022 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.006 | 0.000 | 0.002 | 0.001 | 0.001 | 0.001 | -0.001 | 0.000 | -0.006 | -0.000 | 0.001 | -0.009 | 0.036 |
| Randomized merits panels | `term-limited-balanced` -> `randomized-merits-panels` | -0.006 | 0.001 | 0.001 | 0.001 | 0.000 | -0.000 | 0.000 | 0.000 | 0.003 | 0.001 | 0.000 | 0.006 | 0.046 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.007 | 0.009 | 0.001 | -0.001 | 0.016 | 0.006 | -0.002 | 0.045 | 0.003 | -0.000 | -0.002 | 0.014 | 0.082 |
| Legislative override window | `term-limited-balanced` -> `legislative-override-window` | -0.007 | -0.005 | 0.003 | 0.000 | 0.023 | -0.004 | 0.001 | 0.002 | 0.012 | 0.000 | 0.001 | -0.002 | 0.030 |
| Council with concrete-review backstop | `nonpartisan-commission` -> `council-concrete-hybrid` | -0.008 | 0.015 | 0.003 | -0.000 | 0.015 | 0.006 | -0.002 | 0.045 | 0.006 | 0.001 | -0.001 | 0.026 | 0.099 |
| Panel and jurisdiction safeguards | `term-limited-balanced` -> `panel-jurisdiction-safeguards` | -0.008 | 0.012 | -0.010 | -0.008 | 0.011 | -0.001 | 0.001 | 0.027 | 0.008 | -0.015 | 0.021 | 0.039 | 0.069 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.008 | -0.008 | 0.003 | 0.000 | 0.025 | -0.005 | 0.001 | 0.001 | 0.015 | 0.000 | 0.001 | -0.002 | 0.030 |
| Judicial electorate selection | `nonpartisan-commission` -> `judicial-electorate-selection` | -0.008 | 0.002 | -0.001 | 0.001 | 0.001 | -0.001 | 0.001 | 0.000 | 0.006 | -0.000 | 0.000 | 0.007 | 0.063 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.014 | 0.023 | -0.029 | -0.009 | 0.019 | 0.008 | -0.020 | 0.017 | -0.004 | -0.014 | 0.020 | 0.061 | 0.084 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.030 | -0.025 | -0.003 | -0.008 | 0.030 | -0.010 | 0.003 | -0.003 | 0.010 | -0.015 | 0.020 | -0.041 | 0.119 |
