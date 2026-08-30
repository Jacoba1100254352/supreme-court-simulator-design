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
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.017 | 0.026 | -0.025 | -0.225 | -0.042 | 0.023 | -0.011 | 0.007 | -0.043 | -0.171 | -0.061 | 0.090 | 0.039 |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.015 | -0.016 | -0.002 | -0.314 | -0.042 | 0.031 | -0.016 | 0.017 | -0.035 | -0.226 | -0.113 | 0.009 | 0.082 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.014 | 0.009 | -0.017 | -0.215 | -0.043 | 0.024 | -0.011 | 0.010 | -0.037 | -0.155 | -0.082 | 0.047 | 0.042 |
| Automatic merits follow-up | `current-us-like` -> `automatic-merits-follow-up` | 0.011 | -0.018 | -0.005 | -0.301 | -0.044 | 0.031 | -0.016 | 0.016 | -0.035 | -0.206 | -0.111 | 0.002 | 0.096 |
| Mandatory written emergency reasoning | `current-us-like` -> `mandatory-written-emergency-reasoning` | 0.010 | 0.016 | -0.022 | -0.249 | -0.041 | 0.022 | -0.010 | 0.009 | -0.033 | -0.183 | -0.064 | 0.065 | 0.080 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | 0.009 | 0.008 | -0.017 | -0.214 | -0.041 | 0.021 | -0.011 | 0.010 | -0.031 | -0.156 | -0.081 | 0.047 | 0.070 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.009 | 0.004 | -0.016 | -0.213 | -0.037 | 0.021 | -0.011 | 0.010 | -0.030 | -0.155 | -0.079 | 0.039 | 0.065 |
| Emergency integrity bundle | `current-us-like` -> `emergency-integrity-package` | 0.008 | -0.017 | -0.000 | -0.302 | -0.041 | 0.030 | -0.016 | 0.017 | -0.029 | -0.205 | -0.112 | 0.006 | 0.121 |
| Strong recusal enforcement | `current-us-like` -> `strong-recusal-enforcement` | 0.007 | 0.006 | -0.019 | -0.218 | -0.041 | 0.023 | -0.011 | 0.010 | -0.035 | -0.156 | -0.081 | 0.042 | 0.086 |
| Constitutional remand | `nonpartisan-commission` -> `constitutional-remand` | 0.004 | 0.036 | -0.001 | -0.001 | -0.001 | 0.020 | -0.037 | 0.020 | -0.005 | 0.000 | -0.001 | 0.064 | 0.094 |
| Public-interest litigation filter | `nonpartisan-commission` -> `public-interest-litigation-filter` | 0.002 | 0.007 | 0.006 | -0.002 | -0.004 | 0.002 | -0.000 | 0.000 | -0.001 | -0.000 | -0.003 | 0.015 | 0.024 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.000 | 0.003 | -0.011 | -0.004 | 0.013 | 0.003 | -0.001 | 0.001 | -0.007 | -0.000 | -0.004 | 0.002 | -0.001 |
| Jurisdiction-stripping constraints | `term-limited-balanced` -> `jurisdiction-stripping-constraints` | -0.003 | -0.004 | -0.000 | 0.001 | 0.014 | 0.000 | 0.000 | 0.030 | 0.012 | -0.000 | 0.001 | 0.001 | 0.021 |
| Remand and override-window bundle | `term-limited-balanced` -> `remand-override-window-package` | -0.003 | 0.043 | -0.006 | -0.030 | 0.003 | 0.017 | -0.035 | 0.020 | 0.002 | -0.026 | 0.020 | 0.084 | 0.149 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.003 | 0.002 | 0.001 | 0.000 | -0.000 | 0.002 | -0.001 | 0.000 | -0.007 | 0.000 | 0.001 | 0.009 | 0.038 |
| Randomized merits panels | `term-limited-balanced` -> `randomized-merits-panels` | -0.006 | 0.001 | 0.002 | 0.001 | -0.000 | 0.000 | -0.000 | 0.000 | 0.000 | 0.001 | 0.000 | 0.006 | 0.046 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.006 | 0.011 | -0.000 | -0.002 | 0.015 | 0.007 | -0.002 | 0.045 | 0.002 | -0.000 | -0.002 | 0.017 | 0.082 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.006 | -0.000 | 0.001 | 0.001 | 0.001 | 0.000 | -0.000 | -0.000 | -0.005 | 0.000 | 0.001 | -0.009 | 0.036 |
| Legislative override window | `term-limited-balanced` -> `legislative-override-window` | -0.007 | -0.005 | 0.003 | 0.000 | 0.023 | -0.003 | 0.001 | 0.002 | 0.011 | 0.000 | 0.001 | -0.002 | 0.030 |
| Judicial electorate selection | `nonpartisan-commission` -> `judicial-electorate-selection` | -0.008 | 0.003 | -0.001 | 0.001 | 0.000 | -0.000 | 0.000 | -0.000 | 0.004 | 0.000 | 0.000 | 0.008 | 0.063 |
| Council with concrete-review backstop | `nonpartisan-commission` -> `council-concrete-hybrid` | -0.008 | 0.015 | 0.004 | -0.000 | 0.016 | 0.006 | -0.001 | 0.046 | 0.008 | 0.001 | -0.001 | 0.026 | 0.100 |
| Panel and jurisdiction safeguards | `term-limited-balanced` -> `panel-jurisdiction-safeguards` | -0.008 | 0.012 | -0.010 | -0.007 | 0.012 | -0.002 | 0.002 | 0.027 | 0.010 | -0.015 | 0.022 | 0.040 | 0.070 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.009 | -0.009 | 0.002 | 0.001 | 0.027 | -0.006 | 0.002 | 0.001 | 0.019 | 0.000 | 0.001 | -0.003 | 0.031 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.013 | 0.024 | -0.029 | -0.008 | 0.018 | 0.008 | -0.019 | 0.017 | -0.004 | -0.014 | 0.020 | 0.063 | 0.084 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.030 | -0.024 | -0.004 | -0.008 | 0.029 | -0.010 | 0.004 | -0.003 | 0.011 | -0.015 | 0.020 | -0.040 | 0.119 |
