import pytest
import uuid
from typing import List

from dtos.ExampleRequest import ExampleRequest
from models.Example import Example
from pkg.Enums import ExampleType

from repositories.database.InMemoryDatabase import InMemoryDatabase
from repositories.database.exceptions import ExampleNotFoundException
from services.ExampleService import ExampleService


""" Implemented a few unit tests, for this to be a real
 production ready application there are plenty of tests left to be written.
"""


class TestExampleService:
    def test_create_new_example(self):
        # SETUP
        database = InMemoryDatabase()
        service = ExampleService(database)

        # GIVEN
        example_request = ExampleRequest(
            raw_json={'name': 'sample', 'example_type': 'LARGE_EXAMPLE'}
        )

        # WHEN
        service.create_new_example(example_request)

        # THEN
        examples: List[Example] = database._get_example_storage()

        assert len(examples) == 1
        assert examples[0].example_type == ExampleType.LARGE_EXAMPLE
        assert examples[0].name == 'sample'

    def test_get_example(self):
        # SETUP
        database = InMemoryDatabase()
        service = ExampleService(database)

        # GIVEN
        example_request = ExampleRequest(
            raw_json={'name': 'sample', 'example_type': 'LARGE_EXAMPLE'}
        )
        example_response = service.create_new_example(example_request)

        # WHEN
        example_response = service.get_example(example_response.id)

        # THEN
        assert example_response.example_type == 'LARGE_EXAMPLE'
        assert example_response.name == 'sample'

    def test_not_existing_example(self):
        # SETUP
        database = InMemoryDatabase()
        service = ExampleService(database)

        # GIVEN
        # NO EXAMPLE INSERTED

        # WHEN / THEN
        with pytest.raises(ExampleNotFoundException):
            service.get_example(uuid.uuid4())
