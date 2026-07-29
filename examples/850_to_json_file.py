"""
Convert an X12 850 Purchase Order to JSON.

This example demonstrates converting EDI to JSON where the input and output
are in files instead of Python strings.
"""
from pathlib import Path
from berrywave import EdiService

PROJECT_ROOT = Path(__file__).resolve().parent.parent


def main():
    input_file = (
            PROJECT_ROOT
            / "sample_data"
            / "purchase_order_850.edi"
    )

    output_file = (
            PROJECT_ROOT
            / "output"
            / "850.json"
    )

    if not input_file.exists():
        raise FileNotFoundError(
            f"Input file not found: {input_file}"
        )

    service = EdiService()

    service.edi_file_to_json(
        input_file,
        output_file,
    )


if __name__ == "__main__":
    main()
