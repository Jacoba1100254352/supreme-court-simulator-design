# Mechanism Ablation v2

Pairwise comparisons that change one institutional mechanism at a time where the catalog permits a close proxy.

## Run Configuration

- runs per pair/case: 60
- cases per run: 48
- base seed: 20260501
- mechanisms: 24
- stress cases: 8
- legislative input: simulation-campaign-v21-paper.csv

Positive deltas improve higher-better metrics. Negative deltas improve lower-better diagnostics such as partisan alignment, shadow abuse, conflict, and administrative cost.

## Weighted Mechanism Summary

| Mechanism | Base -> Variant | Directional | Legal | Rights | Shadow | Conflict | Lower-court compliance | LC resistance | Enforcement | Gov. noncomp. | Emerg. opp. | Emerg. downstream | Precedent durability | Admin cost |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.018 | 0.028 | -0.025 | -0.223 | -0.043 | 0.022 | -0.009 | 0.007 | -0.035 | -0.171 | -0.061 | 0.094 | 0.038 |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.015 | -0.014 | -0.002 | -0.308 | -0.044 | 0.032 | -0.016 | 0.017 | -0.035 | -0.225 | -0.111 | 0.011 | 0.080 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.013 | 0.007 | -0.016 | -0.214 | -0.041 | 0.023 | -0.012 | 0.010 | -0.037 | -0.156 | -0.080 | 0.041 | 0.043 |
| Mandatory written emergency reasoning | `current-us-like` -> `mandatory-written-emergency-reasoning` | 0.010 | 0.017 | -0.024 | -0.249 | -0.042 | 0.024 | -0.011 | 0.009 | -0.039 | -0.183 | -0.064 | 0.067 | 0.080 |
| Emergency integrity bundle | `current-us-like` -> `emergency-integrity-package` | 0.009 | -0.014 | -0.002 | -0.303 | -0.045 | 0.033 | -0.017 | 0.017 | -0.043 | -0.206 | -0.113 | 0.008 | 0.119 |
| Automatic merits follow-up | `current-us-like` -> `automatic-merits-follow-up` | 0.009 | -0.020 | -0.003 | -0.299 | -0.043 | 0.031 | -0.016 | 0.016 | -0.039 | -0.205 | -0.111 | -0.005 | 0.096 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.009 | 0.004 | -0.015 | -0.211 | -0.036 | 0.020 | -0.010 | 0.010 | -0.026 | -0.155 | -0.077 | 0.039 | 0.065 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | 0.008 | 0.006 | -0.016 | -0.216 | -0.039 | 0.022 | -0.012 | 0.010 | -0.034 | -0.156 | -0.081 | 0.042 | 0.072 |
| Strong recusal enforcement | `current-us-like` -> `strong-recusal-enforcement` | 0.007 | 0.006 | -0.015 | -0.210 | -0.037 | 0.021 | -0.011 | 0.010 | -0.035 | -0.155 | -0.078 | 0.043 | 0.087 |
| Constitutional remand | `nonpartisan-commission` -> `constitutional-remand` | 0.004 | 0.037 | -0.002 | -0.000 | -0.003 | 0.020 | -0.036 | 0.019 | -0.005 | -0.000 | -0.001 | 0.064 | 0.091 |
| Public-interest litigation filter | `nonpartisan-commission` -> `public-interest-litigation-filter` | 0.001 | 0.007 | 0.006 | -0.000 | -0.002 | 0.002 | -0.001 | 0.000 | -0.002 | 0.000 | -0.001 | 0.017 | 0.025 |
| Jurisdiction-stripping constraints | `term-limited-balanced` -> `jurisdiction-stripping-constraints` | -0.001 | -0.004 | 0.003 | -0.000 | 0.014 | 0.001 | -0.000 | 0.030 | 0.011 | 0.000 | -0.000 | 0.002 | 0.022 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.002 | 0.003 | -0.011 | -0.001 | 0.016 | 0.000 | 0.000 | 0.001 | 0.001 | 0.000 | -0.002 | 0.005 | -0.000 |
| Remand and override-window bundle | `term-limited-balanced` -> `remand-override-window-package` | -0.003 | 0.041 | -0.005 | -0.030 | 0.002 | 0.016 | -0.035 | 0.020 | 0.004 | -0.026 | 0.019 | 0.079 | 0.147 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.005 | 0.001 | 0.000 | -0.000 | -0.000 | 0.000 | 0.000 | 0.000 | 0.003 | 0.000 | 0.001 | 0.005 | 0.038 |
| Randomized merits panels | `term-limited-balanced` -> `randomized-merits-panels` | -0.005 | 0.002 | 0.000 | 0.001 | -0.001 | 0.001 | -0.000 | 0.000 | -0.003 | -0.000 | 0.001 | 0.009 | 0.045 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.007 | -0.005 | 0.002 | -0.001 | 0.020 | -0.003 | 0.001 | 0.001 | 0.010 | 0.000 | -0.000 | -0.001 | 0.028 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.007 | 0.009 | 0.001 | -0.002 | 0.016 | 0.006 | -0.002 | 0.045 | 0.004 | -0.000 | -0.002 | 0.013 | 0.083 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.007 | -0.002 | 0.001 | 0.001 | 0.002 | -0.000 | -0.000 | 0.000 | -0.000 | 0.001 | 0.001 | -0.013 | 0.037 |
| Legislative override window | `term-limited-balanced` -> `legislative-override-window` | -0.008 | -0.007 | 0.001 | -0.000 | 0.025 | -0.004 | 0.001 | 0.002 | 0.013 | 0.000 | 0.001 | -0.004 | 0.030 |
| Council with concrete-review backstop | `nonpartisan-commission` -> `council-concrete-hybrid` | -0.008 | 0.013 | 0.003 | -0.002 | 0.016 | 0.006 | -0.001 | 0.046 | 0.012 | 0.000 | -0.002 | 0.024 | 0.098 |
| Panel and jurisdiction safeguards | `term-limited-balanced` -> `panel-jurisdiction-safeguards` | -0.008 | 0.008 | -0.008 | -0.007 | 0.014 | -0.002 | 0.001 | 0.028 | 0.010 | -0.014 | 0.022 | 0.034 | 0.070 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.012 | 0.024 | -0.028 | -0.009 | 0.018 | 0.009 | -0.021 | 0.017 | -0.014 | -0.015 | 0.018 | 0.063 | 0.084 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.031 | -0.025 | -0.002 | -0.008 | 0.031 | -0.010 | 0.003 | -0.003 | 0.011 | -0.014 | 0.022 | -0.042 | 0.120 |
