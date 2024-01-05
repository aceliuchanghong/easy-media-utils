## image-utils

When I am dealing pics,mp3,mp4.. I always want a media utils to help me work, that's why this project start

### mp4处理

* 转png/jpg等
* 转mp3
* 转gif
* 转竖屏
* 其他格式视频转mp4

### mp3处理

* 转文字
* 转srt
* mp3裁剪
* mp3其他格式,eg:flac,WAV,AAC,Ogg,等互相转换

### 图片png/jpg处理

* 添加文字
* 图片文字识别
* 图片按比例放缩/图片旋转
* 图片转灰白
* 图片按比例剪切
* 图片格式相互转换

### install

```
pip install easy-media-utils
```

<details>
<summary>源码安装(点击展开) </summary>
# pip freeze > requirements.txt

git clone https://github.com/aceliuchanghong/easy-media-utils.git

conda create -n dealMedia python=3.11

conda activate dealMedia

pip install -r requirements.txt
</details>

### ffmpeg

前往官网,下载对应版本的文件,解压放在本地文件并且配置环境变量,确保可以访问到

```
ffmpeg -version
```

### 项目结构

<details>
<summary>项目结构生成(点击展开) </summary>
from tests.struct_tree_out import print_tree
path = 'D:\\aprojectPython\\pythonProject\\easy-media-utils'
print_tree(path)
</details>

```
easy-media-utils/
|
├── LICENSE
├── README.md
├── requirements.txt
├── setup.py
├── base_model/
│   ├── MediaHandler.py
│   ├── __init__.py
│   └── __pycache__/
├── build/
├── dist/
├── easy_media_utils.egg-info/
├── image_utils/
│   ├── __init__.py
│   ├── gpt_prompt.md
│   ├── __pycache__/
│   ├── converters/
│   │   ├── __init__.py
│   │   ├── format_converter.py
│   │   ├── image_to_text.py
│   │   ├── text_add_to_image.py
│   │   └── __pycache__/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── exceptions.py
│   │   ├── image_handler.py
│   │   └── __pycache__/
│   ├── editors/
│   │   ├── __init__.py
│   │   ├── cropper.py
│   │   └── resizer.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_converters.py
│   │   ├── test_editors.py
│   │   ├── test_utils.py
│   │   └── __pycache__/
│   └── utils/
│       ├── __init__.py
│       └── image_utils.py
├── mp3_utils/
│   ├── __init__.py
│   ├── gpt_prompt.md
│   ├── __pycache__/
│   ├── converters/
│   │   ├── __init__.py
│   │   ├── audio_format_converter.py
│   │   ├── mp3_to_text.py
│   │   └── __pycache__/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── exceptions.py
│   │   ├── mp3_handler.py
│   │   └── __pycache__/
│   ├── editors/
│   │   ├── __init__.py
│   │   ├── effects.py
│   │   └── trimmer.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_converters.py
│   │   └── test_editors.py
│   └── utils/
│       ├── __init__.py
│       └── mp3_utils.py
├── mp4_utils/
│   ├── __init__.py
│   ├── gpt_prompt.md
│   ├── __pycache__/
│   ├── converters/
│   │   ├── __init__.py
│   │   ├── mp4_to_gif.py
│   │   ├── mp4_to_mp3.py
│   │   ├── mp4_to_pngs.py
│   │   ├── tv_to_mp4.py
│   │   └── __pycache__/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── exceptions.py
│   │   ├── mp4_handler.py
│   │   └── __pycache__/
│   ├── editors/
│   │   ├── __init__.py
│   │   ├── orientation.py
│   │   └── resizer.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_converters.py
│   │   └── test_editors.py
│   └── utils/
│       ├── __init__.py
│       ├── file_utils.py
│       ├── mp4_utils.py
│       └── __pycache__/
├── testfiles/
│   └── out/
├── tests/
│   ├── __init__.py
│   └── struct_tree_out.py
└── venv/
```

### e.g.

```mp4
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
    file_path = '../../testfiles/out/onboard_cover.mp4'
    gif_out_path = '../../testfiles/out/output.gif'
    mp3_out_path = '../../testfiles/out/output.mp3'
    pngs_out_path = '../../testfiles/out/pngs_output'
    mp4_out_path = '../../testfiles/out/Sample.mp4'

    conv_file = '../../testfiles/out/Sample.mkv'

    converter_type = "img"
    ans_path = pngs_out_path
    converter = main(converter_type, file_path)
    converter.process(ans_path)
```

```mp3
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
```

```img
from image_utils.converters.format_converter import FormatConverter

test_image_path = "../../testfiles/out/pngs_output/frame_0001.png"
output_path = "../../testfiles/out/imgs_output"
txt = "你好"

if __name__ == '__main__':
    converter = FormatConverter(test_image_path)
    converter.process(output_path, "png")

```
