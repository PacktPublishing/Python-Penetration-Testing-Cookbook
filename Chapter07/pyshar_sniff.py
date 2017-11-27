import pyshark
cap = pyshark.LiveCapture(interface='en0', bpf_filter='ip and tcp port 80')

cap.sniff(timeout=5)

for pkt in cap:
	print(pkt.highest_layer)