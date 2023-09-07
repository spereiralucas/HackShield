import nmap3
from app import app, db
from flask import request
from app.models import Vulnerabilities


class VulnerabilitiesController():
    def __init__(self):
        super().__init__()

    def get_vulnerabilities(self):
        scanner = nmap3.Nmap()

        host = request.form.get('host')
        mincvss = request.form.get('criticity')

        try:
            import pdb; pdb.set_trace();
            sweep = scanner.nmap_version_detection(
                host,
                args="--script vulners --script-args mincvss{}"
                .format(mincvss))

            if len(sweep[host]['ports']) > 0:
                for i in sweep[host]['ports']:
                    print(i)

            response = {
                "response": 200,
                "msg": sweep
            }

        except Exception as e:
            response = {
                "response": 400,
                "msg": "ERROR: {}".format(e)
            }

        return response
