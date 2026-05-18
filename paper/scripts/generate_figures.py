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
METRIC_SEMANTICS_CSV = ROOT / "reports" / "metric-semantics-v1.csv"
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
    "rightsPriorityScore",
    "emergencyRestraintScore",
    "democraticResponsivenessPriorityScore",
    "legalStabilityPriorityScore",
    "lowConflictScore",
    "administrativeFeasibilityScore",
    "emergencyProcessIrregularity",
    "processLegitimacyProxy",
    "legalStability",
    "rightsProtection",
    "partisanAlignment",
    "shadowDocketAbuse",
    "emergencyLegitimacyRisk",
    "legitimacy",
    "constitutionalConflict",
    "democraticResponsiveness",
    "administrativeCost",
    "publicConfidence",
    "lowerCourtSplitDepth",
    "genuineLowerCourtSplitRate",
    "lowerCourtIdeologicalDrift",
    "lowerCourtResistanceRisk",
    "eliteAcceptance",
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
    "rightsClaimantSuccess",
    "emergencyRightsClaimantSuccess",
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
    averages = {
        key: {field: totals[key][field] / weights[key] for field in FIELDS}
        for key in totals
    }
    for values in averages.values():
        values.setdefault("emergencyProcessIrregularity", values.get("shadowDocketAbuse", 0.0))
        values.setdefault("processLegitimacyProxy", values.get("publicConfidence", 0.0))
        if not values.get("emergencyProcessIrregularity"):
            values["emergencyProcessIrregularity"] = values.get("shadowDocketAbuse", 0.0)
        if not values.get("processLegitimacyProxy"):
            values["processLegitimacyProxy"] = values.get("publicConfidence", 0.0)
        if not values.get("rightsPriorityScore"):
            values["rightsPriorityScore"] = sum([
                values.get("rightsProtection", 0.0),
                values.get("rightsDomainClaimantSuccess", 0.0),
                values.get("structuralDomainClaimantSuccess", 0.0),
                values.get("lowerCourtCompliance", 0.0),
                1.0 - values.get("governmentNoncomplianceRate", 0.0),
            ]) / 5.0
        if not values.get("emergencyRestraintScore"):
            values["emergencyRestraintScore"] = sum([
                1.0 - values.get("emergencyProcessIrregularity", 0.0),
                1.0 - values.get("emergencyLegitimacyRisk", 0.0),
                1.0 - values.get("emergencyDownstreamEffect", 0.0),
                1.0 - values.get("emergencyOpportunism", 0.0),
                values.get("reasonedEmergencyOrderRate", 0.0),
                values.get("meritsAccelerationRate", 0.0),
            ]) / 6.0
        if not values.get("democraticResponsivenessPriorityScore"):
            values["democraticResponsivenessPriorityScore"] = sum([
                values.get("democraticResponsiveness", 0.0),
                values.get("processLegitimacyProxy", 0.0),
                1.0 - values.get("governmentNoncomplianceRate", 0.0),
                1.0 - values.get("constitutionalConflict", 0.0),
            ]) / 4.0
        if not values.get("legalStabilityPriorityScore"):
            values["legalStabilityPriorityScore"] = sum([
                values.get("legalStability", 0.0),
                values.get("precedentDurability", 0.0),
                values.get("lowerCourtCompliance", 0.0),
                1.0 - values.get("constitutionalConflict", 0.0),
            ]) / 4.0
        if not values.get("lowConflictScore"):
            values["lowConflictScore"] = sum([
                1.0 - values.get("constitutionalConflict", 0.0),
                1.0 - values.get("lowerCourtResistanceRisk", 0.0),
                1.0 - values.get("governmentNoncomplianceRate", 0.0),
                1.0 - values.get("emergencyDownstreamEffect", 0.0),
                values.get("eliteAcceptance", 0.0),
            ]) / 5.0
        if not values.get("administrativeFeasibilityScore"):
            values["administrativeFeasibilityScore"] = sum([
                1.0 - values.get("administrativeCost", 0.0),
                1.0 - values.get("recusalIncentivePressure", 0.0),
                1.0 - values.get("emergencyOpportunism", 0.0),
                values.get("enforcementCapacity", 0.0),
            ]) / 4.0
        if not values.get("emergencyRightsClaimantSuccess"):
            values["emergencyRightsClaimantSuccess"] = values.get("rightsClaimantSuccess", 0.0)
    return averages


