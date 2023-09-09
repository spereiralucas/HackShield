from app.utils.isAdmin import is_admin
from app.models.user import User
from app import constants as cons
from app import db
from flask import request
import hashlib


class UserController():
    def __init__(self):
        super().__init__()

    @staticmethod
    def add(self):
        user_admin = is_admin(self)

        if user_admin is False:
            response = {
                "response": 401,
                "message": "Unhauthorized credentials"
            }

        else:
            try:
                cript_password = "{}{}".format(
                    request.form.get('password'),
                    cons['PASSWORD_SECRET']
                )

                cript_password = hashlib.md5(
                    bytes(cript_password, "utf-8")
                )

                user = User(
                    username=request.form.get("username"),
                    password=cript_password,
                    name=request.form.get("name"),
                    surname=request.form.get("surname"),
                    email=request.form.get("email"),
                    level=request.form.get("level"),
                    active=request.form.get("active")
                )

                db.session.add(user)
                db.session.commit()

                response = {
                    "response": 201,
                    "message": "User {} successfully added!".format(
                        request.form.get("username")
                    )
                }

            except Exception as e:
                response = {
                    "response": 400,
                    "message": f"ERROR: {e}"
                }

        return response
