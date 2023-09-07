from app import db
from sqlalchemy.sql import func


def BaseModel():
    id = db.Column(db.Integer, primary_key=True)
    date_insert = db.Column(db.DateTime(timezone=True), default=func.now())
    date_last_update = db.Column(
        db.DateTime(timezone=True), default=func.now(), onupdate=func.now())

    return id, date_insert, date_last_update