def write_model_flow() -> None:
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begingroup",
        "\\setlength{\\unitlength}{1mm}",
        "\\begin{picture}(128,82)",
        "\\scriptsize",
        "\\put(3,62){\\framebox(22,9){Filed universe}}",
        "\\put(28,62){\\framebox(22,9){Access path}}",
        "\\put(53,62){\\framebox(24,9){Admission screen}}",
        "\\put(6,43){\\framebox(20,8){Screen out}}",
        "\\put(31,43){\\framebox(20,8){Settlement}}",
        "\\put(56,43){\\framebox(22,8){Emergency route}}",
        "\\put(83,43){\\framebox(20,8){Merits route}}",
        "\\put(106,43){\\framebox(18,8){Decision}}",
        "\\put(52,24){\\framebox(26,8){Post-decision response}}",
        "\\put(4,6){\\framebox(18,8){Rights}}",
        "\\put(24,6){\\framebox(23,8){Emergency effects}}",
        "\\put(49,6){\\framebox(22,8){Lower courts}}",
        "\\put(73,6){\\framebox(20,8){Noncompliance}}",
        "\\put(95,6){\\framebox(14,8){Conflict}}",
        "\\put(111,6){\\framebox(13,8){Cost}}",
        "\\put(25,66.5){\\vector(1,0){3}}",
        "\\put(50,66.5){\\vector(1,0){3}}",
        "\\put(77,66.5){\\line(1,0){12}}",
        "\\put(89,66.5){\\vector(0,-1){15.5}}",
        "\\put(65,62){\\line(0,-1){11}}",
        "\\put(65,51){\\vector(0,-1){0.1}}",
        "\\put(65,62){\\line(-1,-1){44}}",
        "\\put(21,47){\\vector(-1,0){0.1}}",
        "\\put(65,62){\\line(-2,-1){22}}",
        "\\put(43,51){\\vector(0,-1){0.1}}",
        "\\put(78,47){\\vector(1,0){5}}",
        "\\put(103,47){\\vector(1,0){3}}",
        "\\put(115,43){\\line(0,-1){11}}",
        "\\put(115,32){\\vector(-1,0){37}}",
        "\\put(65,43){\\line(0,-1){11}}",
        "\\put(65,32){\\vector(0,-1){0.1}}",
        "\\put(65,24){\\line(0,-1){10}}",
        "\\put(13,14){\\vector(0,-1){0.1}}",
        "\\put(35,14){\\vector(0,-1){0.1}}",
        "\\put(60,24){\\line(-4,-1){47}}",
        "\\put(65,24){\\line(-3,-1){30}}",
        "\\put(70,24){\\line(-1,-1){10}}",
        "\\put(71,24){\\line(2,-1){12}}",
        "\\put(75,24){\\line(3,-1){29}}",
        "\\put(78,24){\\line(4,-1){39}}",
        "\\tiny",
        "\\put(6,74){\\makebox(0,0)[l]{Shared filed matters enter access, admission, emergency, merits, and implementation stages.}}",
        "\\put(4,34){\\makebox(0,0)[l]{Admission can terminate, settle, route to emergency relief, or transfer to merits.}}",
        "\\put(4,18){\\makebox(0,0)[l]{Implementation feeds rights, emergency effects, compliance, conflict, and cost.}}",
        "\\end{picture}",
        "\\endgroup",
        "",
    ]
    (FIGURE_DIR / "model_flow.tex").write_text("\n".join(lines))


def write_conflict_confidence_tradeoff(averages: dict[str, dict[str, float]]) -> None:
    left, bottom, width, height = 24.0, 16.0, 86.0, 54.0
    x_min, x_max = 0.44, 0.48
    y_min, y_max = 0.38, 0.68
    label_positions = {
        "current-us-like": (105.0, 22.5, "c"),
        "term-limited-balanced": (52.0, 43.5, "r"),
        "mandatory-written-emergency-reasoning": (70.0, 30.0, "l"),
        "automatic-merits-follow-up": (50.0, 59.5, "r"),
        "emergency-restraint-court": (48.0, 70.5, "l"),
        "strong-recusal-enforcement": (98.0, 38.8, "l"),
        "randomized-merits-panels": (98.0, 48.8, "l"),
        "emergency-integrity-package": (94.0, 58.8, "l"),
        "public-interest-litigation-filter": (95.0, 53.5, "l"),
    }
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begingroup",
        "\\setlength{\\unitlength}{1mm}",
        "\\setlength{\\fboxsep}{0.45pt}",
        "\\begin{picture}(128,84)",
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
        shade = 15 + round(clamp01(values["emergencyProcessIrregularity"] / 0.25) * 70)
        color = "red" if key == "current-us-like" else f"black!{shade}"
        marker = 3.1 if key == "current-us-like" else 2.5
        label_x, label_y, anchor = label_positions[key]
        label_color = "red" if key == "current-us-like" else "black"
        if anchor == "r":
            leader_x = label_x + 2.2
        elif anchor == "l":
            leader_x = label_x - 2.2
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
        f"\\put({fmt(left + width / 2.0)},{fmt(3.8)}){{\\makebox(0,0){{Constitutional conflict (lower is better)}}}}",
        f"\\put(11.0,{fmt(bottom + height / 2.0)}){{\\rotatebox{{90}}{{\\makebox(0,0){{Process legitimacy (higher is better)}}}}}}",
        "\\tiny",
        "\\put(45.0,77.0){\\makebox(0,0)[l]{Darker markers = more emergency irregularity; labels are point estimates.}}",
        "\\end{picture}",
        "\\endgroup",
        "",
    ])
    (FIGURE_DIR / "conflict_confidence_tradeoff.tex").write_text("\n".join(lines))


