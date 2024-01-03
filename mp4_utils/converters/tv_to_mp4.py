# mp4_utils/converters/tv_to_mp4.py
import subprocess
from ..core.mp4_handler import MP4Handler
from ..core.exceptions import ConversionError


class TVToMP4Converter(MP4Handler):
    """
    Class to convert various video formats to MP4.
    """

    def process(self, output_path=None, audio_bitrate='128k'):
        """
        Convert the video file to MP4 format.
        :param output_path: Path to save the converted MP4 file. If None, replaces the original file extension with .mp4
        :param audio_bitrate: Audio bitrate for the output file. Default is '128k'.
        """
        if output_path is None:
            output_path = self.file_path.rsplit('.', 1)[0] + '.mp4'

        self._validate_output_path(output_path)

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vcodec', 'libx264',  # Video codec
            '-acodec', 'aac',  # Audio codec
            '-ab', audio_bitrate,  # Audio bitrate
            '-ar', '44100',  # Audio sample rate
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            raise ConversionError(f"Failed to convert video to MP4: {e}")

        return output_path

# Example usage
# if __name__ == "__main__":
#     converter = TVToMP4Converter("path/to/your/video.file")
#     converted_path = converter.process()
#     print(f"Converted video saved to {converted_path}")
