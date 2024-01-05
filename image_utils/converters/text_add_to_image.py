# image_utils/converters/text_add_to_image.py
# 文字添加到图片上
# 这儿要考虑的太多了,我觉得似乎没必要,之后需要自己重写就好了
import subprocess
from image_utils.core.image_handler import ImageHandler
from PIL import ImageFont


class TextAdder(ImageHandler):
    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, text, output_path, font_file, font_size, font_color, image_width, start_time='00:00:00',
                duration='99999', text_position='center'):
        # 预处理文字，将其分割成多行以适应图片宽度
        processed_text = self._prepare_text(text, font_size, image_width, font_file)

        # 构建ffmpeg命令
        command = [
            'ffmpeg',
            '-i', self.file_path,  # Input file
            '-vf',
            f"drawtext=fontfile={font_file}:text='{processed_text}':x=(w-text_w)/2:y=(h-text_h)/2:fontsize={font_size}:fontcolor={font_color}",
            # Video filters
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        except subprocess.CalledProcessError as e:
            # Handle the error
            raise Exception("Failed to add text to image.") from e

    def _prepare_text(self, text, font_size, image_width, font_path):
        # 使用Pillow来加载字体文件和指定大小
        font = ImageFont.truetype(font_path, font_size)

        words = text.split()
        processed_text = ""
        line = ""
        line_width = 0
        space_width, _ = font.getsize(' ')  # 获取空格的宽度

        for word in words:
            word_width, _ = font.getsize(word)
            # 如果添加这个单词会超出图片宽度，就换行
            if line_width + word_width + space_width > image_width:
                processed_text += line + "\\n"
                line = ""
                line_width = 0
            line += word + " "
            line_width += word_width + space_width

        processed_text += line.strip()  # 添加最后一行

        return processed_text.strip()