def write_emergency_profile(averages: dict[str, dict[str, float]]) -> None:
    left_label, left_axis, scale = 45.0, 50.0, 70.0
    top, row_gap, bar_gap = 66.0, 7.2, 1.65
    metrics = [
        ("emergencyProcessIrregularity", "Emerg. irregularity", "black!75"),
        ("emergencyLegitimacyRisk", "Emerg. legit. risk", "black!45"),
        ("processLegitimacyProxy", "Process legit.", "black!18"),
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
        (30.0, 74.0, metrics[0][1], metrics[0][2]),
        (79.0, 74.0, metrics[1][1], metrics[1][2]),
        (30.0, 70.2, metrics[2][1], metrics[2][2]),
    ]
    for x, y, label, color in legend_positions:
        lines.extend([
            f"\\put({fmt(x)},{fmt(y)}){{\\color{{{color}}}\\rule{{5.0mm}}{{1.8mm}}}}",
            f"\\put({fmt(x + 7.0)},{fmt(y + 0.3)}){{\\makebox(0,0)[l]{{{label}}}}}",
        ])
    lines.extend([
        "\\put(76.0,1.0){\\makebox(0,0){Raw normalized simulation average}}",
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


def delta_heat_color(value: float, scale_max: float) -> tuple[str, str]:
    shade = 7 + round(clamp01(abs(value) / scale_max) * 70)
    if abs(value) < 0.005:
        return "black!5", "black"
    color = f"black!{shade}" if value > 0 else f"red!{shade}"
    text = "white" if shade >= 52 else "black"
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
    left_label = 43.0
    left = 51.0
    top = 58.0
    cell_step = 12.4
    cell_w = 10.8
    cell_h = 5.2
    row_gap = 7.0
    header_y = 68.0
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begingroup",
        "\\setlength{\\unitlength}{1mm}",
        "\\begin{picture}(128,72)",
        "\\scriptsize",
    ]
    baseline = averages["current-us-like"]
    for col_index, (_field, label) in enumerate(columns):
        x = left + col_index * cell_step
        lines.append(f"\\put({fmt(x + cell_w / 2.0)},{fmt(header_y)}){{\\makebox(0,0){{\\textbf{{{label}}}}}}}")
    for row_index, (key, label) in enumerate(SELECTED_SCENARIOS):
        values = averages[key]
        y = top - row_index * row_gap
        label_color = "red" if key == "current-us-like" else "black"
        lines.append(f"\\put({fmt(left_label)},{fmt(y + cell_h / 2.0)}){{\\makebox(0,0)[r]{{\\color{{{label_color}}}{label}}}}}")
        for col_index, (field, _label) in enumerate(columns):
            value = values[field] - baseline[field]
            x = left + col_index * cell_step
            fill, text = delta_heat_color(value, 0.30)
            lines.extend([
                f"\\put({fmt(x)},{fmt(y)}){{\\color{{{fill}}}\\rule{{{fmt(cell_w)}mm}}{{{fmt(cell_h)}mm}}}}",
                f"\\put({fmt(x + cell_w / 2.0)},{fmt(y + cell_h / 2.0)}){{\\makebox(0,0){{\\color{{{text}}}{value:+.2f}}}}}",
            ])
    lines.extend([
        "\\put(72.0,4.0){\\makebox(0,0){Change from current-like claimant success; black is higher, red is lower.}}",
        "\\end{picture}",
        "\\endgroup",
        "",
    ])
    (FIGURE_DIR / "domain_claimant_success.tex").write_text("\n".join(lines))


def write_selected_campaign_table(averages: dict[str, dict[str, float]]) -> None:
    selected = [
        ("current-us-like", "Stylized current U.S.-like court"),
        ("mandatory-written-emergency-reasoning", "Mandatory written emergency reasoning"),
        ("automatic-merits-follow-up", "Automatic merits follow-up"),
        ("emergency-restraint-court", "No emergency relief without merits review"),
        ("strong-recusal-enforcement", "Independent recusal enforcement with substitutes"),
        ("judicial-electorate-selection", "Judicial electorate selection court"),
        ("randomized-merits-panels", "Randomized merits panels with en banc correction"),
        ("emergency-integrity-package", "Emergency integrity package"),
        ("public-interest-litigation-filter", "Public-interest litigation filter"),
    ]
    fields = [
        "rightsProtection",
        "emergencyProcessIrregularity",
        "emergencyDownstreamEffect",
        "processLegitimacyProxy",
        "lowerCourtCompliance",
        "administrativeCost",
    ]
    tradeoffs = {
        "current-us-like": "Higher claimant success but higher emergency irregularity",
        "mandatory-written-emergency-reasoning": "Transparency gains with modest merits-work shift",
        "automatic-merits-follow-up": "Regularizes emergency relief through merits routing",
        "emergency-restraint-court": "Lowest emergency irregularity; watch claimant routes",
        "strong-recusal-enforcement": "Reduces recusal pressure with substitution costs",
        "judicial-electorate-selection": "Appointment insulation, not emergency reform",
        "randomized-merits-panels": "Access/correction tradeoff through en banc review",
        "emergency-integrity-package": "Broad emergency-process package with higher complexity",
        "public-interest-litigation-filter": "Filters access while preserving public-law claims",
    }
    def movement_label(delta: float, lower_is_better: bool = False) -> str:
        adjusted = -delta if lower_is_better else delta
        if abs(adjusted) < 0.010:
            return "none"
        if adjusted >= 0.050:
            return "large better"
        if adjusted >= 0.010:
            return "small better"
        if adjusted <= -0.050:
            return "large worse"
        return "small worse"

    baseline = averages["current-us-like"]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Selected simulation diagnostics for the emergency-review argument}",
        "\\label{tab:v2-selected}",
        "\\Description{Table of selected simulation averages for rights protection, emergency irregularity, emergency downstream effect, process legitimacy, lower-court compliance, administrative cost, movement labels, and the main tradeoff for each design.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{2.5pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.45in}rrrrrr>{\\raggedright\\arraybackslash}p{0.70in}>{\\raggedright\\arraybackslash}p{0.70in}>{\\raggedright\\arraybackslash}p{2.05in}}",
        "\\toprule",
        "Scenario & Rights & Emerg. irregularity & Emerg. downstream & Process legit. & Lower ct. & Cost & Down. move & Cost move & Main tradeoff \\\\",
        "\\midrule",
    ]
    for key, label in selected:
        values = averages[key]
        cells = " & ".join(fmt3(values[field]) for field in fields)
        downstream_move = movement_label(
            values["emergencyDownstreamEffect"] - baseline["emergencyDownstreamEffect"],
            lower_is_better=True,
        )
        cost_move = movement_label(
            values["administrativeCost"] - baseline["administrativeCost"],
            lower_is_better=True,
        )
        lines.append(
            f"{tex_escape(label)} & {cells} & {tex_escape(downstream_move)} & "
            f"{tex_escape(cost_move)} & {tex_escape(tradeoffs[key])} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\par\\footnotesize Movement labels compare each design with the current-like baseline; no material movement means $|\\Delta|<.010$, small means $.010\\leq|\\Delta|<.050$, and large means $|\\Delta|\\geq.050$.",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "v2_selected.tex").write_text("\n".join(lines))


