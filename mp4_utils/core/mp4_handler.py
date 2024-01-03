# mp4_utils/core/mp4_handler.py
from abc import ABC, abstractmethod
import os


class MP4Handler(ABC):
    """
    Abstract base class for MP4 handling.

    在Python中，`ABC`是`abc`模块中的`AbstractBaseClass`的缩写。`ABC`作为基类使用时，为创建的类提供了一个明确的框架，表明这个类是抽象的。即，它不能被直接实例化，而是旨在被其他类继承并且实现其抽象方法。使用`ABC`带来的好处包括：
        1. **强制子类实现特定方法**：通过在基类中定义抽象方法，你可以强制任何继承该基类的子类实现这些方法。如果子类没有实现基类中的所有抽象方法，Python将不允许实例化这个子类，这有助于避免运行时错误。
        2. **提供接口定义**：`ABC`允许你定义一个接口。在面向对象编程中，接口是一个定义了一组方法但不实现它们的类。其他类必须实现这些方法。这样做可以确保不同的类有着相同的方法签名，使得这些类可以互换使用。
        3. **增加代码可读性**：使用抽象基类可以使其他开发者更容易理解你的代码意图。它明确表示哪些类是用于继承的基类，哪些方法是需要在子类中实现的。
        4. **促进代码共享**：抽象基类可以包含可以被多个子类共享的方法（非抽象方法）实现。这样可以减少代码重复。
        5. **类型检查**：可以使用`isinstance()`和`issubclass()`函数来检查某个对象是否是特定抽象基类的实例或子类，这对于确保类型安全很有帮助。
    在`MP4Handler`类的上下文中，使用`ABC`可以确保所有处理MP4文件的类都遵循同样的接口规范，即它们都实现了`convert`, `edit`, 和 `extract_audio`方法。这对于维护和扩展代码库非常有帮助，因为它为未来可能加入的任何新的MP4处理类提供了清晰的指导。
    """

    def __init__(self, file_path):
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        if not file_path.lower().endswith('.mp4'):
            raise ValueError("The file provided is not an MP4 file.")
        self.file_path = file_path

    @abstractmethod
    def process(self, *args, **kwargs):
        """
        Process the MP4 file. This method should be implemented by all subclasses.
        The specific arguments can vary depending on the processing task.
        """
        pass

    import os

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
