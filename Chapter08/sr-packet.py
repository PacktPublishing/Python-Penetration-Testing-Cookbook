from scapy.all import *

ethernet = Ether()
network = IP(dst = 'rejahrehim.com')
transport = TCP(dport=80)
packet = ethernet/network/transport
# sr(packet, iface="en0")

sr1(packet, iface="en0")