def write_normative_scores_table(averages: dict[str, dict[str, float]]) -> None:
    selected = [
        ("current-us-like", "Current-like"),
        ("term-limited-balanced", "18-year terms"),
        ("mandatory-written-emergency-reasoning", "Written reasons"),
        ("automatic-merits-follow-up", "Auto merits"),
        ("emergency-restraint-court", "No merits gap"),
        ("strong-recusal-enforcement", "Recusal enforce."),
        ("judicial-electorate-selection", "Judicial electorate"),
        ("randomized-merits-panels", "Random panels"),
        ("emergency-integrity-package", "Integrity package"),
        ("constitutional-remand", "Constitutional remand"),
        ("public-interest-litigation-filter", "Public-interest filter"),
    ]
    fields = [
        ("rightsPriorityScore", "Rights priority"),
        ("emergencyRestraintScore", "Emergency restraint"),
        ("democraticResponsivenessPriorityScore", "Democratic response"),
        ("legalStabilityPriorityScore", "Legal stability"),
        ("lowConflictScore", "Low conflict"),
        ("administrativeFeasibilityScore", "Admin feasibility"),
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[p]",
        "\\centering",
        "\\caption{Multi-objective reading aids under different normative priorities}",
        "\\label{tab:normative-scores}",
        "\\Description{Table reporting alternative synthetic score families for rights priority, emergency restraint, democratic responsiveness, legal stability, low conflict, and administrative feasibility.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.45in}rrrrrr}",
        "\\toprule",
        "Scenario & Rights priority & Emergency restraint & Democratic response & Legal stability & Low conflict & Admin feasibility \\\\",
        "\\midrule",
    ]
    for key, label in selected:
        values = averages[key]
        cells = " & ".join(fmt3(values[field]) for field, _label in fields)
        lines.append(f"{tex_escape(label)} & {cells} \\\\")
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "normative_scores.tex").write_text("\n".join(lines))


def write_emergency_walkthrough_table() -> None:
    selected = [
        ("current-us-like", "Current-like"),
        ("mandatory-written-emergency-reasoning", "Written reasons"),
        ("automatic-merits-follow-up", "Auto merits follow-up"),
        ("emergency-restraint-court", "No emergency merits gap"),
    ]
    rows: dict[str, dict[str, str]] = {}
    with CAMPAIGN_CSV.open(newline="") as handle:
        for row in csv.DictReader(handle):
            if row["caseKey"] == "emergency-application-flood":
                rows[row["scenarioKey"]] = row
    fields = [
        ("emergencyOrderRate", "Emerg. orders"),
        ("reasonedEmergencyOrderRate", "Reasoned orders"),
        ("meritsAccelerationRate", "Merits accel."),
        ("emergencyProcessIrregularity", "Irregularity"),
        ("emergencyDownstreamEffect", "Downstream"),
        ("rightsClaimantSuccess", "Rights claimants"),
        ("emergencyRightsClaimantSuccess", "Emergency-rights claimants"),
        ("lowerCourtCompliance", "Lower ct."),
        ("administrativeCost", "Admin cost"),
        ("processLegitimacyProxy", "Process legit."),
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Emergency-application-flood walkthrough under a shared assumption case}",
        "\\label{tab:emergency-walkthrough}",
        "\\Description{Table comparing current-like, written-reasons, automatic merits follow-up, and no-emergency-merits-gap designs under the emergency-application-flood assumption case, including emergency orders, reasoned orders, merits acceleration, emergency irregularity, downstream effects, rights-claimant success, emergency-rights claimant success, lower-court compliance, administrative cost, and process legitimacy.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.42in}rrrrrrrrrr}",
        "\\toprule",
        "Design & Emerg. orders & Reasoned orders & Merits accel. & Irregularity & Downstream & Rights claimants & Emerg.-rights & Lower ct. & Cost & Process legit. \\\\",
        "\\midrule",
    ]
    for key, label in selected:
        row = rows[key]
        if "emergencyProcessIrregularity" not in row or not row["emergencyProcessIrregularity"]:
            row["emergencyProcessIrregularity"] = row["shadowDocketAbuse"]
        if "processLegitimacyProxy" not in row or not row["processLegitimacyProxy"]:
            row["processLegitimacyProxy"] = row["publicConfidence"]
        if "emergencyRightsClaimantSuccess" not in row or not row["emergencyRightsClaimantSuccess"]:
            row["emergencyRightsClaimantSuccess"] = row["rightsClaimantSuccess"]
        cells = " & ".join(f"{float(row[field]):.3f}" for field, _label in fields)
        lines.append(f"{tex_escape(label)} & {cells} \\\\")
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "emergency_walkthrough.tex").write_text("\n".join(lines))


