#!/usr/bin/env python3
"""Validate independently returned human coding forms without altering source data."""

import argparse
from collections import Counter
from datetime import date
import json
from pathlib import Path

from prepare_expert_review import ADJUDICATION_FIELDS, HUMAN_FIELDS, REVIEW, ROOT, keyed, read_csv

TREATMENTS = {"followed", "applied", "distinguished", "narrowed", "questioned_or_resisted", "cited_context_only", "unclear"}
REMEDIES = {"full", "partial", "narrow", "symbolic", "resistant", "not_assessable", "not_applicable"}


def validate_date(value: str) -> None:
    parsed = date.fromisoformat(value)
    if parsed.isoformat() != value:
        raise ValueError("Human coding dates must use YYYY-MM-DD")
    if parsed > date.today():
        raise ValueError("Human coding date is in the future")


def validate_return(rows, expected, adjudication=False):
    if not expected:
        raise ValueError("An empty template cannot establish legal coding completion")
    indexed = keyed(rows, "reviewId")
    template = keyed(expected, "reviewId")
    if set(indexed) != set(template):
        raise ValueError("Return must preserve every packet row; leave unreviewed rows blank")
    completed = {}
    fields = ADJUDICATION_FIELDS if adjudication else HUMAN_FIELDS
    for rid, row in indexed.items():
        if set(row) != set(template[rid]):
            raise ValueError(f"Return schema changed: {rid}")
        for field, value in template[rid].items():
            if field not in fields and row[field] != value:
                raise ValueError(f"Source identity/context changed: {rid} {field}")
        if not any(row[field].strip() for field in fields):
            continue
        if row["humanCompleted"] != "yes":
            raise ValueError(f"Explicit human completion declaration required: {rid}")
        required = fields if adjudication else [field for field in fields if field != "uncertaintyNotes"]
        if any(not row[field].strip() for field in required):
            raise ValueError(f"Incomplete coding, identity, date or evidence fields: {rid}")
        identity_field = "adjudicatorId" if adjudication else "coderId"
        if row[identity_field] != row[identity_field].strip():
            raise ValueError(f"Coder IDs must not contain surrounding whitespace: {rid}")
        treatment = row["finalTreatment"] if adjudication else row["treatment"]
        if treatment not in TREATMENTS:
            raise ValueError(f"Unrecognized treatment: {rid}")
        validate_date(row["adjudicatedDate"] if adjudication else row["codedDate"])
        if not adjudication:
            if row["fullTextReviewed"] not in {"yes", "no"}:
                raise ValueError(f"Specify fullTextReviewed yes/no: {rid}")
            if row["fullTextReviewed"] == "no" and treatment != "unclear":
                raise ValueError(f"Directional/citation judgment requires full-text review: {rid}")
            if treatment == "unclear" and not row["uncertaintyNotes"].strip():
                raise ValueError(f"Unclear judgment needs an uncertainty reason: {rid}")
            if row["opinionRole"] not in {"majority", "plurality", "concurrence", "dissent", "order", "combined", "unclear"}:
                raise ValueError(f"Unrecognized opinion role: {rid}")
            if row["confidence"] not in {"high", "medium", "low"} or row["remedyFidelity"] not in REMEDIES:
                raise ValueError(f"Unrecognized confidence or remedy value: {rid}")
        completed[rid] = row
    ids = {row["adjudicatorId"] if adjudication else row["coderId"] for row in completed.values()}
    if len(ids) > 1:
        raise ValueError("Each return must belong to one pseudonymous human coder")
    return completed


def agreement(a, b):
    paired = sorted(set(a) & set(b))
    matrix = Counter((a[rid]["treatment"], b[rid]["treatment"]) for rid in paired)
    count = len(paired)
    matches = sum(left == right for rid in paired for left, right in [(a[rid]["treatment"], b[rid]["treatment"])])
    observed = matches / count if count else None
    kappa = None
    if count >= 2:
        left = Counter(a[rid]["treatment"] for rid in paired)
        right = Counter(b[rid]["treatment"] for rid in paired)
        expected = sum(left[label] * right[label] for label in TREATMENTS) / (count * count)
        if expected < 1:
            kappa = (observed - expected) / (1 - expected)
    return {"pairedRows": count, "agreedRows": matches, "rawAgreement": observed, "cohenKappa": kappa, "kappaNote": "null when fewer than two pairs or marginals are degenerate; selected packet only", "confusionMatrix": [{"reviewerA": left, "reviewerB": right, "rows": n} for (left, right), n in sorted(matrix.items())], "disagreementIds": [rid for rid in paired if a[rid]["treatment"] != b[rid]["treatment"]]}


def summarize(a_rows, b_rows, template, adjudication_rows=None, adjudication_template=None):
    a = validate_return(a_rows, template)
    b = validate_return(b_rows, template)
    if a and b and {row["coderId"] for row in a.values()} & {row["coderId"] for row in b.values()}:
        raise ValueError("Independent coder IDs must differ")
    result = agreement(a, b)
    adjudicated = validate_return(adjudication_rows, adjudication_template, True) if adjudication_rows is not None else {}
    if any(rid not in a or rid not in b for rid in adjudicated):
        raise ValueError("Adjudication requires both independent human returns")
    for rid, row in adjudicated.items():
        if row["adjudicatorId"] in {a[rid]["coderId"], b[rid]["coderId"]}:
            raise ValueError("Use a distinct adjudicator for this packet")
        if row["adjudicatedDate"] < max(a[rid]["codedDate"], b[rid]["codedDate"]):
            raise ValueError("Adjudication predates the independent returns")
    result.update({"expectedRows": len(template), "reviewerACompleted": len(a), "reviewerBCompleted": len(b), "adjudicatedRows": len(adjudicated), "legalCodingComplete": len(a) == len(b) == len(adjudicated) == len(template), "humanIdentityVerification": "self-declared; coordinator must verify qualifications and independence", "methodsSignoff": "not supplied by this coding validator", "interpretation": "Reliability describes this purposive enriched packet; it is not population accuracy or validation of simulator compliance."})
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--reviewer-a", type=Path, required=True)
    parser.add_argument("--reviewer-b", type=Path, required=True)
    parser.add_argument("--adjudication", type=Path)
    args = parser.parse_args()
    template = read_csv(ROOT, REVIEW + "reviewer-a-template.csv")
    adjudication = read_csv(ROOT, REVIEW + "adjudication-template.csv")
    result = summarize(read_csv(args.reviewer_a.parent, args.reviewer_a.name), read_csv(args.reviewer_b.parent, args.reviewer_b.name), template, read_csv(args.adjudication.parent, args.adjudication.name) if args.adjudication else None, adjudication)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
