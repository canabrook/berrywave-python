class BerryWaveError(Exception):
    """Base exception for BerryWave SDK errors."""
    pass


class EdiError(BerryWaveError):
    """Base exception for EDI processing errors."""
    pass


class EdiParseError(EdiError):
    """Raised when an EDI document cannot be converted."""
    pass


class EdiValidationError(EdiError):
    """Raised when EDI validation fails."""
    pass


class LicenseError(BerryWaveError):
    """Raised when license validation fails."""
    pass
