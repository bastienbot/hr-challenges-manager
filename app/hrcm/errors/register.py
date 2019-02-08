from flask import jsonify
from .resource_not_found import ResourceNotFound
from .bad_request import BadRequest


def register_custom_exceptions(app):

    @app.errorhandler(ResourceNotFound)
    @app.errorhandler(BadRequest)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
