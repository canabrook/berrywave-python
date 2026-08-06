"""
Raised when a requested SDK feature is unavailable in the
currently installed BerryWave EDI engine.
"""

from .berrywave_error import BerryWaveError


class FeatureUnavailableError(BerryWaveError):
    """Raised when a requested SDK feature is unavailable."""

    pass