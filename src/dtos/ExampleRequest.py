from pkg.Enums import ExampleType
from jsonschema import validate as jvalidate


class ExampleRequest:
    def __init__(self, raw_json: str) -> None:
        """__init__ raises validation error if json payload is invalid"""
        self.raw_json = raw_json
        self.validate()
        self.name = self.raw_json['name']
        self.example_type = self.raw_json['example_type']

    def validate(self):
        schema = {
            'type': 'object',
            'required': ['name', 'example_type'],
            'properties': {
                'name': {
                    'type': 'string'
                },
                'example_type': {
                    'type': 'string',
                    'pattern': f'({"|".join(e.name for e in ExampleType)})'
                }
            }
        }
        jvalidate(instance=self.raw_json, schema=schema)
