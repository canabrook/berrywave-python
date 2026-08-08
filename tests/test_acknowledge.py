from pathlib import Path

from berrywave import EdiService


DATA_DIR = Path(__file__).parent / "data"


def test_acknowledge_850_997():
    service = EdiService()

    edi = (DATA_DIR / "850.edi").read_text()

    acknowledgment = service.acknowledge(
        edi,
        response_type="997",
    )

    assert acknowledgment
    assert acknowledgment.startswith("ISA")
    assert "ST^997^" in acknowledgment


def test_acknowledge_850_999():
    service = EdiService()

    edi = (DATA_DIR / "850.edi").read_text()

    acknowledgment = service.acknowledge(
        edi,
        response_type="999",
    )

    assert acknowledgment
    assert acknowledgment.startswith("ISA")
    assert "ST^999^" in acknowledgment

def test_acknowledge_x12_default_997():
    service = EdiService()

    edi = (DATA_DIR / "850.edi").read_text()

    acknowledgment = service.acknowledge(edi)

    assert acknowledgment
    assert acknowledgment.startswith("ISA")
    assert "ST^997^" in acknowledgment

def test_acknowledge_orders():
    service = EdiService()

    edi = (DATA_DIR / "orders.edi").read_text()

    acknowledgment = service.acknowledge(edi)

    assert acknowledgment
    assert acknowledgment.startswith("UN")
    assert "UNH+1+CONTRL:D:96A:UN" in acknowledgment