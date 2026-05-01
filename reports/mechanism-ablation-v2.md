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
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.026 | -0.009 | -0.033 | -0.010 | 0.016 | -0.016 | -0.028 | -0.562 | -0.045 | 0.045 | 0.123 | 0.000 |
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.023 | 0.037 | 0.100 | -0.004 | 0.014 | -0.056 | 0.002 | -0.408 | -0.039 | 0.014 | 0.065 | 0.000 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.022 | 0.002 | 0.001 | -0.007 | 0.013 | -0.022 | 0.006 | -0.404 | -0.038 | 0.037 | 0.070 | 0.000 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.016 | 0.001 | -0.003 | -0.007 | 0.013 | -0.021 | -0.032 | -0.403 | -0.038 | 0.037 | 0.099 | 0.000 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | 0.009 | 0.003 | 0.001 | -0.007 | 0.013 | -0.022 | 0.007 | -0.402 | -0.038 | 0.036 | 0.109 | 0.000 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.004 | -0.000 | 0.011 | 0.005 | -0.018 | -0.029 | 0.004 | -0.002 | 0.033 | 0.016 | -0.000 | 0.219 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.010 | 0.010 | 0.024 | 0.005 | 0.001 | -0.010 | 0.008 | 0.002 | -0.002 | -0.006 | 0.047 | 0.000 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.012 | -0.011 | -0.000 | -0.011 | -0.023 | 0.008 | -0.071 | 0.000 | 0.041 | 0.002 | 0.040 | 0.243 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.013 | 0.001 | 0.004 | 0.000 | 0.000 | 0.002 | -0.039 | -0.000 | -0.001 | 0.001 | 0.050 | 0.000 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.036 | 0.015 | 0.033 | -0.001 | 0.013 | -0.008 | 0.018 | -0.002 | 0.032 | 0.024 | 0.121 | 0.209 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.047 | 0.038 | 0.135 | 0.018 | -0.041 | -0.077 | -0.022 | -0.005 | 0.046 | -0.050 | 0.126 | 0.000 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.068 | -0.041 | -0.056 | -0.022 | -0.046 | 0.001 | -0.029 | -0.006 | 0.061 | -0.004 | 0.177 | 0.000 |
