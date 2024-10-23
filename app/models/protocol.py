from enum import Enum
from app import db
from app.models.__base__ import BaseModel


class Protocol(db.Model):
    __tablename__ = 'protocol'

    id, date_insert, date_last_update = BaseModel()

    name = db.Column(db.String(20))
    description = db.Column(db.Text)


class ProtocolEnum(Enum):
    P_20 = 'FTP'
    P_21 = 'FTP'
    P_22 = 'SSH'
    P_23 = 'Telnet'
    P_25 = 'SMTP'
    P_53 = 'DNS'
    P_57 = 'DHCP'
    P_58 = 'DHCP'
    P_59 = 'TFTP'
    P_80 = 'HTTP'
    P_110 = 'POP3'
    P_119 = 'NNTP'
    P_123 = 'NTP'
    P_137 = 'NetBIOS'
    P_138 = 'NetBIOS'
    P_139 = 'NetBIOS'
    P_143 = 'IMAP'
    P_161 = 'SNMP'
    P_162 = 'SNMPTRAP'
    P_179 = 'BGP'
    P_194 = 'IRC'
    P443 = 'HTTPS'
    P445 = 'SMB'
    P465 = 'SMTPS'
    P_514 = 'Syslog'
    P_515 = 'LPD'
    P_993 = 'IMAPS'
    P_995 = 'POP3S'
    P_1433 = 'MS-SQL'
    P_1434 = 'MS-SQL Monitor'
    P_1521 = 'Oracle DB'
    P_2049 = 'NFS'
    P_2082 = 'cPanel'
    P_2083 = 'cPanel (SSL)'
    P_3306 = 'MySQL'
    P_3389 = 'RDP'
    P_5432 = 'PostgreSQL'
    P_5900 = 'VNC'
    P_3379 = 'Redis'
    P_8080 = 'HTTP-Proxy'
    P_8443 = 'HTTPS-Proxy'
    P_9200 = 'Elasticsearch'
    P_11211 = 'Memcached'
    P_27017 = 'MongoDB'


'''
    20 – FTP-DATA – Transferência de Dados (FTP)
    21 – FTP – File Transfer Protocol
    22 – SSH – Secure Shell
    23 – Telnet – Controle remoto (não seguro)
    25 – SMTP – Simple Mail Transfer Protocol
    53 – DNS – Domain Name System
    67 – DHCP – Dynamic Host Configuration Protocol (cliente)
    68 – DHCP – Dynamic Host Configuration Protocol (servidor)
    69 – TFTP – Trivial File Transfer Protocol
    80 – HTTP – Hypertext Transfer Protocol
    110 – POP3 – Post Office Protocol v3
    119 – NNTP – Network News Transfer Protocol
    123 – NTP – Network Time Protocol
    137 – NetBIOS – Name Service
    138 – NetBIOS – Datagram Service
    139 – NetBIOS – Session Service
    143 – IMAP – Internet Message Access Protocol
    161 – SNMP – Simple Network Management Protocol
    162 – SNMPTRAP – SNMP Trap (alertas)
    179 – BGP – Border Gateway Protocol
    194 – IRC – Internet Relay Chat
    443 – HTTPS – Hypertext Transfer Protocol Secure
    445 – SMB – Server Message Block (compartilhamento de arquivos)
    465 – SMTPS – SMTP com SSL/TLS
    514 – Syslog – Registro de eventos em rede
    515 – LPD – Line Printer Daemon
    993 – IMAPS – IMAP com SSL/TLS
    995 – POP3S – POP3 com SSL/TLS
    1433 – MS-SQL – Microsoft SQL Server
    1434 – MS-SQL Monitor – Microsoft SQL Server Monitor
    1521 – Oracle DB – Oracle Database Listener
    2049 – NFS – Network File System
    2082 – cPanel – Interface de gerenciamento web
    2083 – cPanel (SSL) – Interface de gerenciamento web com SSL
    3306 – MySQL – Banco de dados MySQL
    3389 – RDP – Remote Desktop Protocol
    5432 – PostgreSQL – Banco de dados PostgreSQL
    5900 – VNC – Virtual Network Computing
    6379 – Redis – Banco de dados Redis
    8080 – HTTP-Proxy – Proxy HTTP alternativo
    8443 – HTTPS-Proxy – Proxy HTTPS alternativo
    9200 – Elasticsearch – API HTTP do Elasticsearch
    11211 – Memcached – Cache distribuído
    27017 – MongoDB – Banco de dados MongoDB
'''
