# mp3_utils/converters/audio_format_converter.py
import subprocess
from ..core.mp3_handler import MP3Handler
from ..core.exceptions import FormatConversionError


class AudioFormatConverter(MP3Handler):
    """
    Class to handle audio format conversion.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, output_path, target_format):
        """
        Convert the audio file to a specified format.
        :param output_path: The path to save the converted file.
        :param target_format: The target audio format (e.g., 'wav', 'flac').
        """
        self._validate_output_path(output_path)
        converted_file_path = self._generate_output_file_path(output_path, target_format)
        self._convert_audio_format(converted_file_path, target_format)

    def _generate_output_file_path(self, output_path, target_format):
        """
        Generate the output file path with the correct extension.
        """
        if not output_path.endswith(f'.{target_format}'):
            output_path = f"{output_path}.{target_format}"
        return output_path

    def _convert_audio_format(self, output_path, target_format):
        """
        Use ffmpeg to convert the audio file to the target format.
        """
        codec_map = {
            'wav': 'pcm_s16le',  # Linear PCM codec for WAV format
            'mp3': 'libmp3lame',  # MP3 codec
            'flac': 'flac',  # FLAC codec
            'aac': 'aac',  # AAC codec
            'ogg': 'libvorbis',  # Vorbis codec for OGG format
            'opus': 'libopus',  # Opus codec
            'wma': 'wmav2'  # WMA codec
        }
        codec = codec_map.get(target_format)
        if codec is None:
            raise FormatConversionError(self.file_path.split('.')[-1], target_format,
                                        "this project doesn't support " + target_format + " now")

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-acodec', codec,  # Audio codec
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            raise FormatConversionError(self.file_path.split('.')[-1], target_format, str(e))
