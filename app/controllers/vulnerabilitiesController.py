from nmap3 import Nmap
from app import app, db
from flask import request
from app.models import Vulnerabilities


class VulnerabilitiesController():
    def __init__(self):
        super().__init__()
        self.scanner = Nmap()
        self.db = db

    def get_vulnerabilities(self, address, level):
        lista = []

        teste = self.scanner.nmap_version_detection(
            address,
            args="--script vulners --script-args mincvss{}".format(level)
        )
        for key, value in teste.items():
            if isinstance(value, dict) and value.get('ports'):
                for i in value['ports']:
                    try:
                        protocol = i['protocol']
                        port = i['portid']
                        port_state = i['state']
                        service_name = i['service']['name']
                        service_app = i['service']['product']
                        service_version = i['service']['version']
                        service_details = i['service']['extrainfo']
                        service_os = i['service'].get('ostype')
                        try:
                            for om in i['scripts'][0]['data'][i['cpe'][0]['cpe']]['children']:
                                vuln_id = om['id']
                                vuln_type = om['type']
                                vuln_exploit = True if om['is_exploit'] == 'true' else False
                                vuln_url = f'https://vulners.com/{vuln_type}/{vuln_id}'
                                vuln_severity = om['cvss']

                                diction = {
                                    'host': address,
                                    'protocol': protocol,
                                    'port': port,
                                    'port_state': port_state,
                                    'service_name': service_name,
                                    'service_app': service_app,
                                    'service_version': service_version,
                                    'service_details': service_details,
                                    'service_os': service_os,
                                    'vuln_id': vuln_id,
                                    'vuln_type': vuln_type,
                                    'vuln_exploit': vuln_exploit,
                                    'vuln_severity': vuln_severity,
                                    'vuln_url': vuln_url
                                }
                                lista.append(diction)
                        except KeyError:
                            try:
                                diction = {
                                    'host': address,
                                    'protocol': protocol,
                                    'port': port,
                                    'port_state': port_state,
                                    'service_name': service_name,
                                    'service_app': service_app,
                                    'service_version': service_version,
                                    'service_details': service_details,
                                    'service_os': service_os,
                                    'vuln_id': om['id'],
                                    'vuln_type': om['type'],
                                    'vuln_exploit': True if om['is_exploit'] == 'true' else False,
                                    'vuln_severity': om['cvss'],
                                    'vuln_url': f'https://vulners.com/{om["type"]}/{om["id"]}'
                                }
                                lista.append(diction)
                            except KeyError:
                                continue
                        except Exception:
                            continue
                    except KeyError:
                        try:
                            diction = {
                                'host': address,
                                'protocol': protocol,
                                'port': port,
                                'port_state': port_state,
                                'service_name': service_name,
                                'service_app': service_app,
                                'service_version': service_version,
                                'service_details': service_details,
                                'service_os': service_os,
                                'vuln_id': om['id'],
                                'vuln_type': om['type'],
                                'vuln_exploit': True if om['is_exploit'] == 'true' else False,
                                'vuln_severity': om['cvss'],
                                'vuln_url': f'https://vulners.com/{om["type"]}/{om["id"]}'
                            }
                            lista.append(diction)
                        except KeyError:
                            continue
            elif isinstance(value, list):
                continue
            else:
                continue

        return {
            'status_code': 200,
            'total': lista.__len__(),
            'vulnerabilities': lista
        }
