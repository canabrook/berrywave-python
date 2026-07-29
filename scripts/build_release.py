#!/usr/bin/env python3
"""
Build a BerryWave EDI Python SDK release.

Produces release artifacts in the dist/ directory.

Current artifacts:

    berrywave_edi-<version>-py3-none-any.whl

Future artifacts:

    berrywave_edi_examples-<version>.zip
"""

from pathlib import Path
import shutil
import subprocess
import tomllib

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
PYPROJECT = ROOT / "pyproject.toml"


def read_version() -> str:
    """Read the project version from pyproject.toml."""

    with PYPROJECT.open("rb") as f:
        project = tomllib.load(f)

    return project["project"]["version"]


def clean_dist():
    """Remove previous release artifacts."""

    print("Cleaning dist/ ...")

    if DIST.exists():
        shutil.rmtree(DIST)

    DIST.mkdir()


def build_wheel():
    """Build the Python wheel."""

    print("Building wheel ...")

    subprocess.run(
        ["python", "-m", "build", "--wheel"],
        cwd=ROOT,
        check=True,
    )


def build_examples(version: str):
    """Create the examples archive."""

    print(f"Building examples archive ({version}) ...")

    # TODO
    # berrywave_edi_examples-<version>.zip


def list_artifacts():
    """Display generated release artifacts."""

    print()
    print("Release artifacts")
    print("-----------------")

    for artifact in sorted(DIST.iterdir()):
        size = artifact.stat().st_size
        print(f"{artifact.name:<55} {size:>8,d} bytes")

    print()


def banner(version: str):
    print()
    print("BerryWave Python SDK Release Builder")
    print("====================================")
    print(f"Version : {version}")
    print()


def main():

    version = read_version()

    banner(version)

    clean_dist()

    build_wheel()

    build_examples(version)

    list_artifacts()

    print("Release build completed successfully.")


if __name__ == "__main__":
    main()