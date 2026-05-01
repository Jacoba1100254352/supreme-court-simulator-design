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
| Invalidation threshold | `current-us-like` -> `supermajority-review` | 0.011 | 0.010 | 0.036 | -0.008 | 0.001 | -0.008 | 0.003 | -0.212 | -0.003 | -0.003 | 0.047 | 0.000 |
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.009 | 0.004 | 0.014 | -0.001 | 0.000 | 0.001 | 0.002 | -0.197 | -0.001 | 0.004 | 0.052 | 0.000 |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.002 | 0.017 | 0.042 | 0.007 | 0.001 | -0.009 | -0.020 | -0.270 | -0.003 | -0.004 | 0.106 | 0.000 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | 0.000 | 0.006 | 0.017 | 0.000 | 0.001 | -0.003 | -0.017 | -0.195 | -0.001 | 0.002 | 0.082 | 0.000 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.001 | 0.005 | 0.012 | 0.005 | -0.003 | -0.008 | 0.001 | 0.001 | 0.005 | 0.000 | 0.001 | 0.056 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | -0.005 | 0.006 | 0.017 | -0.000 | 0.000 | -0.001 | 0.002 | -0.195 | -0.001 | 0.003 | 0.092 | 0.000 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.009 | 0.002 | 0.006 | 0.001 | 0.000 | -0.002 | 0.011 | 0.000 | -0.000 | -0.002 | 0.043 | 0.000 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.010 | -0.005 | -0.008 | -0.001 | -0.005 | 0.001 | -0.045 | 0.000 | 0.007 | 0.003 | 0.040 | 0.063 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.014 | 0.002 | 0.004 | 0.001 | 0.000 | -0.001 | -0.025 | -0.000 | -0.000 | -0.000 | 0.050 | 0.000 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.017 | 0.011 | 0.020 | 0.005 | 0.007 | -0.006 | 0.012 | -0.000 | 0.004 | 0.006 | 0.072 | 0.049 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.041 | -0.009 | 0.015 | -0.010 | -0.031 | -0.014 | -0.019 | -0.016 | 0.038 | -0.011 | 0.118 | 0.000 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.056 | -0.022 | -0.018 | -0.017 | -0.031 | 0.001 | -0.020 | -0.019 | 0.039 | -0.000 | 0.166 | 0.000 |
