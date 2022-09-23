import logging
from http.client import BAD_REQUEST, INTERNAL_SERVER_ERROR, NOT_FOUND, OK, CONFLICT
from flask import Blueprint, request, Response
from dtos.ExampleRequest import ExampleRequest
from dtos.ErrorResponse import ErrorDTO
from services.ExampleService import ExampleService
from pkg.Enums import ErrorTypes
from jsonschema.exceptions import ValidationError
from repositories.database.exceptions import ExampleNotFoundException, DuplicateExampleException


class ExampleController:
    """ ExampleController is responsible for
    ensuring that incoming payloads are properly json formated
    and that the user receives a valid response after request is finished.
    """

    def __init__(self, service: ExampleService) -> None:
        self.example_blueprint = Blueprint('example_blueprint', __name__)
        self.__register_routes()
        self.example_service = service

    def __register_routes(self) -> None:
        self.example_blueprint.add_url_rule(
            '/example', methods=['POST'], view_func=self.create_example)
        self.example_blueprint.add_url_rule(
            '/example/<id>', methods=['GET'], view_func=self.get_example)

    def get_blueprint(self) -> Blueprint:
        return self.example_blueprint

    def create_example(self) -> Response:
        try:
            incoming_data = request.get_json()

            # Performs JSON Validation
            example_request = ExampleRequest(incoming_data)
            example_response = self.example_service.create_new_example(example_request)

            return Response(
                example_response.json(),
                status=OK)

        except ValidationError as e:
            return Response(
                ErrorDTO(ErrorTypes.VALIDATION_ERROR, e.message).json(),
                status=BAD_REQUEST)

        except DuplicateExampleException as e:
            return Response(
                ErrorDTO(type=ErrorTypes.COLLISION_ERROR, message=f'{e.msg}').json(),
                status=CONFLICT)

        except Exception as e:
            logging.error(f'internal server error: {e}')
            return Response(
                ErrorDTO(ErrorTypes.INTERNAL_SERVER_ERROR, 'unable to process request').json(),
                status=INTERNAL_SERVER_ERROR)

    def get_example(self, id: str) -> Response:
        try:
            example_response = self.example_service.get_example(id)
            return Response(
                example_response.json(),
                status=OK)

        except ExampleNotFoundException as e:
            return Response(
                ErrorDTO(type=ErrorTypes.NOT_FOUND_ERROR, message=str(e)).json(),
                status=NOT_FOUND)

        except Exception as e:
            logging.error(f'internal server error: {e}')
            return Response(
                ErrorDTO(ErrorTypes.INTERNAL_SERVER_ERROR, 'unable to process request').json(),
                status=INTERNAL_SERVER_ERROR)
