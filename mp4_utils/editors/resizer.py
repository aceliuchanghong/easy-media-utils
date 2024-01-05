# mp4_utils/editors/resizer.py
import subprocess
from ..core.mp4_handler import MP4Handler
from ..core.exceptions import EditingError
from ..utils.mp4_utils import get_video_info


class Resizer(MP4Handler):
    """
    Class to handle MP4 video resolution resizing.
    """

    def process(self, output_path, target_width, target_height):
        """
        Resize the video to the specified width and height.
        :param target_width: New width of the video.
        :param target_height: New height of the video.
        :param output_path: Path to save the resized video.
        """
        # Validate and set the output path
        output_path = self._validate_output_path(output_path)

        # Get original video dimensions
        video_info = get_video_info(self.file_path)
        original_width = video_info['width']
        original_height = video_info['height']

        # Calculate padding if necessary
        pad_width = max(0, target_width - original_width) // 2
        pad_height = max(0, target_height - original_height) // 2

        # Construct the ffmpeg command with padding if needed
        scale_filter = f"scale={target_width}:{target_height}"
        pad_filter = f"pad={target_width}:{target_height}:{pad_width}:{pad_height}:black"
        video_filter = f"{scale_filter},{pad_filter}" if pad_width or pad_height else scale_filter

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vf', video_filter,  # Video filter for scaling and padding
            '-c:a', 'copy',  # Copy audio stream
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            raise EditingError(f"Failed to resize video: {e}")
