from models.Example import Example
from models.Order import Order
from repositories.database.Interface import DatabaseInterface
from typing import List
from repositories.database.exceptions import ExampleNotFoundException, DuplicateExampleException, OrderNotFoundException


class InMemoryDatabase(DatabaseInterface):
    """ Implementation only works as long as examples can't be updated,
    currently each order holds a copy of the example object associated with them, in a more permanent solution
    the the order would instead only hold a reference to the example_id.
    """
    def __init__(self) -> None:
        self.example_storage: List[Example] = []
        self.order_storage: List[Order] = []

    def _get_example_storage(self) -> List[Example]:
        return self.example_storage

    def _get_order_storage(self) -> List[Order]:
        return self.order_storage

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