def write_mechanical_emergent_table() -> None:
    rows = [
        (
            "Written emergency reasons reduce emergency irregularity",
            "Partly coded",
            "Downstream disruption, compliance, and rights outputs",
            "Read with downstream disruption, compliance, and rights outputs",
        ),
        (
            "Automatic merits follow-up reduces merits-displacing emergency relief",
            "Partly coded",
            "Workload, lower-court compliance, and process-legitimacy changes",
            "Read with emergency walkthrough and mechanism table",
        ),
        (
            "No emergency relief without merits review produces the lowest irregularity",
            "Strongly coded",
            "Tradeoff is whether rights claimant success, settlement, or downstream compliance worsens",
            "Treat as design implication plus tradeoff test",
        ),
        (
            "Judicial-electorate selection affects appointment-pressure diagnostics more than emergency outputs",
            "Independent of emergency metric",
            "Emergent if legitimacy/alignment changes without comparable emergency movement",
            "Read as selection-design contrast",
        ),
        (
            "Randomized panels or remand rules have mixed profiles",
            "Weakly coded",
            "Emergent through access, correction, compliance, and administrative-cost channels",
            "Read through access, correction, and implementation channels",
        ),
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Interpretive rules for index and downstream effects}",
        "\\label{tab:mechanical-emergent}",
        "\\Description{Table distinguishing index movement that follows directly from coding from downstream effects that depend on simulated tradeoffs.}",
        "\\footnotesize",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.7in}>{\\raggedright\\arraybackslash}p{1.0in}>{\\raggedright\\arraybackslash}p{2.25in}>{\\raggedright\\arraybackslash}p{2.1in}}",
        "\\toprule",
        "Claim & Coding relationship & Downstream check & Manuscript use \\\\",
        "\\midrule",
    ]
    for claim, mechanical, diagnostic, use in rows:
        lines.append(
            f"{tex_escape(claim)} & {tex_escape(mechanical)} & {tex_escape(diagnostic)} & {tex_escape(use)} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "mechanical_emergent.tex").write_text("\n".join(lines))


def write_non_mechanical_diagnostics_table(averages: dict[str, dict[str, float]]) -> None:
    selected = [
        ("current-us-like", "Current-like"),
        ("mandatory-written-emergency-reasoning", "Written reasons"),
        ("automatic-merits-follow-up", "Auto merits"),
        ("emergency-restraint-court", "No merits gap"),
        ("emergency-integrity-package", "Integrity package"),
    ]

    def downstream_only(values: dict[str, float]) -> float:
        return sum([
            1.0 - values["emergencyDownstreamEffect"],
            values["rightsClaimantSuccess"],
            values["lowerCourtCompliance"],
            1.0 - values["governmentNoncomplianceRate"],
            1.0 - values["administrativeCost"],
        ]) / 5.0

    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Non-mechanical downstream diagnostics for emergency-review reforms}",
        "\\label{tab:non-mechanical-diagnostics}",
        "\\Description{Table comparing reported emergency irregularity with formula ablations and downstream-only diagnostics for selected emergency-review designs.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.35in}rrrrrrrr}",
        "\\toprule",
        "Scenario & Reported irregularity & No reasons credit & No accel. credit & Downstream & Rights claimants & Lower ct. & Gov. noncomp. & Downstream-only \\\\",
        "\\midrule",
    ]
    for key, label in selected:
        values = averages[key]
        no_reasons_credit = clamp01(
            values["emergencyProcessIrregularity"] + 0.08 * values["reasonedEmergencyOrderRate"]
        )
        no_acceleration_credit = clamp01(
            values["emergencyProcessIrregularity"] + 0.07 * values["meritsAccelerationRate"]
        )
        lines.append(
            f"{tex_escape(label)} & "
            f"{fmt3(values['emergencyProcessIrregularity'])} & "
            f"{fmt3(no_reasons_credit)} & "
            f"{fmt3(no_acceleration_credit)} & "
            f"{fmt3(values['emergencyDownstreamEffect'])} & "
            f"{fmt3(values['rightsClaimantSuccess'])} & "
            f"{fmt3(values['lowerCourtCompliance'])} & "
            f"{fmt3(values['governmentNoncomplianceRate'])} & "
            f"{fmt3(downstream_only(values))} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\par\\footnotesize The two ablation columns recalculate the irregularity index with the direct reason-giving or merits-acceleration credit removed from the reported aggregate; the downstream-only score excludes emergency irregularity and process legitimacy.",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "non_mechanical_diagnostics.tex").write_text("\n".join(lines))


def write_process_legitimacy_robustness_table(averages: dict[str, dict[str, float]]) -> None:
    selected = [
        ("current-us-like", "Current-like"),
        ("mandatory-written-emergency-reasoning", "Written reasons"),
        ("automatic-merits-follow-up", "Auto merits"),
        ("emergency-restraint-court", "No merits gap"),
        ("strong-recusal-enforcement", "Recusal enforce."),
        ("emergency-integrity-package", "Integrity package"),
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Process-legitimacy penalty ablations}",
        "\\label{tab:process-legitimacy-robustness}",
        "\\Description{Table recalculating the process-legitimacy index after removing selected emergency irregularity, emergency risk, and partisan-alignment penalty channels, with visible-procedure and implementation-only comparison indices.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.35in}rrrrrr}",
        "\\toprule",
        "Scenario & Reported & No irregularity penalty & Half irregularity penalty & No emergency-risk penalty & No partisan penalty & Implementation-only \\\\",
        "\\midrule",
    ]
    for key, label in selected:
        values = averages[key]
        reported = values["processLegitimacyProxy"]
        no_irregularity = clamp01(reported + 0.24 * values["emergencyProcessIrregularity"])
        half_irregularity = clamp01(reported + 0.12 * values["emergencyProcessIrregularity"])
        no_emergency_risk = clamp01(reported + 0.18 * values["emergencyLegitimacyRisk"])
        no_partisan = clamp01(reported + 0.32 * values["partisanAlignment"])
        implementation_only = sum([
            values["lowerCourtCompliance"],
            values["eliteAcceptance"],
            1.0 - values["governmentNoncomplianceRate"],
            1.0 - values["constitutionalConflict"],
            1.0 - values["administrativeCost"],
        ]) / 5.0
        lines.append(
            f"{tex_escape(label)} & "
            f"{fmt3(reported)} & "
            f"{fmt3(no_irregularity)} & "
            f"{fmt3(half_irregularity)} & "
            f"{fmt3(no_emergency_risk)} & "
            f"{fmt3(no_partisan)} & "
            f"{fmt3(implementation_only)} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\par\\footnotesize Recalculations are aggregate penalty ablations, not new case-level reruns. They test whether the visual process-legitimacy pattern depends mainly on the directly coded emergency and partisan penalty channels.",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "process_legitimacy_robustness.tex").write_text("\n".join(lines))


