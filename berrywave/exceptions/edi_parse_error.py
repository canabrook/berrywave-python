"""
Raised when an EDI document cannot be parsed or processed.
"""

from .berrywave_error import BerryWaveError


class EdiParseError(BerryWaveError):
    """Raised when an EDI document cannot be parsed."""

    pass