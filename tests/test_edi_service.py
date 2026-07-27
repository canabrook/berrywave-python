from berrywave import EdiService


def test_edi_to_json():
    service = EdiService()

    edi = """
ISA^00^          ^00^          ^ZZ^1556150        ^12^5088942073     ^100903^0143^U^00401^500009740^0^P^|~
GS^PO^007941230^8145^20100903^0143^653^X^004010~
ST^850^8620~
BEG^00^SA^16683^^20100902~
SE^3^8620~
GE^1^653~
IEA^1^500009740~
"""

    json_text = service.edi_to_json(edi)

    assert json_text is not None
    assert len(json_text) > 0
    assert '"850"' in json_text