def write_litigation_pipeline_table(averages: dict[str, dict[str, float]]) -> None:
    selected = [
        ("current-us-like", "Current-like"),
        ("term-limited-balanced", "18-year terms"),
        ("mandatory-written-emergency-reasoning", "Written emergency reasons"),
        ("automatic-merits-follow-up", "Automatic merits follow-up"),
        ("emergency-restraint-court", "No emergency merits gap"),
        ("strong-recusal-enforcement", "Strong recusal enforcement"),
        ("judicial-electorate-selection", "Judicial electorate selection"),
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
        ("current-shadow-abuse", "Emerg. irregularity"),
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


def write_calibration_quality_table() -> None:
    selected = [
        "docket-rights",
        "docket-admin-law",
        "current-merits-transfer",
        "current-invalidation",
        "current-emergency-applications",
        "current-shadow-abuse",
        "current-recusal",
        "emergency-restraint-shadow",
    ]
    rows_by_key = {row["targetKey"]: row for row in read_calibration_rows()}

    def denominator_quality(row: dict[str, str]) -> str:
        guardrail = row["guardrailClass"]
        if guardrail == "strict_validation":
            return "near source denominator"
        if guardrail == "loose_calibration":
            return "broad source range"
        if guardrail == "proxy_sanity_check":
            return "proxy only"
        if guardrail == "mechanism_sanity_check":
            return "mechanism proxy"
        return "design prior"

    def failure_rule(row: dict[str, str]) -> str:
        guardrail = row["guardrailClass"]
        if guardrail == "strict_validation":
            return "outside source range"
        if guardrail == "loose_calibration":
            return "outside broad range"
        if guardrail == "mechanism_sanity_check":
            return "wrong direction"
        if guardrail == "proxy_sanity_check":
            return "proxy warning"
        return "coding review"

    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Calibration-quality audit for selected plausibility checks}",
        "\\label{tab:calibration-quality}",
        "\\Description{Table reporting simulated value, source median, source range width, distance from median, denominator quality, calibration use, and failure rule for selected plausibility checks.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.25in}rrrrr>{\\raggedright\\arraybackslash}p{1.15in}>{\\raggedright\\arraybackslash}p{1.00in}>{\\raggedright\\arraybackslash}p{1.05in}}",
        "\\toprule",
        "Check & Sim. value & Source median & Full range & Range width & Distance & Denominator quality & Use & Failure rule \\\\",
        "\\midrule",
    ]
    for key in selected:
        row = rows_by_key[key]
        observed = float(row["observed"])
        source_median = float(row["sourceMedian"] or 0.0)
        range_min = float(row["min"])
        range_max = float(row["max"])
        range_width = range_max - range_min
        distance = abs(observed - source_median) if row.get("sourceMedian") else 0.0
        lines.append(
            f"{tex_escape(row['target'])} & "
            f"{observed:.3f} & "
            f"{source_median:.3f} & "
            f"{range_min:.3f}--{range_max:.3f} & "
            f"{range_width:.3f} & "
            f"{distance:.3f} & "
            f"{tex_escape(denominator_quality(row))} & "
            f"{tex_escape(row['guardrailClass'].replace('_', ' '))} & "
            f"{tex_escape(failure_rule(row))} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\par\\footnotesize Wide ranges and proxy rows are reported as calibration weaknesses, not as stronger evidence merely because the simulated value falls inside the interval.",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "calibration_quality.tex").write_text("\n".join(lines))


