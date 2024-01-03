# mp3_utils/core/mp3_handler.py
from base_model.MediaHandler import MediaHandler


class MP3Handler(MediaHandler):
    """
    Class for handling MP3 files.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, *args, **kwargs):
        # Implementation specific to MP3 processing
        pass
