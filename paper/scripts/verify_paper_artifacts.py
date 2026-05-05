#!/usr/bin/env python3
"""Verify that manuscript artifacts match the report manifests."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
PAPER_LEGISLATIVE_INPUT = "data/external/legislative/simulation-campaign-v21-paper.csv"
MANIFESTS = [
    ROOT / "reports" / "constitutional-review-campaign-v2-manifest.json",
    ROOT / "reports" / "calibration-baseline-manifest.json",
    ROOT / "reports" / "parameter-sweep-v4-manifest.json",
]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message: str) -> None:
    print(f"Paper artifact verification failed: {message}", file=sys.stderr)
    raise SystemExit(1)


def check_manifest(path: Path) -> None:
    if not path.exists():
        fail(f"missing manifest {path.relative_to(ROOT)}")
    data = json.loads(path.read_text())
    command = data.get("javaCommand", "")
    manifest_text = path.read_text()
    local_home_marker = "/" + "Users" + "/"
    if local_home_marker in manifest_text:
        fail(f"{path.name} contains a local absolute path")
    if path.name in {"constitutional-review-campaign-v2-manifest.json", "calibration-baseline-manifest.json"}:
        if "--legislative-input" not in command:
            fail(f"{path.name} was not generated with the paper legislative input contract")
        if PAPER_LEGISLATIVE_INPUT not in command:
            fail(f"{path.name} was not generated with the frozen paper legislative fixture")
    for artifact in data.get("artifacts", []):
        artifact_path = ROOT / artifact["path"]
        if not artifact_path.exists():
            fail(f"missing artifact {artifact['path']} listed by {path.name}")
        actual = sha256(artifact_path)
        expected = artifact["sha256"]
        if actual != expected:
            fail(f"{artifact['path']} hash {actual} does not match manifest {expected}")


def main() -> None:
    for manifest in MANIFESTS:
        check_manifest(manifest)
    print(f"Paper artifact verification passed ({len(MANIFESTS)} manifests).")


if __name__ == "__main__":
    main()
