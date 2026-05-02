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
| Term regularization | `current-us-like` -> `term-limited-balanced` | 0.003 | 0.003 | 0.011 | -0.004 | 0.003 | -0.006 | 0.001 | -0.183 | -0.012 | 0.015 | 0.042 | 0.000 |
| Emergency restraint | `current-us-like` -> `emergency-restraint-court` | 0.001 | 0.007 | 0.023 | -0.003 | 0.004 | -0.004 | -0.014 | -0.258 | -0.014 | 0.020 | 0.083 | 0.000 |
| Appointment screening | `current-us-like` -> `nonpartisan-commission` | -0.002 | 0.006 | 0.020 | -0.003 | 0.001 | -0.006 | -0.012 | -0.181 | -0.008 | 0.017 | 0.067 | 0.000 |
| Recusal and emergency process | `current-us-like` -> `recusal-and-emergency-reform` | -0.002 | 0.006 | 0.015 | -0.002 | 0.005 | -0.008 | 0.004 | -0.186 | -0.014 | 0.013 | 0.069 | 0.000 |
| Accountability election | `nonpartisan-commission` -> `accountability-retention-court` | -0.003 | 0.002 | 0.007 | 0.004 | -0.005 | -0.010 | -0.001 | -0.001 | 0.009 | 0.004 | -0.000 | 0.076 |
| Invalidation threshold | `current-us-like` -> `supermajority-review` | -0.003 | 0.013 | 0.044 | -0.005 | 0.002 | -0.016 | 0.003 | -0.192 | -0.009 | 0.009 | 0.040 | 0.000 |
| Court expansion | `term-limited-balanced` -> `expanded-court-fifteen` | -0.006 | 0.002 | 0.006 | 0.001 | -0.000 | -0.001 | -0.021 | -0.000 | -0.000 | -0.000 | 0.037 | 0.000 |
| Panel routing | `term-limited-balanced` -> `panel-en-banc` | -0.007 | 0.002 | 0.010 | 0.001 | -0.003 | 0.001 | 0.012 | 0.001 | 0.005 | 0.004 | 0.042 | 0.000 |
| Legislative override | `term-limited-balanced` -> `legislative-override` | -0.008 | -0.003 | 0.005 | -0.003 | -0.010 | 0.004 | -0.035 | 0.003 | 0.019 | 0.005 | 0.033 | 0.081 |
| Constitutional council | `nonpartisan-commission` -> `constitutional-council` | -0.014 | 0.007 | 0.012 | 0.001 | 0.008 | -0.003 | 0.008 | -0.001 | 0.011 | 0.012 | 0.074 | 0.069 |
| Dual-court filter | `nonpartisan-commission` -> `dual-supreme-courts` | -0.033 | -0.027 | -0.038 | -0.016 | -0.027 | 0.003 | -0.017 | -0.006 | 0.037 | 0.001 | 0.125 | 0.000 |
| Cross-checking court | `nonpartisan-commission` -> `cross-checking-courts` | -0.035 | -0.001 | 0.021 | -0.000 | -0.025 | -0.024 | -0.015 | -0.006 | 0.031 | -0.018 | 0.088 | 0.000 |
