import uuid
from models.Example import Example
from dtos.ExampleResponse import ExampleResponse
from dtos.ExampleRequest import ExampleRequest
from pkg.Enums import ExampleType
from repositories.database.Interface import DatabaseInterface


class ExampleService:
    def __init__(self, db: DatabaseInterface) -> None:
        self.db = db

    def create_new_example(self, example_request: ExampleRequest) -> ExampleResponse:
        """create_new_example returns example id on success"""

        example_id = str(uuid.uuid4())

        example = Example(
            example_id,
            example_request.name,
            ExampleType[example_request.example_type]
        )

        self.db.write_example(example)
        return ExampleResponse(str(example.id), example.name, example.example_type.name)

    def get_example(self, example_id: str) -> ExampleResponse:
        example = self.db.get_example(example_id)
        return ExampleResponse(str(example.id), example.name, example.example_type.name)
