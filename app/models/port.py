from app import db
from app.models.__base__ import BaseModel


class Port(db.Model):
    __tablename__ = 'port'

    id, date_insert, date_last_update = BaseModel()

    port = db.Column(db.Integer, nullable=False)
    state = db.Column(db.Boolean)
    protocol = db.Column(db.ForeignKey('protocol.id'))
    service = db.Column(db.String(255))

    def __init__(self, port, state, protocol, service):
        self.port = port
        self.state = state
        self.protocol = protocol
        self.service = service

    def __repr__(self):
        return "%r" % self.port
