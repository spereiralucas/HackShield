from app import db
from app.models.__base__ import BaseModel


class ScanType(db.Model):
    __tablename__ = 'scan_type'

    id, date_insert, date_last_update = BaseModel()

    type = db.Column(db.String(255))
    description = db.Column(db.Text)

    def __init__(self, type, description):
        self.type = type
        self.description = description

    def __repr__(self):
        return "%r" % self.type
