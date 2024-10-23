from app import db
from app.models.__base__ import BaseModel


class ScanEquipment(db.Model):
    __tablename__ = 'n2n_scan_equipment'

    id, date_insert, date_last_update = BaseModel()

    scan = db.Column(db.ForeignKey('scan.id'))
    equipment = db.Column(db.ForeignKey('equipment.id'))

    def __init__(self, scan, equipment):
        self.scan = scan
        self.equipment = equipment

    def __repr__(self):
        return "%r" % self.id
