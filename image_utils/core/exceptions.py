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
