from scapy.all import *

senderMac = "aa:aa:aa:aa:aa:aa"
broadcastMac = "ff:ff:ff:ff:ff:ff"


for ssid in open('ssidList.txt', 'r').readlines():
    pkt = RadioTap()/Dot11(type = 0, subtype = 4 ,addr1 = broadcastMac, addr2 = senderMac, addr3 = broadcastMac)/Dot11ProbeReq()/Dot11Elt(ID=0, info =ssid.strip()) / Dot11Elt(ID=1, info = "\x02\x04\x0b\x16") / Dot11Elt(ID=3, info="\x08")

    print ("Checking ssid:" + ssid)
    print(pkt.show())
    sendp (pkt, iface ="en0", count=1)
