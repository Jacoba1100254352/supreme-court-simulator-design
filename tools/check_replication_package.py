#!/usr/bin/env python3
"""Verify that a clean copied source tree can rebuild core artifacts."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {
    ".git",
    ".idea",
    "dist",
    "out",
    "build",
    "__pycache__",
}


def candidate_files() -> list[Path]:
    try:
        output = subprocess.check_output(
            ["git", "ls-files", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            text=True,
        )
    except subprocess.CalledProcessError as exception:
        raise SystemExit("Unable to list repository files for replication check") from exception
    files: list[Path] = []
    for line in output.splitlines():
        if not line.strip():
            continue
        path = ROOT / line
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if path.name == ".DS_Store" or any(part in EXCLUDED_PARTS for part in relative.parts):
            continue
        files.append(path)
    return files


def copy_tree(destination: Path) -> None:
    for path in candidate_files():
        relative = path.relative_to(ROOT)
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)


def run(command: list[str], cwd: Path) -> None:
    print("Running " + " ".join(command))
    subprocess.run(command, cwd=cwd, check=True)


def main() -> None:
    with tempfile.TemporaryDirectory(prefix="constitutional-review-replication-") as temp:
        checkout = Path(temp) / "repo"
        checkout.mkdir()
        copy_tree(checkout)
        run(["make", "test"], checkout)
        run(["make", "validation-dashboards"], checkout)
        run(["make", "paper-strict-check"], checkout)
        run(["make", "replication-package"], checkout)
        archive = checkout / "dist" / "constitutional-review-replication.zip"
        manifest = checkout / "dist" / "replication-package-manifest.json"
        if not archive.exists() or not manifest.exists():
            raise SystemExit("Replication package outputs were not created in clean copied tree")
        print("Clean copied-tree replication check passed.")


if __name__ == "__main__":
    main()
