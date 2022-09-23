import abc
from models.Example import Example
from models.Order import Order


class DatabaseInterface (abc.ABC):

    @abc.abstractclassmethod
    def get_example(self, id: str) -> Example:
        pass

    @abc.abstractclassmethod
    def write_example(self, example: Example) -> str:
        pass
