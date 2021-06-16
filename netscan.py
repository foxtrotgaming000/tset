#!/usr/bin/python

import scapy.all as scapy
import optparse

parser = optparse.OptionParser()
parser.add_option('-t', '--target', dest='target', help='Target(s) of the Network Scanner')
(options, arguments) = parser.parse_args()

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    arp_request_broadcast = broadcast/arp_request
    answered = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients = []
    for e in answered:
        client_dict = {'ip': e[1].psrc, 'mac': e[1].hwsrc}
        clients.append(client_dict)
    return clients

def print_result(results):
    print('\nIP\t\t\tMAC_ADDRESS\n-----------------------------------------')
    for e in results:
        print(e['ip'], '\t   ', e['mac'])

scan_result = scan(options.target)
print_result(scan_result)
