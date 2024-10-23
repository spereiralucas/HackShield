from app import db
from app.models.__base__ import BaseModel


class EquipmentPort(db.Model):
    __tablename__ = 'n2n_equipment_port'

    id, date_insert, date_last_update = BaseModel()

    equipment = db.Column(db.ForeignKey('equipment.id'))
    port = db.Column(db.ForeignKey('port.id'))

    def __init__(self, equipment, port):
        self.equipment = equipment
        self.port = port

    def __repr__(self):
        return "%r" % self.id
