"""
Convert an X12 850 Purchase Order to JSON.

This example demonstrates the simplest use of the BerryWave Python SDK by
converting an EDI document held in a Python string.
"""
from berrywave import EdiService


def main():
    service = EdiService()

    service.edi_file_to_json(
        "sample_data/purchase_order_850.edi",
        "output/850.json",
        pretty=True,
    )


if __name__ == "__main__":
    main()
