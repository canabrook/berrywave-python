#!/usr/bin/env python3
"""
Build a BerryWave Python SDK release.

Produces:

    dist/
        berrywave_edi-<version>-py3-none-any.whl
        berrywave_edi_examples-<version>.zip
"""

from pathlib import Path
import shutil
import subprocess
import tomllib
import zipfile

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
PYPROJECT = ROOT / "pyproject.toml"


def read_version() -> str:
    """Read the project version from pyproject.toml."""

    with PYPROJECT.open("rb") as f:
        project = tomllib.load(f)

    return project["project"]["version"]


def clean_dist():
    """Remove any previous release artifacts."""

    if DIST.exists():
        shutil.rmtree(DIST)

    DIST.mkdir()


def build_wheel():
    """Build the wheel."""

    subprocess.run(
        ["python", "-m", "build", "--wheel"],
        cwd=ROOT,
        check=True,
    )


def wheel_file() -> Path:
    wheels = list(DIST.glob("*.whl"))

    if len(wheels) != 1:
        raise RuntimeError("Expected exactly one wheel.")

    return wheels[0]

def build_examples(version: str):
    print(f"Building examples archive {version}...")


def main():

    version = read_version()

    print(f"BerryWave SDK {version}")

    clean_dist()

    build_wheel()

    build_examples(version)

    print("Done.")


if __name__ == "__main__":
    main()
