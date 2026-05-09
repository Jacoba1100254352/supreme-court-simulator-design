#!/usr/bin/env python3
"""Generate lightweight LaTeX figure and table fragments from report outputs.

The fragments use only standard LaTeX picture primitives plus xcolor, so the
paper remains portable across the local fallback build and the Cambridge
template path.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CAMPAIGN_CSV = ROOT / "reports" / "constitutional-review-campaign-v2.csv"
CALIBRATION_CSV = ROOT / "reports" / "calibration-baseline.csv"
SWEEP_CSV = ROOT / "reports" / "parameter-sweep-v4.csv"
SWEEP_DRIVERS_CSV = ROOT / "reports" / "parameter-sweep-drivers-v4.csv"
PRIOR_UNCERTAINTY_CSV = ROOT / "reports" / "prior-uncertainty-v1.csv"
PATHWAY_DASHBOARD_CSV = ROOT / "reports" / "pathway-validation-dashboard-v1.csv"
MECHANISM_CSV = ROOT / "reports" / "mechanism-ablation-v2.csv"
FIGURE_DIR = ROOT / "paper" / "figures"
TABLE_DIR = ROOT / "paper" / "tables"

SELECTED_SCENARIOS = [
    ("current-us-like", "Current-like"),
    ("term-limited-balanced", "18-year terms"),
    ("mandatory-written-emergency-reasoning", "Written reasons"),
    ("automatic-merits-follow-up", "Auto merits"),
    ("emergency-restraint-court", "No merits gap"),
    ("strong-recusal-enforcement", "Recusal enforce."),
    ("randomized-merits-panels", "Random panels"),
    ("emergency-integrity-package", "Integrity pkg."),
]

FIELDS = [
    "admissionRate",
    "certiorariAdmissionRate",
    "courtRequestedResponseRate",
    "cvsgRequestRate",
    "paidCfrRequestRate",
    "ifpCfrRequestRate",
    "directionalScore",
    "legalStability",
    "rightsProtection",
    "partisanAlignment",
    "shadowDocketAbuse",
    "emergencyLegitimacyRisk",
    "constitutionalConflict",
    "democraticResponsiveness",
    "administrativeCost",
    "publicConfidence",
    "lowerCourtSplitDepth",
    "genuineLowerCourtSplitRate",
    "lowerCourtIdeologicalDrift",
    "lowerCourtResistanceRisk",
    "forumShoppingPressure",
    "preReviewSettlementPressure",
    "settledBeforeReviewRate",
    "strategicPlaintiffSelection",
    "repeatPlayerAdvantage",
    "repeatPlayerLearning",
    "emergencyIncentiveLearning",
    "complianceLearning",
    "barCapital",
    "claimStrength",
    "vehicleQuality",
    "governmentNoncomplianceRate",
    "enforcementCapacity",
    "emergencyOpportunism",
    "recusalIncentivePressure",
    "reasonedEmergencyOrderRate",
    "meritsAccelerationRate",
    "constitutionalRemandRate",
    "publicInterestFilteredRate",
    "precedentDurability",
    "emergencyDownstreamEffect",
    "lowerCourtCompliance",
    "rightsDomainClaimantSuccess",
    "structuralDomainClaimantSuccess",
    "electionDomainClaimantSuccess",
    "executivePowerDomainClaimantSuccess",
    "administrativeDomainClaimantSuccess",
    "economicDomainClaimantSuccess",
]


def fmt(value: float) -> str:
    return f"{value:.1f}"


def tex_escape(value: str) -> str:
    return (
        value.replace("\\", "\\textbackslash{}")
        .replace("&", "\\&")
        .replace("%", "\\%")
        .replace("$", "\\$")
        .replace("#", "\\#")
        .replace("_", "\\_")
        .replace("{", "\\{")
        .replace("}", "\\}")
    )


def humanize_identifier(value: str) -> str:
    """Convert generated metric keys into journal-table labels that can wrap."""
    spaced = value.replace("_", " ")
    spaced = re.sub(r"(?<=[a-z])(?=[A-Z])", " ", spaced)
    spaced = re.sub(r"(?<=[A-Z])(?=[A-Z][a-z])", " ", spaced)
    spaced = spaced.replace("PP", "percentage points")
    spaced = spaced.replace("QPC", "QPC")
    return " ".join(spaced.split()).lower()


def fmt3(value: float) -> str:
    return f"{value:.3f}"


def clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def read_weighted_averages() -> dict[str, dict[str, float]]:
    totals: dict[str, defaultdict[str, float]] = defaultdict(lambda: defaultdict(float))
    weights: dict[str, float] = defaultdict(float)
    with CAMPAIGN_CSV.open(newline="") as handle:
        for row in csv.DictReader(handle):
            key = row["scenarioKey"]
            weight = float(row.get("caseWeight") or 1.0)
            weights[key] += weight
            for field in FIELDS:
                if row.get(field):
                    totals[key][field] += float(row[field]) * weight
    return {
        key: {field: totals[key][field] / weights[key] for field in FIELDS}
        for key in totals
    }


def write_conflict_confidence_tradeoff(averages: dict[str, dict[str, float]]) -> None:
    left, bottom, width, height = 24.0, 16.0, 86.0, 54.0
    x_min, x_max = 0.44, 0.48
    y_min, y_max = 0.38, 0.68
    label_positions = {
        "current-us-like": (101.0, 22.0, "c"),
        "term-limited-balanced": (55.0, 51.5, "l"),
        "mandatory-written-emergency-reasoning": (64.0, 47.0, "l"),
        "automatic-merits-follow-up": (36.0, 61.5, "r"),
        "emergency-restraint-court": (55.0, 70.5, "l"),
        "strong-recusal-enforcement": (66.0, 59.3, "l"),
        "randomized-merits-panels": (69.0, 66.5, "l"),
        "emergency-integrity-package": (94.0, 58.0, "l"),
        "public-interest-litigation-filter": (95.0, 53.5, "l"),
    }
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begingroup",
        "\\setlength{\\unitlength}{1mm}",
        "\\setlength{\\fboxsep}{0.45pt}",
        "\\begin{picture}(128,82)",
        "\\scriptsize",
    ]
    for tick in (0.44, 0.45, 0.46, 0.47, 0.48):
        x = left + ((tick - x_min) / (x_max - x_min)) * width
        lines.extend([
            f"\\put({fmt(x)},{fmt(bottom)}){{\\color{{black!15}}\\line(0,1){{{fmt(height)}}}}}",
            f"\\put({fmt(x)},{fmt(bottom - 3.2)}){{\\makebox(0,0){{{tick:.2f}}}}}",
        ])
    for tick in (0.40, 0.46, 0.52, 0.58, 0.64, 0.68):
        y = bottom + ((tick - y_min) / (y_max - y_min)) * height
        lines.extend([
            f"\\put({fmt(left)},{fmt(y)}){{\\color{{black!15}}\\line(1,0){{{fmt(width)}}}}}",
            f"\\put({fmt(left - 4.0)},{fmt(y)}){{\\makebox(0,0)[r]{{{tick:.2f}}}}}",
        ])
    lines.extend([
        f"\\put({fmt(left)},{fmt(bottom)}){{\\line(1,0){{{fmt(width)}}}}}",
        f"\\put({fmt(left)},{fmt(bottom)}){{\\line(0,1){{{fmt(height)}}}}}",
    ])
    for key, label in SELECTED_SCENARIOS:
        values = averages[key]
        x = left + ((values["constitutionalConflict"] - x_min) / (x_max - x_min)) * width
        y = bottom + ((values["publicConfidence"] - y_min) / (y_max - y_min)) * height
        x = max(left, min(left + width, x))
        y = max(bottom, min(bottom + height, y))
        shade = 15 + round(clamp01(values["shadowDocketAbuse"] / 0.25) * 70)
        color = "red" if key == "current-us-like" else f"black!{shade}"
        marker = 3.1 if key == "current-us-like" else 2.5
        label_x, label_y, anchor = label_positions[key]
        label_color = "red" if key == "current-us-like" else "black"
        if anchor == "r":
            leader_x = label_x + 1.0
        elif anchor == "l":
            leader_x = label_x - 1.0
        else:
            leader_x = label_x
        leader_mid_x = (x + leader_x) / 2.0
        leader_mid_y = (y + label_y) / 2.0
        lines.extend([
            f"\\qbezier({fmt(x)},{fmt(y)})({fmt(leader_mid_x)},{fmt(leader_mid_y)})({fmt(leader_x)},{fmt(label_y)})",
            f"\\put({fmt(x - marker / 2.0)},{fmt(y - marker / 2.0)}){{\\color{{{color}}}\\rule{{{marker:.1f}mm}}{{{marker:.1f}mm}}}}",
            f"\\put({fmt(label_x)},{fmt(label_y)}){{\\makebox(0,0)[{anchor}]{{\\colorbox{{white}}{{\\color{{{label_color}}}{label}}}}}}}",
        ])
    lines.extend([
        f"\\put({fmt(left + width / 2.0)},{fmt(4.5)}){{\\makebox(0,0){{Constitutional conflict $\\downarrow$}}}}",
        f"\\put({fmt(left - 5.0)},{fmt(bottom + height + 5.0)}){{\\makebox(0,0)[l]{{Public confidence $\\uparrow$}}}}",
        "\\tiny",
        "\\put(61.0,76.0){\\makebox(0,0)[l]{Marker shade increases with shadow-docket abuse.}}",
        "\\end{picture}",
        "\\endgroup",
        "",
    ])
    (FIGURE_DIR / "conflict_confidence_tradeoff.tex").write_text("\n".join(lines))


def write_emergency_profile(averages: dict[str, dict[str, float]]) -> None:
    left_label, left_axis, scale = 45.0, 50.0, 70.0
    top, row_gap, bar_gap = 66.0, 7.2, 1.65
    metrics = [
        ("shadowDocketAbuse", "Shadow abuse", "black!75"),
        ("emergencyLegitimacyRisk", "Emerg. legit. risk", "black!45"),
        ("publicConfidence", "Public confidence", "black!18"),
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begingroup",
        "\\setlength{\\unitlength}{1mm}",
        "\\begin{picture}(128,80)",
        "\\scriptsize",
    ]
    for tick in (0.0, 0.2, 0.4, 0.6):
        x = left_axis + tick * scale
        lines.extend([
            f"\\put({fmt(x)},{fmt(8.0)}){{\\color{{black!15}}\\line(0,1){{62.0}}}}",
            f"\\put({fmt(x)},{fmt(4.7)}){{\\makebox(0,0){{{tick:.1f}}}}}",
        ])
    for row_index, (key, label) in enumerate(SELECTED_SCENARIOS):
        values = averages[key]
        y = top - row_index * row_gap
        label_color = "red" if key == "current-us-like" else "black"
        lines.append(f"\\put({fmt(left_label)},{fmt(y)}){{\\makebox(0,0)[r]{{\\color{{{label_color}}}{label}}}}}")
        for metric_index, (field, _metric_label, color) in enumerate(metrics):
            bar_color = ("red!80", "red!55", "red!25")[metric_index] if key == "current-us-like" else color
            bar_y = y + (1 - metric_index) * bar_gap
            value = max(0.0, averages[key][field])
            bar_width = max(value * scale, 0.35)
            lines.append(
                f"\\put({fmt(left_axis)},{fmt(bar_y)}){{\\color{{{bar_color}}}\\rule{{{bar_width:.1f}mm}}{{1.1mm}}}}"
            )
            lines.append(
                f"\\put({fmt(min(left_axis + bar_width + 1.2, 122.0))},{fmt(bar_y + 0.55)})"
                f"{{\\makebox(0,0)[l]{{\\tiny {value:.2f}}}}}"
            )
    legend_positions = [
        (37.0, 74.0, metrics[0][1], metrics[0][2]),
        (75.0, 74.0, metrics[1][1], metrics[1][2]),
        (37.0, 70.2, metrics[2][1], metrics[2][2]),
    ]
    for x, y, label, color in legend_positions:
        lines.extend([
            f"\\put({fmt(x)},{fmt(y)}){{\\color{{{color}}}\\rule{{5.0mm}}{{1.8mm}}}}",
            f"\\put({fmt(x + 7.0)},{fmt(y + 0.3)}){{\\makebox(0,0)[l]{{{label}}}}}",
        ])
    lines.extend([
        "\\put(76.0,1.0){\\makebox(0,0){Raw normalized campaign average}}",
        "\\end{picture}",
        "\\endgroup",
        "",
    ])
    (FIGURE_DIR / "emergency_profile.tex").write_text("\n".join(lines))


def heat_color(value: float, scale_max: float, current: bool = False) -> tuple[str, str]:
    shade = 8 + round(clamp01(value / scale_max) * 72)
    color = f"red!{shade}" if current else f"black!{shade}"
    text = "white" if shade >= 54 else "black"
    return color, text


def write_domain_claimant_success(averages: dict[str, dict[str, float]]) -> None:
    columns = [
        ("rightsDomainClaimantSuccess", "Rights"),
        ("structuralDomainClaimantSuccess", "Struct."),
        ("electionDomainClaimantSuccess", "Elect."),
        ("executivePowerDomainClaimantSuccess", "Exec."),
        ("administrativeDomainClaimantSuccess", "Admin."),
        ("economicDomainClaimantSuccess", "Econ."),
    ]
    left_label = 45.0
    left = 51.0
    top = 60.0
    cell_w = 12.2
    cell_h = 5.1
    row_gap = 6.3
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begingroup",
        "\\setlength{\\unitlength}{1mm}",
        "\\begin{picture}(128,72)",
        "\\scriptsize",
    ]
    for col_index, (_field, label) in enumerate(columns):
        x = left + col_index * cell_w
        lines.append(f"\\put({fmt(x + cell_w / 2.0)},{fmt(66.0)}){{\\makebox(0,0){{\\textbf{{{label}}}}}}}")
    for row_index, (key, label) in enumerate(SELECTED_SCENARIOS):
        values = averages[key]
        y = top - row_index * row_gap
        label_color = "red" if key == "current-us-like" else "black"
        lines.append(f"\\put({fmt(left_label)},{fmt(y + cell_h / 2.0)}){{\\makebox(0,0)[r]{{\\color{{{label_color}}}{label}}}}}")
        for col_index, (field, _label) in enumerate(columns):
            value = values[field]
            x = left + col_index * cell_w
            fill, text = heat_color(value, 0.55, key == "current-us-like")
            lines.extend([
                f"\\put({fmt(x)},{fmt(y)}){{\\color{{{fill}}}\\rule{{{fmt(cell_w - 0.8)}mm}}{{{fmt(cell_h)}mm}}}}",
                f"\\put({fmt(x + cell_w / 2.0 - 0.4)},{fmt(y + cell_h / 2.0)}){{\\makebox(0,0){{\\color{{{text}}}{value:.2f}}}}}",
            ])
    lines.extend([
        "\\put(72.0,4.0){\\makebox(0,0){Domain-specific claimant-success rates; darker cells are higher.}}",
        "\\end{picture}",
        "\\endgroup",
        "",
    ])
    (FIGURE_DIR / "domain_claimant_success.tex").write_text("\n".join(lines))


def write_selected_campaign_table(averages: dict[str, dict[str, float]]) -> None:
    selected = [
        ("current-us-like", "Stylized current U.S.-like court"),
        ("term-limited-balanced", "18-year staggered terms"),
        ("mandatory-written-emergency-reasoning", "Mandatory written emergency reasoning"),
        ("automatic-merits-follow-up", "Automatic merits follow-up"),
        ("emergency-restraint-court", "No emergency relief without merits review"),
        ("strong-recusal-enforcement", "Independent recusal enforcement with substitutes"),
        ("randomized-merits-panels", "Randomized merits panels with en banc correction"),
        ("emergency-integrity-package", "Emergency integrity package"),
        ("constitutional-remand", "Constitutional remand before invalidation"),
        ("remand-override-window-package", "Remand with override window"),
        ("public-interest-litigation-filter", "Public-interest litigation filter"),
    ]
    fields = [
        "rightsProtection",
        "shadowDocketAbuse",
        "emergencyLegitimacyRisk",
        "emergencyDownstreamEffect",
        "governmentNoncomplianceRate",
        "lowerCourtCompliance",
        "precedentDurability",
        "publicConfidence",
        "directionalScore",
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Selected v2 campaign averages, grouped by emergency-power and rights-protection profile}",
        "\\label{tab:v2-selected}",
        "\\Description{Table of selected campaign averages for rights protection, shadow-docket abuse, emergency legitimacy risk, emergency downstream effect, government noncompliance, lower-court compliance, precedent durability, public confidence, and directional score.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.55in}rrrrrrrrr}",
        "\\toprule",
        "Scenario & Rights & Shadow & Emerg. risk & Downstream & Gov. noncomp. & Lower ct. & Prec. dur. & Public & Score \\\\",
        "\\midrule",
    ]
    for key, label in selected:
        values = averages[key]
        cells = " & ".join(fmt3(values[field]) for field in fields)
        lines.append(f"{tex_escape(label)} & {cells} \\\\")
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "v2_selected.tex").write_text("\n".join(lines))


def write_litigation_pipeline_table(averages: dict[str, dict[str, float]]) -> None:
    selected = [
        ("current-us-like", "Current-like"),
        ("term-limited-balanced", "18-year terms"),
        ("mandatory-written-emergency-reasoning", "Written emergency reasons"),
        ("automatic-merits-follow-up", "Automatic merits follow-up"),
        ("emergency-restraint-court", "No emergency merits gap"),
        ("strong-recusal-enforcement", "Strong recusal enforcement"),
        ("randomized-merits-panels", "Random merits panels"),
        ("emergency-integrity-package", "Emergency integrity package"),
        ("jurisdiction-stripping-constraints", "Jurisdiction-stripping constraints"),
        ("legislative-override-window", "Legislative override window"),
        ("constitutional-remand", "Constitutional remand"),
        ("public-interest-litigation-filter", "Public-interest filter"),
        ("remand-override-window-package", "Remand + override window"),
        ("panel-jurisdiction-safeguards", "Panel + jurisdiction safeguards"),
    ]
    fields = [
        "certiorariAdmissionRate",
        "courtRequestedResponseRate",
        "cvsgRequestRate",
        "barCapital",
        "claimStrength",
        "vehicleQuality",
        "genuineLowerCourtSplitRate",
        "lowerCourtSplitDepth",
        "lowerCourtResistanceRisk",
        "forumShoppingPressure",
        "settledBeforeReviewRate",
        "strategicPlaintiffSelection",
        "repeatPlayerAdvantage",
        "enforcementCapacity",
        "emergencyOpportunism",
        "recusalIncentivePressure",
        "governmentNoncomplianceRate",
        "emergencyDownstreamEffect",
        "precedentDurability",
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Litigation-pipeline and downstream-enforcement diagnostics}",
        "\\label{tab:pipeline-diagnostics}",
        "\\Description{Table reporting certiorari admission, court-requested response, CVSG request, bar capital, claim strength, vehicle quality, genuine split rate, lower-court split depth, lower-court resistance, forum shopping, settlement, strategic plaintiff selection, repeat-player advantage, enforcement capacity, emergency opportunism, recusal incentive pressure, government noncompliance, emergency downstream effect, and precedent durability for selected designs.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{2pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.38in}rrrrrrrrrrrrrrrrrrr}",
        "\\toprule",
        "Scenario & Cert admit & CFR & CVSG & Bar & Claim & Vehicle & Genuine split & Split & Resistance & Forum & Settlement & Plaintiff sel. & Repeat player & Enforcement & Emerg. opp. & Recusal press. & Gov. noncomp. & Emerg. down. & Prec. dur. \\\\",
        "\\midrule",
    ]
    for key, label in selected:
        values = averages[key]
        cells = " & ".join(fmt3(values[field]) for field in fields)
        lines.append(f"{tex_escape(label)} & {cells} \\\\")
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "pipeline_diagnostics.tex").write_text("\n".join(lines))


def read_calibration_rows() -> list[dict[str, str]]:
    with CALIBRATION_CSV.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_calibration_guardrails() -> None:
    selected = [
        ("current-merits-transfer", "Merits transfer"),
        ("current-paid-cfr-stage", "Paid CFR stage"),
        ("current-ifp-cfr-stage", "IFP CFR stage"),
        ("current-invalidation", "Invalidation"),
        ("current-emergency-applications", "Emergency filings"),
        ("current-shadow-abuse", "Shadow abuse"),
        ("commission-partisan-alignment", "Partisan alignment"),
        ("emergency-restraint-shadow", "Emergency restraint"),
    ]
    rows_by_key = {row["targetKey"]: row for row in read_calibration_rows()}
    source_labels = {
        "deep-research-intake-synthesis": "source register",
        "scdb-modern-2025-01": "SCDB",
        "shadow-docket-v2-0": "shadow database",
        "black-epstein-recusal": "recusal data",
        "supreme-court-simulator-calibration-targets": "research tables",
    }

    def source_basis(row: dict[str, str]) -> str:
        source = source_labels.get(row["sourceKey"], row["sourceKey"])
        basis = "model fallback" if row["rangeBasis"] == "fallback" else "source range"
        return f"{source}; {basis}"

    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Selected calibration guardrails}",
        "\\label{tab:calibration-guardrails}",
        "\\Description{Table showing selected calibration guardrails, their intended use, simulated observations, source-informed ranges, source bases, and status.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.92in}>{\\raggedright\\arraybackslash}p{0.64in}>{\\raggedright\\arraybackslash}p{0.70in}>{\\raggedright\\arraybackslash}p{0.74in}rr>{\\raggedright\\arraybackslash}p{0.80in}r}",
        "\\toprule",
        "Guardrail & Scenario & Use & Evidence & Observed & Range & Source basis & Status \\\\",
        "\\midrule",
    ]
    for key, label in selected:
        row = rows_by_key[key]
        scenario = {
            "current-us-like": "Current-like",
            "emergency-restraint-court": "No-gap",
            "nonpartisan-commission": "Commission",
            "legislative-override": "Override",
        }.get(row["scenarioKey"], row["scenario"])
        lines.append(
            f"{tex_escape(label)} & {tex_escape(scenario)} & "
            f"{tex_escape(row['guardrailClass'].replace('_', ' '))} & "
            f"{tex_escape(row.get('sourceTier', 'unknown').replace('_', ' '))} & "
            f"{float(row['observed']):.3f} & "
            f"{float(row['min']):.3f}--{float(row['max']):.3f} & "
            f"{tex_escape(source_basis(row))} & {'within' if row['pass'] == 'true' else 'review'} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "calibration_guardrails.tex").write_text("\n".join(lines))


def write_calibration_classification_table() -> None:
    rows = read_calibration_rows()
    counts: dict[str, dict[str, int]] = defaultdict(lambda: {"total": 0, "pass": 0})
    for row in rows:
        guardrail_class = row["guardrailClass"].replace("_", " ")
        counts[guardrail_class]["total"] += 1
        counts[guardrail_class]["pass"] += 1 if row["pass"] == "true" else 0
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Calibration-use classification summary}",
        "\\label{tab:calibration-classification}",
        "\\Description{Table counting calibration guardrails by intended validation use and pass status.}",
        "\\footnotesize",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.85in}rr>{\\raggedright\\arraybackslash}p{2.35in}}",
        "\\toprule",
        "Guardrail use & Rows & Within range & Interpretation \\\\",
        "\\midrule",
    ]
    interpretations = {
        "strict validation": "closest to source-denominator checks",
        "loose calibration": "plausibility range, not point validation",
        "proxy sanity": "related proxy, not same empirical construct",
        "mechanism sanity": "checks expected mechanism direction",
        "model prior": "documents coding prior or design context",
    }
    for guardrail_class, values in sorted(counts.items()):
        lines.append(
            f"{tex_escape(guardrail_class)} & {values['total']} & {values['pass']} & "
            f"{tex_escape(interpretations.get(guardrail_class, 'context row'))} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "calibration_classification.tex").write_text("\n".join(lines))


def read_sweep_rows() -> dict[str, dict[str, str]]:
    with SWEEP_CSV.open(newline="") as handle:
        return {row["scenarioKey"]: row for row in csv.DictReader(handle)}


def read_sweep_driver_rows() -> list[dict[str, str]]:
    with SWEEP_DRIVERS_CSV.open(newline="") as handle:
        return list(csv.DictReader(handle))


def read_prior_uncertainty_rows() -> list[dict[str, str]]:
    with PRIOR_UNCERTAINTY_CSV.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_sampled_prior_uncertainty_table() -> None:
    selected = {
        "term-limited-balanced",
        "mandatory-written-emergency-reasoning",
        "automatic-merits-follow-up",
        "emergency-restraint-court",
        "current-us-like",
        "strong-recusal-enforcement",
        "randomized-merits-panels",
        "constitutional-remand",
    }
    rows = [row for row in read_prior_uncertainty_rows() if row["scenarioKey"] in selected]
    rows.sort(key=lambda row: float(row["directionalP50"]), reverse=True)
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Sampled-prior uncertainty bands for selected designs}",
        "\\label{tab:sampled-prior-uncertainty}",
        "\\Description{Table reporting sampled-prior 5th, 50th, and 95th percentile bands for directional score, rights protection, shadow-docket abuse, emergency downstream effect, lower-court compliance, government noncompliance, and constitutional conflict.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.45in}rrrrrrr>{\\raggedright\\arraybackslash}p{1.35in}}",
        "\\toprule",
        "Scenario & Score & Rights & Shadow & Emerg. down. & Lower ct. & Gov. noncomp. & Conflict & Interpretation \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['scenario'])} & "
            f"{float(row['directionalP05']):.3f}/{float(row['directionalP50']):.3f}/{float(row['directionalP95']):.3f} & "
            f"{float(row['rightsProtectionP05']):.3f}/{float(row['rightsProtectionP50']):.3f}/{float(row['rightsProtectionP95']):.3f} & "
            f"{float(row['shadowDocketAbuseP05']):.3f}/{float(row['shadowDocketAbuseP50']):.3f}/{float(row['shadowDocketAbuseP95']):.3f} & "
            f"{float(row['emergencyDownstreamP05']):.3f}/{float(row['emergencyDownstreamP50']):.3f}/{float(row['emergencyDownstreamP95']):.3f} & "
            f"{float(row['lowerCourtComplianceP05']):.3f}/{float(row['lowerCourtComplianceP50']):.3f}/{float(row['lowerCourtComplianceP95']):.3f} & "
            f"{float(row['governmentNoncomplianceP05']):.3f}/{float(row['governmentNoncomplianceP50']):.3f}/{float(row['governmentNoncomplianceP95']):.3f} & "
            f"{float(row['constitutionalConflictP05']):.3f}/{float(row['constitutionalConflictP50']):.3f}/{float(row['constitutionalConflictP95']):.3f} & "
            f"{tex_escape(row['interpretation'])} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "sampled_prior_uncertainty.tex").write_text("\n".join(lines))


def write_uncertainty_bands(averages: dict[str, dict[str, float]]) -> None:
    sweep = read_sweep_rows()
    selected = [
        ("term-limited-balanced", "18-year terms"),
        ("mandatory-written-emergency-reasoning", "Written emergency reasons"),
        ("automatic-merits-follow-up", "Emergency merits follow-up"),
        ("emergency-restraint-court", "No emergency merits gap"),
        ("current-us-like", "Current-like"),
        ("strong-recusal-enforcement", "Strong recusal enforcement"),
        ("constitutional-remand", "Constitutional remand"),
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Campaign scores and uncertainty bands for selected designs}",
        "\\label{tab:uncertainty-bands}",
        "\\Description{Table comparing campaign averages with named-prior uncertainty bands for directional score, shadow-docket abuse, and constitutional conflict.}",
        "\\footnotesize",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.65in}rrrr}",
        "\\toprule",
        "Scenario & Campaign score & Score 5/50/95 & Shadow 5/50/95 & Conflict 5/50/95 \\\\",
        "\\midrule",
    ]
    for key, label in selected:
        row = sweep[key]
        lines.append(
            f"{tex_escape(label)} & {fmt3(averages[key]['directionalScore'])} & "
            f"{float(row['directionalP05']):.3f}/{float(row['directionalMedian']):.3f}/{float(row['directionalP95']):.3f} & "
            f"{float(row['shadowDocketAbuseP05']):.3f}/{float(row['shadowDocketAbuseMedian']):.3f}/{float(row['shadowDocketAbuseP95']):.3f} & "
            f"{float(row['constitutionalConflictP05']):.3f}/{float(row['constitutionalConflictMedian']):.3f}/{float(row['constitutionalConflictP95']):.3f} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "uncertainty_bands.tex").write_text("\n".join(lines))


def write_sensitivity_drivers_table() -> None:
    selected_priors = {
        "baseline",
        "high-emergency-share",
        "high-rights-risk",
        "high-conflict",
        "weak-mandate",
        "imported-legislative-family",
    }
    rows = []
    per_prior: dict[str, int] = defaultdict(int)
    for row in read_sweep_driver_rows():
        if row["priorKey"] not in selected_priors or per_prior[row["priorKey"]] >= 2:
            continue
        rows.append(row)
        per_prior[row["priorKey"]] += 1
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Sensitivity drivers and interpretation caveats}",
        "\\label{tab:sensitivity-drivers}",
        "\\Description{Table reporting top-cluster scenarios under selected named priors and the caveat that would change the interpretation.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.35in}>{\\raggedright\\arraybackslash}p{1.65in}rrrrrr>{\\raggedright\\arraybackslash}p{1.15in}}",
        "\\toprule",
        "Prior & Top-cluster design & Score & Rights & Shadow & Emerg. down. & Gov. noncomp. & LC resist. & Caveat \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['priorName'])} & {tex_escape(row['scenario'])} & "
            f"{float(row['directionalScore']):.3f} & {float(row['rightsProtection']):.3f} & "
            f"{float(row['shadowDocketAbuse']):.3f} & {float(row['emergencyDownstreamEffect']):.3f} & "
            f"{float(row['governmentNoncomplianceRate']):.3f} & {float(row['lowerCourtResistanceRisk']):.3f} & "
            f"{tex_escape(row['interpretationRisk'])} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "sensitivity_drivers.tex").write_text("\n".join(lines))


def read_pathway_dashboard_rows() -> list[dict[str, str]]:
    with PATHWAY_DASHBOARD_CSV.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_pathway_validation_table() -> None:
    selected = [
        ("certiorari", "paidCfrRequestRate"),
        ("certiorari", "certiorariAdmissionRate"),
        ("emergency", "emergencyStayDocketRate"),
        ("emergency", "emergencyGrantRate"),
        ("complaint_referral", "admissionRate"),
        ("lower_court_compliance", "lowerCourtCompliance"),
        ("lower_court_compliance", "governmentNoncomplianceRate"),
        ("complaint_referral", "constitutionalRemandRate"),
        ("override_remand", "overrideAttemptRate"),
    ]
    by_key = {(row["pathway"], row["simulatorMetric"]): row for row in read_pathway_dashboard_rows()}
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Pathway-specific validation dashboard}",
        "\\label{tab:pathway-validation}",
        "\\Description{Table separating certiorari, emergency, complaint/referral, lower-court compliance, and override/remand validation denominators with source tiers and next validation actions.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.95in}>{\\raggedright\\arraybackslash}p{1.25in}>{\\raggedright\\arraybackslash}p{1.12in}r>{\\raggedright\\arraybackslash}p{1.1in}>{\\raggedright\\arraybackslash}p{1.0in}>{\\raggedright\\arraybackslash}p{1.5in}}",
        "\\toprule",
        "Pathway & Construct & Sim. metric & Current & Source metric & Evidence & Next action \\\\",
        "\\midrule",
    ]
    for key in selected:
        row = by_key[key]
        lines.append(
            f"{tex_escape(row['pathway'].replace('_', ' '))} & "
            f"{tex_escape(row['construct'])} & "
            f"{tex_escape(humanize_identifier(row['simulatorMetric']))} & "
            f"{row['currentLikeValue']} & "
            f"{tex_escape(humanize_identifier(row['sourceMetric']))} & "
            f"{tex_escape(row['sourceTier'].replace('_', ' '))} & "
            f"{tex_escape(row['nextValidationAction'])} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "pathway_validation.tex").write_text("\n".join(lines))


def read_mechanism_rows() -> list[dict[str, str]]:
    with MECHANISM_CSV.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_mechanism_summary() -> None:
    fields = [
        "deltaDirectional",
        "deltaRightsProtection",
        "deltaShadowDocketAbuse",
        "deltaLowerCourtCompliance",
        "deltaLowerCourtResistanceRisk",
        "deltaEnforcementCapacity",
        "deltaGovernmentNoncomplianceRate",
        "deltaEmergencyOpportunism",
        "deltaEmergencyDownstreamEffect",
        "deltaPrecedentDurability",
        "deltaAdministrativeCost",
    ]
    selected = [
        "emergency-restraint",
        "written-emergency-reasoning",
        "automatic-merits-follow-up",
        "strong-recusal-enforcement",
        "randomized-merits-panels",
        "constitutional-remand",
        "public-interest-filter",
        "override-window",
        "jurisdiction-stripping-constraints",
        "emergency-integrity-bundle",
        "remand-override-window-bundle",
        "panel-jurisdiction-safeguards",
        "council-concrete-hybrid",
    ]
    totals: dict[str, defaultdict[str, float]] = defaultdict(lambda: defaultdict(float))
    weights: dict[str, float] = defaultdict(float)
    names: dict[str, str] = {}
    for row in read_mechanism_rows():
        key = row["mechanismKey"]
        names[key] = row["mechanism"]
        weight = float(row.get("caseWeight") or 1.0)
        weights[key] += weight
        for field in fields:
            totals[key][field] += float(row[field]) * weight

    def average(key: str, field: str) -> float:
        return totals[key][field] / weights[key]

    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Mechanism-level paired contrasts against the current-like design}",
        "\\label{tab:mechanism-summary}",
        "\\Description{Table of weighted average paired contrasts for emergency-procedure, recusal, pipeline, remand, public-interest, override, and bundled institutional mechanisms across campaign assumption cases.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.45in}rrrrrrrrrrrr}",
        "\\toprule",
        "Mechanism & Score & Rights & Shadow & Lower ct. & LC resist. & Enforce. & Gov. noncomp. & Emerg. opp. & Emerg. down. & Prec. dur. & Cost \\\\",
        "\\midrule",
    ]
    for key in selected:
        lines.append(
            f"{tex_escape(names[key])} & "
            f"{average(key, 'deltaDirectional'):+.3f} & "
            f"{average(key, 'deltaRightsProtection'):+.3f} & "
            f"{average(key, 'deltaShadowDocketAbuse'):+.3f} & "
            f"{average(key, 'deltaLowerCourtCompliance'):+.3f} & "
            f"{average(key, 'deltaLowerCourtResistanceRisk'):+.3f} & "
            f"{average(key, 'deltaEnforcementCapacity'):+.3f} & "
            f"{average(key, 'deltaGovernmentNoncomplianceRate'):+.3f} & "
            f"{average(key, 'deltaEmergencyOpportunism'):+.3f} & "
            f"{average(key, 'deltaEmergencyDownstreamEffect'):+.3f} & "
            f"{average(key, 'deltaPrecedentDurability'):+.3f} & "
            f"{average(key, 'deltaAdministrativeCost'):+.3f} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "mechanism_summary.tex").write_text("\n".join(lines))


def main() -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    averages = read_weighted_averages()
    write_conflict_confidence_tradeoff(averages)
    write_emergency_profile(averages)
    write_domain_claimant_success(averages)
    write_selected_campaign_table(averages)
    write_litigation_pipeline_table(averages)
    write_calibration_guardrails()
    write_calibration_classification_table()
    write_uncertainty_bands(averages)
    write_sampled_prior_uncertainty_table()
    write_sensitivity_drivers_table()
    write_pathway_validation_table()
    write_mechanism_summary()


if __name__ == "__main__":
    main()
