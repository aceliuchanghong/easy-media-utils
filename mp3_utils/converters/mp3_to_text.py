# mp3_utils/converters/mp3_to_text.py
# https://github.com/SYSTRAN/faster-whisper
from ..core.mp3_handler import MP3Handler
from ..core.exceptions import FormatConversionError


class MP3ToTEXTConverter(MP3Handler):
    """
    Class to handle audio format conversion.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, output_path, target_format):
        """
        Convert the file to a specified format.
        :param output_path: The path to save the converted file.
        :param target_format: The target format (e.g., 'txt', 'srt').
        """
