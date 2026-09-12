"""Test review isolation, missingness semantics, and real return-validation failures."""

from copy import deepcopy
from pathlib import Path
import sys
import tempfile
import unittest
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from prepare_expert_review import ADJUDICATION_FIELDS, HUMAN_FIELDS, REVIEW, ROOT, applicable, csv_bytes, prepare, protect_completed_forms, read_csv, substantive, write_archives
from review_coding_returns import agreement, summarize, validate_return


class ExpertReviewTests(unittest.TestCase):
    def template(self):
        return [{"reviewId": "E001", "sourceRecordId": "source:1"} | {field: "" for field in HUMAN_FIELDS}]

    def returned(self, coder="reader-A", treatment="applied"):
        rows = self.template()
        rows[0].update({"coderId": coder, "humanCompleted": "yes", "codedDate": "2026-07-26", "fullTextReviewed": "yes", "treatment": treatment, "opinionRole": "majority", "proposition": "fixture rule", "sourceLocator": "fixture p. 1", "rationale": "fixture explanation", "confidence": "medium", "remedyFidelity": "not_assessable"})
        return rows

    def test_blank_forms_never_count_as_signoff(self):
        result = summarize(self.template(), self.template(), self.template())
        self.assertEqual(result["pairedRows"], 0)
        self.assertIsNone(result["rawAgreement"])
        self.assertFalse(result["legalCodingComplete"])

    def test_human_declaration_sources_and_independence_required(self):
        for field, value in [("humanCompleted", "no"), ("sourceLocator", ""), ("sourceRecordId", "wrong"), ("fullTextReviewed", "no"), ("coderId", " reader-A"), ("codedDate", "20260726"), ("codedDate", "2999-01-01"), ("treatment", "invented")]:
            rows = self.returned()
            rows[0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate_return(rows, self.template())
        with self.assertRaises(ValueError):
            summarize(self.returned(), self.returned(), self.template())
        with self.assertRaises(ValueError):
            summarize([], [], [])

    def test_adjudication_requires_complete_independent_returns(self):
        template = [{"reviewId": "E001", "sourceRecordId": "source:1"} | {field: "" for field in ADJUDICATION_FIELDS}]
        adjudicated = deepcopy(template)
        adjudicated[0].update({"adjudicatorId": "adjudicator", "humanCompleted": "yes", "adjudicatedDate": "2026-07-27", "finalTreatment": "applied", "sourceLocator": "fixture p. 1", "rationale": "fixture adjudication"})
        a, b = self.returned(), self.returned("reader-B")
        self.assertFalse(summarize(a, b, self.template(), template, template)["legalCodingComplete"])
        self.assertTrue(summarize(a, b, self.template(), adjudicated, template)["legalCodingComplete"])
        for field, value in [("adjudicatorId", "reader-A"), ("adjudicatedDate", "2026-07-25"), ("humanCompleted", "no"), ("sourceLocator", "")]:
            modified = deepcopy(adjudicated)
            modified[0][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                summarize(a, b, self.template(), modified, template)
        with self.assertRaises(ValueError):
            summarize(self.template(), b, self.template(), adjudicated, template)

    def test_regeneration_preserves_accidentally_completed_templates(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            name = REVIEW + "reviewer-a-template.csv"
            path = root / name
            path.parent.mkdir(parents=True)
            blank = csv_bytes(self.template())
            path.write_bytes(blank)
            protect_completed_forms({name: blank}, root)
            returned = csv_bytes(self.returned())
            path.write_bytes(returned)
            with self.assertRaises(ValueError):
                protect_completed_forms({name: blank}, root)
            self.assertEqual(path.read_bytes(), returned)

    def test_agreement_and_degenerate_kappa(self):
        a = {"1": {"treatment": "applied"}, "2": {"treatment": "distinguished"}}
        b = deepcopy(a)
        self.assertEqual(agreement(a, b)["cohenKappa"], 1)
        b["2"]["treatment"] = "applied"
        self.assertEqual(agreement(a, b)["rawAgreement"], 0.5)
        self.assertEqual(agreement(a, b)["cohenKappa"], 0)
        self.assertIsNone(agreement({"1": a["1"], "2": a["1"]}, b)["cohenKappa"])

    def test_placeholder_and_conditional_coverage(self):
        self.assertFalse(substantive("other_or_uncoded"))
        self.assertFalse(substantive("brief filed"))
        self.assertTrue(substantive("no"))
        self.assertFalse(applicable({"cvsgRequested": "no"}, "sgRecommendation"))

    def test_review_archives_do_not_disclose_machine_labels(self):
        outputs, summary = prepare()
        self.assertEqual(summary["reviewPacketRows"], 16)
        self.assertEqual(summary["completedHumanReviews"], 0)
        self.assertEqual(summary["pilotRows"], 40)
        self.assertEqual(summary["cvsgPriorityRows"], 30)
        self.assertEqual(summary["emergencyMatters"], 227)
        self.assertEqual(summary["emergencySourceRows"], 241)
        self.assertEqual(summary["legacyFailuresMatchedInCohort"], 4)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "docs").mkdir()
            for name in ("expert-legal-coding-protocol.md", "evidence-acquisition-priorities.md"):
                (root / "docs" / name).write_bytes((ROOT / "docs" / name).read_bytes())
            write_archives(outputs, root)
            for role in ("reviewer-a", "reviewer-b"):
                with zipfile.ZipFile(root / "dist" / f"expert-legal-coding-{role}-v1.zip") as archive:
                    self.assertEqual(set(archive.namelist()), {"case-cards.md", "coding-protocol.md", "coding-form.csv", "archive-manifest.json"})
                    form = archive.read("coding-form.csv")
                    self.assertNotIn(b"automatedTreatment", form)
                    self.assertNotIn(b"reviewStratum", form)
            self.assertIn(REVIEW + "coordinator-key.csv", outputs)

    def test_malformed_csv_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for payload in ("id,id\n1,2\n", "id,kind\n1\n", "id\n1,2\n"):
                (root / "bad.csv").write_text(payload)
                with self.assertRaises(ValueError):
                    read_csv(root, "bad.csv")


if __name__ == "__main__":
    unittest.main()
