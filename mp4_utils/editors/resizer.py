# mp4_utils/editors/resizer.py
import subprocess
from ..core.mp4_handler import MP4Handler
from ..core.exceptions import EditingError


class Resizer(MP4Handler):
    """
    Class to handle MP4 video resolution resizing.
    TODO 没什么需求,这个没测试,之后要使用记得测试
    """

    def process(self, output_path, width, height):
        """
        Resize the video to the specified width and height.
        :param width: New width of the video.
        :param height: New height of the video.
        :param output_path: Path to save the resized video.
        """
        # Validate and set the output path
        output_path = self._validate_output_path(output_path)

        # Construct the ffmpeg command
        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vf', f"scale={width}:{height}",  # Video filter for scaling
            '-c:a', 'copy',  # Copy audio stream
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            raise EditingError(f"Failed to resize video: {e}")

# Example usage
# resizer = Resizer("path/to/video.mp4")
# resizer.process("path/to/resized_video.mp4", 1280, 720)
