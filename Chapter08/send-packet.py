from scapy.all import *
from pprint import pprint

ethernet = Ether()
network = IP(dst = '192.168.1.1')
transport = ICMP()
packet = ethernet/network/transport
sendp(packet, iface="en0")
