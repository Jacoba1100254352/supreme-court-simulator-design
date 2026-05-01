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

- Highest directional score: No emergency relief without merits review at 0.699.
- Highest rights protection: Stylized current U.S.-like supreme court at 0.695.
- Lowest shadow-docket abuse: No emergency relief without merits review at 0.011.
- Lowest partisan alignment: Dual supreme courts with disagreement filter at 0.045.
- Directional score is a reading aid, not a final constitutional judgment. It averages stability/rights, legitimacy/control, and administrative feasibility.

## Metric Direction Legend

- Higher `legalStability`, `rightsProtection`, `legitimacy`, and `democraticResponsiveness` are usually better.
- Lower `partisanAlignment`, `shadowDocketAbuse`, `reversalRate`, `constitutionalConflict`, and `administrativeCost` are usually better.
- Invalidation, emergency, replacement, recusal, concurrence, dissent, panel, en banc, council, cross-check, and override rates are diagnostic.

## Scenario Averages Across Cases

| Scenario | Directional | Stability/rights | Legitimacy/control | Legal stability | Precedent | Statutory | Compliance | Rights protection | Partisan align. | Shadow abuse | Legitimacy | Reversal | Conflict | Responsiveness | Strategic | Evasion | Exec flood | Admin cost | Merits accel. | Replacement | Override att. | Override |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| No emergency relief without merits review | 0.699 | 0.630 | 0.842 | 0.576 | 0.726 | 0.589 | 0.413 | 0.679 | 0.071 | 0.011 | 0.901 | 0.150 | 0.583 | 0.746 | 0.346 | 0.230 | 0.524 | 0.376 | 0.806 | 0.145 | 0.000 | 0.000 |
| 60 percent invalidation threshold | 0.697 | 0.639 | 0.770 | 0.611 | 0.834 | 0.588 | 0.410 | 0.651 | 0.109 | 0.148 | 0.760 | 0.116 | 0.591 | 0.723 | 0.387 | 0.226 | 0.565 | 0.318 | 0.278 | 0.068 | 0.000 | 0.000 |
| 18-year staggered terms + regular appointments | 0.696 | 0.632 | 0.779 | 0.582 | 0.748 | 0.587 | 0.410 | 0.683 | 0.112 | 0.157 | 0.795 | 0.146 | 0.593 | 0.742 | 0.383 | 0.231 | 0.545 | 0.322 | 0.534 | 0.146 | 0.000 | 0.000 |
| Nonpartisan commission appointments | 0.691 | 0.633 | 0.793 | 0.585 | 0.756 | 0.589 | 0.410 | 0.680 | 0.071 | 0.157 | 0.804 | 0.143 | 0.592 | 0.741 | 0.359 | 0.227 | 0.545 | 0.353 | 0.536 | 0.143 | 0.000 | 0.000 |
| Retention-election accountability court | 0.687 | 0.621 | 0.793 | 0.585 | 0.767 | 0.594 | 0.395 | 0.654 | 0.076 | 0.156 | 0.807 | 0.137 | 0.620 | 0.754 | 0.368 | 0.236 | 0.547 | 0.353 | 0.543 | 0.257 | 0.195 | 0.095 |
| Three-judge panels with en banc correction | 0.686 | 0.634 | 0.794 | 0.590 | 0.767 | 0.591 | 0.411 | 0.676 | 0.118 | 0.158 | 0.874 | 0.139 | 0.591 | 0.738 | 0.358 | 0.230 | 0.543 | 0.369 | 0.525 | 0.528 | 0.000 | 0.000 |
| Judicial review with legislative supermajority override | 0.684 | 0.622 | 0.794 | 0.572 | 0.751 | 0.577 | 0.389 | 0.690 | 0.046 | 0.157 | 0.808 | 0.144 | 0.630 | 0.744 | 0.395 | 0.267 | 0.545 | 0.362 | 0.535 | 0.145 | 0.220 | 0.024 |
| Peer recusal + reasoned emergency docket | 0.683 | 0.632 | 0.780 | 0.584 | 0.753 | 0.588 | 0.410 | 0.680 | 0.114 | 0.157 | 0.801 | 0.144 | 0.592 | 0.741 | 0.382 | 0.230 | 0.544 | 0.362 | 0.537 | 0.146 | 0.000 | 0.000 |
| Expanded 15-seat court | 0.683 | 0.632 | 0.790 | 0.582 | 0.748 | 0.587 | 0.410 | 0.683 | 0.072 | 0.158 | 0.810 | 0.146 | 0.592 | 0.743 | 0.383 | 0.230 | 0.544 | 0.372 | 0.530 | 0.148 | 0.000 | 0.000 |
| Stylized current U.S.-like supreme court | 0.675 | 0.638 | 0.642 | 0.582 | 0.753 | 0.594 | 0.398 | 0.695 | 0.111 | 0.536 | 0.523 | 0.100 | 0.626 | 0.711 | 0.422 | 0.226 | 0.619 | 0.255 | 0.000 | 0.069 | 0.000 | 0.000 |
| Pre-enactment constitutional council | 0.656 | 0.631 | 0.808 | 0.602 | 0.793 | 0.590 | 0.424 | 0.669 | 0.082 | 0.154 | 0.909 | 0.126 | 0.620 | 0.762 | 0.384 | 0.256 | 0.544 | 0.471 | 0.548 | 0.207 | 0.186 | 0.024 |
| Supreme court with cross-checking constitutional court | 0.644 | 0.627 | 0.784 | 0.614 | 0.871 | 0.601 | 0.369 | 0.612 | 0.048 | 0.147 | 0.785 | 0.077 | 0.640 | 0.697 | 0.365 | 0.224 | 0.564 | 0.479 | 0.283 | 0.185 | 0.000 | 0.000 |
| Dual supreme courts with disagreement filter | 0.623 | 0.605 | 0.794 | 0.537 | 0.686 | 0.563 | 0.364 | 0.687 | 0.045 | 0.149 | 0.789 | 0.148 | 0.655 | 0.741 | 0.382 | 0.236 | 0.563 | 0.529 | 0.272 | 0.188 | 0.000 | 0.000 |

