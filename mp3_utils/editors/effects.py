# mp3_utils/editors/effects.py
import subprocess
from ..core.mp3_handler import MP3Handler
from ..core.exceptions import AudioProcessingError


class MP3Effects(MP3Handler):
    """
    MP3 Effects class for applying audio effects to MP3 files.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def adjust_volume(self, output_path, volume_change):
        """
        Adjust the volume of the MP3 file.
        :param output_path: Path to save the modified file.
        :param volume_change: Volume change in dB (positive or negative).
        TODO 由于音频效果处理是一个广泛的领域，涵盖了从简单的音量调整到复杂的声音效果，这里仅演示一个基本的音量调整功能作为示例。
        TODO 未测试
        """
        # Validate and prepare the output path
        output_path = self._validate_output_path(output_path)

        # Construct the ffmpeg command for volume adjustment
        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-filter:a', f"volume={volume_change}dB",  # Audio filter for volume change
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            raise AudioProcessingError(f"Error adjusting volume: {e}")

        return output_path
