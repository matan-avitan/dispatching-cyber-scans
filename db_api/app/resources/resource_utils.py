from flask_restful import abort
from http import HTTPStatus


def error_handler(func):
    def handler(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            abort(HTTPStatus.INTERNAL_SERVER_ERROR, message=str(e))

    return handler
