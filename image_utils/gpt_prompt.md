对于处理图像文件文件的包，提供 添加文字在图片上 图片文字识别 图片按比例放缩/图片旋转 图片转灰白 图片按比例剪切 图片格式之间相互转换 等功能 
以下是图像处理的结构：
```
media_utils/
│
├── base_model/
│   ├── __init__.py            # 新增的初始化文件
│   └── MediaHandler.py        # 基础类
│
└── image_utils/
    │
    ├── __init__.py
    │
    ├── core/
    │   ├── __init__.py
    │   ├── image_handler.py     # 抽象类和核心图像处理功能
    │   └── exceptions.py        # 自定义异常
    │
    ├── converters/
    │   ├── __init__.py
    │   ├── image_to_text.py     # 图片文字识别功能，可能使用OCR技术
    │   ├── text_add_to_image.py.py     # 在图片上添加文字
    │   └── format_converter.py  # 图片格式之间的转换功能
    │
    ├── editors/
    │   ├── __init__.py
    │   ├── resizer.py           # 图片按比例放缩和旋转功能
    │   └── cropper.py           # 图片按比例剪切功能
    │
    ├── utils/
    │   ├── __init__.py
    │   ├── image_utils.py       # 图片提取基本信息等
    │   └── file_utils.py        # 文件操作相关的辅助函数
    │
    └── tests/
        ├── __init__.py
        ├── test_converters.py
        ├── test_editors.py
        └── test_utils.py

```

首先是exceptions.py，它定义了可能在处理图像文件时遇到的自定义异常：

```
# image_utils/core/exceptions.py
class ImageProcessingError(Exception):
    """基础异常类，用于图像处理错误"""
    pass

class FormatConversionError(ImageProcessingError):
    """当图像格式转换失败时抛出"""
    def __init__(self, source_format, target_format, message="Image format conversion failed"):
        self.source_format = source_format
        self.target_format = target_format
        self.message = f"{message}: {source_format} to {target_format}"
        super().__init__(self.message)

class FileHandlingError(ImageProcessingError):
    """当文件操作出现问题时抛出"""
    def __init__(self, filepath, message="Error handling image file"):
        self.filepath = filepath
        self.message = f"{message}: {filepath}"
        super().__init__(self.message)

class OCRProcessingError(ImageProcessingError):
    """当图像文字识别过程失败时抛出"""
    def __init__(self, message="OCR processing failed"):
        self.message = message
        super().__init__(self.message)

class ImageResizingError(ImageProcessingError):
    """当图像调整大小或旋转失败时抛出"""
    def __init__(self, message="Image resizing or rotation failed"):
        self.message = message
        super().__init__(self.message)

class ImageCroppingError(ImageProcessingError):
    """当图像剪切过程失败时抛出"""
    def __init__(self, message="Image cropping failed"):
        self.message = message
        super().__init__(self.message)

class ImageColorConversionError(ImageProcessingError):
    """当图像颜色转换过程失败时抛出"""
    def __init__(self, message="Image color conversion failed"):
        self.message = message
        super().__init__(self.message)

```

接下来是 image_handler.py，这里我们定义了一个抽象基类ImageHandler,继承自MediaHandler，它将被所有处理图像的类继承：

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

# image_utils/core/image_handler.py
from base_model.MediaHandler import MediaHandler

class ImageHandler(MediaHandler):
    """
    Class for handling image files.
    """
    def __init__(self, file_path):
        super().__init__(file_path)
        # You can add additional checks specific to image files here
        # For example, checking the file extension to be one of the common image formats (jpg, png, etc.)

    def process(self, *args, **kwargs):
        # Implementation specific to image processing
        # This could include operations like resizing, format conversion, filtering, etc.
        pass

```

```
基于以上帮我使用ffmpeg完善 cropper.py继承ImageHandler,我能想到的参数比如 output_path 等
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
