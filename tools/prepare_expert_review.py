#!/usr/bin/env python3
"""Rebuild review forms, semantic coverage, and acquisition queues from frozen inputs.

Never writes into returned-review storage or changes empirical source rows.
Use --check to fail on missing or stale generated artifacts.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import csv
from datetime import date
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
BENCH = "data/benchmarks/"
REVIEW = "data/review/expert-legal-coding-v1/"
REPORT = "reports/"
MISSING = {"", "other_or_uncoded", "uncoded", "unclear", "unknown", "brief filed"}
CHARACTERISTICS = ["petitionerType", "respondentType", "lowerCourt", "lowerCourtOrigin", "issueArea", "specialistCounselFlag", "formerClerkCounselFlag", "allegedSplitFlag", "genuineSplitFlag", "splitDepth", "vehicleQualityObjection", "sgRecommendation", "meritsDecisionDate", "meritsOutcome", "reversalOrVacatur"]
HUMAN_FIELDS = ["coderId", "humanCompleted", "codedDate", "fullTextReviewed", "treatment", "opinionRole", "proposition", "sourceLocator", "rationale", "confidence", "remedyFidelity", "uncertaintyNotes"]
ADJUDICATION_FIELDS = ["adjudicatorId", "humanCompleted", "adjudicatedDate", "finalTreatment", "sourceLocator", "rationale"]


def read_csv(root: Path, relative: str) -> list[dict[str, str]]:
    with (root / relative).open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        fields = reader.fieldnames or []
        if not fields or len(fields) != len(set(fields)):
            raise ValueError(f"Missing or duplicate CSV headers: {relative}")
        rows = list(reader)
    if any(None in row or any(value is None for value in row.values()) for row in rows):
        raise ValueError(f"Ragged CSV record: {relative}")
    return rows


def keyed(rows: list[dict[str, str]], field: str) -> dict[str, dict[str, str]]:
    result = {row[field]: row for row in rows}
    if "" in result or len(result) != len(rows):
        raise ValueError(f"Blank or duplicate primary key: {field}")
    return result


def csv_bytes(rows: list[dict[str, object]], fields: list[str] | None = None) -> bytes:
    text = io.StringIO(newline="")
    writer = csv.DictWriter(text, fieldnames=fields or list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return text.getvalue().encode("utf-8")


def substantive(value: str) -> bool:
    return value.strip().lower() not in MISSING


def applicable(row: dict[str, str], field: str) -> bool:
    if field == "sgRecommendation":
        return row["cvsgRequested"] == "yes"
    if field in {"meritsDecisionDate", "meritsOutcome", "reversalOrVacatur"}:
        return row["grantSetForArgument"] == "yes"
    return True


def stable_order(value: str) -> str:
    return hashlib.sha256(("review-v1:" + value).encode()).hexdigest()


def prepare(root: Path = ROOT) -> tuple[dict[str, bytes], dict[str, object]]:
    outputs: dict[str, bytes] = {}
    inputs: set[str] = set()

    def read(relative):
        inputs.add(relative)
        return read_csv(root, relative)

    def metadata(relative):
        inputs.add(relative)
        return json.loads((root / relative).read_text())

    def csv_output(relative, rows, fields=None):
        outputs[relative] = csv_bytes(rows, fields)

    def text_output(relative, lines):
        # Markdown presentation trims trailing whitespace; source rows and their
        # context fingerprints remain untouched.
        outputs[relative] = ("\n".join(line.rstrip() for line in lines).rstrip() + "\n").encode()

    coverage, petition_queue, integrity = [], [], []
    all_petitions = []
    snapshots = {}
    cohort_by_term = {}
    for term in ("ot2023", "ot2024"):
        relative = BENCH + f"certiorari-docketed-cohort-{term}.csv"
        rows = read(relative)
        manifest = metadata(BENCH + f"certiorari-docketed-cohort-{term}-manifest.json")
        keyed(rows, "docketNumber")
        keyed(rows, "sourceRecordId")
        if len(rows) != manifest["rowCount"] or len(rows) != manifest["expectedRowCount"]:
            raise ValueError(f"Cohort count mismatch: {term}")
        snapshots[term.upper()] = manifest["snapshotDate"]
        cohort_by_term[term.upper()] = keyed(rows, "docketNumber")
        petitions = [row for row in rows if row["petitionType"] == "certiorari"]
        for row in rows:
            for field in ("petitionFiledDate", "cfrDate", "cvsgDate", "dispositionDate", "meritsDecisionDate"):
                if row[field] and date.fromisoformat(row[field]) > date.fromisoformat(manifest["snapshotDate"]):
                    raise ValueError(f"Date beyond frozen snapshot: {term} {row['docketNumber']} {field}")
            if row["responseFiled"] not in {"yes", "no", "waived"}:
                raise ValueError("Unknown response category")
        integrity.append({"dataset": relative, "grain": "one docket", "rows": len(rows), "uniqueKeys": len(rows), "checkStatus": "passed", "snapshotDate": manifest["snapshotDate"]})
        all_petitions.extend(petitions)
        for field in CHARACTERISTICS:
            eligible = [row for row in petitions if applicable(row, field)]
            populated = sum(bool(row[field].strip()) for row in eligible)
            known = sum(substantive(row[field]) for row in eligible)
            coverage.append({"term": term.upper(), "field": field, "denominatorRule": "CVSG-requested certiorari petitions" if field == "sgRecommendation" else "certiorari petitions granted for argument; outcome completion requires docket review" if field in {"meritsDecisionDate", "meritsOutcome", "reversalOrVacatur"} else "all docketed certiorari petitions", "eligibleRows": len(eligible), "populatedRows": populated, "substantivelyCodedRows": known, "placeholderRows": populated - known, "blankRows": len(eligible) - populated, "missingSubstantiveRows": len(eligible) - known, "coverageFraction": f"{known / len(eligible):.6f}" if eligible else "", "snapshotDate": manifest["snapshotDate"]})

    # Pilot selection precedes sorting by work priority and uses no outcome fields.
    pilot = set()
    for term in snapshots:
        for payment in ("paid", "ifp"):
            stratum = [row for row in all_petitions if row["term"] == term and row["paidOrIfp"] == payment]
            pilot.update(row["sourceRecordId"] for row in sorted(stratum, key=lambda row: stable_order(row["sourceRecordId"]))[:10])
    for row in all_petitions:
        missing = [field for field in CHARACTERISTICS if applicable(row, field) and not substantive(row[field])]
        if not missing:
            continue
        tier = "1_cvsg_brief" if row["cvsgRequested"] == "yes" else "2_stratified_pilot" if row["sourceRecordId"] in pilot else "3_remaining_cohort"
        petition_queue.append({"priorityTier": tier, "pilotSelected": "yes" if row["sourceRecordId"] in pilot else "no", "term": row["term"], "docketNumber": row["docketNumber"], "sourceRecordId": row["sourceRecordId"], "sourceUrl": row["sourceUrl"], "paidOrIfp": row["paidOrIfp"], "missingCharacteristics": ";".join(missing), "neededDocuments": "petition; brief in opposition or waiver; lower-court opinion; counsel source dated by filing" + ("; invited SG brief" if row["cvsgRequested"] == "yes" else ""), "codingStatus": "pending_source_and_human_coding", "snapshotDate": snapshots[row["term"]]})
    petition_queue.sort(key=lambda row: (row["priorityTier"], stable_order(row["sourceRecordId"])))
    csv_output(REPORT + "petition-characteristics-coverage-v1.csv", coverage)
    csv_output(REPORT + "petition-characteristics-priority-queue-v1.csv", petition_queue)

    events = read(BENCH + "lower-court-environmental-treatment-events-v1.csv")
    event_index = keyed(events, "sourceRecordId")
    env_manifest = metadata(BENCH + "environmental-implementation-cohort-v1-manifest.json")
    review_rows = read(BENCH + "environmental-directional-treatment-review-queue-v1.csv")
    keyed(review_rows, "sourceRecordId")
    for row in events:
        if not row["postDecisionWindowStart"] <= row["sourceRecordDate"] <= row["postDecisionWindowEnd"]:
            raise ValueError(f"Event outside decision window: {row['sourceRecordId']}")
        if row["opinionStatus"] != "Published":
            raise ValueError("Environmental snapshot includes a nonpublished document")
        if row["fullTextStatus"] == "available" and not row["citationContext"]:
            raise ValueError("Available environmental text lacks retained context")
    integrity.append({"dataset": BENCH + "lower-court-environmental-treatment-events-v1.csv", "grain": "source decision x citing opinion document", "rows": len(events), "uniqueKeys": len(events), "checkStatus": "passed", "snapshotDate": env_manifest["extractionDate"]})
    missing_text = [{key: row[key] for key in ("sourceRecordId", "sourceDecisionKey", "sourceUrl", "citingCaseName", "courtId", "sourceRecordDate", "courtlistenerOpinionType", "fullTextUnavailableReason", "fullTextSourceUrl")} | {"nextAction": "check provider opinion page and official court opinion or docket; record access date and hash; unavailable is not a treatment code", "retrievalStatus": "pending_source_recovery"} for row in events if row["fullTextStatus"] != "available"]
    csv_output(REPORT + "environmental-text-recovery-queue-v1.csv", missing_text)
    blind, coordinator, cards = [], [], []
    ordered = sorted(review_rows, key=lambda row: stable_order(row["sourceRecordId"]))
    decisions = {row["decisionKey"]: row for row in env_manifest["decisions"]}
    for index, prior in enumerate(ordered, 1):
        event = event_index[prior["sourceRecordId"]]
        if prior["citationContext"] != event["citationContext"] or prior["automatedTreatment"] != event["treatmentType"]:
            raise ValueError("Review queue is not aligned with event source")
        if prior["reviewStatus"] != "pending_expert_review" or any(prior[field] for field in ("secondCoderTreatment", "agreement", "adjudicatedTreatment")):
            raise ValueError("Frozen review queue has human values; ingest returns separately and version the packet")
        rid = f"E{index:03}"
        decision = decisions[event["sourceDecisionKey"]]
        record = {"reviewId": rid, "sourceRecordId": event["sourceRecordId"], "sourceDecision": event["caseName"], "sourceCitation": event["decisionCitation"], "citingCaseName": event["citingCaseName"], "sourceUrl": event["sourceUrl"], "fullTextSourceUrl": event["fullTextSourceUrl"], "contextSha256": hashlib.sha256(event["citationContext"].encode()).hexdigest()}
        blind.append(record | {field: "" for field in HUMAN_FIELDS})
        coordinator.append({"reviewId": rid, "sourceRecordId": event["sourceRecordId"], "automatedTreatment": prior["automatedTreatment"], "reviewStratum": prior["reviewStratum"], "codingRule": prior["codingRule"]})
        cards.extend([f"## {rid}: {event['citingCaseName']}", "", f"Source decision: {event['caseName']} ({event['decisionCitation']}); {decision['decisionDate']}.", f"Source decision provider entry: https://www.courtlistener.com/opinion/{decision['courtlistenerOpinionIds'][0]}/", f"Citing document: {event['sourceUrl']}", f"Full text: {event['fullTextSourceUrl']}", f"Court/date/document type: {event['lowerCourt']}; {event['sourceRecordDate']}; {event['courtlistenerOpinionType']}.", "", "Retained context (may combine overlapping snippets or omit qualifying text; verify the full opinion):", "", event["citationContext"], ""])
    for name in ("reviewer-a-template.csv", "reviewer-b-template.csv"):
        csv_output(REVIEW + name, blind)
    csv_output(REVIEW + "coordinator-key.csv", coordinator)
    csv_output(REVIEW + "adjudication-template.csv", [{"reviewId": row["reviewId"], "sourceRecordId": row["sourceRecordId"]} | {field: "" for field in ADJUDICATION_FIELDS} for row in blind])
    text_output(REVIEW + "case-cards.md", ["# Independent legal coding case cards", "", "Read the coding protocol before recording judgments. Automated labels are held in the coordinator packet until independent coding is complete.", "", *cards])

    granted = read(BENCH + "emergency-application-linkage-coded-v1.csv")
    denied = read(BENCH + "emergency-application-denied-linkage-coded-v1.csv")
    source_orders = read(BENCH + "emergency-application-order-extract-shadow-docket-v3-0.csv")
    source_index = keyed(source_orders, "sourceRecordId")
    combined = granted + denied
    keyed(combined, "sourceRecordId")
    if {row["sourceRecordId"] for row in combined} != set(source_index):
        raise ValueError("Emergency granted/denied join does not cover exactly the source order rows")
    grouped = defaultdict(list)
    for row in combined:
        source = source_index[row["sourceRecordId"]]
        if row["term"].removeprefix("OT") != source["term"].removeprefix("OT") or row["docketNumber"] != source["docketNumber"]:
            raise ValueError("Emergency docket join mismatch")
        grouped[(row["term"], row["docketNumber"])].append(row)
    downstream = []
    for (term, docket), rows in sorted(grouped.items()):
        grant = any(row["reliefGranted"] == "1" for row in rows)
        downstream.append({"priorityTier": "1_granted_matter" if grant else "2_denied_or_nonbinary_matter", "term": term, "docketNumber": docket, "sourceRowCount": len(rows), "sourceRecordIds": ";".join(sorted(row["sourceRecordId"] for row in rows)), "sourceUrl": rows[0]["sourceUrl"], "orderEvents": json.dumps([{key: row[key] for key in ("sourceRecordId", "dispositionDate", "applicationClass", "reliefGranted", "dispositionType", "downstreamPolicyStatus")} for row in rows], sort_keys=True, separators=(",", ":")), "externalSourceUrl": "", "externalObservationDate": "", "externalObservationLocator": "", "observedActorAction": "", "policyStatus": "", "sourceSha256": "", "reviewStatus": "pending_external_implementation_evidence", "completionRule": "link external lower-court order or official implementation record to the specific order event; retain date, locator, actor, action and unavailable-source log"})
    downstream.sort(key=lambda row: (row["priorityTier"], row["term"], row["docketNumber"]))
    csv_output(REPORT + "emergency-implementation-priority-queue-v1.csv", downstream)
    integrity.append({"dataset": "emergency granted + denied linkage", "grain": "one source order record", "rows": len(combined), "uniqueKeys": len(combined), "checkStatus": "passed", "snapshotDate": "see source manifests and row notes"})

    legacy = metadata(BENCH + "certiorari-journal-docket-detail-ot2023-manifest.json")
    reconciliation = []
    for failure in legacy["failedFetches"]:
        current = cohort_by_term["OT2023"].get(failure["docketNumber"])
        reconciliation.append({"docketNumber": failure["docketNumber"], "historicalJournalRecordId": failure["sourceRecordId"], "historicalError": failure["error"], "cohortRecordId": current["sourceRecordId"] if current else "", "cohortSourceUrl": current["sourceUrl"] if current else "", "cohortPetitionFiledDate": current["petitionFiledDate"] if current else "", "cohortDisposition": current["certDisposition"] if current else "", "status": "later_cohort_row_available" if current else "retrieval_still_needed", "interpretation": "historical Journal fetch failure remains in its frozen extract; later cohort already provides docket detail; no new network retrieval claimed"})
    csv_output(REPORT + "legacy-docket-recovery-reconciliation-v1.csv", reconciliation)
    csv_output(REPORT + "review-data-integrity-v1.csv", integrity)
    summary = {"sourceSnapshots": snapshots, "certiorariPetitions": len(all_petitions), "petitionQueueRows": len(petition_queue), "pilotRows": len(pilot), "cvsgPriorityRows": sum(row["priorityTier"] == "1_cvsg_brief" for row in petition_queue), "environmentalEvents": len(events), "missingFullText": len(missing_text), "reviewPacketRows": len(blind), "completedHumanReviews": 0, "emergencySourceRows": len(combined), "emergencyMatters": len(downstream), "grantedEmergencyMatters": sum(row["priorityTier"] == "1_granted_matter" for row in downstream), "legacyFailuresMatchedInCohort": sum(row["status"] == "later_cohort_row_available" for row in reconciliation)}
    text_output(REPORT + "review-data-quality-v1.md", ["# Review data quality and evidence priorities", "", "The frozen data pass row-shape, primary-key, decision-window, source-order join, and snapshot-date checks. These checks establish integrity of the stated sources; the substantive coverage gaps below remain open.", "", f"Petition snapshots: {snapshots}. This report does not refresh case outcomes to the preparation date.", "", f"- Petition cohort: {len(all_petitions):,} certiorari rows; {len(petition_queue):,} require characteristics coding.", f"- CVSG first pass: {summary['cvsgPriorityRows']} petitions. Legacy 'brief filed' values contain no recommendation direction.", f"- Pilot: {len(pilot)} petitions, ten per term/payment stratum, selected by a fixed hash without using outcomes. The CVSG priority set is purposive; use the complete cohort or a documented probability sample for prevalence estimates.", f"- Environmental legal packet: {len(blind)} documents; zero completed human reviews. The selected sample is enriched for automated directional candidates and is not a population accuracy estimate.", f"- Public-text recovery queue: {len(missing_text)}/{len(events)} documents. Missingness is nonrandom; do not impute treatment from snippets.", f"- Emergency evidence: {len(combined)} source order rows map to {len(downstream)} distinct term/docket matters, including {summary['grantedEmergencyMatters']} granted matters. All remain queued for external observations.", f"- Historical Journal recovery: {summary['legacyFailuresMatchedInCohort']}/{len(reconciliation)} failed rows match the later closed cohort. Frozen historical failures are preserved as provenance.", "", "## Substantive petition coverage", "", "A populated value such as other_or_uncoded or brief filed does not count as a substantive code. Merits rows use granted-for-argument petitions as a review denominator; pending, consolidated, DIG and missing outcomes need separate docket adjudication. CVSG recommendations use CVSG-requested petitions. All other fields use every certiorari petition.", "", "| Term | Field | Substantive / eligible | Placeholder | Blank |", "|---|---|---:|---:|---:|", *[f"| {row['term']} | {row['field']} | {row['substantivelyCodedRows']} / {row['eligibleRows']} | {row['placeholderRows']} | {row['blankRows']} |" for row in coverage], "", "## Required human decisions", "", "See docs/expert-legal-coding-protocol.md and docs/evidence-acquisition-priorities.md. Human legal classification, opportunity-denominator design, remedy fidelity and methods acceptance remain open. The independent AI review supplies no human signoff.", "", "Reproduce with make expert-review-packet; inspect tools/prepare_expert_review.py or notebooks/review-data-quality.ipynb. Run make expert-review-check to detect stale outputs. Return files belong in ignored data/raw/expert-reviews/, never in generated templates."])
    inputs.update({"tools/prepare_expert_review.py", "tools/review_coding_returns.py", "docs/expert-legal-coding-protocol.md", "docs/evidence-acquisition-priorities.md"})
    manifest = {"packetVersion": "v1", "purpose": "independent human legal coding and evidence acquisition preparation", "humanSignoff": "pending; no human review performed by this build", "summary": summary, "inputs": [{"path": name, "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest()} for name in sorted(inputs)], "outputs": [{"path": name, "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()} for name, payload in sorted(outputs.items())]}
    outputs[REVIEW + "manifest.json"] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
    return outputs, summary


def write_archives(outputs: dict[str, bytes], root: Path = ROOT) -> None:
    dist = root / "dist"
    dist.mkdir(exist_ok=True)
    protocol = (root / "docs/expert-legal-coding-protocol.md").read_bytes()
    for role in ("reviewer-a", "reviewer-b", "coordinator"):
        files = {"coding-protocol.md": protocol, "case-cards.md": outputs[REVIEW + "case-cards.md"]}
        if role == "coordinator":
            files.update({name.removeprefix(REVIEW): payload for name, payload in outputs.items() if name.startswith(REVIEW)})
            files["evidence-acquisition-priorities.md"] = (root / "docs/evidence-acquisition-priorities.md").read_bytes()
        else:
            files["coding-form.csv"] = outputs[REVIEW + role + "-template.csv"]
        manifest = {"role": role, "humanSignoff": "pending", "files": [{"path": name, "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()} for name, payload in sorted(files.items())]}
        files["archive-manifest.json"] = (json.dumps(manifest, indent=2, sort_keys=True) + "\n").encode()
        with zipfile.ZipFile(dist / f"expert-legal-coding-{role}-v1.zip", "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for name, payload in sorted(files.items()):
                info = zipfile.ZipInfo(name, (2026, 5, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                archive.writestr(info, payload)


def protect_completed_forms(outputs: dict[str, bytes], root: Path = ROOT) -> None:
    """Fail before any writes if a reader mistakenly filled a generated template."""
    for name in outputs:
        if not name.startswith(REVIEW) or not name.endswith("-template.csv"):
            continue
        if not (root / name).exists():
            continue
        fields = ADJUDICATION_FIELDS if name.endswith("adjudication-template.csv") else HUMAN_FIELDS
        for row in read_csv(root, name):
            if any(row.get(field, "").strip() for field in fields):
                raise ValueError(f"Preserve completed review fields before regeneration: {name}; move the return to ignored data/raw/expert-reviews/")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs, summary = prepare()
    if not args.check:
        protect_completed_forms(outputs)
    for name, payload in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_bytes() != payload:
                raise SystemExit(f"Missing or stale review artifact: {name}; run make expert-review-packet")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(payload)
    if not args.check:
        write_archives(outputs)
    print(("Verified" if args.check else "Prepared") + " expert review artifacts: " + json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
