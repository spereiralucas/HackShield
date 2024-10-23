from app import db
from app.models.__base__ import BaseModel


class Equipment(db.Model):
    __tablename__ = 'equipment'

    id, date_insert, date_last_update = BaseModel()

    host = db.Column(db.String(15), unique=True)
    hostname = db.Column(db.String(255), unique=True, nullable=True)
    os = db.Column(db.String(50))

    def __init__(self, host, hostname, os):
        self.host = host
        self.hostname = hostname
        self.os = os

    def __repr__(self):
        return "%r" % self.hostname
