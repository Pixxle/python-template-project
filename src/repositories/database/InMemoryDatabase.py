from models.Example import Example
from repositories.database.Interface import DatabaseInterface
from typing import List
from repositories.database.exceptions import ExampleNotFoundException, DuplicateExampleException


class InMemoryDatabase(DatabaseInterface):
    """ Implementation only works as long as examples can't be updated
    """
    def __init__(self) -> None:
        self.example_storage: List[Example] = []

    def _get_example_storage(self) -> List[Example]:
        return self.example_storage

    def get_example(self, id: str) -> Example:
        for cust in self.example_storage:
            if cust.id == id:
                return cust
        else:
            raise ExampleNotFoundException(id)

    def write_example(self, example: Example) -> str:
        for cust in self.example_storage:
            if cust.id == example.id:
                raise DuplicateExampleException(f'id:{example.id} already exists in database')
        else:
            self.example_storage.append(example)
