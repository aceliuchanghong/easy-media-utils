# mp4_utils/core/exceptions.py


class MP4UtilsError(Exception):
    """Base exception class for MP4 utils errors."""
    pass


class InvalidFormatError(MP4UtilsError):
    """Raised when an invalid format is provided for conversion."""
    pass


class ConversionError(MP4UtilsError):
    """Raised when a conversion process fails."""
    pass


class EditingError(MP4UtilsError):
    """Raised when an editing process fails."""
    pass
