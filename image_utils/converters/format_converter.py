# image_utils/converters/format_converter.py
import os
import subprocess

from mp4_utils.utils.file_utils import copy_file
from ..core.image_handler import ImageHandler
from ..core.exceptions import FormatConversionError


class FormatConverter(ImageHandler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def convert_format(self, output_path, target_format):
        """
        Convert the image to a different format using ffmpeg.
        :param output_path: Path to save the converted image.
        :param target_format: The target image format (e.g., 'png', 'jpg').
        """
        original_format = os.path.splitext(self.file_path)[-1].lstrip('.').lower()
        if original_format == target_format.lower():
            copy_file(self.file_path, output_path)
            print("same ext " + original_format)
            return self.file_path

        output_path = self._validate_output_path(output_path)

        # Check if output_path is a directory
        if os.path.isdir(output_path):
            # Extract filename without extension and add target format
            filename = os.path.splitext(os.path.basename(self.file_path))[0] + f'.{target_format}'
            output_path = os.path.join(output_path, filename)
        elif not output_path.endswith(f'.{target_format}'):
            # Change file extension to target format
            output_path = os.path.splitext(output_path)[0] + f'.{target_format}'

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            output_path
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            raise FormatConversionError(self.file_path.split('.')[-1], target_format, str(e))

        return output_path
