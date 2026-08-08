from pathlib import Path

import pytest

from berrywave import EdiParseError, EdiService

DATA_DIR = Path(__file__).parent / "data"


def test_edi_to_json():
    service = EdiService()

    edi = (DATA_DIR / "850.edi").read_text()

    json_text = service.edi_to_json(edi)

    assert json_text
    assert '"850"' in json_text


def test_edi_to_json_pretty():
    service = EdiService()

    edi = (DATA_DIR / "850.edi").read_text()

    json_text = service.edi_to_json(edi, pretty=True)

    assert json_text
    assert '"850"' in json_text
    assert "\n" in json_text


def test_edi_to_json_invalid_edi():
    service = EdiService()

    with pytest.raises(EdiParseError):
        service.edi_to_json("This is not valid EDI")
