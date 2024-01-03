# mp4_utils/converters/mp4_to_gif.py
import subprocess
from ..core.mp4_handler import MP4Handler
from ..core.exceptions import ConversionError


class MP4ToGIFConverter(MP4Handler):
    def process(self, output_path, start_time=0, duration=None, gif_width=None, fps=10, flags='lanczos'):
        """
        Convert MP4 to GIF.
        :param output_path: Path to save the GIF.
        :param start_time: Start time for the GIF in seconds.
        :param duration: Duration of the GIF in seconds.
        :param gif_width: Width of the GIF. Height is set automatically to maintain aspect ratio.
        :param fps: Frames per second of the GIF.
        :param flags: Scaling algorithm.
        """
        output_path = self._validate_output_path(output_path)

        # Set default duration if not specified
        if duration is None:
            duration = '5'  # Default duration in seconds

        # Set default gif width if not specified
        if gif_width is None:
            gif_width = '320'  # Default width in pixels

        command = [
            'ffmpeg',
            '-ss', str(start_time),  # Start time
            '-t', str(duration),  # Duration
            '-i', self.file_path,  # Input file
            '-vf', f"fps={fps},scale={gif_width}:-1:flags={flags}",  # Video filters
            '-c:v', 'gif',  # Codec Video: gif
            '-f', 'gif',  # Format: gif
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            raise ConversionError(f"Failed to convert MP4 to GIF: {e}")

# Example usage
# converter = MP4ToGIFConverter("path/to/video.mp4")
# converter.process("path/to/output.gif", start_time=5, duration=15, gif_width=500)
