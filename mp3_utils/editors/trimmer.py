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

    def process(self, output_path: str, duration: float = None, start_time: float = 0) -> str:
        """
        Trim the MP3 file from start_time for the given duration and save it to output_path.
        :param start_time: Start time in seconds or in 'HH:MM:SS' format.
        :param duration: Duration in seconds.
        :param output_path: Path to save the trimmed file.
        """
        # Validate and prepare the output path
        output_path = self._validate_output_path(output_path)

        # Construct the ffmpeg command
        command = [
            'ffmpeg',
            '-ss', str(start_time),  # Start time
            '-i', self.file_path,  # Input file
            '-acodec', 'copy',  # Keep original audio codec
            '-y'  # Overwrite output file without asking
        ]

        # If duration is specified, add it to the command
        if duration is not None:
            command += ['-t', str(duration)]

        command.append(output_path)  # Output file

        try:
            # Execute the command and capture the output and errors
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            # result = subprocess.run(command, check=True, capture_output=True)
        except subprocess.CalledProcessError as e:
            raise AudioProcessingError(f"Error trimming MP3 file: {e.stderr.decode()}")

        return output_path
