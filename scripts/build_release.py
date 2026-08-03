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
import tempfile

ROOT = Path(__file__).resolve().parent.parent
DIST = ROOT / "dist"
PYPROJECT = ROOT / "pyproject.toml"

EXAMPLES_DIR = ROOT / "examples"
EXAMPLES_OUTPUT = "berrywave_edi_examples"
SAMPLE_DATA_DIR = ROOT / "sample_data"
OUTPUT_DATA_DIR = ROOT / "output"

BENCHMARKS_DIR = ROOT / "benchmarks"
BENCHMARK_DATA_DIR = ROOT / "benchmark_data"
BENCHMARKS_OUTPUT = "berrywave_edi_benchmarks"


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


def find_wheel() -> Path:
    """Find the generated wheel."""

    wheels = list(DIST.glob("*.whl"))

    if len(wheels) != 1:
        raise RuntimeError(
            f"Expected one wheel, found {len(wheels)}"
        )

    return wheels[0]


def add_directory_to_zip(
        archive,
        directory,
        output_name,
        version):
    """Add a directory tree to an archive."""

    if not directory.exists():
        return

    for file in directory.rglob("*"):

        if not file.is_file():
            continue

        if "__pycache__" in file.parts:
            continue

        if file.suffix == ".pyc":
            continue

        relative_path = file.relative_to(ROOT)

        archive.write(
            file,
            arcname=Path(
                f"{output_name}-{version}"
            ) / relative_path,
        )


def build_examples(version: str):
    """Create the examples archive."""

    archive_name = f"{EXAMPLES_OUTPUT}-{version}.zip"
    archive_path = DIST / archive_name

    print(f"Building examples archive ({archive_name}) ...")

    with zipfile.ZipFile(
            archive_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        add_directory_to_zip(
            archive,
            EXAMPLES_DIR,
            EXAMPLES_OUTPUT,
            version,
        )

        add_directory_to_zip(
            archive,
            SAMPLE_DATA_DIR,
            EXAMPLES_OUTPUT,
            version,
        )

        add_directory_to_zip(
            archive,
            OUTPUT_DATA_DIR,
            EXAMPLES_OUTPUT,
            version,
        )

    print(f"Created {archive_path}")


def build_benchmarks(version: str):
    """Create the benchmarks archive."""

    archive_name = f"{BENCHMARKS_OUTPUT}-{version}.zip"
    archive_path = DIST / archive_name

    print(f"Building benchmarks archive ({archive_name}) ...")

    with zipfile.ZipFile(
            archive_path,
            "w",
            compression=zipfile.ZIP_DEFLATED,
    ) as archive:
        add_directory_to_zip(
            archive,
            BENCHMARKS_DIR,
            BENCHMARKS_OUTPUT,
            version,
        )

        add_directory_to_zip(
            archive,
            BENCHMARK_DATA_DIR,
            BENCHMARKS_OUTPUT,
            version,
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


def verify_release():
    """Install the wheel in a clean virtual environment and test import."""

    print("Verifying wheel installation ...")

    wheel = find_wheel()

    with tempfile.TemporaryDirectory() as temp_dir:

        venv = Path(temp_dir) / ".venv"

        subprocess.run(
            [
                "python",
                "-m",
                "venv",
                str(venv),
            ],
            check=True,
        )

        if Path("/usr/bin/python3").exists():
            python = venv / "bin" / "python"
        else:
            python = venv / "bin" / "python"

        subprocess.run(
            [
                str(python),
                "-m",
                "pip",
                "install",
                str(wheel),
            ],
            check=True,
        )

        subprocess.run(
            [
                str(python),
                "-c",
                "import berrywave; print('Import successful')",
            ],
            check=True,
        )

    print("Wheel verification successful.")


def main():
    version = read_version()

    banner(version)

    clean_dist()

    build_wheel()

    build_examples(version)

    build_benchmarks(version)

    verify_release()

    list_artifacts()

    print("Release build completed successfully.")


if __name__ == "__main__":
    main()
