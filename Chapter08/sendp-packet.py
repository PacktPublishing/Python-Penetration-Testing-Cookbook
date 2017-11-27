from scapy.all import *
from pprint import pprint

network = IP(dst = '192.168.1.1')
transport = ICMP()
packet = network/transport
send(packet)
