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
