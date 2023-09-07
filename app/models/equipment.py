from app import db
from app.models.__base__ import BaseModel


class Equipment(db.Model):
    __tablename__ = 'equipment'

    id, date_insert, date_last_update = BaseModel()

    host = db.Column(db.String(15), unique=True)
    port = db.Column(db.Text)
    protocol = db.Column(db.String(20))
    reference = db.Column(db.Text)
    impact = db.Column(db.Text)
    solution = db.Column(db.Text)

    def __init__(self, vuln_id, vulnerability, port, protocol,
                 reference, impact, solution):
        self.vuln_id = vuln_id
        self.vulnerability = vulnerability
        self.port = port
        self.protocol = protocol
        self.reference = reference
        self.impact = impact
        self.solution = solution

    def __repr__(self):
        return "%r" % self.vuln_id
