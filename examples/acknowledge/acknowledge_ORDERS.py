"""
Generate a technical acknowledgment for an EDIFACT ORDERS message.

This example demonstrates the simplest use of the BerryWave Python EDI SDK by
passing an EDIFACT ORDERS message held in a Python string to
EdiService.acknowledge().

The SDK automatically generates the appropriate technical acknowledgment based
on the input document. For EDIFACT input, the response will be a CONTRL
message.
"""

from berrywave import EdiService


def main():
    service = EdiService()

    # Sample EDIFACT ORDERS message
    edi_document = """UNA:+.? '
UNB+UNOA:3+8712345003008:14+8712345900007:14+960629:0921+00163++++++1'
UNH+METRO00001+ORDERS:D:96A:UN:EAN008'
BGM+220::9+100001+9+NA'
DTM+137:200308301200:203'
DTM+2:200302281500:203'
RFF+PD:2003134'
NAD+BY+8711576000012::9'
NAD+SU+4012345500004::9'
NAD+DP+8711576100019::9'
TAX+7+ACT++++E'
LIN+1++8712345003005:EN'
QTY+21:48'
RFF+PD:99'
LIN+2++8712345004002:EN'
QTY+21:50'
RFF+PD:99'
UNS+S'
UNT+17+METRO00001'
UNZ+1+00163'
"""

    # Generate the appropriate technical acknowledgment.
    acknowledgment = service.acknowledge(edi_document)

    print("Generated acknowledgment:\n")
    print(acknowledgment)


if __name__ == "__main__":
    main()
