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
            'aac': 'aac',  # AAC codec for AAC format (in an ADTS container)
            'm4a': 'aac',  # AAC codec for M4A format (typically in an MP4/M4A container)
            'ogg': 'libvorbis',  # Vorbis codec for OGG format
            'opus': 'libopus',  # Opus codec for OPUS format
            'wma': 'wmav2',  # WMA codec
            'alac': 'alac',  # Apple Lossless Audio Codec for M4A format
            'ac3': 'ac3',  # Dolby Digital AC-3 codec
            'eac3': 'eac3',  # Enhanced AC-3 codec
            'dts': 'dca',  # DTS Coherent Acoustics codec
            'mp2': 'mp2',  # MP2 (MPEG Audio Layer 2) codec
            'amr': 'libopencore_amrnb',  # Adaptive Multi-Rate NarrowBand codec
            'amr-wb': 'libvo_amrwbenc',  # Adaptive Multi-Rate WideBand codec
            'pcm_mulaw': 'pcm_mulaw',  # G.711 mu-law
            'pcm_alaw': 'pcm_alaw',  # G.711 A-law
            'g722': 'g722',  # G.722 ADPCM
            'spx': 'libspeex',  # Speex codec
            'aiiff': 'pcm_s16be',  # PCM codec for AIFF format
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
