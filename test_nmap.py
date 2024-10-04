import nmap3

scanner = nmap3.Nmap()
discover = nmap3.NmapHostDiscovery()

# test = nmap3.NmapScanTechniques()
# scanner.as_root = True
# a = scanner.scan_top_ports("192.168.16.98")
# b = scanner.nmap_version_detection("192.168.16.98")
# c = scanner.nmap_list_scan("192.168.16.98")
# d = scanner.nmap_detect_firewall("192.168.16.254") # Necessita root
# e = scanner.nmaptool # Aponta diretorio da lib
# f = scanner.default_command() # Imprime opções
# g = scanner.nmap_os_detection('192.168.16.98')  # Necessita root
# h = scanner.nmap_subnet_scan('192.168.16.98') # Necessita root
# i = scanner.nmap_stealth_scan("192.168.16.98")  # Necessita root
# jo = scanner.nmap_dns_brute_script("192.168.16.98")

opt = '+0.0'
host = input('Enter host: ')

teste = scanner.nmap_version_detection(
    host,
    args="--script vulners --script-args mincvss{}".format(opt)
)

lista = []
for key, value in teste.items():
    if type(value) is dict and value.get('ports'):
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

                        dict = {
                            'HOST': host,
                            'PROTOCOL': protocol,
                            'PORT': port,
                            'PORT STATE': port_state,
                            'SERVICE NAME': service_name,
                            'SERVICE APP': service_app,
                            'SERVICE VERSION': service_version,
                            'SERVICE DETAILS': service_details,
                            'SERVICE OS': service_os,
                            'VULN. ID': vuln_id,
                            'VULN. TYPE': vuln_type,
                            'VULN. EXPLOIT': vuln_exploit,
                            'VULN. SEVERITY': vuln_severity,
                            'VULN. URL': vuln_url
                        }
                        lista.append(dict)
                except KeyError:
                    try:
                        dict = {
                            'HOST': host,
                            'PROTOCOL': protocol,
                            'PORT': port,
                            'PORT STATE': port_state,
                            'SERVICE NAME': service_name,
                            'SERVICE APP': service_app,
                            'SERVICE VERSION': service_version,
                            'SERVICE DETAILS': service_details,
                            'SERVICE OS': service_os,
                            'VULN. ID': om['id'],
                            'VULN. TYPE': om['type'],
                            'VULN. EXPLOIT': True if om['is_exploit'] == 'true' else False,
                            'VULN. SEVERITY': om['cvss'],
                            'VULN. URL': f'https://vulners.com/{om["type"]}/{om["id"]}'
                        }
                        lista.append(dict)
                    except KeyError:
                        continue
                except Exception:
                    continue
            except KeyError:
                try:
                    dict = {
                        'HOST': host,
                        'PROTOCOL': protocol,
                        'PORT': port,
                        'PORT STATE': port_state,
                        'SERVICE NAME': service_name,
                        'SERVICE APP': service_app,
                        'SERVICE VERSION': service_version,
                        'SERVICE DETAILS': service_details,
                        'SERVICE OS': service_os,
                        'VULN. ID': om['id'],
                        'VULN. TYPE': om['type'],
                        'VULN. EXPLOIT': True if om['is_exploit'] == 'true' else False,
                        'VULN. SEVERITY': om['cvss'],
                        'VULN. URL': f'https://vulners.com/{om["type"]}/{om["id"]}'
                    }
                    lista.append(dict)
                except KeyError:
                    continue
    elif type(value) is list:
        continue
    else:
        continue

for item in lista:
    for subitem in item:
        print(f'{subitem}: {item[subitem]}')
    print('\n')

print(f'Total: {lista.__len__()} vulnerabilidades encontradas')
