# image_utils/editors/resizer.py
import subprocess
from image_utils.core.image_handler import ImageHandler
from image_utils.core.exceptions import ImageResizingError


class ImageResizer(ImageHandler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, output_path, width, height):
        """
        Resize the image to the given width and height using ffmpeg.

        :param width: New width for the image.
        :param height: New height for the image.
        :param output_path: The output file path. If None, overwrite the original image.
        """
        if not output_path:
            output_path = self.file_path.rsplit('.', 1)[0] + '_resized.' + self.file_path.rsplit('.', 1)[1]

        # Ensure the output directory exists
        output_path = self._validate_output_path(output_path)

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vf', f"scale={width}:{height}",  # Resize filter
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise ImageResizingError(f"Failed to resize the image: {e.stderr.decode()}")

        return output_path

    def rotate(self, angle, output_path=None):
        """
        Rotate the image by the given angle using ffmpeg.

        :param angle: The angle to rotate the image. Positive values will rotate clockwise.
        :param output_path: The output file path. If None, overwrite the original image.
        """
        if not output_path:
            output_path = self.file_path.rsplit('.', 1)[0] + '_rotated.' + self.file_path.rsplit('.', 1)[1]

        # Ensure the output directory exists
        output_path = self._validate_output_path(output_path)

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vf', f"transpose={angle}",  # Rotate filter
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise ImageResizingError(f"Failed to rotate the image: {e.stderr.decode()}")

        return output_path

# Example usage:
# resizer = ImageResizer('path/to/image.jpg')
# resized_image_path = resizer.resize(800, 600, 'path/to/output_image.jpg')
# rotated_image_path = resizer.rotate(2, 'path/to/output_rotated_image.jpg')
