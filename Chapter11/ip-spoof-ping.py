
from scapy.all import *

iface = "en0"
fake_ip = '192.168.1.3'
destination_ip = '192.168.1.5'
dns_destination ='8.8.8.8'
def ping(source, destination, iface):
    srloop(IP(src=source,dst=destination)/ICMP(), iface=iface)

def dnsQuery(source, destination, iface):
    sr1(IP(dst=destination,src=source)/UDP()/DNS(rd=1,qd=DNSQR(qname="example.com")))


try:
    print ("Starting Ping")
    # ping(fake_ip,destination_ip,iface)
    dnsQuery(fake_ip,dns_destination,iface)

except KeyboardInterrupt:
    print("Exiting.. ")
    sys.exit(0)

