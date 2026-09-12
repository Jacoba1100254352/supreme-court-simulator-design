"""Regression tests for rendered manuscript length and companion freshness."""

from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "paper/scripts"))
import check_jlc_format as jlc
import check_pdf_freshness as freshness


class ManuscriptDeliveryTests(unittest.TestCase):
    def test_rendered_count_includes_tables_references_and_numbers(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "main.pdf"
            pdf.touch()
            extracted = "Main prose\nTable 1\nObserved rate 0.25\fReferences\nExample Author 2026"
            with patch.object(jlc, "required_tool", return_value="pdftotext"), patch.object(
                jlc.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, stdout=extracted)
            ) as run:
                self.assertEqual(jlc.rendered_word_count(pdf), 11)
                self.assertEqual(run.call_args.args[0], ["pdftotext", "-layout", str(pdf), "-"])

    def test_missing_pdf_does_not_fall_back_to_source_count(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(jlc.subprocess, "run") as run:
            with self.assertRaises(SystemExit):
                jlc.rendered_word_count(Path(directory) / "missing.pdf")
            run.assert_not_called()

    def test_empty_or_failed_extraction_is_not_a_pass(self):
        with tempfile.TemporaryDirectory() as directory:
            pdf = Path(directory) / "main.pdf"
            pdf.touch()
            with patch.object(jlc, "required_tool", return_value="pdftotext"), patch.object(
                jlc.subprocess, "run", return_value=subprocess.CompletedProcess([], 0, stdout=" \n\f")
            ):
                with self.assertRaises(SystemExit):
                    jlc.rendered_word_count(pdf)
            with patch.object(jlc, "required_tool", return_value="pdftotext"), patch.object(
                jlc.subprocess, "run", side_effect=subprocess.CalledProcessError(1, "pdftotext")
            ):
                with self.assertRaises(subprocess.CalledProcessError):
                    jlc.rendered_word_count(pdf)

    def test_rendered_word_limit_boundary(self):
        with patch.object(jlc, "rendered_word_count", return_value=10_000):
            self.assertEqual(jlc.check_rendered_word_limit(Path("fixture.pdf")), 10_000)
        with patch.object(jlc, "rendered_word_count", return_value=10_001):
            with self.assertRaises(SystemExit):
                jlc.check_rendered_word_limit(Path("fixture.pdf"))

    def test_strict_and_anonymous_postbuild_modes_require_rendered_check(self):
        # Use the actual checked-in manuscript structure, but isolate expensive rendering.
        for flag in ["--strict-submission", "--rendered-word-count"]:
            with self.subTest(flag=flag), patch.object(sys, "argv", ["check", flag]), patch.object(
                jlc, "check_domain_heatmap_layout"
            ), patch.object(jlc, "check_conflict_confidence_axis_labels"), patch.object(
                jlc, "check_rendered_conflict_label_layout"
            ), patch.object(jlc, "check_rendered_word_limit", return_value=9_000) as check:
                # Anonymous packages intentionally omit the separate title page.
                if flag == "--strict-submission" and not jlc.TITLE_PAGE.exists():
                    with self.assertRaises(SystemExit):
                        jlc.main()
                else:
                    jlc.main()
                check.assert_called_once_with(jlc.PDF)

    def test_companion_pdf_missing_or_stale_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, pdf = root / "technical-supplement.tex", root / "technical-supplement.pdf"
            source.write_text("fixture")
            with patch.object(freshness, "ROOT", root):
                with self.assertRaises(SystemExit):
                    freshness.check_document(pdf, [source.name])
                pdf.touch()
                os.utime(pdf, (100, 100))
                os.utime(source, (200, 200))
                with self.assertRaises(SystemExit):
                    freshness.check_document(pdf, [source.name])
                os.utime(pdf, (300, 300))
                freshness.check_document(pdf, [source.name])


if __name__ == "__main__":
    unittest.main()
