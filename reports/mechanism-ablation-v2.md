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
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.020 | 0.001 | 0.003 | -0.351 | -0.032 | 0.037 | -0.016 | 0.020 | -0.013 | -0.230 | -0.101 | 0.061 | 0.099 |
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.018 | 0.021 | -0.026 | -0.261 | -0.033 | 0.028 | -0.010 | 0.010 | -0.022 | -0.174 | -0.066 | 0.089 | 0.044 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.017 | 0.005 | -0.008 | -0.248 | -0.031 | 0.028 | -0.012 | 0.013 | -0.019 | -0.160 | -0.081 | 0.049 | 0.049 |
| Automatic merits follow-up | `current-us-like` -> `automatic-merits-follow-up` | 0.014 | -0.009 | 0.005 | -0.338 | -0.033 | 0.035 | -0.015 | 0.019 | -0.015 | -0.209 | -0.090 | 0.029 | 0.114 |
| Emergency integrity bundle | `current-us-like` -> `emergency-integrity-package` | 0.012 | 0.001 | 0.004 | -0.338 | -0.029 | 0.038 | -0.017 | 0.020 | -0.019 | -0.209 | -0.087 | 0.054 | 0.145 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.012 | 0.004 | -0.006 | -0.243 | -0.022 | 0.024 | -0.012 | 0.014 | -0.014 | -0.159 | -0.077 | 0.054 | 0.080 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | 0.011 | 0.007 | -0.012 | -0.248 | -0.030 | 0.026 | -0.010 | 0.013 | -0.008 | -0.160 | -0.081 | 0.058 | 0.082 |
| Mandatory written emergency reasoning | `current-us-like` -> `mandatory-written-emergency-reasoning` | 0.010 | 0.010 | -0.013 | -0.290 | -0.025 | 0.024 | -0.010 | 0.013 | -0.005 | -0.186 | -0.068 | 0.069 | 0.095 |
| Strong recusal enforcement | `current-us-like` -> `strong-recusal-enforcement` | 0.009 | 0.004 | -0.007 | -0.245 | -0.023 | 0.024 | -0.012 | 0.014 | -0.012 | -0.159 | -0.078 | 0.052 | 0.103 |
| Jurisdiction-stripping constraints | `term-limited-balanced` -> `jurisdiction-stripping-constraints` | -0.002 | -0.001 | -0.000 | 0.004 | 0.016 | -0.001 | 0.000 | 0.031 | 0.017 | 0.001 | 0.003 | 0.008 | 0.028 |
| Constitutional remand | `nonpartisan-commission` -> `constitutional-remand` | -0.002 | 0.031 | -0.004 | 0.002 | 0.009 | 0.014 | -0.035 | 0.022 | 0.004 | 0.000 | 0.003 | 0.059 | 0.115 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.002 | 0.003 | -0.014 | 0.001 | 0.015 | -0.001 | 0.000 | 0.001 | 0.005 | 0.000 | -0.000 | 0.005 | 0.002 |
| Public-interest litigation filter | `nonpartisan-commission` -> `public-interest-litigation-filter` | -0.006 | -0.005 | 0.012 | 0.007 | 0.016 | -0.008 | 0.000 | 0.002 | 0.014 | 0.002 | 0.007 | 0.002 | 0.042 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.006 | 0.000 | 0.002 | 0.004 | 0.007 | -0.002 | -0.000 | 0.001 | 0.005 | 0.001 | 0.004 | 0.011 | 0.046 |
| Legislative override window | `term-limited-balanced` -> `legislative-override-window` | -0.006 | -0.005 | 0.005 | 0.000 | 0.024 | -0.004 | 0.000 | 0.002 | 0.008 | 0.000 | 0.001 | 0.004 | 0.036 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.008 | 0.011 | -0.003 | -0.001 | 0.015 | 0.007 | -0.002 | 0.047 | 0.005 | -0.001 | -0.002 | 0.018 | 0.092 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.008 | -0.007 | 0.005 | 0.001 | 0.025 | -0.006 | 0.002 | 0.001 | 0.021 | 0.000 | 0.003 | 0.002 | 0.036 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.008 | -0.002 | 0.002 | 0.001 | 0.004 | -0.001 | -0.000 | 0.001 | 0.002 | 0.001 | 0.002 | -0.013 | 0.043 |
| Randomized merits panels | `term-limited-balanced` -> `randomized-merits-panels` | -0.008 | 0.000 | 0.002 | 0.004 | 0.007 | -0.004 | 0.000 | 0.001 | 0.010 | 0.001 | 0.003 | 0.011 | 0.055 |
| Council with concrete-review backstop | `nonpartisan-commission` -> `council-concrete-hybrid` | -0.008 | 0.021 | -0.010 | -0.002 | 0.007 | 0.011 | -0.002 | 0.046 | -0.002 | -0.001 | -0.003 | 0.036 | 0.106 |
| Remand and override-window bundle | `term-limited-balanced` -> `remand-override-window-package` | -0.011 | 0.032 | -0.005 | -0.038 | 0.016 | 0.010 | -0.035 | 0.023 | 0.008 | -0.025 | 0.021 | 0.068 | 0.183 |
| Panel and jurisdiction safeguards | `term-limited-balanced` -> `panel-jurisdiction-safeguards` | -0.012 | 0.004 | -0.009 | -0.008 | 0.019 | -0.005 | 0.001 | 0.028 | 0.012 | -0.013 | 0.021 | 0.033 | 0.084 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.020 | 0.012 | -0.035 | -0.013 | 0.030 | 0.004 | -0.019 | 0.017 | 0.003 | -0.013 | 0.015 | 0.049 | 0.099 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.036 | -0.034 | -0.000 | -0.014 | 0.040 | -0.011 | 0.004 | -0.003 | 0.010 | -0.013 | 0.016 | -0.055 | 0.139 |
