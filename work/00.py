# Example usage within a script:
from mp4_utils.converters.mp4_to_gif import MP4ToGIFConverter
from mp4_utils.converters.mp4_to_mp3 import MP4ToMP3Converter
from mp4_utils.converters.mp4_to_pngs import MP4ToPNGsConverter
from mp4_utils.converters.tv_to_mp4 import TVToMP4Converter
from mp4_utils.core.mp4_handler import MP4Handler


def main(converter_type, file_path='../../testfiles/onboard_cover.mp4') -> MP4Handler:
    """
    Convert MP4 each frame.
    :param converter_type:
    :param file_path:
    """
    Converter = {
        "gif": MP4ToGIFConverter,
        "mp3": MP4ToMP3Converter,
        "img": MP4ToPNGsConverter,
        "other": TVToMP4Converter,
    }
    # converter = Converter[converter_type](file_path)
    converter = Converter.get(converter_type)(file_path)

    return converter


if __name__ == "__main__":
    file_path = r'C:\Users\lawrence\Documents\malin\malin-article\马林思维-article.mp4'

    out_path = r'C:\Users\lawrence\Documents\malin\malin-article\0.gif'

    converter_type = "gif"
    converter = main(converter_type, file_path)
    converter.process(out_path, gif_width=1024, fps=32)
