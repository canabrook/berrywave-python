from .exceptions import EdiParseError
from .jvm import start_jvm

import jpype


class EdiService:

    def __init__(self) -> None:
        start_jvm()

        edi_service_java = jpype.JClass(
            "berrywave.core.edi.EdiService"
        )

        self._service = edi_service_java.getInstance()

        Config = jpype.JClass("berrywave.config.Config")
        config = Config.getInstance()

        properties = config.getBerryWaveProperties()
        license = properties.getLicense()
        license.setCompany("BerryWave Developer")

        print(self._service.getLicenseInfo())

    def edi_to_json(self, edi: str, pretty: bool = False) -> str:
        try:
            return self._service.ediToJson(
                edi,
                None,
                pretty,
            )
        except Exception as exc:
            raise EdiParseError(str(exc)) from exc

    def license_info(self) -> str:
        return self._service.getLicenseInfo()
