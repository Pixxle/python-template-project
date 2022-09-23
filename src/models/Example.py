from pkg.Enums import ExampleType


class Example:
    def __init__(self, id: str, name: str, example_type: ExampleType) -> None:
        self.id = id
        self.name = name
        self.example_type = example_type
