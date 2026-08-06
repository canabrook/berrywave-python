"""
Generate a technical acknowledgment for an EDI document.

This example demonstrates the simplest use of the BerryWave Python EDI SDK by
passing an EDI document held in a Python string to EdiService.acknowledge().

The SDK automatically generates the appropriate technical acknowledgment based
on the input document. For X12 input, the response will typically be a 997 or
999 Functional Acknowledgment. For EDIFACT input, the response will be a CONTRL
message.
"""

from berrywave import EdiService


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
SE^7^8620~
GE^1^653~
IEA^1^500009740~
"""

    # Generate the appropriate technical acknowledgment.
    acknowledgment = service.acknowledge(edi_document)

    print("Acknowledging 850 with:")
    print(acknowledgment)


if __name__ == "__main__":
    main()