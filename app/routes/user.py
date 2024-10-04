from app import app
from flask import jsonify, make_response, request
from app.controllers.userController import UserController


@app.route('/user/add', methods=['POST'])
def add_user():
    usr = UserController()
    new = usr.add(request=dict(request.form))

    new_usr = jsonify(new)

    return make_response(new_usr)
