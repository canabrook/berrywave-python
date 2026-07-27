from .jvm import start_jvm
import jpype


class EdiService:

    def __init__(self) -> None:
        start_jvm()

        EdiServiceJava = jpype.JClass(
            "berrywave.core.edi.EdiService"
        )

        self._service = EdiServiceJava.getInstance()

        Config = jpype.JClass("berrywave.config.Config")
        config = Config.getInstance()

        properties = config.getBerryWaveProperties()
        license = properties.getLicense()
        license.setCompany("BerryWave Developer")

        print(self._service.getLicenseInfo())

    def edi_to_json(self, edi: str, formatted: bool = True) -> str:
        return self._service.ediToJson(
            edi,
            None,
            formatted
        )

    def license_info(self) -> str:
        return self._service.getLicenseInfo()