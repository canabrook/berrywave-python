from pathlib import Path

from berrywave import EdiService

DATA_DIR = Path(__file__).parent / "data"


def test_license_info():
    service = EdiService()

    edi = (DATA_DIR / "850.edi").read_text()

    info = service.license_info()

    assert info
    assert "Community Edition" in info
