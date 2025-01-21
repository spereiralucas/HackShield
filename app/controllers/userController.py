from app.utils.isAdmin import is_admin
from app.models.user import User
from app import constants as cons
from app import db
import hashlib


class UserController():
    def __init__(self):
        super().__init__()
        self.db = db

    def add(self, request):
        user_admin = is_admin(self)

        # if user_admin is False:
        #     response = {
        #         "response": 401,
        #         "message": "Unhauthorized credentials"
        #     }

        # else:
        try:
            cript_password = "{}{}".format(
                request.get('password'),
                cons['PASSWORD_SECRET']
            )

            cript_password = hashlib.md5(
                bytes(cript_password, "utf-8")
            )

            user = User(
                username=request.get("username"),
                password=cript_password.hexdigest(),
                name=request.get("name"),
                surname=request.get("surname"),
                email=request.get("email"),
                level=request.get("level"),
                active=int(request.get("active"))
            )

            db.session.add(user)
            db.session.commit()

            response = {
                "status_code": 201,
                "message": "User {} successfully added!".format(
                    request.get("username")
                )
            }

        except Exception as e:
            response = {
                "status_code": 400,
                "message": f"ERROR: {e}"
            }

        return response
