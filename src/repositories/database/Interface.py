import abc
from models.Example import Example


class DatabaseInterface (abc.ABC):

    @abc.abstractclassmethod
    def get_example(self, id: str) -> Example:
        pass

    @abc.abstractclassmethod
    def write_example(self, example: Example) -> str:
        pass
