from app import db
from app.models.__base__ import BaseModel


class User(db.Model):
    __tablename__ = 'user'

    id, date_insert, date_last_update = BaseModel()

    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(50), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    level = db.Column(db.Integer, nullable=False)
    active = db.Column(db.Boolean, nullable=False)

    def __init__(self, username, password, name,
                 surname, email, level, active):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname
        self.email = email
        self.level = level
        self.active = active

    def __repr__(self):
        return "%r" % self.username
