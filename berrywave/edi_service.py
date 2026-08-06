from pathlib import Path

from .exceptions import (
    EdiParseError,
    FeatureUnavailableError,
)

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
        Generate a business response for an EDI document provided as a string.

        Args:
            edi: EDI document content.
            response_type:
                Business response type to generate.

                Supported values:
                - 855: X12 Purchase Order Acknowledgment (850 response)
                - 277: X12 Healthcare Claim Response (837 response)

        Returns:
            Business response EDI document as a string.

        Raises:
            ValueError:
                If response_type is missing or unsupported.
            EdiParseError:
                If the EDI document cannot be processed.
        """

        if response_type is None:
            raise ValueError(
                "response_type is required for respond(). "
                "Supported values: 855, 277"
            )

        try:
            if response_type == "855":
                return str(self._service.x850To855(
                    edi,
                    "",
                    "",
                ))

            elif response_type == "277":
                return str(self._service.x837To277(
                    edi,
                    "",
                    "",
                ))

            else:
                raise ValueError(
                    f"Unsupported response type: {response_type}. "
                    "Supported values: 855, 277"
                )

        except ValueError:
            raise

        except Exception as exc:
            raise EdiParseError(str(exc)) from exc

    def respond_file(
            self,
            input_file: Path | str,
            output_file: Path | str,
            *,
            response_type: str | None = None
    ) -> None:
        """
        Generate a business response from an EDI file.

        This file-based API is provided as part of the SDK interface but is
        not yet implemented.

        Args:
            input_file:
                Path to the input EDI document.

            output_file:
                Path where the generated response will be written.

            response_type:
                Business response type to generate.

                Supported values:
                - 855: X12 Purchase Order Acknowledgment
                - 277: X12 Healthcare Claim Response

        Raises:
            NotImplementedError:
                Always, until file-based responses are implemented.
        """

        raise NotImplementedError(
            "respond_file() is not yet implemented"
        )

    def validate(
            self,
            edi: str,
            *,
            response_type: str | None = None,
    ) -> str:
        """
        Validate an EDI document provided as a string.

        Validation performs EDI compliance checking and returns an
        appropriate validation response (for example, an X12 997/999 or
        EDIFACT CONTRL message).

        Args:
            edi: EDI document content.
            response_type: Optional requested validation response type,
                such as "997", "999", or "CONTRL". If omitted, the SDK
                will choose the appropriate response type.

        Returns:
            Validation response as an EDI string.

        Raises:
            FeatureUnavailableError: Validation is not available in the
                currently installed BerryWave EDI engine.
        """
        raise FeatureUnavailableError(
            "EDI validation is not available in the Community Edition. "
            "This feature requires the Enterprise Edition of the "
            "BerryWave EDI engine."
        )

    def validate_file(
            self,
            input_file: Path | str,
            output_file: Path | str,
            *,
            response_type: str | None = None,
    ) -> None:
        """
        Validate an EDI file and write the validation response to an
        output file.

        Raises:
            FeatureUnavailableError: Validation is not available in the
                currently installed BerryWave EDI engine.
        """
        raise FeatureUnavailableError(
            "EDI validation is not available in the Community Edition. "
            "This feature requires the Enterprise Edition of the "
            "BerryWave EDI engine."
        )

    def license_info(self) -> str:
        return self._service.getLicenseInfo()
