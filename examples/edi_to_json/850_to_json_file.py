"""
Convert an X12 850 Purchase Order to JSON.

This example demonstrates converting EDI to JSON where the input and output
are files instead of Python strings.
"""

from pathlib import Path
from tempfile import TemporaryDirectory

from berrywave import EdiService


EDI_DOCUMENT = """
ISA^00^          ^00^          ^ZZ^1556150        ^12^5088942073     ^100903^0143^U^00401^500009740^0^P^|~
GS^PO^007941230^8145^20100903^0143^653^X^004010~
ST^850^8620~
BEG^00^SA^16683^^20100902~
N1^ST^OWENS & MINOR - HOUSTON^92^056551~
PO1^001^2^CA^74.8692^UM^VC^130^IN^0565000130~
PO1^002^3^CA^95.5^UM^VC^0565TRN1184^IN^0565TRN1184~
CTT^Q2~
SE^7^8620~
GE^1^653~
IEA^1^500009740~
"""


def main():
    service = EdiService()

    with TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        input_file = temp_path / "850.edi"
        output_file = temp_path / "850.json"

        input_file.write_text(EDI_DOCUMENT.strip())

        service.edi_to_json_file(
            input_file,
            output_file,
        )

        json_document = output_file.read_text()

        print(json_document)


if __name__ == "__main__":
    main()