import pyshark
cap = pyshark.FileCapture('sample.pcap')
print(cap)
print(cap[0])
print(dir(cap[0]))

for pkt in cap:
	print(pkt.highest_layer)