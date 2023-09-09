from app import db
from app.models.__base__ import BaseModel


class Scan(db.Model):
    __tablename__ = 'scan'

    id, date_insert, date_last_update = BaseModel()

    start = db.Column(db.DateTime)
    end = db.Column(db.DateTime)
    scan_type = db.Column(db.ForeignKey('scan_type.id'))

    def __init__(self, start, end, scan_type):
        self.start = start
        self.end = end
        self.scan_type = scan_type

    def __repr__(self):
        return "%r" % self.id
