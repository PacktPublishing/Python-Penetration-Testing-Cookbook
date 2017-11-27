from scapy.all import *

ap_list = []
def ssid(pkt):
    # print(pkt.show())
    if pkt.haslayer(Dot11):
        print(pkt.show())
        if pkt.type == 0 and pkt.subtype == 8:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)
                print("AP: %s SSID: %s" % (pkt.addr2, pkt.info))

sniff(iface='en0', prn=ssid, count=10, timeout=3, store=0)
# for packet in sniff(offline='sample.pcap', prn=changePacketParameters):
#     packets.append(packet)

# for packet in packets:
#     if packet.haslayer(TCP):
#         writeToPcapFile(packet)
#         print(packet.show())