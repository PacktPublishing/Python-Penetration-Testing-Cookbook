from scapy.all import *

packets = []

def changePacketParameters(packet):
    packet[Ether].dst = '00:11:22:dd:bb:aa'
    packet[Ether].src = '00:11:22:dd:bb:aa'

def writeToPcapFile(pkt):
    wrpcap('filteredPackets.pcap', pkt, append=True)

for packet in sniff(offline='sample.pcap', prn=changePacketParameters):
    packets.append(packet)

for packet in packets:
    if packet.haslayer(TCP):
        writeToPcapFile(packet)
        print(packet.show())

sendp(packets)
# wrpcap("editted.cap", packets)