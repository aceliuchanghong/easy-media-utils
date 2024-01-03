from mp3_utils.converters.audio_format_converter import AudioFormatConverter
from mp3_utils.converters.mp3_to_srt import MP3ToSRTConverter
from mp3_utils.converters.mp3_to_text import MP3ToTXTConverter
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
    converter = Converter.get(converter_type)(file_path)

    return converter


if __name__ == "__main__":
    mp3_path = '../../testfiles/out/output.mp3'
    wav_path = '../../testfiles/out/output.wav'
    flac_path = '../../testfiles/out/output.flac'

    converter_type = "format"
    ans_path = flac_path

    converter = main(converter_type, wav_path)
    converter.process(ans_path, 'flac')
