import jwt
from app import constants as cons
from flask import request
from app.models.user import User


def is_admin(self):
    current_user = get_user_hash(request.headers['Auth'])['user']
    admin = get_admin(self, current_user)

    return admin


def get_user_hash(encoded_hash):
    # Returns decoded user hash (expiration time, user, password)
    JWT_SECRET = cons['JWT_SECRET']
    try:
        jwt_payload = jwt.decode(
            encoded_hash, JWT_SECRET, algorithms=["HS256"])
        return jwt_payload

    except Exception:
        pass


def get_admin(self, user):
    isAdmin = self.db.session.query(
        User.username,
        User.level
    ).filter(User.username == user)

    for i in isAdmin.all():
        if i.level == 1:
            return True
        elif i.is_admin is True:
            return True
        else:
            return False


def get_current_user(self):
    cur_user = get_user_hash(
        request.headers['Auth'])['user']

    query = self.db.session.query(
        User.id
    ).filter_by(username=cur_user)

    for i in query.all():
        current_id = i.id

    return current_id
