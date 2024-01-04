对于处理MP4文件的包，提供转换为GIF、提取音频、裁剪视频、调整分辨率* 转png/jpg 横竖互转 等功能以下是项目结构：

```
media_utils/
│
├── base_model/
│   ├── __init__.py            # 新增的初始化文件
│   └── MediaHandler.py        # 基础类
│
└── mp4_utils/
    │
    ├── __init__.py
    │
    ├── core/
    │   ├── __init__.py
    │   ├── mp4_handler.py  # 抽象类和核心功能
    │   └── exceptions.py   # 自定义异常
    │
    ├── converters/
    │   ├── __init__.py
    │   ├── mp4_to_gif.py   # MP4转GIF功能
    │   ├── mp4_to_mp3.py   # MP4提取音频功能
    │   ├── tv_to_mp4.py    # 其他视频转MP4功能
    │   └── mp4_to_pngs.py   # MP4转pngs
    │
    ├── editors/
    │   ├── __init__.py
    │   ├── orientation.py  # 视频横屏,竖屏样式互转
    │   └── resizer.py      # 视频裁剪功能
    │
    ├── utils/
    │   ├── __init__.py
    │   ├── mp4_utils.py    # MP4提取基本信息等
    │   └── file_utils.py   # 文件操作相关的辅助函数
    │
    └── tests/
        ├── __init__.py
        ├── test_converters.py
        └── test_editors.py
```

首先是exceptions.py，它定义了可能在处理MP4文件时遇到的自定义异常：

```
# mp4_utils/core/exceptions.py
class MP4UtilsError(Exception):
    """Base exception class for MP4 utils errors."""
    pass

class InvalidFormatError(MP4UtilsError):
    """Raised when an invalid format is provided for conversion."""
    pass

class ConversionError(MP4UtilsError):
    """Raised when a conversion process fails."""
    pass

class EditingError(MP4UtilsError):
    """Raised when an editing process fails."""
    pass

```

接下来是mp4_handler.py，这里我们定义了一个抽象基类，它将被所有处理MP4的类继承：

``` 
# base_model/MediaHandler.py
class MediaHandler(ABC):
    """
    Abstract base class for media file handling.
    """

    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        # if not file_path.lower().endswith(file_extension):
        #     raise ValueError(f"The file provided is not a {file_extension.upper()} file.")
        self.file_path = file_path

    @abstractmethod
    def process(self, *args, **kwargs):
        """
        Process the media file. This method should be implemented by all subclasses.
        The specific arguments can vary depending on the processing task.
        """
        pass

    def _validate_output_path(self, output_path):
        """
        Validate the output path. If the path is a directory, create it if it doesn't exist.
        If it's a file path and the directory does not exist, create it.
        """
        if os.path.isdir(output_path) or not os.path.splitext(output_path)[1]:
            output_dir = output_path
        else:
            output_dir = os.path.dirname(output_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        return output_path
        
# mp4_utils/core/mp4_handler.py
from base_model.MediaHandler import MediaHandler
class MP4Handler(MediaHandler):
    """
    Class for handling MP4 files.
    """
    def __init__(self, file_path):
        super().__init__(file_path)

    def process(self, *args, **kwargs):
        # Implementation specific to MP4 processing
        pass

```

```
基于以上帮我使用ffmpeg完善 mp4_to_gif.py,我能想到的参数比如output_path, start_time, duration, gif_width(需要获取当前mp4值),帧率fps,缩放算法flags等
         核心代码参考:command = [
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
```
