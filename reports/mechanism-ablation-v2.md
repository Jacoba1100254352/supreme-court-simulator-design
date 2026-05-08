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
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.015 | 0.023 | -0.025 | -0.225 | -0.034 | 0.017 | -0.007 | 0.007 | -0.012 | -0.171 | -0.061 | 0.089 | 0.039 |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.011 | -0.020 | -0.001 | -0.305 | -0.029 | 0.025 | -0.013 | 0.017 | -0.007 | -0.224 | -0.109 | 0.005 | 0.084 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.010 | 0.003 | -0.018 | -0.216 | -0.033 | 0.018 | -0.008 | 0.010 | -0.006 | -0.156 | -0.082 | 0.039 | 0.043 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.006 | 0.002 | -0.015 | -0.211 | -0.028 | 0.016 | -0.008 | 0.010 | -0.009 | -0.155 | -0.078 | 0.039 | 0.067 |
| Mandatory written emergency reasoning | `current-us-like` -> `mandatory-written-emergency-reasoning` | 0.006 | 0.012 | -0.026 | -0.248 | -0.031 | 0.018 | -0.008 | 0.009 | -0.014 | -0.183 | -0.063 | 0.062 | 0.082 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | 0.006 | 0.004 | -0.017 | -0.214 | -0.030 | 0.017 | -0.008 | 0.010 | -0.008 | -0.156 | -0.079 | 0.043 | 0.074 |
| Automatic merits follow-up | `current-us-like` -> `automatic-merits-follow-up` | 0.005 | -0.026 | -0.004 | -0.303 | -0.031 | 0.025 | -0.013 | 0.017 | -0.006 | -0.206 | -0.112 | -0.010 | 0.100 |
| Emergency integrity bundle | `current-us-like` -> `emergency-integrity-package` | 0.005 | -0.020 | -0.002 | -0.303 | -0.031 | 0.026 | -0.014 | 0.017 | -0.016 | -0.206 | -0.112 | 0.004 | 0.123 |
| Constitutional remand | `nonpartisan-commission` -> `constitutional-remand` | 0.003 | 0.036 | -0.002 | -0.001 | -0.001 | 0.020 | -0.036 | 0.020 | 0.000 | -0.001 | -0.001 | 0.065 | 0.094 |
| Strong recusal enforcement | `current-us-like` -> `strong-recusal-enforcement` | 0.003 | 0.002 | -0.016 | -0.208 | -0.026 | 0.016 | -0.008 | 0.010 | -0.011 | -0.155 | -0.076 | 0.039 | 0.089 |
| Public-interest litigation filter | `nonpartisan-commission` -> `public-interest-litigation-filter` | 0.001 | 0.006 | 0.005 | -0.003 | -0.002 | 0.002 | -0.001 | 0.001 | -0.001 | -0.000 | -0.002 | 0.015 | 0.025 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.002 | 0.003 | -0.013 | -0.002 | 0.017 | -0.001 | 0.001 | 0.000 | 0.006 | 0.000 | -0.003 | 0.006 | -0.001 |
| Remand and override-window bundle | `term-limited-balanced` -> `remand-override-window-package` | -0.002 | 0.043 | -0.006 | -0.032 | 0.003 | 0.017 | -0.035 | 0.021 | 0.001 | -0.026 | 0.018 | 0.083 | 0.152 |
| Jurisdiction-stripping constraints | `term-limited-balanced` -> `jurisdiction-stripping-constraints` | -0.004 | -0.006 | 0.001 | 0.002 | 0.018 | -0.002 | 0.001 | 0.030 | 0.017 | 0.000 | 0.002 | -0.001 | 0.023 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.006 | -0.002 | 0.001 | 0.001 | 0.000 | -0.000 | 0.000 | 0.000 | 0.002 | 0.001 | 0.002 | -0.001 | 0.039 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.006 | -0.001 | 0.002 | -0.000 | 0.001 | -0.000 | -0.000 | 0.000 | 0.001 | -0.000 | -0.001 | -0.009 | 0.036 |
| Randomized merits panels | `term-limited-balanced` -> `randomized-merits-panels` | -0.006 | 0.002 | 0.001 | 0.002 | 0.001 | -0.001 | 0.000 | 0.000 | 0.005 | 0.000 | 0.003 | 0.009 | 0.047 |
| Council with concrete-review backstop | `nonpartisan-commission` -> `council-concrete-hybrid` | -0.007 | 0.017 | 0.002 | -0.002 | 0.013 | 0.007 | -0.001 | 0.045 | 0.007 | -0.001 | -0.004 | 0.029 | 0.097 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.007 | 0.009 | 0.001 | -0.002 | 0.019 | 0.005 | -0.002 | 0.046 | 0.009 | -0.000 | -0.002 | 0.015 | 0.086 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.007 | -0.008 | 0.003 | -0.001 | 0.025 | -0.003 | 0.001 | 0.001 | 0.011 | -0.000 | -0.001 | -0.004 | 0.030 |
| Legislative override window | `term-limited-balanced` -> `legislative-override-window` | -0.008 | -0.005 | -0.001 | -0.001 | 0.025 | -0.004 | 0.001 | 0.002 | 0.014 | 0.000 | 0.000 | -0.000 | 0.030 |
| Panel and jurisdiction safeguards | `term-limited-balanced` -> `panel-jurisdiction-safeguards` | -0.009 | 0.009 | -0.008 | -0.006 | 0.016 | -0.003 | 0.002 | 0.028 | 0.014 | -0.014 | 0.023 | 0.037 | 0.073 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.013 | 0.025 | -0.030 | -0.007 | 0.020 | 0.008 | -0.020 | 0.017 | -0.008 | -0.015 | 0.020 | 0.066 | 0.085 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.032 | -0.029 | -0.002 | -0.008 | 0.033 | -0.010 | 0.003 | -0.003 | 0.007 | -0.014 | 0.021 | -0.051 | 0.123 |
