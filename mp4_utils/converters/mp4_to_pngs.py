# mp4_utils/converters/mp4_to_pngs.py
import subprocess
from ..core.mp4_handler import MP4Handler
from ..core.exceptions import ConversionError


class MP4ToPNGsConverter(MP4Handler):
    def process(self, output_folder, output_ext='png', frame_rate='1'):
        """
        Convert MP4 to a series of PNG images, one for each frame.
        :param output_ext:
        :param output_folder: Folder to save the PNG images.
        :param frame_rate: Number of frames to extract per second.
        """
        output_folder = self._validate_output_path(output_folder)

        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vf', f'fps={frame_rate}',  # Set frame rate for extraction
            '-y',  # Overwrite output files without asking
            f'{output_folder}/frame_%04d.{output_ext}'  # Output file pattern
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            raise ConversionError(f"Failed to convert MP4 to {output_ext}s: {e}")

# Example usage
# converter = MP4ToPNGsConverter("path/to/video.mp4")
# converter.process("path/to/output_folder")
