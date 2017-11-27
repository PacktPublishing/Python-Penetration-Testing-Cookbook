from scapy.all import *
from pprint import pprint

pkts = sniff(filter="arp",count=10)
print(pkts.summary())