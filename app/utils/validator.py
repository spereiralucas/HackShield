from cerberus import Validator
from functools import update_wrapper, wraps
from flask import request, make_response, jsonify


def errorValidation(errors):
    response = {
        "response": 400,
        "msg": "Bad request was sent",
        "errors": errors
    }

    result = jsonify(response)
    result.status_code = response["response"]

    return result


def validate(schema):
    def decorator(f):
        @wraps(f)
        def wrapper_function(*args, **kws):
            valid_params = _validate(schema)

            if valid_params is not True:
                return valid_params

            return f(*args, **kws)
        return wrapper_function
    return decorator


def _validate(schema):
    params = {}

    for key, value in request.values.items():
        if not key == 'auth':
            params[key] = value

    v = Validator(schema)
    result = v.validate(params)

    # If not result, get the errors and return to the 400 response
    if not result:
        errors = v.errors
        error_response = {
            'response': 400,
            'errors': errors
        }

        return make_response(error_response, 400)

    return True
