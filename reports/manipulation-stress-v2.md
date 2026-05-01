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

- Highest directional score: No emergency relief without merits review at 0.679.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.716.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.019.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.064.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `reversalRate`, `constitutionalConflict`, and `administrativeCost` are usually better.
- Invalidation, emergency, replacement, recusal, concurrence, dissent, panel, en banc, council, cross-check, and override rates are diagnostic.

## Scenario Averages Across Cases

| Scenario | Directional | Stability/rights | Legitimacy/control | Legal stability | Precedent | Statutory | Compliance | Rights protection | Partisan align. | Shadow abuse | Legitimacy | Reversal | Conflict | Responsiveness | Strategic | Evasion | Exec flood | Admin cost | Merits accel. | Replacement | Override att. | Override |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.679 | 0.595 | 0.831 | 0.521 | 0.642 | 0.549 | 0.373 | 0.701 | 0.102 | 0.019 | 0.902 | 0.210 | 0.633 | 0.756 | 0.385 | 0.256 | 0.580 | 0.388 | 0.881 | 0.145 | 0.000 | 0.000 |
| 60 percent invalidation threshold | 0.676 | 0.613 | 0.744 | 0.586 | 0.825 | 0.560 | 0.372 | 0.652 | 0.140 | 0.182 | 0.725 | 0.149 | 0.636 | 0.719 | 0.419 | 0.247 | 0.622 | 0.330 | 0.280 | 0.068 | 0.000 | 0.000 |
| 18-year staggered terms + regular appointments | 0.674 | 0.600 | 0.756 | 0.546 | 0.713 | 0.554 | 0.370 | 0.691 | 0.146 | 0.190 | 0.770 | 0.196 | 0.640 | 0.744 | 0.419 | 0.263 | 0.599 | 0.335 | 0.558 | 0.148 | 0.000 | 0.000 |
| Nonpartisan commission appointments | 0.669 | 0.601 | 0.771 | 0.547 | 0.716 | 0.555 | 0.370 | 0.689 | 0.097 | 0.190 | 0.781 | 0.194 | 0.639 | 0.743 | 0.397 | 0.263 | 0.602 | 0.364 | 0.551 | 0.149 | 0.000 | 0.000 |
| Retention-election accountability court | 0.665 | 0.586 | 0.772 | 0.549 | 0.736 | 0.560 | 0.351 | 0.657 | 0.103 | 0.189 | 0.783 | 0.185 | 0.675 | 0.762 | 0.403 | 0.263 | 0.602 | 0.364 | 0.559 | 0.266 | 0.237 | 0.126 |
| Three-judge panels with en banc correction | 0.664 | 0.604 | 0.769 | 0.558 | 0.743 | 0.559 | 0.371 | 0.682 | 0.153 | 0.194 | 0.844 | 0.185 | 0.637 | 0.739 | 0.392 | 0.250 | 0.601 | 0.382 | 0.535 | 0.542 | 0.000 | 0.000 |
| Judicial review with legislative supermajority override | 0.663 | 0.589 | 0.773 | 0.534 | 0.715 | 0.543 | 0.345 | 0.698 | 0.065 | 0.190 | 0.786 | 0.191 | 0.684 | 0.746 | 0.436 | 0.301 | 0.603 | 0.374 | 0.554 | 0.151 | 0.258 | 0.034 |
| Expanded 15-seat court | 0.662 | 0.600 | 0.770 | 0.545 | 0.710 | 0.554 | 0.370 | 0.693 | 0.095 | 0.189 | 0.792 | 0.197 | 0.640 | 0.744 | 0.418 | 0.257 | 0.602 | 0.384 | 0.552 | 0.153 | 0.000 | 0.000 |
| Peer recusal + reasoned emergency docket | 0.661 | 0.602 | 0.755 | 0.549 | 0.720 | 0.556 | 0.371 | 0.689 | 0.152 | 0.191 | 0.776 | 0.192 | 0.639 | 0.743 | 0.417 | 0.253 | 0.603 | 0.374 | 0.551 | 0.153 | 0.000 | 0.000 |
| Stylized current U.S.-like supreme court | 0.652 | 0.616 | 0.602 | 0.552 | 0.738 | 0.563 | 0.356 | 0.716 | 0.144 | 0.612 | 0.460 | 0.124 | 0.680 | 0.704 | 0.460 | 0.250 | 0.686 | 0.262 | 0.000 | 0.073 | 0.000 | 0.000 |
| Pre-enactment constitutional council | 0.633 | 0.602 | 0.786 | 0.570 | 0.770 | 0.555 | 0.384 | 0.679 | 0.111 | 0.188 | 0.889 | 0.169 | 0.674 | 0.768 | 0.427 | 0.288 | 0.602 | 0.490 | 0.568 | 0.212 | 0.223 | 0.029 |
| Supreme court with cross-checking constitutional court | 0.623 | 0.603 | 0.761 | 0.591 | 0.869 | 0.576 | 0.328 | 0.606 | 0.067 | 0.183 | 0.758 | 0.099 | 0.687 | 0.691 | 0.398 | 0.243 | 0.627 | 0.493 | 0.280 | 0.185 | 0.000 | 0.000 |
| Dual supreme courts with disagreement filter | 0.601 | 0.574 | 0.772 | 0.503 | 0.654 | 0.535 | 0.322 | 0.688 | 0.064 | 0.185 | 0.764 | 0.193 | 0.704 | 0.739 | 0.415 | 0.263 | 0.619 | 0.543 | 0.263 | 0.190 | 0.000 | 0.000 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Appointment Timing Manipulation | 18-year staggered terms + regular appointments (0.724) | Dual supreme courts with disagreement filter (0.677) | No emergency relief without merits review (0.005) | Dual supreme courts with disagreement filter (0.049) |
| Emergency Application Flood | No emergency relief without merits review (0.676) | Stylized current U.S.-like supreme court (0.710) | No emergency relief without merits review (0.028) | Dual supreme courts with disagreement filter (0.052) |
| Override Evasion Loop | 60 percent invalidation threshold (0.663) | Stylized current U.S.-like supreme court (0.731) | No emergency relief without merits review (0.016) | Dual supreme courts with disagreement filter (0.059) |
| Recusal Pressure Campaign | No emergency relief without merits review (0.674) | Stylized current U.S.-like supreme court (0.734) | No emergency relief without merits review (0.022) | Dual supreme courts with disagreement filter (0.067) |
| Court Expansion Retaliation | 60 percent invalidation threshold (0.658) | Stylized current U.S.-like supreme court (0.752) | No emergency relief without merits review (0.025) | Judicial review with legislative supermajority override (0.094) |
