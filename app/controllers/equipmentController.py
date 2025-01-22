from app.models import Equipment
from app import constants as cons
from app import db


class EquipmentController():
    def __init__(self):
        super().__init__()
        self.db = db.session

    def list(self):
        result = []
        try:
            equipment = self.db.query(
                Equipment.id,
                Equipment.date_insert,
                Equipment.host,
                Equipment.hostname,
                Equipment.os
            )

            for item in equipment.all():
                equip = {
                    'id': item[0],
                    'date_insert': item[1].strftime('%d/%m/%Y %H:%M:%S'),
                    'host': item[2],
                    'hostname': item[3],
                    'os': item[4]
                }

                result.append(equip)

            return {
                'response': 200,
                'count': result.__len__(),
                'equipments': result
            }

        except Exception as e:
            return {
                'response': 400,
                'items': e
            }
        finally:
            self.db.close()
