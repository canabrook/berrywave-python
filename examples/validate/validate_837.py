"""
Validate an X12 837 Healthcare Claim.

This example demonstrates the planned BerryWave Python EDI SDK validation API.

Validation is separate from technical acknowledgments:
- acknowledge() generates 997/999/CONTRL messages
- validate() performs EDI compliance validation and reports errors

Validation requires the Enterprise Edition of the BerryWave EDI engine.
The Community Edition included with this SDK release raises a feature
availability exception when this example is executed.
"""

from berrywave import EdiService


def main():
    service = EdiService()

    # Sample X12 837 Professional Healthcare Claim (005010X222A1)
    edi_document = """
ISA*00*          *00*          *ZZ*123456789012345*ZZ*123456789012346*061015*1705*>*00501*000010216*0*T*:~
GS*HC*1234567890*9876543210*20061015*1705*20213*X*005010X222A1~
ST*837*0001*005010X222A1~
BHT*0019*00*0123*20050117*1023*CH~
NM1*41*2*PROVIDER MEDICAL GROUP*****46*N305~
PER*IC*NINA*TE*6155551212~
NM1*40*2*ABC PAYER*****46*05440~
HL*1**20*1~
NM1*85*2*PROVIDER MEDICAL GROUP*****XX*2366554859~
N3*1234 WEST END AVE~
N4*NASHVILLE*TN*37232~
REF*EI*756473826~
HL*2*1*22*0~
SBR*P*18*******MB~
NM1*IL*1*JONES*MARGARET****MI*123456789A~
N3*123 RAINBOW ROAD~
N4*NASHVILLE*TN*37232~
DMG*D8*19740303*F~
NM1*PR*2*ABC PAYER*****PI*05440~
CLM*153829140*827***22:B:1*Y*A*Y*Y~
SE*20*0001~
GE*1*20213~
IEA*1*000010216~
"""

    # Validation requires Enterprise Edition of the BerryWave EDI processing engine.
    result = service.validate(edi_document)

    print(result)


if __name__ == "__main__":
    main()
