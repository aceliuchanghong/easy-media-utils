# mp3_utils/editors/trimmer.py
import subprocess
from ..core.mp3_handler import MP3Handler
from ..core.exceptions import AudioProcessingError


class MP3Trimmer(MP3Handler):
    """
    MP3 Trimmer class for trimming MP3 files.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, output_path, duration=None, start_time=0):
        """
        Trim the MP3 file from start_time for the given duration and save it to output_path.
        :param start_time: Start time in seconds or in 'HH:MM:SS' format.
        :param duration: Duration in seconds.
        :param output_path: Path to save the trimmed file.
        TODO 未测试
        """
        # Validate and prepare the output path
        output_path = self._validate_output_path(output_path)

        # 构建ffmpeg命令
        command = [
            'ffmpeg',
            '-ss', str(start_time),  # 开始时间
            '-i', self.file_path,  # 输入文件
            '-acodec', 'copy',  # 保持原始音频编解码器
            '-y',  # 覆盖输出文件而不询问
            output_path  # 输出文件
        ]

        if duration is not None:
            command.insert(3, '-t')
            command.insert(4, str(duration))

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except subprocess.CalledProcessError as e:
            raise AudioProcessingError(f"Error trimming MP3 file: {e}")

        return output_path
