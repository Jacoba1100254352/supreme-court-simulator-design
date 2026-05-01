# Adversarial Manipulation Stress Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 13
- experiment cases: 5

- legislative input: simulation-campaign-v21-paper.csv: volume=0.324 quality=0.617 weakMandate=0.174 rightsRisk=0.106 partisanSkew=0.233 volatility=0.121 legitimacy=0.550

## Case Weights

| Case | Weight | Legislative source | Description |
| --- | ---: | --- | --- |
| Appointment Timing Manipulation | 1.000 | adversarial/imported blend | Political actors time vacancies under high capture and public pressure. |
| Emergency Application Flood | 1.000 | emergency-flood synthetic legislature | Executives and litigants route controversial policies through urgent stay requests. |
| Override Evasion Loop | 1.000 | override-evasion synthetic legislature | Legislatures repeatedly revise invalidated laws to test rights carveouts and override thresholds. |
| Recusal Pressure Campaign | 0.850 | recusal-pressure synthetic legislature | High-salience litigants try to force or avoid recusals around ideologically charged cases. |
| Court Expansion Retaliation | 0.850 | expansion-retaliation synthetic legislature | A polarized political system reacts to judicial conflict with expansion threats and capture pressure. |

## Headline Findings

- Highest directional score: 60 percent invalidation threshold at 0.769.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.684.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.004.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.045.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `reversalRate`, `constitutionalConflict`, and `administrativeCost` are usually better.
- Invalidation, emergency, replacement, recusal, concurrence, dissent, panel, en banc, council, cross-check, and override rates are diagnostic.

## Scenario Averages Across Cases

| Scenario | Directional | Stability/rights | Legitimacy/control | Legal stability | Precedent | Statutory | Compliance | Rights protection | Partisan align. | Shadow abuse | Legitimacy | Reversal | Conflict | Responsiveness | Admin cost | Merits accel. | Replacement | Override att. | Override |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.769 | 0.761 | 0.826 | 0.732 | 0.966 | 0.668 | 0.561 | 0.675 | 0.098 | 0.067 | 0.785 | 0.024 | 0.339 | 0.706 | 0.280 | 0.232 | 0.026 | 0.000 | 0.000 |
| 18-year staggered terms + regular appointments | 0.767 | 0.760 | 0.825 | 0.731 | 0.958 | 0.675 | 0.560 | 0.683 | 0.098 | 0.086 | 0.792 | 0.032 | 0.341 | 0.713 | 0.285 | 0.355 | 0.106 | 0.000 | 0.000 |
| No emergency relief without merits review | 0.761 | 0.763 | 0.861 | 0.739 | 0.972 | 0.684 | 0.561 | 0.672 | 0.070 | 0.004 | 0.849 | 0.022 | 0.338 | 0.704 | 0.340 | 0.532 | 0.103 | 0.000 | 0.000 |
| Nonpartisan commission appointments | 0.759 | 0.760 | 0.833 | 0.732 | 0.959 | 0.676 | 0.560 | 0.681 | 0.069 | 0.086 | 0.799 | 0.031 | 0.340 | 0.712 | 0.315 | 0.357 | 0.103 | 0.000 | 0.000 |
| Retention-election accountability court | 0.758 | 0.759 | 0.832 | 0.733 | 0.962 | 0.680 | 0.558 | 0.675 | 0.072 | 0.088 | 0.799 | 0.027 | 0.344 | 0.713 | 0.315 | 0.360 | 0.114 | 0.046 | 0.016 |
| Judicial review with legislative supermajority override | 0.758 | 0.758 | 0.840 | 0.729 | 0.956 | 0.675 | 0.556 | 0.681 | 0.045 | 0.086 | 0.802 | 0.032 | 0.346 | 0.714 | 0.325 | 0.358 | 0.104 | 0.055 | 0.008 |
| Three-judge panels with en banc correction | 0.756 | 0.760 | 0.839 | 0.732 | 0.959 | 0.676 | 0.560 | 0.680 | 0.114 | 0.087 | 0.888 | 0.032 | 0.340 | 0.711 | 0.330 | 0.363 | 0.445 | 0.000 | 0.000 |
| Stylized current U.S.-like supreme court | 0.756 | 0.758 | 0.741 | 0.723 | 0.933 | 0.675 | 0.560 | 0.684 | 0.097 | 0.297 | 0.639 | 0.031 | 0.342 | 0.711 | 0.232 | 0.000 | 0.026 | 0.000 | 0.000 |
| Peer recusal + reasoned emergency docket | 0.754 | 0.760 | 0.826 | 0.732 | 0.959 | 0.676 | 0.560 | 0.681 | 0.100 | 0.086 | 0.800 | 0.032 | 0.340 | 0.713 | 0.325 | 0.360 | 0.101 | 0.000 | 0.000 |
| Expanded 15-seat court | 0.753 | 0.761 | 0.835 | 0.732 | 0.959 | 0.676 | 0.560 | 0.683 | 0.066 | 0.087 | 0.808 | 0.032 | 0.340 | 0.712 | 0.335 | 0.362 | 0.101 | 0.000 | 0.000 |
| Pre-enactment constitutional council | 0.740 | 0.761 | 0.852 | 0.738 | 0.965 | 0.681 | 0.569 | 0.675 | 0.084 | 0.086 | 0.903 | 0.025 | 0.344 | 0.719 | 0.392 | 0.362 | 0.165 | 0.042 | 0.010 |
| Supreme court with cross-checking constitutional court | 0.719 | 0.747 | 0.843 | 0.717 | 0.959 | 0.665 | 0.528 | 0.671 | 0.047 | 0.068 | 0.810 | 0.020 | 0.380 | 0.703 | 0.433 | 0.234 | 0.143 | 0.000 | 0.000 |
| Dual supreme courts with disagreement filter | 0.703 | 0.745 | 0.847 | 0.709 | 0.943 | 0.657 | 0.527 | 0.683 | 0.045 | 0.068 | 0.817 | 0.031 | 0.382 | 0.711 | 0.484 | 0.237 | 0.143 | 0.000 | 0.000 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | 60 percent invalidation threshold (0.809) | Dual supreme courts with disagreement filter (0.723) | No emergency relief without merits review (0.000) | Judicial review with legislative supermajority override (0.027) |
| Emergency Application Flood | No emergency relief without merits review (0.742) | Stylized current U.S.-like supreme court (0.678) | No emergency relief without merits review (0.010) | Dual supreme courts with disagreement filter (0.039) |
| Override Evasion Loop | 60 percent invalidation threshold (0.767) | Stylized current U.S.-like supreme court (0.655) | No emergency relief without merits review (0.001) | Dual supreme courts with disagreement filter (0.040) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.765) | Dual supreme courts with disagreement filter (0.680) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.048) |
| Court Expansion Retaliation | 60 percent invalidation threshold (0.760) | Stylized current U.S.-like supreme court (0.687) | No emergency relief without merits review (0.004) | Judicial review with legislative supermajority override (0.069) |
