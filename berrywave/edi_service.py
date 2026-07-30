from pathlib import Path

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

    def edi_to_json(
            self,
            edi: str,
            *,
            pretty: bool = False,
    ) -> str:
        """
        Convert an EDI document provided as a string to JSON.

        Args:
            edi: EDI document content.
            pretty: Format JSON output for readability.

        Returns:
            JSON document as a string.

        Raises:
            EdiParseError: If the EDI document cannot be converted.
        """
        try:
            return str(self._service.ediToJson(
                edi,
                None,
                pretty,
            ))
        except Exception as exc:
            raise EdiParseError(str(exc)) from exc

    def edi_file_to_json(
            self,
            input_file: str | Path,
            output_file: str | Path,
            *,
            pretty: bool = False,
    ) -> None:
        """
        Convert an EDI file to a JSON file.

        This initial implementation reads the file into memory and uses
        edi_to_json(). The public API is designed to allow future versions
        to use the BerryWave streaming engine directly.

        Args:
            input_file: Path to the input EDI file.
            output_file: Path where JSON output will be written.
            pretty: Format JSON output for readability.

        Raises:
            EdiParseError: If the EDI document cannot be converted.
        """
        input_path = Path(input_file)
        output_path = Path(output_file)

        try:
            edi = input_path.read_text(encoding="utf-8")

            json_document = self.edi_to_json(
                edi,
                pretty=pretty,
            )

            output_path.parent.mkdir(parents=True, exist_ok=True)

            output_path.write_text(
                json_document,
                encoding="utf-8",
            )

        except EdiParseError:
            raise

        except Exception as exc:
            raise EdiParseError(
                f"Unable to convert EDI file '{input_path}': {exc}"
            ) from exc

    def license_info(self) -> str:
        return self._service.getLicenseInfo()
