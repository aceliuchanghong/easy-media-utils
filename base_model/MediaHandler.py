from abc import ABC, abstractmethod
import os


class MediaHandler(ABC):
    """
    Abstract base class for media file handling.
    """

    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        # if not file_path.lower().endswith(file_extension):
        #     raise ValueError(f"The file provided is not a {file_extension.upper()} file.")
        self.file_path = file_path

    @abstractmethod
    def process(self, *args, **kwargs):
        """
        Process the media file. This method should be implemented by all subclasses.
        The specific arguments can vary depending on the processing task.
        """
        pass

    def _validate_output_path(self, output_path):
        """
        Validate the output path. If the path is a directory, create it if it doesn't exist.
        If it's a file path and the directory does not exist, create it.
        """
        if os.path.isdir(output_path) or not os.path.splitext(output_path)[1]:
            output_dir = output_path
        else:
            output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_path
