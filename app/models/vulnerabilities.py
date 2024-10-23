from app import db
from app.models.__base__ import BaseModel


class Vulnerabilities(db.Model):
    __tablename__ = 'vulnerabilities'

    id, date_insert, date_last_update = BaseModel()

    vuln_id = db.Column(db.String(255))
    is_exploit = db.Column(db.Boolean)
    severity = db.Column(db.Float)
    type = db.Column(db.ForeignKey('vulnerability_type.id'))
    url = db.Column(db.String(255))
    port = db.Column(db.ForeignKey('port.id'))

    def __init__(self, vuln_id, is_exploit,
                 severity, type, url, port):
        self.vuln_id = vuln_id
        self.is_exploit = is_exploit
        self.severity = severity
        self.type = type
        self.url = url
        self.port = port

    def __repr__(self):
        return '%r' % self.vuln_id
