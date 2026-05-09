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
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.018 | 0.028 | -0.026 | -0.232 | -0.045 | 0.023 | -0.010 | 0.007 | -0.037 | -0.172 | -0.063 | 0.093 | 0.039 |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.015 | -0.017 | -0.001 | -0.317 | -0.043 | 0.032 | -0.017 | 0.017 | -0.038 | -0.226 | -0.113 | 0.007 | 0.083 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.013 | 0.006 | -0.018 | -0.224 | -0.044 | 0.024 | -0.012 | 0.010 | -0.035 | -0.157 | -0.084 | 0.040 | 0.043 |
| Automatic merits follow-up | `current-us-like` -> `automatic-merits-follow-up` | 0.010 | -0.021 | -0.003 | -0.314 | -0.045 | 0.033 | -0.017 | 0.017 | -0.042 | -0.208 | -0.115 | -0.007 | 0.099 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | 0.010 | 0.008 | -0.016 | -0.222 | -0.044 | 0.025 | -0.013 | 0.010 | -0.044 | -0.157 | -0.082 | 0.045 | 0.073 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.010 | 0.006 | -0.016 | -0.223 | -0.042 | 0.023 | -0.011 | 0.010 | -0.033 | -0.157 | -0.083 | 0.041 | 0.065 |
| Mandatory written emergency reasoning | `current-us-like` -> `mandatory-written-emergency-reasoning` | 0.009 | 0.015 | -0.026 | -0.258 | -0.044 | 0.024 | -0.011 | 0.009 | -0.039 | -0.184 | -0.066 | 0.063 | 0.081 |
| Emergency integrity bundle | `current-us-like` -> `emergency-integrity-package` | 0.009 | -0.015 | -0.003 | -0.312 | -0.046 | 0.034 | -0.018 | 0.017 | -0.046 | -0.207 | -0.116 | 0.008 | 0.123 |
| Strong recusal enforcement | `current-us-like` -> `strong-recusal-enforcement` | 0.006 | 0.004 | -0.016 | -0.219 | -0.038 | 0.021 | -0.011 | 0.010 | -0.031 | -0.156 | -0.081 | 0.040 | 0.088 |
| Constitutional remand | `nonpartisan-commission` -> `constitutional-remand` | 0.003 | 0.036 | -0.002 | -0.000 | -0.002 | 0.020 | -0.036 | 0.021 | -0.001 | -0.001 | -0.000 | 0.064 | 0.095 |
| Public-interest litigation filter | `nonpartisan-commission` -> `public-interest-litigation-filter` | 0.002 | 0.009 | 0.003 | -0.002 | -0.005 | 0.003 | -0.001 | 0.000 | -0.003 | -0.000 | -0.002 | 0.020 | 0.025 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.002 | 0.001 | -0.010 | -0.002 | 0.018 | -0.001 | 0.000 | 0.001 | 0.004 | 0.000 | -0.002 | 0.002 | 0.000 |
| Remand and override-window bundle | `term-limited-balanced` -> `remand-override-window-package` | -0.003 | 0.043 | -0.005 | -0.033 | 0.003 | 0.017 | -0.035 | 0.021 | 0.002 | -0.026 | 0.018 | 0.083 | 0.152 |
| Jurisdiction-stripping constraints | `term-limited-balanced` -> `jurisdiction-stripping-constraints` | -0.004 | -0.005 | 0.000 | 0.002 | 0.017 | -0.002 | 0.001 | 0.030 | 0.020 | 0.000 | 0.002 | 0.000 | 0.023 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.005 | -0.001 | 0.001 | 0.000 | 0.000 | -0.000 | 0.000 | 0.000 | 0.001 | 0.000 | 0.001 | 0.001 | 0.039 |
| Randomized merits panels | `term-limited-balanced` -> `randomized-merits-panels` | -0.006 | 0.002 | -0.000 | 0.003 | 0.001 | -0.000 | -0.000 | 0.000 | -0.001 | 0.000 | 0.003 | 0.008 | 0.047 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.006 | 0.001 | -0.000 | 0.001 | 0.000 | 0.000 | -0.000 | -0.000 | -0.001 | 0.000 | -0.000 | -0.006 | 0.037 |
| Council with concrete-review backstop | `nonpartisan-commission` -> `council-concrete-hybrid` | -0.007 | 0.017 | 0.001 | -0.002 | 0.013 | 0.007 | -0.001 | 0.045 | 0.009 | -0.000 | -0.003 | 0.029 | 0.098 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.007 | 0.009 | 0.003 | -0.002 | 0.017 | 0.005 | -0.001 | 0.046 | 0.010 | -0.001 | -0.003 | 0.013 | 0.085 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.007 | -0.008 | 0.004 | -0.000 | 0.023 | -0.003 | 0.001 | 0.001 | 0.009 | 0.000 | 0.000 | -0.005 | 0.030 |
| Legislative override window | `term-limited-balanced` -> `legislative-override-window` | -0.008 | -0.006 | 0.000 | 0.000 | 0.025 | -0.005 | 0.002 | 0.002 | 0.017 | 0.000 | 0.001 | -0.002 | 0.030 |
| Panel and jurisdiction safeguards | `term-limited-balanced` -> `panel-jurisdiction-safeguards` | -0.009 | 0.008 | -0.006 | -0.006 | 0.017 | -0.003 | 0.001 | 0.028 | 0.008 | -0.014 | 0.024 | 0.037 | 0.074 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.013 | 0.025 | -0.030 | -0.008 | 0.018 | 0.008 | -0.020 | 0.017 | -0.005 | -0.015 | 0.019 | 0.066 | 0.085 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.032 | -0.027 | -0.003 | -0.009 | 0.031 | -0.010 | 0.003 | -0.003 | 0.010 | -0.014 | 0.021 | -0.048 | 0.122 |
