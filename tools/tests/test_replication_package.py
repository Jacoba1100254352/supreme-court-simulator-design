"""Regression checks for delivered-archive integrity and public file boundaries."""

import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
import warnings
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import check_replication_package as check
from package_policy import excluded_name, skip_source, write_transformed_utf8


class ArchiveTests(unittest.TestCase):
    def make_archive(self, root, extra=None, corrupt=False, duplicate=False):
        payload = b"frozen analytic input\n"
        entries = [{"path": "data/input.csv", "bytes": len(payload), "sha256": hashlib.sha256(payload).hexdigest()}]
        manifest = {"files": entries, "fileCount": 1, "packageTreeSha256": check.package_tree_sha256(entries), "gitDirty": False, "gitStatusEntryCount": 0, "analyticReproductionScope": "frozen normalized inputs", "sourceAcquisitionScope": "network access"}
        dest = root / "test.zip"
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", UserWarning)
            with zipfile.ZipFile(dest, "w") as archive:
                archive.writestr("data/input.csv", b"tampered" if corrupt else payload)
                if duplicate:
                    archive.writestr("data/input.csv", payload)
                if extra:
                    archive.writestr(extra, b"unmanifested")
                archive.writestr("replication-package-manifest.json", json.dumps(manifest))
        return dest

    def test_manifest_members_and_content_must_match(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(check, "REQUIRED_ARCHIVE_CONTENTS", {"data/input.csv"}):
            root = Path(directory)
            check.check_archive_contents(self.make_archive(root))
            for kwargs in [{"extra": "data/extra.csv"}, {"extra": "../outside.txt"}, {"extra": "data/.env"}, {"corrupt": True}, {"duplicate": True}]:
                with self.subTest(kwargs=kwargs), self.assertRaises(SystemExit):
                    check.check_archive_contents(self.make_archive(root, **kwargs))

    def test_private_files_excluded_and_template_allowed(self):
        for name in ["docs/.env", "data/.env.production", "data/raw/source.txt", "tools/key.pem", "docs/.netrc", "tools/__pycache__/x.pyc", "docs/credentials.local.json"]:
            self.assertTrue(excluded_name(name), name)
        self.assertFalse(excluded_name("docs/.env.example"))
        self.assertFalse(excluded_name("data/benchmarks/input.csv"))

    def test_symbolic_link_not_followed(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            target = root / "source.txt"
            target.write_text("fixture")
            link = root / "linked.txt"
            link.symlink_to(target)
            with self.assertRaises(SystemExit):
                skip_source(link, root)

    def test_text_redaction_preserves_frozen_newlines(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, destination = root / "source.csv", root / "copy.csv"
            payload = b'key,notes\r\n1,"line one\r\nline two"\r\n2,public\n'
            source.write_bytes(payload)
            write_transformed_utf8(source, destination, lambda text: text)
            self.assertEqual(destination.read_bytes(), payload)
            write_transformed_utf8(source, destination, lambda text: text.replace("public", "anonymous"))
            self.assertEqual(destination.read_bytes(), payload.replace(b"public", b"anonymous"))

    def test_split_uploads_must_reconstruct_combined_files(self):
        def write(root, stem, files):
            entries = [{"path": name, "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()} for name, data in sorted(files.items())]
            manifest = {"files": entries, "fileCount": len(entries), "packageTreeSha256": check.package_tree_sha256(entries)}
            path = root / (stem + ".zip")
            with zipfile.ZipFile(path, "w") as archive:
                for name, data in files.items():
                    archive.writestr(name, data)
                archive.writestr(stem + "-manifest.json", json.dumps(manifest))
            return path
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manuscript_files = {"paper/main.tex": b"manuscript"}
            supplement_files = {"data/input.csv": b"evidence"}
            combined = write(root, "anonymous-submission", manuscript_files | supplement_files)
            manuscript = write(root, "anonymous-manuscript", manuscript_files)
            supplement = write(root, "anonymous-supplement", supplement_files)
            check.check_split_archives(combined, manuscript, supplement)
            supplement = write(root, "anonymous-supplement", {"data/input.csv": b"different"})
            with self.assertRaises(SystemExit):
                check.check_split_archives(combined, manuscript, supplement)


if __name__ == "__main__":
    unittest.main()
