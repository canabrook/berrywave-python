"""
Attempt to convert structurally flawed EDI to JSON.

This example demonstrates handling an invalid X12 envelope.
"""

from berrywave import EdiService, EdiParseError


def main():
    service = EdiService()

    edi_document = """
ISA^00^          ^00^          ^ZZ^1556150        ^12^5088942073     ^100903^0143^U^00401^500009740^0^P^|~
GS^PO^007941230^8145^20100903^0143^653^X^004010~
ST^850^8620~
BEG^00^SA^16683^^20100902~
N1^ST^OWENS & MINOR - HOUSTON^92^056551~
PO1^001^2^CA^74.8692^UM^VC^130^IN^0565000130~
PO1^002^3^CA^95.5^UM^VC^0565TRN1184^IN^0565TRN1184~
CTT^Q2~
SE^78^8622~
GE^1^653~
IEA^1^500009740~
"""

    try:
        json_document = service.edi_to_json(edi_document)
        print(json_document)

    except EdiParseError as error:
        print("EDI conversion failed:")
        print(error)


if __name__ == "__main__":
    main()
