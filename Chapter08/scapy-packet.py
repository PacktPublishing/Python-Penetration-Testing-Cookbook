from scapy.all import *
from pprint import pprint

ethernet = Ether()
network = IP(dst = ['rejahrehim.com', '192.168.1.1', '192.168.1.2'])
# transport = TCP(dport=53, flags = 'S')
transport = TCP(dport=[(53, 100)], flags = 'S')
packet = ethernet/network/transport
# pprint(packet)
# pprint([pkt for pkt in packet])

for pkt in packet:
	# ls(pkt)
	pkt.show()
