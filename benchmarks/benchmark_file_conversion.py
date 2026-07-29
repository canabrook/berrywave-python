"""
Benchmark BerryWave EDI file conversion performance.

Measures:
- Input file size
- Output file size
- Conversion time
- Throughput
"""

from pathlib import Path
from time import perf_counter

from berrywave import EdiService


def format_bytes(value: int) -> str:
    if value < 1024:
        return f"{value} bytes"

    if value < 1024 * 1024:
        return f"{value / 1024:.1f} KB"

    return f"{value / (1024 * 1024):.1f} MB"


def main():
    input_file = Path(
        "sample_data/837s-100x100.edi"
    )

    output_file = Path(
        "output/large_837.json"
    )

    service = EdiService()

    input_size = input_file.stat().st_size

    start = perf_counter()

    service.edi_file_to_json(
        input_file,
        output_file,
    )

    elapsed = perf_counter() - start

    output_size = output_file.stat().st_size

    print()
    print("BerryWave EDI Performance Benchmark")
    print("----------------------------------")
    print(f"Input file : {input_file}")
    print(f"Input size : {format_bytes(input_size)}")
    print(f"Output size: {format_bytes(output_size)}")
    print()
    print(f"Elapsed    : {elapsed:.3f} seconds")
    print(
        f"Throughput : "
        f"{input_size / elapsed / (1024 * 1024):.1f} MB/sec"
    )


if __name__ == "__main__":
    main()
