"""
Benchmark BerryWave EDI to JSON performance using a large X12 837 file.

Measures:
- JVM startup time
- EDI to JSON conversion time
- File sizes
- Claim throughput
"""

from pathlib import Path
from time import perf_counter

from berrywave import EdiService


PROJECT_ROOT = Path(__file__).resolve().parent.parent


def format_bytes(value: int) -> str:
    if value < 1024:
        return f"{value} bytes"

    if value < 1024 * 1024:
        return f"{value / 1024:.1f} KB"

    return f"{value / (1024 * 1024):.1f} MB"


def main():
    input_file = (
        PROJECT_ROOT
        / "benchmark_data"
        / "837s-100x100.edi"
    )

    output_file = (
        PROJECT_ROOT
        / "output"
        / "837s-100x100.json"
    )

    if not input_file.exists():
        raise FileNotFoundError(
            f"Benchmark input file not found: {input_file}"
        )

    #
    # Measure JVM startup and SDK initialization
    #
    start = perf_counter()

    service = EdiService()

    jvm_elapsed = perf_counter() - start

    #
    # Measure EDI conversion
    #
    input_size = input_file.stat().st_size

    start = perf_counter()

    service.edi_file_to_json(
        input_file,
        output_file,
    )

    conversion_elapsed = perf_counter() - start

    output_size = output_file.stat().st_size

    #
    # Known characteristics of this benchmark file.
    # 837s-100x100 means:
    #   100 ST transactions
    #   100 claims per transaction
    #
    claims = 100 * 100

    print()
    print("BerryWave 837 Claims Performance Benchmark")
    print("------------------------------------------")
    print(f"Input file      : {input_file.name}")
    print(f"Input size      : {format_bytes(input_size)}")
    print(f"Output size     : {format_bytes(output_size)}")
    print()
    print(f"Claims          : {claims:,}")
    print()
    print(f"JVM startup     : {jvm_elapsed:.3f} seconds")
    print(f"EDI → JSON       : {conversion_elapsed:.3f} seconds")
    print()
    print(
        f"Throughput      : "
        f"{input_size / conversion_elapsed / (1024 * 1024):.1f} MB/sec"
    )
    print(
        f"Claims/sec      : "
        f"{claims / conversion_elapsed:,.0f}"
    )


if __name__ == "__main__":
    main()