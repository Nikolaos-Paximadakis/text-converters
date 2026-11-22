"""Check the built wheel and sdist before they are published.

Usage: python scripts/check_dist.py DIST_DIR [--tag vX.Y.Z]

Fails (exit 1) when a file is missing from either archive, or when the version in
pyproject.toml, text_converters.__version__, the archive names and the release tag
(if given) disagree.
"""

import argparse
import re
import sys
import tarfile
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PACKAGE_FILES = (
    "text_converters/__init__.py",
    "text_converters/character_converters.py",
    "text_converters/py.typed",
)
SDIST_FILES = (*PACKAGE_FILES, "LICENSE", "README.md", "pyproject.toml", "PKG-INFO")


def project_versions() -> tuple[str, str]:
    with (ROOT / "pyproject.toml").open("rb") as f:
        pyproject_version = str(tomllib.load(f)["project"]["version"])
    init = (ROOT / "text_converters" / "__init__.py").read_text(encoding="utf-8")
    match = re.search(r'^__version__ = "([^"]+)"', init, re.MULTILINE)
    if match is None:
        raise SystemExit("__version__ not found in text_converters/__init__.py")
    return pyproject_version, match.group(1)


def check(dist: Path, tag: str | None) -> list[str]:
    problems: list[str] = []
    pyproject_version, init_version = project_versions()
    if pyproject_version != init_version:
        problems.append(
            f"pyproject.toml has {pyproject_version}, __version__ is {init_version}"
        )
    if tag is not None and tag != f"v{pyproject_version}":
        problems.append(f"tag {tag} does not match version v{pyproject_version}")

    wheels = sorted(dist.glob("text_converters-*.whl"))
    sdists = sorted(dist.glob("text_converters-*.tar.gz"))
    if len(wheels) != 1 or len(sdists) != 1:
        return [*problems, f"expected one wheel and one sdist in {dist}"]
    wheel, sdist = wheels[0], sdists[0]
    problems += [
        f"{archive.name} is not version {pyproject_version}"
        for archive in (wheel, sdist)
        if f"-{pyproject_version}" not in archive.name
    ]

    with zipfile.ZipFile(wheel) as zf:
        names = set(zf.namelist())
        problems += [f"wheel lacks {n}" for n in PACKAGE_FILES if n not in names]
        if not any(n.endswith(".dist-info/licenses/LICENSE") for n in names):
            problems.append("wheel lacks the LICENSE file")
        metadata_name = next(n for n in names if n.endswith(".dist-info/METADATA"))
        metadata = zf.read(metadata_name).decode("utf-8")
        for field in ("License-Expression: MIT", "Requires-Python: >=3.11"):
            if field not in metadata:
                problems.append(f"wheel METADATA lacks '{field}'")

    with tarfile.open(sdist) as tf:
        prefix = sdist.name.removesuffix(".tar.gz") + "/"
        names = {m.name.removeprefix(prefix) for m in tf.getmembers()}
        problems += [f"sdist lacks {n}" for n in SDIST_FILES if n not in names]
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dist", type=Path)
    parser.add_argument("--tag")
    args = parser.parse_args()
    problems = check(args.dist, args.tag)
    for problem in problems:
        print(f"ERROR: {problem}", file=sys.stderr)
    if not problems:
        print(f"{args.dist}: wheel and sdist complete, versions consistent")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
