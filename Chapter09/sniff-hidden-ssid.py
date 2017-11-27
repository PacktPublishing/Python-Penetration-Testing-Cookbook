from scapy.all import *

hiddenSSIDs = dict()

def parseSSID(pkt):
    if pkt.haslayer(Dot11Beacon) or pkt.haslayer(Dot11ProbeResp):
        if not hiddenSSIDs.has_key(pkt[Dot11].addr3):
            ssid       = pkt[Dot11Elt].info
            bssid      = pkt[Dot11].addr3
            channel    = int( ord(pkt[Dot11Elt:3].info))
            capability = pkt.sprintf("{Dot11Beacon:%Dot11Beacon.cap%}\{Dot11ProbeResp:%Dot11ProbeResp.cap%}")

            if re.search("privacy", capability): 
                encrypted = 'Y'
            else: 
                encrypted  = 'N'
            hiddenSSIDs[pkt[Dot11].addr3] =[encrypted, ssid, bssid, channel] 
            print (hiddenSSIDs)

sniff(iface='wlp3s0b1', prn=parseSSID, count=10, timeout=3, store=0)
