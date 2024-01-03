from mp3_utils.converters.audio_format_converter import AudioFormatConverter
from mp3_utils.core.mp3_handler import MP3Handler


def main(converter_type, file_path='../../testfiles/out/output.mp3') -> MP3Handler:
    """
    Convert MP4 each frame.
    :param converter_type:
    :param file_path:
    """
    Converter = {
        "format": AudioFormatConverter,
        "srt": MP3ToSRTConverter,
        "txt": MP3ToTXTConverter,
    }
    # converter = Converter[converter_type](file_path)
    converter = Converter.get(converter_type)(file_path)

    return converter


if __name__ == "__main__":
    mp3_path = '../../testfiles/out/output.mp3'
    converter_type = "other"
    ans_path = mp4_out_path
    converter = main(converter_type, conv_file)
    converter.process(ans_path)
