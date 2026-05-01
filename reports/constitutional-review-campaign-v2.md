# Constitutional Review Campaign v2

Deterministic batch campaign for comparing supreme-court and constitutional-review designs.

## Run Configuration

- runs per case: 80
- cases per run: 64
- base seed: 20260501
- scenarios per case: 13
- experiment cases: 20

- legislative input: simulation-campaign-v21-paper.csv: volume=0.324 quality=0.617 weakMandate=0.174 rightsRisk=0.106 partisanSkew=0.233 volatility=0.121 legitimacy=0.550

## Case Weights

| Case | Weight | Legislative source | Description |
| --- | ---: | --- | --- |
| Baseline | 1.000 | neutral synthetic legislature | Moderate polarization, ordinary emergency pressure, and neutral legislative output. |
| Partisan Appointment Pressure | 1.000 | neutral synthetic legislature | High appointment capture and polarized justice pool. |
| Rights-Risk Legislation | 1.000 | rights-risk synthetic legislature | Legislative output creates concentrated rights burdens and weak mandates. |
| Shadow-Docket Stress | 1.000 | emergency-pressure synthetic legislature | High emergency pressure and executive-defiance disputes. |
| High Democratic Mandate | 1.000 | high-mandate synthetic legislature | Popular, high-mandate laws create accountability pressure against invalidation. |
| Constitutional Conflict | 1.000 | conflict synthetic legislature | Polarized laws, executive defiance, and public attention raise court-legislature conflict. |
| Imported Legislative Output | 1.000 | neutral/imported blend | Docket assumptions derived from a legislative simulator campaign CSV. |
| Low Appointment Capture | 0.750 | neutral synthetic legislature | Appointment incentives are less partisan and the justice pool is less polarized. |
| Extreme Appointment Capture | 1.000 | neutral synthetic legislature | Appointment incentives are highly partisan and vacancies become ideological leverage points. |
| Low Emergency Pressure | 0.750 | neutral synthetic legislature | Few cases arrive through urgent stay requests or executive emergency disputes. |
| Extreme Emergency Pressure | 1.000 | extreme-emergency synthetic legislature | Emergency applications, executive-power disputes, and time-sensitive election conflicts are common. |
| Low Rights Risk | 0.750 | low-rights-risk synthetic legislature | Legislative output is legally careful, low-volatility, and rarely burdens protected interests. |
| Extreme Rights Risk | 1.000 | extreme-rights-risk synthetic legislature | Legislative output often creates concentrated rights burdens under contested public mandates. |
| Weak-Mandate Legislation | 1.000 | weak-mandate synthetic legislature | Many reviewed laws have low public legitimacy and high override pressure after invalidation. |
| Strong-Mandate Legislation | 0.750 | strong-mandate synthetic legislature | Popular legislation creates the hardest democratic-responsiveness pressure for review. |
| Appointment Timing Manipulation | 1.000 | adversarial/imported blend | Political actors time vacancies under high capture and public pressure. |
| Emergency Application Flood | 1.000 | emergency-flood synthetic legislature | Executives and litigants route controversial policies through urgent stay requests. |
| Override Evasion Loop | 1.000 | override-evasion synthetic legislature | Legislatures repeatedly revise invalidated laws to test rights carveouts and override thresholds. |
| Recusal Pressure Campaign | 0.850 | recusal-pressure synthetic legislature | High-salience litigants try to force or avoid recusals around ideologically charged cases. |
| Court Expansion Retaliation | 0.850 | expansion-retaliation synthetic legislature | A polarized political system reacts to judicial conflict with expansion threats and capture pressure. |

## Headline Findings

- Highest directional score: 60 percent invalidation threshold at 0.745.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.703.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.008.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.042.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `reversalRate`, `constitutionalConflict`, and `administrativeCost` are usually better.
- Invalidation, emergency, replacement, recusal, concurrence, dissent, panel, en banc, council, cross-check, and override rates are diagnostic.

## Scenario Averages Across Cases

