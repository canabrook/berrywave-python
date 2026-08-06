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

    def edi_to_json_file(
            self,
            input_file: str | Path,
            output_file: str | Path,
            *,
            pretty: bool = False,
    ) -> None:
        """
        Convert an EDI file to a JSON file.

        Args:
            input_file: Path to the input EDI file.
            output_file: Path where the JSON output will be written.
            pretty: Format JSON output for readability.

        Raises:
            EdiParseError: If the EDI document cannot be converted.
        """
        input_path = Path(input_file)
        output_path = Path(output_file)

        try:
            self._service.ediToJsonFiles(
                str(input_path),
                str(output_path),
                pretty,
            )

        except Exception as exc:
            raise EdiParseError(f"Unable to convert EDI file '{input_path}': {exc}") from exc

    def acknowledge(
            self,
            edi: str,
            *,
            response_type: str | None = None
    ) -> str:
        """
        Acknowledge an EDI document provided as a string.

        Args:
            edi: EDI document content.

        Returns:
            EDI acknowledgement as a string.

        Raises:
            EdiParseError: If the EDI document cannot be converted.
        """
        try:
            return str(self._service.acknowledge(
                edi,
                "",
                response_type,
            ))
        except Exception as exc:
            raise EdiParseError(str(exc)) from exc

    def acknowledge_file(
            self,
            input_file: Path | str,
            output_file: Path | str,
            *,
            response_type: str | None = None
    ) -> None:
        raise NotImplementedError(
            "acknowledge_file() is not yet implemented"
        )

    def respond(
            self,
            edi: str,
            *,
            response_type: str | None = None
    ) -> str:
        """
        Respond to an EDI document provided as a string.

        Args:
            edi: EDI document content.

        Returns:
            EDI response as a string.

        Raises:
            EdiParseError: If the EDI document cannot be converted.
        """
        try:
            return str(self._service.acknowledge(
                edi,
                "",
                response_type,
            ))
        except Exception as exc:
            raise EdiParseError(str(exc)) from exc

    def license_info(self) -> str:
        return self._service.getLicenseInfo()
