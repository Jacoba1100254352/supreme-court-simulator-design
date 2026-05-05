# Mechanism Ablation v2

Pairwise comparisons that change one institutional mechanism at a time where the catalog permits a close proxy.

## Run Configuration

- runs per pair/case: 60
- cases per run: 48
- base seed: 20260501
- mechanisms: 20
- stress cases: 8
- legislative input: simulation-campaign-v21-paper.csv

Positive deltas improve higher-better metrics. Negative deltas improve lower-better diagnostics such as partisan alignment, shadow abuse, conflict, and administrative cost.

## Weighted Mechanism Summary

| Mechanism | Base -> Variant | Directional | Legal | Rights | Shadow | Conflict | Lower-court compliance | Gov. noncomp. | Emerg. downstream | Precedent durability | Admin cost |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.018 | 0.004 | 0.001 | -0.329 | -0.033 | 0.033 | -0.018 | -0.095 | 0.064 | 0.095 |
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.015 | 0.018 | -0.022 | -0.245 | -0.028 | 0.022 | -0.013 | -0.060 | 0.086 | 0.044 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.014 | 0.005 | -0.010 | -0.235 | -0.031 | 0.024 | -0.014 | -0.076 | 0.048 | 0.046 |
| Automatic merits follow-up | `current-us-like` -> `automatic-merits-follow-up` | 0.011 | -0.007 | 0.006 | -0.318 | -0.030 | 0.030 | -0.015 | -0.080 | 0.033 | 0.112 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.011 | 0.004 | -0.003 | -0.229 | -0.022 | 0.020 | -0.015 | -0.072 | 0.052 | 0.077 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | 0.011 | 0.006 | -0.008 | -0.235 | -0.030 | 0.024 | -0.018 | -0.076 | 0.051 | 0.080 |
| Mandatory written emergency reasoning | `current-us-like` -> `mandatory-written-emergency-reasoning` | 0.010 | 0.011 | -0.014 | -0.279 | -0.029 | 0.024 | -0.012 | -0.065 | 0.066 | 0.092 |
| Strong recusal enforcement | `current-us-like` -> `strong-recusal-enforcement` | 0.008 | 0.004 | -0.005 | -0.236 | -0.024 | 0.022 | -0.013 | -0.074 | 0.052 | 0.100 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.003 | 0.002 | -0.014 | -0.002 | 0.014 | -0.000 | 0.006 | -0.001 | 0.004 | -0.000 |
| Jurisdiction-stripping constraints | `term-limited-balanced` -> `jurisdiction-stripping-constraints` | -0.003 | -0.005 | 0.002 | 0.001 | 0.016 | -0.004 | 0.012 | 0.001 | 0.000 | 0.027 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.005 | 0.003 | 0.001 | -0.002 | -0.003 | 0.002 | -0.003 | -0.001 | -0.006 | 0.038 |
| Public-interest litigation filter | `nonpartisan-commission` -> `public-interest-litigation-filter` | -0.006 | -0.003 | 0.009 | 0.004 | 0.013 | -0.006 | 0.009 | 0.004 | 0.006 | 0.040 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.006 | -0.000 | 0.003 | 0.002 | 0.007 | -0.003 | 0.005 | 0.002 | 0.010 | 0.046 |
| Constitutional remand | `nonpartisan-commission` -> `constitutional-remand` | -0.007 | 0.024 | -0.005 | 0.001 | 0.014 | 0.005 | 0.005 | 0.001 | 0.049 | 0.112 |
| Legislative override window | `term-limited-balanced` -> `legislative-override-window` | -0.008 | -0.005 | 0.004 | 0.002 | 0.025 | -0.004 | 0.008 | 0.002 | 0.003 | 0.037 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.008 | -0.008 | 0.006 | 0.002 | 0.025 | -0.006 | 0.018 | 0.002 | -0.001 | 0.035 |
| Randomized merits panels | `term-limited-balanced` -> `randomized-merits-panels` | -0.008 | -0.002 | 0.003 | 0.002 | 0.006 | -0.002 | -0.002 | 0.003 | 0.005 | 0.054 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.010 | 0.009 | -0.001 | -0.001 | 0.017 | -0.001 | 0.005 | -0.001 | 0.019 | 0.090 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.023 | 0.006 | -0.034 | -0.013 | 0.034 | -0.001 | 0.008 | 0.013 | 0.038 | 0.098 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.035 | -0.031 | 0.000 | -0.013 | 0.043 | -0.009 | 0.013 | 0.015 | -0.049 | 0.138 |
