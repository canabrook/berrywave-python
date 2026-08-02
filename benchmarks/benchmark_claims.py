"""
Benchmark BerryWave EDI to JSON performance using multiple X12 837 files.

Benchmark files must follow this naming pattern:

    837-NxM.edi

where:
    N = number of ST transactions
    M = number of claims per transaction

Example:
    837-100x100.edi

means:
    100 transactions
    100 claims per transaction
    10,000 total claims
"""

from pathlib import Path
from time import perf_counter
import csv
import re
import platform
import importlib.metadata

import jpype
import matplotlib.pyplot as plt

from berrywave import EdiService

PROJECT_ROOT = Path(__file__).resolve().parent.parent

BENCHMARK_DATA = PROJECT_ROOT / "benchmark_data"
OUTPUT_DIR = PROJECT_ROOT / "benchmark_output"

FILE_PATTERN = re.compile(
    r"837-(\d+)-(\d+)\.edi$"
)


def format_bytes(value: int) -> str:
    if value < 1024:
        return f"{value} bytes"

    if value < 1024 * 1024:
        return f"{value / 1024:.1f} KB"

    return f"{value / (1024 * 1024):.1f} MB"


def print_environment():
    print()
    print("Environment")
    print("-----------")
    print(f"Python          : {platform.python_version()}")

    if jpype.isJVMStarted():
        java_version = jpype.java.lang.System.getProperty(
            "java.version"
        )
        print(f"Java            : {java_version}")

    print(
        f"BerryWave SDK   : "
        f"{importlib.metadata.version('berrywave-edi')}"
    )


def find_benchmark_files():
    files = []

    for file in BENCHMARK_DATA.glob("*.edi"):
        print(file.name)
        match = FILE_PATTERN.match(file.name)

        if match:
            print(f"Found benchmark file: {file.name}")
            transactions = int(match.group(1))
            claims_per_transaction = int(match.group(2))

            files.append(
                {
                    "file": file,
                    "transactions": transactions,
                    "claims_per_transaction": claims_per_transaction,
                    "claims": (
                            transactions *
                            claims_per_transaction
                    ),
                }
            )

    return sorted(
        files,
        key=lambda x: x["claims"]
    )


def main():
    OUTPUT_DIR.mkdir(exist_ok=True)

    benchmarks = find_benchmark_files()

    if not benchmarks:
        raise RuntimeError(
            f"No benchmark files found in {BENCHMARK_DATA}"
        )

    print_environment()

    #
    # Start JVM once. Do not include startup time in each conversion.
    #
    start = perf_counter()
    service = EdiService()
    jvm_elapsed = perf_counter() - start

    print()
    print(
        "BerryWave 837 Claims Scaling Benchmark"
    )
    print(
        "-------------------------------------"
    )
    print()
    print(
        f"JVM startup: {jvm_elapsed:.3f} seconds"
    )

    results = []

    for item in benchmarks:
        input_file = item["file"]

        output_file = (
                OUTPUT_DIR /
                f"{input_file.stem}.json"
        )

        input_size = input_file.stat().st_size

        print(input_file.name)
        start = perf_counter()

        service.edi_file_to_json(
            input_file,
            output_file,
        )

        elapsed = perf_counter() - start

        output_size = output_file.stat().st_size

        result = {
            "file": input_file.name,
            "input_bytes": input_size,
            "output_bytes": output_size,
            "claims": item["claims"],
            "seconds": elapsed,
            "mb_per_sec": (
                    input_size /
                    elapsed /
                    (1024 * 1024)
            ),
            "claims_per_sec": (
                    item["claims"] /
                    elapsed
            ),
        }

        results.append(result)

    #
    # Console table
    #
    print()
    print(
        f"{'File':35} "
        f"{'Input':>10} "
        f"{'Output':>10} "
        f"{'Claims':>10} "
        f"{'Seconds':>10} "
        f"{'Claims/sec':>12}"
    )
    print("-" * 95)

    for r in results:
        print(
            f"{r['file']:35} "
            f"{format_bytes(r['input_bytes']):>10} "
            f"{format_bytes(r['output_bytes']):>10} "
            f"{r['claims']:>10,} "
            f"{r['seconds']:>10.3f} "
            f"{r['claims_per_sec']:>12,.0f}"
        )

    #
    # CSV output
    #
    csv_file = OUTPUT_DIR / "claims_benchmark_results.csv"

    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=results[0].keys()
        )
        writer.writeheader()
        writer.writerows(results)

    #
    # Scatter plot
    #
    plt.figure(figsize=(8, 5))

    plt.scatter(
        [r["claims"] for r in results],
        [r["claims_per_sec"] for r in results],
    )

    plt.xlabel("Number of Claims")
    plt.ylabel("Claims per Second")
    plt.title(
        "BerryWave 837 Conversion Scaling"
    )

    plt.grid(True)

    graph_file = OUTPUT_DIR / "claims_scaling.png"

    plt.savefig(
        graph_file,
        bbox_inches="tight",
        dpi=150,
    )

    print()
    print(f"Results CSV : {csv_file}")
    print(f"Graph       : {graph_file}")


if __name__ == "__main__":
    main()
