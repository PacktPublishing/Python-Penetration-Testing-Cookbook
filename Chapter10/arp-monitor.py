#! /usr/bin/env python

from scapy.all import *

def parsePacket(pkt):

    if ARP in pkt and pkt[ARP].op in (1,2): 
        return pkt.sprintf("%ARP.hwsrc% %ARP.psrc%")
    
sniff(prn=parsePacket, filter="arp", store=0)
