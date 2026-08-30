#!/usr/bin/env python3
"""Create an optional immutable source snapshot for the environmental cohort."""

from __future__ import annotations

import hashlib
import json
import zipfile
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw" / "environmental-implementation-cohort"
DIST = ROOT / "dist"
ARCHIVE = DIST / "environmental-implementation-source-snapshot.zip"
MANIFEST = DIST / "environmental-implementation-source-snapshot-manifest.json"
ARCHIVE_PREFIX = "data/raw/environmental-implementation-cohort"
FIXED_TIME = (2026, 5, 1, 0, 0, 0)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def source_tree_sha256(entries: list[dict[str, object]]) -> str:
    payload = "".join(
        f"{row['path']}\t{row['bytes']}\t{row['sha256']}\n" for row in entries
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def source_files() -> list[Path]:
    if not RAW_DIR.exists():
        raise SystemExit(
            "Environmental source cache is missing; run "
            "`make environmental-implementation-cohort` first."
        )
    files = sorted(
        (path for path in RAW_DIR.rglob("*") if path.is_file()),
        key=lambda path: path.relative_to(RAW_DIR).as_posix(),
    )
    if not files:
        raise SystemExit("Environmental source cache contains no files")
    return files


def build_manifest(files: list[Path]) -> dict[str, object]:
    entries = [
        {
            "path": path.relative_to(RAW_DIR).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
        }
        for path in files
    ]
    categories = Counter(
        Path(str(entry["path"])).parts[0] for entry in entries
    )
    return {
        "schemaVersion": "1.0",
        "createdAtUtc": datetime.now(UTC).replace(microsecond=0).isoformat(),
        "archive": ARCHIVE.name,
        "sourceRoot": str(RAW_DIR.relative_to(ROOT)),
        "fileCount": len(entries),
        "totalBytes": sum(int(entry["bytes"]) for entry in entries),
        "categoryCounts": dict(sorted(categories.items())),
        "sourceTreeSha256": source_tree_sha256(entries),
        "files": entries,
        "reproductionScope": (
            "Immutable acquisition snapshot for rerunning the environmental cohort "
            "extractor without refetching cached CourtListener search pages, public "
            "opinion documents, Crossref metadata, or official implementation sources."
        ),
        "licenseBoundary": (
            "The Gurganus article full text is not included. The snapshot contains "
            "CourtListener search metadata and public opinion documents, Crossref "
            "metadata, and official U.S. agency or Federal Register documents."
        ),
        "notes": [
            "This optional archive is separate from the normalized analytic replication package.",
            "Source acquisition can instead be repeated from the public network endpoints with make environmental-implementation-cohort ARGS=\"--refresh\".",
            "Review repository or archive-host redistribution policies before public deposit.",
        ],
    }


def write_archive(files: list[Path], manifest: dict[str, object]) -> None:
    with zipfile.ZipFile(ARCHIVE, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            relative = path.relative_to(RAW_DIR).as_posix()
            info = zipfile.ZipInfo(f"{ARCHIVE_PREFIX}/{relative}", FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
        info = zipfile.ZipInfo(
            "environmental-implementation-source-snapshot-manifest.json",
            FIXED_TIME,
        )
        info.compress_type = zipfile.ZIP_DEFLATED
        archive.writestr(
            info, json.dumps(manifest, indent=2, sort_keys=True) + "\n"
        )


def verify_archive(manifest: dict[str, object]) -> None:
    expected = {
        f"{ARCHIVE_PREFIX}/{entry['path']}": entry["sha256"]
        for entry in manifest["files"]
    }
    with zipfile.ZipFile(ARCHIVE) as archive:
        names = set(archive.namelist())
        missing = set(expected) - names
        if missing:
            raise SystemExit(
                "Environmental source snapshot is missing files: "
                + ", ".join(sorted(missing)[:10])
            )
        for name, expected_hash in expected.items():
            actual = hashlib.sha256(archive.read(name)).hexdigest()
            if actual != expected_hash:
                raise SystemExit(f"Environmental source snapshot hash mismatch: {name}")


def main() -> None:
    DIST.mkdir(parents=True, exist_ok=True)
    files = source_files()
    manifest = build_manifest(files)
    MANIFEST.write_text(
        json.dumps(manifest, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    write_archive(files, manifest)
    verify_archive(manifest)
    print(f"Wrote {ARCHIVE.relative_to(ROOT)}")
    print(f"Wrote {MANIFEST.relative_to(ROOT)}")
    print(
        f"Snapshotted {manifest['fileCount']} files "
        f"({manifest['totalBytes']} bytes)"
    )


if __name__ == "__main__":
    main()
