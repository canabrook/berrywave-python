from .jvm import start_jvm
import jpype


class EdiService:

    def __init__(self):
        start_jvm()

        java_class = jpype.JClass(
            "berrywave.core.edi.EdiService"
        )

        self._service = java_class.getInstance()

        Config = jpype.JClass("berrywave.config.Config")
        config = Config.getInstance()
        # print(config)

        properties = config.getBerryWaveProperties()
        # print(properties)

        license = properties.getLicense()
        # print(license)
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