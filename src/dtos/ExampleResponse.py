from json import dumps


class ExampleResponse:
    def __init__(self, id: int, name: str, example_type: str) -> None:
        self.id = id
        self.name = name
        self.example_type = example_type

    def json(self) -> str:
        return dumps(
            {
                'id': self.id,
                'name': self.name,
                'example_type': self.example_type
            })