| Scenario | Directional | Stability/rights | Legitimacy/control | Legal stability | Precedent | Statutory | Compliance | Rights protection | Partisan align. | Shadow abuse | Legitimacy | Reversal | Conflict | Responsiveness | Strategic | Admin cost | Merits accel. | Replacement | Override att. | Override |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 60 percent invalidation threshold | 0.745 | 0.706 | 0.824 | 0.671 | 0.879 | 0.633 | 0.503 | 0.685 | 0.100 | 0.086 | 0.802 | 0.074 | 0.458 | 0.727 | 0.206 | 0.295 | 0.235 | 0.051 | 0.000 | 0.000 |
| 18-year staggered terms + regular appointments | 0.742 | 0.702 | 0.824 | 0.659 | 0.837 | 0.637 | 0.503 | 0.698 | 0.102 | 0.106 | 0.811 | 0.091 | 0.459 | 0.737 | 0.202 | 0.300 | 0.404 | 0.131 | 0.000 | 0.000 |
| No emergency relief without merits review | 0.740 | 0.708 | 0.865 | 0.673 | 0.869 | 0.645 | 0.506 | 0.689 | 0.065 | 0.008 | 0.874 | 0.080 | 0.450 | 0.731 | 0.181 | 0.354 | 0.608 | 0.130 | 0.000 | 0.000 |
| Nonpartisan commission appointments | 0.735 | 0.703 | 0.833 | 0.662 | 0.845 | 0.638 | 0.503 | 0.697 | 0.065 | 0.107 | 0.819 | 0.088 | 0.458 | 0.736 | 0.201 | 0.330 | 0.402 | 0.131 | 0.000 | 0.000 |
| Retention-election accountability court | 0.733 | 0.698 | 0.832 | 0.665 | 0.858 | 0.643 | 0.495 | 0.683 | 0.070 | 0.106 | 0.820 | 0.082 | 0.473 | 0.741 | 0.206 | 0.330 | 0.409 | 0.192 | 0.114 | 0.049 |
| Three-judge panels with en banc correction | 0.732 | 0.704 | 0.836 | 0.663 | 0.848 | 0.639 | 0.503 | 0.695 | 0.113 | 0.107 | 0.901 | 0.086 | 0.458 | 0.735 | 0.200 | 0.345 | 0.400 | 0.494 | 0.000 | 0.000 |
| Judicial review with legislative supermajority override | 0.731 | 0.698 | 0.835 | 0.655 | 0.842 | 0.633 | 0.491 | 0.701 | 0.043 | 0.107 | 0.822 | 0.088 | 0.478 | 0.738 | 0.225 | 0.340 | 0.404 | 0.129 | 0.126 | 0.015 |
| Stylized current U.S.-like supreme court | 0.730 | 0.703 | 0.731 | 0.656 | 0.832 | 0.640 | 0.496 | 0.703 | 0.100 | 0.368 | 0.631 | 0.071 | 0.477 | 0.723 | 0.240 | 0.243 | 0.000 | 0.051 | 0.000 | 0.000 |
| Peer recusal + reasoned emergency docket | 0.729 | 0.703 | 0.825 | 0.661 | 0.843 | 0.638 | 0.503 | 0.698 | 0.101 | 0.107 | 0.817 | 0.088 | 0.458 | 0.737 | 0.201 | 0.340 | 0.406 | 0.128 | 0.000 | 0.000 |
| Expanded 15-seat court | 0.729 | 0.703 | 0.834 | 0.661 | 0.843 | 0.638 | 0.503 | 0.699 | 0.066 | 0.107 | 0.825 | 0.089 | 0.458 | 0.737 | 0.201 | 0.350 | 0.403 | 0.131 | 0.000 | 0.000 |
| Pre-enactment constitutional council | 0.710 | 0.704 | 0.847 | 0.676 | 0.874 | 0.642 | 0.512 | 0.689 | 0.078 | 0.106 | 0.922 | 0.075 | 0.472 | 0.747 | 0.215 | 0.421 | 0.410 | 0.197 | 0.106 | 0.016 |
| Supreme court with cross-checking constitutional court | 0.693 | 0.695 | 0.835 | 0.666 | 0.893 | 0.637 | 0.469 | 0.665 | 0.044 | 0.086 | 0.825 | 0.054 | 0.500 | 0.713 | 0.207 | 0.450 | 0.240 | 0.170 | 0.000 | 0.000 |
| Dual supreme courts with disagreement filter | 0.674 | 0.683 | 0.840 | 0.629 | 0.802 | 0.618 | 0.466 | 0.700 | 0.042 | 0.088 | 0.830 | 0.090 | 0.507 | 0.736 | 0.220 | 0.500 | 0.233 | 0.173 | 0.000 | 0.000 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | 60 percent invalidation threshold (0.767) | Dual supreme courts with disagreement filter (0.703) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.031) |
| Partisan Appointment Pressure | 60 percent invalidation threshold (0.768) | Dual supreme courts with disagreement filter (0.698) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.035) |
| Rights-Risk Legislation | 60 percent invalidation threshold (0.734) | Judicial review with legislative supermajority override (0.732) | No emergency relief without merits review (0.006) | Dual supreme courts with disagreement filter (0.037) |
| Shadow-Docket Stress | No emergency relief without merits review (0.728) | Stylized current U.S.-like supreme court (0.695) | No emergency relief without merits review (0.013) | Judicial review with legislative supermajority override (0.039) |
| High Democratic Mandate | 60 percent invalidation threshold (0.779) | Dual supreme courts with disagreement filter (0.684) | No emergency relief without merits review (0.002) | Dual supreme courts with disagreement filter (0.019) |
| Constitutional Conflict | No emergency relief without merits review (0.719) | Stylized current U.S.-like supreme court (0.721) | No emergency relief without merits review (0.016) | Judicial review with legislative supermajority override (0.059) |
| Imported Legislative Output | 60 percent invalidation threshold (0.771) | Dual supreme courts with disagreement filter (0.695) | No emergency relief without merits review (0.003) | Judicial review with legislative supermajority override (0.029) |
| Low Appointment Capture | 60 percent invalidation threshold (0.768) | Judicial review with legislative supermajority override (0.701) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.021) |
| Extreme Appointment Capture | 60 percent invalidation threshold (0.766) | Dual supreme courts with disagreement filter (0.700) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.042) |
| Low Emergency Pressure | 60 percent invalidation threshold (0.773) | Dual supreme courts with disagreement filter (0.704) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.028) |
| Extreme Emergency Pressure | No emergency relief without merits review (0.720) | Stylized current U.S.-like supreme court (0.696) | No emergency relief without merits review (0.018) | Dual supreme courts with disagreement filter (0.046) |
| Low Rights Risk | 60 percent invalidation threshold (0.787) | Dual supreme courts with disagreement filter (0.692) | No emergency relief without merits review (0.002) | Judicial review with legislative supermajority override (0.019) |
| Extreme Rights Risk | 60 percent invalidation threshold (0.702) | No emergency relief without merits review (0.736) | No emergency relief without merits review (0.009) | Dual supreme courts with disagreement filter (0.049) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.738) | Stylized current U.S.-like supreme court (0.731) | No emergency relief without merits review (0.007) | Judicial review with legislative supermajority override (0.035) |
| Strong-Mandate Legislation | 60 percent invalidation threshold (0.783) | Dual supreme courts with disagreement filter (0.680) | No emergency relief without merits review (0.002) | Dual supreme courts with disagreement filter (0.020) |
| Appointment Timing Manipulation | 60 percent invalidation threshold (0.771) | Dual supreme courts with disagreement filter (0.699) | No emergency relief without merits review (0.002) | Judicial review with legislative supermajority override (0.042) |
| Emergency Application Flood | No emergency relief without merits review (0.707) | Stylized current U.S.-like supreme court (0.701) | No emergency relief without merits review (0.026) | Dual supreme courts with disagreement filter (0.059) |
| Override Evasion Loop | 60 percent invalidation threshold (0.719) | Stylized current U.S.-like supreme court (0.702) | No emergency relief without merits review (0.010) | Judicial review with legislative supermajority override (0.052) |
| Recusal Pressure Campaign | 60 percent invalidation threshold (0.721) | Stylized current U.S.-like supreme court (0.719) | No emergency relief without merits review (0.015) | Judicial review with legislative supermajority override (0.076) |
| Court Expansion Retaliation | 60 percent invalidation threshold (0.711) | Stylized current U.S.-like supreme court (0.722) | No emergency relief without merits review (0.017) | Dual supreme courts with disagreement filter (0.078) |
