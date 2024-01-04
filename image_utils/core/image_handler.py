# png_utils/core/png_handler.py
from base_model.MediaHandler import MediaHandler


class IMAGEHandler(MediaHandler):
    """
    Class for handling PNG files.
    """

    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, *args, **kwargs):
        # Implementation specific to PNG processing
        pass
