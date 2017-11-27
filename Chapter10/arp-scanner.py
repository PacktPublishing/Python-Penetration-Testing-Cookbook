from scapy.all import *

interface = "en0"
ip_rage = "192.168.1.1/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

conf.verb = 0
ans, unans = srp(Ether(dst=broadcastMac)/ARP(pdst = ip_rage), timeout =2, iface=interface, inter=0.1)

for send,recive in ans:
	print (recive.sprintf(r"%Ether.src% - %ARP.psrc%"))