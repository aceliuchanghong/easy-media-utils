# mp4_utils/converters/mp4_to_mp3.py
import os
import subprocess
from ..core.mp4_handler import MP4Handler
from ..core.exceptions import ConversionError


class MP4ToMP3Converter(MP4Handler):
    def process(self, output_path, audio_bitrate='192k'):
        """
        Extract audio from MP4 and save it as an MP3 file.
        :param output_path: Path to save the MP3 file.
        :param audio_bitrate: Bitrate of the audio file.
        """
        output_path = self._validate_output_path(output_path)

        # Ensure the input file exists
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Input file not found: {self.file_path}")

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vn',  # No video
            '-ab', audio_bitrate,  # Audio bitrate
            '-ar', '44100',  # Audio sample rate
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            raise ConversionError(f"Failed to convert MP4 to MP3: {e}")

# Example usage
# converter = MP4ToMP3Converter("path/to/video.mp4")
# converter.process("path/to/output.mp3")
