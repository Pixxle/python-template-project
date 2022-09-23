from pkg.Enums import ErrorTypes
from json import dumps


class ErrorDTO:
    def __init__(self, type: ErrorTypes, message: str) -> None:
        self.type = type
        self.message = message

    def json(self) -> str:
        return dumps(
            {
                'error_type': self.type.name,
                'error_message': self.message
            })
