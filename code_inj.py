#!/usr/bin/python
# 2 #
import netfilterqueue
import re
import scapy.all as scapy

rpat = r'Accept-Encoding:.*?\\r\\n'

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    scp = scapy_packet
    if scp.haslayer(scapy.Raw):
        if scp[scapy.TCP].dport == 80:
            print('request > \n')
            modload = re.sub(rpat, '', scp[scapy.Raw].load)
            newpack = set_load(scp(modload))
            packet.set_payload(str(newpack))    
            
        elif scp[scapy.TCP].sport == 80:
            print('responce > \n')
            print(scp.show())
        
    
    packet.accept()
                
                
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
