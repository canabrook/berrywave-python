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
import zipfile

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
PYPROJECT = ROOT / "pyproject.toml"

EXAMPLES_DIR = ROOT / "examples"
EXAMPLES_OUTPUT = "berrywave_edi_examples"


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

    archive_name = f"{EXAMPLES_OUTPUT}-{version}.zip"
    archive_path = DIST / archive_name

    print(f"Building examples archive ({archive_name}) ...")

    if not EXAMPLES_DIR.exists():
        raise RuntimeError(
            f"Examples directory not found: {EXAMPLES_DIR}"
        )

    with zipfile.ZipFile(
            archive_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
    ) as archive:

        for file in EXAMPLES_DIR.rglob("*"):

            if file.is_file():
                relative_path = file.relative_to(ROOT)

                archive.write(
                    file,
                    arcname=Path(
                        f"{EXAMPLES_OUTPUT}-{version}"
                    ) / relative_path
                )

    print(f"Created {archive_path}")


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
