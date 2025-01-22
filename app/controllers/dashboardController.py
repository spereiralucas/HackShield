from app.models import Equipment, Vulnerabilities
from sqlalchemy import func, case
from app import db


class DashboardController():
    def __init__(self):
        super().__init__()
        self.db = db.session

    def list_charts(self):
        result = []
        try:
            equip = self.db.query(func.count(Equipment.id)).scalar()
            result.append({'total_equip': equip})

            faixas = case(
                (Vulnerabilities.severity.between(0.0, 0.0), 'non-risk'),
                (Vulnerabilities.severity.between(0.1, 3.9), 'low'),
                (Vulnerabilities.severity.between(4.0, 6.9), 'medium'),
                (Vulnerabilities.severity.between(7.0, 8.9), 'high'),
                (Vulnerabilities.severity.between(9.0, 10.0), 'critical')
            )

            critic = self.db.query(
                faixas.label('faixa_criticidade'),
                func.count(Vulnerabilities.severity)
            ).group_by(faixas).all()

            severity = {}
            for item in critic:
                result.append({item[0]: item[1]})

            result.append({'severity': severity})
            return {
                'response': 200,
                'dashboards': result,
                'severity': severity
            }

        except Exception as e:
            return {
                'response': 400,
                'message': f'ERROR: {e}'
            }
        finally:
            self.db.close()
