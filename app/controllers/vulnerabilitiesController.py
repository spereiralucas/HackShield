import socket
from app import db
from nmap3 import Nmap
from datetime import datetime
from app.models import Vulnerabilities, Equipment, Scan, Port, \
    Protocol, ScanType, EquipmentPort, ScanEquipment, VulnerabilityType


class VulnerabilitiesController():
    def __init__(self):
        super().__init__()
        self.scanner = Nmap()
        self.db = db.session

    def get_vulnerabilities(self, address, script, level):
        start = datetime.now()
        lista = []

        teste = self.scanner.nmap_version_detection(
            address,
            args="--script {} --script-args mincvss{}".format(script, level)
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

        # import pdb; pdb.set_trace();
        self.insert_vulnerability(
            sc_type=script, start=start, end=datetime.now(),
            vuln={'total': lista.__len__(), 'vulnerabilities': lista})

        return {
            'status_code': 200,
            'total': lista.__len__(),
            'vulnerabilities': lista
        }

    def insert_vulnerability(self, sc_type=str, start=datetime,
                             end=datetime, vuln=dict):

        scan = Scan(start=start, end=end, scan_type=None)
        self.db.add(scan)
        self.db.flush()

        for i in vuln['vulnerabilities']:
            try:
                # Equipment
                equipment = self.db.query(
                    Equipment).filter_by(host=i['host']).first()
                if not equipment:
                    equipment = Equipment(
                        host=i['host'],
                        hostname=self.get_hostname(i['host']),
                        os=i['service_os'])
                    self.db.add(equipment)
                    self.db.flush()

                # Protocol
                protocol = self.db.query(
                    Protocol).filter_by(name=i['protocol']).first()
                if not protocol:
                    protocol = Protocol(name=i['protocol'])
                    self.db.add(protocol)
                    self.db.flush()

                # Port
                port = self.db.query(Port).filter_by(port=i['port']).first()
                if not port:
                    port = Port(
                        port=i['port'],
                        state=True if i['port_state'] == 'open' else False,
                        protocol=protocol.id,
                        service=f'{i["service_name"]} - {i["service_app"]} - {i["service_version"]}')
                    self.db.add(port)
                    self.db.flush()

                # EquipmentPort
                n2n = EquipmentPort(equipment=equipment.id, port=port.id)
                self.db.add(n2n)
                self.db.flush()

                # Vulnerability Type
                vulnType = self.db.query(
                    VulnerabilityType).filter_by(name=i['vuln_type']).first()
                if not vulnType:
                    vulnType = VulnerabilityType(name=i['vuln_type'])
                    self.db.add(vulnType)
                    self.db.flush()

                # Vulnerability
                vulner = self.db.query(
                    Vulnerabilities).filter_by(vuln_id=i['vuln_id']).first()
                if not vulner:
                    vulner = Vulnerabilities(
                        vuln_id=i['vuln_id'],
                        is_exploit=i['vuln_exploit'],
                        severity=float(i['vuln_severity']),
                        type=vulnType.id,
                        url=i['vuln_url'],
                        port=port.id
                    )

                    self.db.add(vulner)
                    self.db.flush()

                # ScanType
                scanType = self.db.query(
                    ScanType).filter_by(type=sc_type).first()
                if not scanType:
                    scanType = ScanType(type=sc_type, description=None)
                    self.db.add(scanType)
                    self.db.flush()

                scan.scan_type = scanType.id
                self.db.add(scan)
                self.db.flush()

                scanEquip = ScanEquipment(scan=scan.id, equipment=equipment.id)
                self.db.add(scanEquip)
                self.db.flush()
                self.db.commit()

            except Exception as e:
                self.db.rollback()
                import pdb; pdb.set_trace();
                print(f'ERROR: {e}')

    def list(self, id=None):
        try:
            query = self.db.query(
                Vulnerabilities.id,
                Vulnerabilities.date_insert,
                Vulnerabilities.vuln_id,
                Vulnerabilities.is_exploit,
                Vulnerabilities.severity,
                Vulnerabilities.url,
                Vulnerabilities.port.label('id_port'),
                Port.port,
                Port.state,
                Port.service,
                Port.protocol,
                Protocol.name,
                Protocol.description,
                Equipment.host,
                Equipment.hostname,
                Equipment.os
            ).join(Port,
                   Port.id == Vulnerabilities.port
            ).join(Protocol,
                   Protocol.id == Port.protocol
            ).join(EquipmentPort,
                   EquipmentPort.id == Port.id
            ).join(Equipment,
                   Equipment.id == EquipmentPort.equipment
            ).order_by(Vulnerabilities.id.asc())

            if id:
                # query = query.filter(Equipment.id == id).first()
                pass

            list = []
            for i in query.all():
                vuln = {
                    'id': i.id,
                    'date': i.date_insert.strftime('%d, %b %Y %H:%M:%S'),
                    'vuln_id': i.vuln_id,
                    'exploit': i.is_exploit,
                    'severity': i.severity,
                    'url_doc': i.url,
                    'port': i.port,
                    'port_state': i.state,
                    'service': i.service,
                    'protocol': i.name,
                    'description': i.description,
                    'host': i.host,
                    'hostname': i.hostname,
                    'os': i.os
                }
                list.append(vuln)

            return {
                'response': 200,
                'vulnerabilities': list
            }

        except Exception as e:
            return {
                'response': 400,
                'msg': f'Error: {e}'
            }

    @staticmethod
    def get_hostname(ip):
        try:
            return socket.gethostbyaddr(ip)[0]
        except Exception:
            return None