## Stress Case Leaders

| Case | Best directional | Highest rights | Lowest shadow abuse | Lowest partisan align. |
| --- | --- | --- | --- | --- |
| Baseline | No emergency relief without merits review (0.721) | Dual supreme courts with disagreement filter (0.687) | No emergency relief without merits review (0.005) | Dual supreme courts with disagreement filter (0.034) |
| Partisan Appointment Pressure | No emergency relief without merits review (0.721) | Expanded 15-seat court (0.686) | No emergency relief without merits review (0.005) | Dual supreme courts with disagreement filter (0.039) |
| Rights-Risk Legislation | 60 percent invalidation threshold (0.680) | No emergency relief without merits review (0.769) | No emergency relief without merits review (0.009) | Dual supreme courts with disagreement filter (0.041) |
| Shadow-Docket Stress | No emergency relief without merits review (0.696) | Stylized current U.S.-like supreme court (0.697) | No emergency relief without merits review (0.016) | Judicial review with legislative supermajority override (0.041) |
| High Democratic Mandate | 18-year staggered terms + regular appointments (0.733) | Dual supreme courts with disagreement filter (0.650) | No emergency relief without merits review (0.004) | Dual supreme courts with disagreement filter (0.022) |
| Constitutional Conflict | No emergency relief without merits review (0.671) | Stylized current U.S.-like supreme court (0.742) | No emergency relief without merits review (0.023) | Judicial review with legislative supermajority override (0.063) |
| Imported Legislative Output | 18-year staggered terms + regular appointments (0.727) | Dual supreme courts with disagreement filter (0.679) | No emergency relief without merits review (0.004) | Judicial review with legislative supermajority override (0.032) |
| Low Appointment Capture | 18-year staggered terms + regular appointments (0.721) | Dual supreme courts with disagreement filter (0.689) | No emergency relief without merits review (0.005) | Dual supreme courts with disagreement filter (0.023) |
| Extreme Appointment Capture | No emergency relief without merits review (0.720) | Dual supreme courts with disagreement filter (0.691) | No emergency relief without merits review (0.005) | Dual supreme courts with disagreement filter (0.047) |
| Low Emergency Pressure | 60 percent invalidation threshold (0.726) | Dual supreme courts with disagreement filter (0.719) | No emergency relief without merits review (0.005) | Dual supreme courts with disagreement filter (0.031) |
| Extreme Emergency Pressure | No emergency relief without merits review (0.691) | Stylized current U.S.-like supreme court (0.704) | No emergency relief without merits review (0.019) | Dual supreme courts with disagreement filter (0.046) |
| Low Rights Risk | 18-year staggered terms + regular appointments (0.743) | Dual supreme courts with disagreement filter (0.640) | No emergency relief without merits review (0.002) | Judicial review with legislative supermajority override (0.021) |
| Extreme Rights Risk | 60 percent invalidation threshold (0.660) | No emergency relief without merits review (0.774) | No emergency relief without merits review (0.014) | Dual supreme courts with disagreement filter (0.054) |
| Weak-Mandate Legislation | 60 percent invalidation threshold (0.685) | No emergency relief without merits review (0.758) | No emergency relief without merits review (0.010) | Judicial review with legislative supermajority override (0.038) |
| Strong-Mandate Legislation | 18-year staggered terms + regular appointments (0.736) | Dual supreme courts with disagreement filter (0.631) | No emergency relief without merits review (0.003) | Dual supreme courts with disagreement filter (0.024) |
| Appointment Timing Manipulation | No emergency relief without merits review (0.724) | Dual supreme courts with disagreement filter (0.680) | No emergency relief without merits review (0.005) | Judicial review with legislative supermajority override (0.050) |
| Emergency Application Flood | No emergency relief without merits review (0.676) | Stylized current U.S.-like supreme court (0.706) | No emergency relief without merits review (0.028) | Dual supreme courts with disagreement filter (0.060) |
| Override Evasion Loop | 60 percent invalidation threshold (0.664) | Stylized current U.S.-like supreme court (0.732) | No emergency relief without merits review (0.016) | Judicial review with legislative supermajority override (0.057) |
| Recusal Pressure Campaign | No emergency relief without merits review (0.674) | Stylized current U.S.-like supreme court (0.736) | No emergency relief without merits review (0.022) | Judicial review with legislative supermajority override (0.081) |
| Court Expansion Retaliation | No emergency relief without merits review (0.657) | Stylized current U.S.-like supreme court (0.750) | No emergency relief without merits review (0.025) | Dual supreme courts with disagreement filter (0.084) |
