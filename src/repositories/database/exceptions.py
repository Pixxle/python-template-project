class ExampleNotFoundException(Exception):
    def __init__(self, id: str):
        self.id = id

    def __str__(self) -> str:
        return f'No example with id:{self.id} found'


class DuplicateExampleException(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    def __str__(self) -> str:
        return f'Example already exists, {self.msg}'
