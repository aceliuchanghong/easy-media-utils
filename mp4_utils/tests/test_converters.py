# Example usage within a script:
from mp4_utils.converters.mp4_to_gif import MP4ToGIFConverter
from mp4_utils.converters.mp4_to_mp3 import MP4ToMP3Converter
from mp4_utils.converters.mp4_to_pngs import MP4ToPNGsConverter

if __name__ == "__main__":
    file_path = '../../testfiles/onboard_cover.mp4'
    gif_out_path = '../../testfiles/out/output.gif'
    mp3_out_path = '../../testfiles/out/output.mp3'
    pngs_out_path = '../../testfiles/out/pngs_output'
    converter = MP4ToGIFConverter(file_path)
    converter.process(gif_out_path)
    converter2 = MP4ToMP3Converter(file_path)
    converter2.process(mp3_out_path)
    converter3 = MP4ToPNGsConverter(file_path)
    converter3.process(pngs_out_path)
