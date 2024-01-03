对于处理MP3文件的包，提供 转文字 转srt mp3裁剪 mp3其他格式,eg:flac,WAV,AAC,Ogg,等互相转换等功能 以下是项目结构：
```
mp3_utils/
│
├── __init__.py
│
├── core/
│   ├── __init__.py
│   ├── mp3_handler.py       # 抽象类和核心功能
│   └── exceptions.py        # 自定义异常
│
├── converters/
│   ├── __init__.py
│   ├── mp3_to_text.py       # MP3转文字功能，可能使用语音识别API
│   ├── mp3_to_srt.py        # MP3转SRT字幕文件功能
│   └── audio_format_converter.py  # 通用音频格式转换功能
│
├── editors/
│   ├── __init__.py
│   ├── trimmer.py           # MP3裁剪功能
│   └── effects.py           # MP3音效处理功能
│
├── utils/
│   ├── __init__.py
│   ├── mp3_utils.py         # MP3提取基本信息等
│   └── file_utils.py        # 文件操作相关的辅助函数
│
└── tests/
    ├── __init__.py
    ├── test_converters.py
    └── test_editors.py
```

首先是exceptions.py，它定义了可能在处理MP3文件时遇到的自定义异常：

```
# mp3_utils/core/exceptions.py
class AudioProcessingError(Exception):
    """基础异常类，用于音频处理错误"""
    pass

class FormatConversionError(AudioProcessingError):
    """当格式转换失败时抛出"""

    def __init__(self, source_format, target_format, message="Format conversion failed"):
        self.source_format = source_format
        self.target_format = target_format
        self.message = f"{message}: {source_format} to {target_format}"
        super().__init__(self.message)

class FileHandlingError(AudioProcessingError):
    """当文件操作出现问题时抛出"""

    def __init__(self, filepath, message="Error handling file"):
        self.filepath = filepath
        self.message = f"{message}: {filepath}"
        super().__init__(self.message)

class SpeechRecognitionError(AudioProcessingError):
    """当语音识别过程失败时抛出"""

    def __init__(self, message="Speech recognition failed"):
        self.message = message
        super().__init__(self.message)
```

接下来是mp3_handler.py，这里我们定义了一个抽象基类，它将被所有处理MP3的类继承：

``` 
# mp3_utils/core/mp3_handler.py
from abc import ABC, abstractmethod
import os

class MP3Handler(ABC):
    """
    Abstract base class for MP3 handling.
    """
    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        # if not file_path.lower().endswith('.mp3'):
        #     raise ValueError("The file provided is not an MP3 file.")
        self.file_path = file_path
    @abstractmethod
    def process(self, *args, **kwargs):
        """
        Process the MP3 file. This method should be implemented by all subclasses.
        The specific arguments can vary depending on the processing task.
        """
        pass
    def _validate_output_path(self, output_path):
        """
        Validate the output path. If the path is a directory, create it if it doesn't exist.
        If it's a file path and the directory does not exist, create it.
        """
        if os.path.isdir(output_path) or not os.path.splitext(output_path)[1]:
            # The output_path is a directory or seems like a directory (no file extension)
            output_dir = output_path
        else:
            # The output_path is a file path
            output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_path
```

```
基于以上帮我使用ffmpeg完善 audio_format_converter.py,我能想到的参数比如output_path, ext格式,等
         参考一下格式,核心代码:command = [
            'ffmpeg',
            '-ss', start_time,  # Start time
            '-t', str(duration),  # Duration
            '-i', self.file_path,  # Input file
            '-vf', f"fps=10,scale={gif_width}:-1:flags=lanczos",  # Video filters
            '-c:v', 'gif',  # Codec Video: gif
            '-f', 'gif',  # Format: gif
            '-y',  # Overwrite output file without asking
            output_path  # Output file
        ]

        try:
            # Execute the command
            subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
基于以上帮我使用ffmpeg完善mp4_to_mp3.py
基于以上帮我使用ffmpeg完善mp4_to_pngs.py,使得视频可以逐帧输出到某个文件夹
基于以上帮我使用ffmpeg完善resizer.py
```
