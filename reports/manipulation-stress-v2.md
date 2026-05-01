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

- Highest directional score: 60 percent invalidation threshold at 0.726.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.708.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.015.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.060.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `reversalRate`, `constitutionalConflict`, and `administrativeCost` are usually better.
- Invalidation, emergency, replacement, recusal, concurrence, dissent, panel, en banc, council, cross-check, and override rates are diagnostic.

## Scenario Averages Across Cases

| Scenario | Directional | Stability/rights | Legitimacy/control | Legal stability | Precedent | Statutory | Compliance | Rights protection | Partisan align. | Shadow abuse | Legitimacy | Reversal | Conflict | Responsiveness | Strategic | Admin cost | Merits accel. | Replacement | Override att. | Override |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.726 | 0.681 | 0.805 | 0.647 | 0.879 | 0.599 | 0.463 | 0.680 | 0.129 | 0.111 | 0.786 | 0.099 | 0.506 | 0.726 | 0.233 | 0.309 | 0.256 | 0.055 | 0.000 | 0.000 |
| No emergency relief without merits review | 0.723 | 0.682 | 0.854 | 0.645 | 0.860 | 0.609 | 0.466 | 0.692 | 0.094 | 0.015 | 0.877 | 0.112 | 0.497 | 0.735 | 0.207 | 0.367 | 0.687 | 0.132 | 0.000 | 0.000 |
| 18-year staggered terms + regular appointments | 0.722 | 0.673 | 0.806 | 0.624 | 0.810 | 0.600 | 0.463 | 0.699 | 0.135 | 0.131 | 0.799 | 0.124 | 0.507 | 0.740 | 0.230 | 0.313 | 0.446 | 0.134 | 0.000 | 0.000 |
| Nonpartisan commission appointments | 0.717 | 0.675 | 0.817 | 0.630 | 0.824 | 0.602 | 0.463 | 0.699 | 0.089 | 0.131 | 0.809 | 0.121 | 0.506 | 0.739 | 0.229 | 0.343 | 0.444 | 0.131 | 0.000 | 0.000 |
| Retention-election accountability court | 0.713 | 0.668 | 0.815 | 0.632 | 0.839 | 0.606 | 0.452 | 0.681 | 0.096 | 0.132 | 0.809 | 0.116 | 0.527 | 0.748 | 0.237 | 0.343 | 0.451 | 0.217 | 0.146 | 0.066 |
| Judicial review with legislative supermajority override | 0.711 | 0.667 | 0.819 | 0.619 | 0.814 | 0.594 | 0.448 | 0.704 | 0.061 | 0.132 | 0.812 | 0.122 | 0.533 | 0.742 | 0.261 | 0.353 | 0.444 | 0.132 | 0.161 | 0.020 |
| Three-judge panels with en banc correction | 0.711 | 0.675 | 0.816 | 0.631 | 0.826 | 0.603 | 0.463 | 0.695 | 0.149 | 0.133 | 0.883 | 0.119 | 0.506 | 0.737 | 0.228 | 0.359 | 0.441 | 0.500 | 0.000 | 0.000 |
| Expanded 15-seat court | 0.710 | 0.674 | 0.819 | 0.626 | 0.814 | 0.601 | 0.463 | 0.701 | 0.089 | 0.133 | 0.818 | 0.124 | 0.507 | 0.740 | 0.230 | 0.364 | 0.450 | 0.130 | 0.000 | 0.000 |
| Peer recusal + reasoned emergency docket | 0.709 | 0.674 | 0.807 | 0.628 | 0.819 | 0.602 | 0.463 | 0.697 | 0.138 | 0.132 | 0.807 | 0.123 | 0.506 | 0.739 | 0.229 | 0.353 | 0.450 | 0.137 | 0.000 | 0.000 |
| Stylized current U.S.-like supreme court | 0.708 | 0.677 | 0.698 | 0.624 | 0.812 | 0.605 | 0.455 | 0.708 | 0.134 | 0.431 | 0.590 | 0.092 | 0.531 | 0.720 | 0.275 | 0.252 | 0.000 | 0.055 | 0.000 | 0.000 |
| Pre-enactment constitutional council | 0.688 | 0.676 | 0.832 | 0.645 | 0.856 | 0.604 | 0.475 | 0.690 | 0.104 | 0.129 | 0.915 | 0.105 | 0.526 | 0.756 | 0.250 | 0.445 | 0.456 | 0.205 | 0.137 | 0.020 |
| Supreme court with cross-checking constitutional court | 0.674 | 0.668 | 0.820 | 0.640 | 0.888 | 0.605 | 0.427 | 0.656 | 0.063 | 0.111 | 0.818 | 0.073 | 0.550 | 0.710 | 0.233 | 0.465 | 0.255 | 0.175 | 0.000 | 0.000 |
| Dual supreme courts with disagreement filter | 0.654 | 0.651 | 0.826 | 0.585 | 0.750 | 0.582 | 0.424 | 0.699 | 0.060 | 0.112 | 0.825 | 0.122 | 0.559 | 0.737 | 0.250 | 0.515 | 0.246 | 0.173 | 0.000 | 0.000 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | 18-year staggered terms + regular appointments (0.771) | Dual supreme courts with disagreement filter (0.699) | No emergency relief without merits review (0.003) | Judicial review with legislative supermajority override (0.043) |
| Emergency Application Flood | No emergency relief without merits review (0.707) | Stylized current U.S.-like supreme court (0.701) | No emergency relief without merits review (0.027) | Dual supreme courts with disagreement filter (0.051) |
| Override Evasion Loop | 60 percent invalidation threshold (0.721) | Judicial review with legislative supermajority override (0.709) | No emergency relief without merits review (0.011) | Dual supreme courts with disagreement filter (0.055) |
| Recusal Pressure Campaign | No emergency relief without merits review (0.721) | Stylized current U.S.-like supreme court (0.718) | No emergency relief without merits review (0.015) | Dual supreme courts with disagreement filter (0.062) |
| Court Expansion Retaliation | 60 percent invalidation threshold (0.713) | Stylized current U.S.-like supreme court (0.721) | No emergency relief without merits review (0.017) | Judicial review with legislative supermajority override (0.088) |
