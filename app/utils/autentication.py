import jwt
import datetime as dt
from app import constants as cons


def create_jwt_hash(username, password):
    pass


def valid_user(user, password):
    expire_date = dt.datetime.utcnow() + dt.timedelta(
        seconds=cons['JWT_EXPIRE_TIME']
    )

    jwt_payload = jwt.encode(
        {
            "exp": cons['JWT_EXPIRE_TIME'],
            "user": user,
            "password": password
        },
        cons['JWT_SECRET']
    )
    return expire_date, jwt_payload