def write_parameter_justification_table() -> None:
    rows = [
        (
            "Admission weights",
            "Certiorari and intake source-register patterns plus model priors",
            "No",
            "partial",
            "overfits cert-like processes if comparative access paths are under-calibrated",
        ),
        (
            "Emergency irregularity",
            "Emergency-procedure theory, shadow-docket scholarship, design prior",
            "No",
            "ablation table",
            "headline movement can be partly mechanical",
        ),
        (
            "Process legitimacy",
            "Procedural-legitimacy theory and process-visibility coding",
            "No",
            "penalty ablations",
            "can inherit emergency-irregularity and partisan-alignment penalties",
        ),
        (
            "Rights and claimant success",
            "Legal-domain profiles and rights-burden coding",
            "No",
            "domain heatmap",
            "claimant success is not identical to rights protection",
        ),
        (
            "Compliance and conflict",
            "Implementation literature, lower-court behavior, proxy rows",
            "No",
            "partial",
            "denominator matches remain weak",
        ),
        (
            "Administrative cost",
            "Institutional-complexity and docket-processing design prior",
            "No",
            "mechanism contrasts",
            "can understate real institutional capacity constraints",
        ),
        (
            "Override/remand behavior",
            "Weak-form and comparative constitutional-design literature",
            "No",
            "partial",
            "cross-jurisdiction comparisons are not direct validation targets",
        ),
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Parameter-justification framework}",
        "\\label{tab:parameter-justification}",
        "\\Description{Table classifying major parameter families by source of discipline, whether coefficients are estimated, sensitivity status, and main risk.}",
        "\\footnotesize",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.35in}>{\\raggedright\\arraybackslash}p{2.05in}>{\\raggedright\\arraybackslash}p{0.45in}>{\\raggedright\\arraybackslash}p{1.05in}>{\\raggedright\\arraybackslash}p{2.10in}}",
        "\\toprule",
        "Parameter family & Source of discipline & Est. & Sensitivity tested? & Main risk \\\\",
        "\\midrule",
    ]
    for family, discipline, estimated, sensitivity, risk in rows:
        lines.append(
            f"{tex_escape(family)} & {tex_escape(discipline)} & {tex_escape(estimated)} & "
            f"{tex_escape(sensitivity)} & {tex_escape(risk)} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "parameter_justification.tex").write_text("\n".join(lines))


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
        "judicial-electorate-selection",
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
        "\\Description{Table reporting sampled-prior 5th, 50th, and 95th percentile bands for directional score, rights protection, emergency irregularity, emergency downstream effect, lower-court compliance, government noncompliance, and constitutional conflict.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.45in}rrrrrrr>{\\raggedright\\arraybackslash}p{1.35in}}",
        "\\toprule",
        "Scenario & Score & Rights & Emerg. irregularity & Emerg. down. & Lower ct. & Gov. noncomp. & Conflict & Interpretation \\\\",
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
            f"{tex_escape(row['interpretation'].replace('front-line cluster', 'leading group'))} \\\\"
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
        ("judicial-electorate-selection", "Judicial electorate selection"),
        ("constitutional-remand", "Constitutional remand"),
    ]
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Simulation scores and uncertainty bands for selected designs}",
        "\\label{tab:uncertainty-bands}",
        "\\Description{Table comparing simulation averages with named-prior uncertainty bands for directional score, emergency irregularity, and constitutional conflict.}",
        "\\footnotesize",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.65in}rrrr}",
        "\\toprule",
        "Scenario & Avg. score & Score 5/50/95 & Irregularity 5/50/95 & Conflict 5/50/95 \\\\",
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
        "}%",
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
        "Prior & Top-cluster design & Score & Rights & Emerg. irregularity & Emerg. down. & Gov. noncomp. & LC resist. & Caveat \\\\",
        "\\midrule",
    ]
    for row in rows:
        lines.append(
            f"{tex_escape(row['priorName'])} & {tex_escape(row['scenario'])} & "
            f"{float(row['directionalScore']):.3f} & {float(row['rightsProtection']):.3f} & "
            f"{float(row['shadowDocketAbuse']):.3f} & {float(row['emergencyDownstreamEffect']):.3f} & "
            f"{float(row['governmentNoncomplianceRate']):.3f} & {float(row['lowerCourtResistanceRisk']):.3f} & "
            f"{tex_escape(row['interpretationRisk'].replace('front-line cluster', 'leading group'))} \\\\"
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
        ("certiorari", "paidCertPetitionShare"),
        ("certiorari", "paidCfrRequestRate"),
        ("certiorari", "certiorariAdmissionRate"),
        ("emergency", "emergencyStayDocketRate"),
        ("emergency", "emergencyGrantConditionalRate"),
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
        "\\caption{Pathway-specific denominator audit}",
        "\\label{tab:pathway-validation}",
        "\\Description{Table separating certiorari, emergency, complaint/referral, lower-court compliance, and override/remand denominators with manuscript-use labels and next validation actions.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{0.86in}>{\\raggedright\\arraybackslash}p{1.08in}>{\\raggedright\\arraybackslash}p{1.18in}r>{\\raggedright\\arraybackslash}p{1.15in}>{\\raggedright\\arraybackslash}p{0.86in}>{\\raggedright\\arraybackslash}p{0.94in}>{\\raggedright\\arraybackslash}p{1.26in}}",
        "\\toprule",
        "Pathway & Construct & Sim. metric & Current & Source metric & Use & Compatibility & Next action \\\\",
        "\\midrule",
    ]
    for key in selected:
        row = by_key[key]
        next_action = row["nextValidationAction"]
        if row["denominatorCompatibility"] == "denominator_mismatch":
            next_action = "validation target needed"
        elif row["denominatorCompatibility"] == "mechanism_proxy":
            next_action = "mechanism proxy"
        elif row["validationUse"] == "proxy_context":
            next_action = "proxy only"
        elif "near" in row["denominatorCompatibility"]:
            next_action = "near match"
        lines.append(
            f"{tex_escape(row['pathway'].replace('_', ' '))} & "
            f"{tex_escape(row['construct'])} & "
            f"{tex_escape(humanize_identifier(row['simulatorMetric']))} & "
            f"{row['currentLikeValue']} & "
            f"{tex_escape(humanize_identifier(row['sourceMetric']))} & "
            f"{tex_escape(row['validationUse'].replace('_', ' '))} & "
            f"{tex_escape(row['denominatorCompatibility'].replace('_', ' '))} & "
            f"{tex_escape(next_action)} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "pathway_validation.tex").write_text("\n".join(lines))


def read_metric_semantics_rows() -> list[dict[str, str]]:
    with METRIC_SEMANTICS_CSV.open(newline="") as handle:
        return list(csv.DictReader(handle))


def write_metric_semantics_table() -> None:
    selected = [
        "paidCertPetitionShare",
        "certiorariAdmissionRate",
        "emergencyGrantConditionalRate",
        "admissionRate",
        "lowerCourtCompliance",
        "governmentNoncomplianceRate",
        "overrideRate",
        "directionalScore",
        "rightsClaimantSuccess",
        "emergencyRightsClaimantSuccess",
        "emergencyProcessIrregularity",
        "processLegitimacyProxy",
        "constitutionalConflict",
    ]
    by_metric = {row["metric"]: row for row in read_metric_semantics_rows()}
    if "emergencyProcessIrregularity" not in by_metric and "shadowDocketAbuse" in by_metric:
        by_metric["emergencyProcessIrregularity"] = {
            **by_metric["shadowDocketAbuse"],
            "metric": "emergencyProcessIrregularity",
            "manuscriptInterpretation": "constructed emergency irregularity index",
        }
    if "emergencyProcessIrregularity" not in by_metric:
        by_metric["emergencyProcessIrregularity"] = {
            "metricFamily": "headline",
            "metric": "emergencyProcessIrregularity",
            "empiricalUse": "synthetic output",
            "denominatorCompatibility": "not empirical target",
            "manuscriptInterpretation": "constructed emergency irregularity index",
        }
    if "processLegitimacyProxy" not in by_metric and "publicConfidence" in by_metric:
        by_metric["processLegitimacyProxy"] = {
            **by_metric["publicConfidence"],
            "metric": "processLegitimacyProxy",
            "manuscriptInterpretation": "constructed process-legitimacy index",
        }
    if "emergencyRightsClaimantSuccess" not in by_metric:
        by_metric["emergencyRightsClaimantSuccess"] = {
            "metricFamily": "rights",
            "metric": "emergencyRightsClaimantSuccess",
            "empiricalUse": "synthetic output",
            "denominatorCompatibility": "simulated emergency rights claimants",
            "manuscriptInterpretation": "claimant success among rights-claimant cases with an emergency route",
        }
    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[p]",
        "\\centering",
        "\\caption{Metric semantics and manuscript use}",
        "\\label{tab:metric-semantics}",
        "\\Description{Table distinguishing empirical source comparisons, synthetic outputs, and reading-aid metrics by denominator or scale.}",
        "\\scriptsize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.12in}>{\\raggedright\\arraybackslash}p{1.42in}>{\\raggedright\\arraybackslash}p{1.02in}>{\\raggedright\\arraybackslash}p{1.12in}>{\\raggedright\\arraybackslash}p{2.55in}}",
        "\\toprule",
        "Family & Metric & Use & Compatibility & Manuscript interpretation \\\\",
        "\\midrule",
    ]
    for metric in selected:
        row = by_metric[metric]
        lines.append(
            f"{tex_escape(row['metricFamily'].replace('_', ' '))} & "
            f"{tex_escape(humanize_identifier(row['metric']))} & "
            f"{tex_escape(row['empiricalUse'].replace('_', ' '))} & "
            f"{tex_escape(row['denominatorCompatibility'].replace('_', ' '))} & "
            f"{tex_escape(row['manuscriptInterpretation'])} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "metric_semantics.tex").write_text("\n".join(lines))


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
        "judicial-electorate-selection",
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

    def movement(value: float, lower_is_better: bool = False) -> str:
        adjusted = -value if lower_is_better else value
        if adjusted >= 0.050:
            return "large improvement"
        if adjusted >= 0.010:
            return "small improvement"
        if adjusted <= -0.050:
            return "large deterioration"
        if adjusted <= -0.010:
            return "small deterioration"
        return "no material movement"

    def mechanism_reading(key: str) -> str:
        if key in {"emergency-restraint", "written-emergency-reasoning", "automatic-merits-follow-up", "emergency-integrity-bundle"}:
            return "emergency-process mechanism"
        if key == "strong-recusal-enforcement":
            return "recusal and process legitimacy"
        if key == "judicial-electorate-selection":
            return "appointment insulation comparison"
        if key in {"constitutional-remand", "override-window", "remand-override-window-bundle"}:
            return "post-decision response mechanism"
        if key in {"randomized-merits-panels", "panel-jurisdiction-safeguards"}:
            return "routing and correction mechanism"
        return "mixed institutional mechanism"

    lines = [
        "% Auto-generated by paper/scripts/generate_figures.py",
        "\\begin{table}[hbt!]",
        "\\centering",
        "\\caption{Mechanism-level paired contrasts, interpreted by movement thresholds}",
        "\\label{tab:mechanism-summary}",
        "\\Description{Table summarizing weighted average paired contrasts as qualitative movement categories for emergency irregularity, emergency downstream effect, rights protection, lower-court compliance, administrative cost, and mechanism reading.}",
        "\\footnotesize",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\resizebox{\\textwidth}{!}{%",
        "\\begin{tabular}{>{\\raggedright\\arraybackslash}p{1.55in}>{\\raggedright\\arraybackslash}p{1.25in}>{\\raggedright\\arraybackslash}p{1.25in}>{\\raggedright\\arraybackslash}p{1.05in}>{\\raggedright\\arraybackslash}p{1.05in}>{\\raggedright\\arraybackslash}p{1.05in}>{\\raggedright\\arraybackslash}p{1.55in}}",
        "\\toprule",
        "Mechanism & Emerg. irregularity & Emerg. downstream & Rights & Lower ct. & Cost & Reading \\\\",
        "\\midrule",
    ]
    for key in selected:
        shadow = average(key, "deltaShadowDocketAbuse")
        downstream = average(key, "deltaEmergencyDownstreamEffect")
        rights = average(key, "deltaRightsProtection")
        lower_court = average(key, "deltaLowerCourtCompliance")
        cost = average(key, "deltaAdministrativeCost")
        lines.append(
            f"{tex_escape(names[key])} & "
            f"{tex_escape(movement(shadow, lower_is_better=True))} ({shadow:+.3f}) & "
            f"{tex_escape(movement(downstream, lower_is_better=True))} ({downstream:+.3f}) & "
            f"{tex_escape(movement(rights))} ({rights:+.3f}) & "
            f"{tex_escape(movement(lower_court))} ({lower_court:+.3f}) & "
            f"{tex_escape(movement(cost, lower_is_better=True))} ({cost:+.3f}) & "
            f"{tex_escape(mechanism_reading(key))} \\\\"
        )
    lines.extend([
        "\\bottomrule",
        "\\end{tabular}",
        "}%",
        "\\par\\footnotesize Thresholds: no material movement is $|\\Delta|<.010$; small movement is $.010\\leq|\\Delta|<.050$; large movement is $|\\Delta|\\geq.050$. Cost deterioration means higher modeled administrative cost.",
        "\\end{table}",
        "",
    ])
    (TABLE_DIR / "mechanism_summary.tex").write_text("\n".join(lines))


def main() -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    TABLE_DIR.mkdir(parents=True, exist_ok=True)
    averages = read_weighted_averages()
    write_model_flow()
    write_conflict_confidence_tradeoff(averages)
    write_emergency_profile(averages)
    write_domain_claimant_success(averages)
    write_selected_campaign_table(averages)
    write_normative_scores_table(averages)
    write_emergency_walkthrough_table()
    write_non_mechanical_diagnostics_table(averages)
    write_process_legitimacy_robustness_table(averages)
    write_mechanical_emergent_table()
    write_litigation_pipeline_table(averages)
    write_calibration_guardrails()
    write_calibration_classification_table()
    write_calibration_quality_table()
    write_parameter_justification_table()
    write_uncertainty_bands(averages)
    write_sampled_prior_uncertainty_table()
    write_sensitivity_drivers_table()
    write_pathway_validation_table()
    write_metric_semantics_table()
    write_mechanism_summary()


if __name__ == "__main__":
    main()
