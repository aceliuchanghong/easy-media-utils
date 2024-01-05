# mp4_utils/editors/orientation.py
import subprocess
from base_model.MediaHandler import MediaHandler
from mp4_utils.utils.mp4_utils import get_video_info


class OrientationHandler(MediaHandler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, output_path, target_aspect_ratio='16:9'):
        """
        Pad the video to change its orientation to landscape mode, keeping the original content.

        :param output_path: The path to output the processed video file.
        :param target_aspect_ratio: The target aspect ratio, default is '16:9' for landscape mode.
        """
        self._validate_output_path(output_path)

        # Get the video information to calculate the pad values
        video_info = get_video_info(self.file_path)
        original_width = video_info['width']
        original_height = video_info['height']
        original_aspect_ratio = original_width / original_height

        target_aspect_ratio_values = [int(n) for n in target_aspect_ratio.split(':')]
        target_aspect_ratio = target_aspect_ratio_values[0] / target_aspect_ratio_values[1]

        # Calculate the new width and height to maintain the aspect ratio
        if original_aspect_ratio < target_aspect_ratio:
            # The video is narrower than the target aspect ratio
            new_width = int(original_height * target_aspect_ratio)
            new_height = original_height
            x_pad = int((new_width - original_width) / 2)
            y_pad = 0
        else:
            # The video is wider than the target aspect ratio
            new_height = int(original_width / target_aspect_ratio)
            new_width = original_width
            x_pad = 0
            y_pad = int((new_height - original_height) / 2)

        filter_complex = f"pad={new_width}:{new_height}:{x_pad}:{y_pad}:black"

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vf', filter_complex,  # Video filter for padding
            '-codec:a', 'copy',  # Copy the audio stream without re-encoding
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            # Handle the error
            print(f"An error occurred: {e}")
            raise

# Example usage:
# To pad a vertical video to landscape mode:
# orientation_handler = OrientationHandler('input_video.mp4')
# orientation_handler.process('output_video_cropped.mp4', '9:16')
# orientation_handler.process('output_video_padded.mp4', '16:9')
