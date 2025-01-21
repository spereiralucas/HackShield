from app import app
from app.utils.validator import validate
from app.utils.autentication import valid_user
from app.schemas.userSchema import login_schema
from flask import jsonify, make_response, request
from app.controllers.userController import UserController


@app.route('/user/auth', methods=['POST'])
# @validate(login_schema)
def auth():
    params = request.get_json(silent=True)
    username = params['username']
    password = params['password']

    valid_login, jwt_payload = valid_user(username, password)

    if valid_login == 503:
        response = {
            'response': 503,
            'msg': 'Service Off'
        }
    elif valid_login:
        response = {
            'response': 201,
            'auth': jwt_payload
        }
    else:
        response = {
            'response': 401,
            'msg': 'Invalid user or password'
        }
    result = jsonify(response)
    result.status_code = response['response']
    return make_response(result)


@app.route('/user/add', methods=['POST'])
def add_user():
    usr = UserController()
    new = usr.add(request=dict(request.form))

    new_usr = jsonify(new)

    return make_response(new_usr)
