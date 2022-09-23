from enum import Enum, auto
from typing import Any


class Value:
    def __init__(self, value: Any):
        self.value = value


class ExampleType(Enum):
    SMALL_EXAMPLE = auto()
    LARGE_EXAMPLE = auto()
    PRIVATE = auto()


class Article(Enum):
    PEN = Value(25)
    BLOCK = Value(60)
    PAPER = Value(500)
    ERASER = Value(10)

    @property
    def val(self):
        return self.value.value


class ErrorTypes(Enum):
    VALIDATION_ERROR = auto()
    INTERNAL_SERVER_ERROR = auto()
    COLLISION_ERROR = auto()
    NOT_FOUND_ERROR = auto()
