import sys
from scapy.all import *

interface = "en0"

def callBackParser(packet):
    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
            print("From : " + str(source_ip) + " to -> " + str(destination_ip) + "( " + str(packet.getlayer(DNS).qd.qname) + " )")

        if packet.haslayer(TCP):
            try:
                if packet[TCP].dport == 80 or packet[TCP].sport == 80:
                    print(packet[TCP].payload)	
            except:
                pass
sniff(iface=interface, prn=callBackParser)
