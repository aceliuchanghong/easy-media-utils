from mp3_utils.converters.audio_format_converter import AudioFormatConverter
from mp3_utils.core.mp3_handler import MP3Handler


def main(converter_type, file_path='../../testfiles/out/output.mp3') -> MP3Handler:
    """
    Convert MP3 each frame.
    :param converter_type:
    :param file_path:
    """
    Converter = {
        "format": AudioFormatConverter,
    }
    converter = Converter.get(converter_type)(file_path)

    return converter


if __name__ == "__main__":
    mp3_path = '../../testfiles/out/output.mp3'
    wav_path = '../../testfiles/out/output.wav'
    flac_path = '../../testfiles/out/output.flac'
    out_path = '../../testfiles/out/'

    converter_type = "format"
    ans_path = out_path

    converter = main(converter_type, wav_path)
    converter.process(out_path, 'flac')
