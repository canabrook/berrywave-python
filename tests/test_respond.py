from pathlib import Path

from berrywave import EdiService

DATA_DIR = Path(__file__).parent / "data"


def test_response_850():
    service = EdiService()

    edi = (DATA_DIR / "850.edi").read_text()

    acknowledgment = service.respond(edi, response_type="855")

    assert acknowledgment
    assert acknowledgment.startswith("ISA")
    assert "ST*855*" in acknowledgment


def test_response_837():
    service = EdiService()

    edi = (DATA_DIR / "837.edi").read_text()

    acknowledgment = service.respond(edi, response_type="277")

    assert acknowledgment
    assert acknowledgment.startswith("ISA")
    assert "ST*277*" in acknowledgment
