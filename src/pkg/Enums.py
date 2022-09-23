from enum import Enum, auto
from typing import Any


class Value:
    def __init__(self, value: Any):
        self.value = value


class ExampleType(Enum):
    SMALL_EXAMPLE = auto()
    LARGE_EXAMPLE = auto()
    PRIVATE = auto()


class ErrorTypes(Enum):
    VALIDATION_ERROR = auto()
    INTERNAL_SERVER_ERROR = auto()
    COLLISION_ERROR = auto()
    NOT_FOUND_ERROR = auto()
