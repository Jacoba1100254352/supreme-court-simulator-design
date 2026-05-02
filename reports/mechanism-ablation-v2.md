# Mechanism Ablation v2

Pairwise comparisons that change one institutional mechanism at a time where the catalog permits a close proxy.

## Run Configuration

- runs per pair/case: 60
- cases per run: 48
- base seed: 20260501
- mechanisms: 12
- stress cases: 8
- legislative input: simulation-campaign-v21-paper.csv

Positive deltas improve higher-better metrics. Negative deltas improve lower-better diagnostics such as partisan alignment, shadow abuse, conflict, and administrative cost.

## Weighted Mechanism Summary

| Mechanism | Base -> Variant | Directional | Legal | Precedent | Statutory | Compliance | Rights | Partisan | Shadow | Conflict | Responsiveness | Admin cost | Override att. |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.007 | -0.010 | -0.023 | -0.012 | 0.008 | -0.008 | -0.024 | -0.449 | -0.030 | 0.048 | 0.108 | 0.000 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.002 | 0.008 | 0.017 | -0.003 | 0.011 | -0.027 | 0.001 | -0.322 | -0.032 | 0.029 | 0.057 | 0.000 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | -0.004 | 0.010 | 0.027 | -0.004 | 0.008 | -0.023 | -0.024 | -0.320 | -0.027 | 0.033 | 0.087 | 0.000 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | -0.005 | 0.008 | 0.015 | -0.003 | 0.011 | -0.026 | 0.004 | -0.321 | -0.031 | 0.029 | 0.090 | 0.000 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.006 | 0.002 | 0.012 | 0.004 | -0.011 | -0.018 | 0.002 | -0.000 | 0.020 | 0.009 | 0.001 | 0.129 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.007 | 0.001 | 0.004 | 0.000 | 0.000 | -0.001 | -0.036 | 0.000 | -0.001 | -0.001 | 0.042 | 0.000 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.011 | 0.004 | 0.016 | 0.001 | -0.004 | 0.001 | 0.009 | 0.004 | 0.006 | 0.003 | 0.047 | 0.000 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.012 | -0.008 | 0.005 | -0.008 | -0.018 | 0.008 | -0.054 | 0.003 | 0.032 | 0.008 | 0.040 | 0.142 |
| Invalidation threshold | `current-us-like` -> `supermajority-review` | -0.013 | 0.033 | 0.090 | 0.000 | 0.010 | -0.055 | 0.002 | -0.320 | -0.031 | 0.010 | 0.055 | 0.000 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.020 | 0.016 | 0.031 | 0.004 | 0.014 | -0.009 | 0.012 | -0.001 | 0.017 | 0.016 | 0.099 | 0.118 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.041 | -0.040 | -0.063 | -0.021 | -0.036 | 0.002 | -0.024 | 0.001 | 0.049 | 0.000 | 0.147 | 0.000 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.051 | 0.012 | 0.061 | 0.007 | -0.032 | -0.049 | -0.022 | -0.000 | 0.039 | -0.034 | 0.104 | 0.000 |
