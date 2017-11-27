from scapy.all import *

ssid = []
def parseSSID(pkt):
    if pkt.haslayer(Dot11):
        print(pkt.show())
        if pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)
                print("SSID: pkt.info")

sniff(iface='en0', prn=ssid, count=10, timeout=3, store=0)
