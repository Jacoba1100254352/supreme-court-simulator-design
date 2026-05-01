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
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.016 | 0.019 | 0.055 | -0.008 | 0.008 | -0.022 | 0.000 | -0.304 | -0.022 | 0.006 | 0.055 | 0.000 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.013 | 0.004 | 0.009 | -0.005 | 0.007 | -0.007 | 0.008 | -0.285 | -0.021 | 0.018 | 0.059 | 0.000 |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.012 | 0.017 | 0.037 | 0.003 | 0.010 | -0.013 | -0.029 | -0.391 | -0.030 | 0.014 | 0.113 | 0.000 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.006 | 0.008 | 0.019 | -0.002 | 0.008 | -0.009 | -0.024 | -0.281 | -0.022 | 0.016 | 0.089 | 0.000 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | 0.000 | 0.005 | 0.012 | -0.004 | 0.007 | -0.006 | 0.009 | -0.285 | -0.021 | 0.019 | 0.099 | 0.000 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.002 | -0.000 | 0.007 | 0.004 | -0.011 | -0.016 | 0.002 | -0.002 | 0.019 | 0.009 | 0.000 | 0.145 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.011 | 0.003 | 0.007 | 0.002 | 0.000 | -0.004 | 0.010 | 0.002 | -0.001 | -0.002 | 0.046 | 0.000 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.011 | -0.005 | 0.004 | -0.005 | -0.014 | 0.003 | -0.066 | -0.000 | 0.024 | 0.002 | 0.040 | 0.158 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.013 | -0.002 | -0.004 | -0.001 | -0.000 | 0.003 | -0.042 | 0.002 | 0.000 | 0.001 | 0.051 | 0.000 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.027 | 0.015 | 0.031 | 0.004 | 0.010 | -0.009 | 0.013 | -0.002 | 0.017 | 0.013 | 0.097 | 0.128 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.042 | 0.010 | 0.062 | 0.002 | -0.034 | -0.039 | -0.022 | -0.020 | 0.041 | -0.028 | 0.121 | 0.000 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.061 | -0.034 | -0.045 | -0.020 | -0.038 | 0.002 | -0.026 | -0.019 | 0.050 | -0.001 | 0.171 | 0.000 |
