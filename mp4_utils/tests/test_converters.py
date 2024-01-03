# Example usage within a script:
from mp4_utils.converters.mp4_to_gif import MP4ToGIFConverter
from mp4_utils.converters.mp4_to_mp3 import MP4ToMP3Converter
from mp4_utils.converters.mp4_to_pngs import MP4ToPNGsConverter
from mp4_utils.core.mp4_handler import MP4Handler


def main(converter_type, file_path='../../testfiles/onboard_cover.mp4') -> MP4Handler:
    """
    Convert MP4 each frame.
    :param converter_type:
    :param ans_path:
    :param file_path:
    """
    Converter = {
        "gif": MP4ToGIFConverter,
        "mp3": MP4ToMP3Converter,
        "img": MP4ToPNGsConverter,
    }
    # converter = Converter[converter_type](file_path)
    converter = Converter.get(converter_type)(file_path)

    return converter


if __name__ == "__main__":
    file_path = '../../testfiles/onboard_cover.mp4'
    gif_out_path = '../../testfiles/out/output.gif'
    mp3_out_path = '../../testfiles/out/output.mp3'
    pngs_out_path = '../../testfiles/out/pngs_output'

    converter_type = "gif"
    ans_path = gif_out_path
    converter = main(converter_type, file_path)
    converter.process(ans_path)
