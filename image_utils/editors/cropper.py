# image_utils/editors/cropper.py
import subprocess
from image_utils.core.image_handler import ImageHandler
from image_utils.core.exceptions import ImageCroppingError


class ImageCropper(ImageHandler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, output_path, width, height, x, y):
        """
        Crop the image using ffmpeg.

        :param width: The width of the cropped area
        :param height: The height of the cropped area
        :param x: The x offset for cropping (top-left corner)
        :param y: The y offset for cropping (top-left corner)
        :param output_path: The output file path
        """
        if not output_path:
            output_path = self.file_path.rsplit('.', 1)[0] + '_cropped.' + self.file_path.rsplit('.', 1)[1]

        # Ensure the output directory exists
        output_path = self._validate_output_path(output_path)

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vf', f"crop={width}:{height}:{x}:{y}",  # Crop filter
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            raise ImageCroppingError(f"Failed to crop the image: {e.stderr.decode()}")

        return output_path

# Example usage:
# cropper = ImageCropper('path/to/image.jpg')
# cropped_image_path = cropper.crop(200, 200, 10, 10, 'path/to/output_image.jpg')
