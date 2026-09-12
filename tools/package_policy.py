"""Shared file boundary for public analytic and anonymous review archives."""

from pathlib import Path, PurePosixPath
from collections.abc import Callable


EXCLUDED_PARTS = {".git", ".idea", "dist", "out", "build", "__pycache__", ".direnv", ".secrets", "credentials.local"}
PRIVATE_NAMES = {".envrc", ".secrets", ".npmrc", ".netrc", ".pypirc", "id_rsa", "id_ed25519", "credentials.local"}
PRIVATE_SUFFIXES = {".pem", ".key", ".p8", ".p12", ".pfx", ".jks", ".keystore", ".mobileprovision"}


def write_transformed_utf8(source: Path, destination: Path, transform: Callable[[str], str]) -> None:
    """Apply intentional redactions without normalizing frozen source newlines."""
    text = source.read_bytes().decode("utf-8")
    destination.write_bytes(transform(text).encode("utf-8"))


def excluded_name(name: str) -> bool:
    parts = PurePosixPath(name).parts
    return (
        parts[:2] == ("data", "raw")
        or any(part in EXCLUDED_PARTS for part in parts)
        or any(part in PRIVATE_NAMES or part.startswith("credentials.local.") for part in parts)
        or any((part == ".env" or part.startswith(".env.")) and part != ".env.example" for part in parts)
        or PurePosixPath(name).suffix in PRIVATE_SUFFIXES | {".iml", ".pyc", ".class"}
        or PurePosixPath(name).name == ".DS_Store"
    )


def skip_source(path: Path, root: Path) -> bool:
    relative = path.relative_to(root)
    if excluded_name(relative.as_posix()):
        return True
    # Reject links rather than following a link outside the declared input tree.
    if any(parent.is_symlink() for parent in [path, *path.parents] if parent != root and root in parent.parents):
        raise SystemExit(f"Archive source must not be a symbolic link: {relative}")
    return False


def validate_member_name(name: str) -> None:
    parts = PurePosixPath(name).parts
    if not name or "\\" in name or ":" in name or name.startswith("/") or any(p in {".", "..", ""} for p in name.split("/")):
        raise SystemExit(f"Unsafe archive member name: {name!r}")
    if not parts or excluded_name(name):
        raise SystemExit(f"Excluded archive member: {name}")
