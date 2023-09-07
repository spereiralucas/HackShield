import nmap3
import json

scanner = nmap3.Nmap()
discover = nmap3.NmapHostDiscovery()

import pdb; pdb.set_trace();
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

# import pdb; pdb.set_trace();
host = input('Enter host: ')

k = scanner.nmap_version_detection(
    host,
    args="--script vulners --script-args mincvss{}".format(opt))

n = json.dumps(k)

print(n)
