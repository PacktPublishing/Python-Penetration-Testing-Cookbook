from scapy.all import *
import sys
import random
import os

ssid = "fakeap" 
iface = "en0"

dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=str(RandMAC()), addr3=str(RandMAC()))
dot11beacon = Dot11Beacon(cap='ESS+privacy')
dot11essid = Dot11Elt(ID='SSID',info=ssid, len=len(ssid))
rsn = Dot11Elt(ID='RSNinfo', info=(
  '\x01\x00'                 #For RSN Version 1
  '\x00\x0f\xac\x02'         #Group Cipher Suite : 00-0f-ac TKIP
  '\x02\x00'                 #2 Pairwise Cipher Suites (next two lines)
  '\x00\x0f\xac\x04'         #AES Cipher
  '\x00\x0f\xac\x02'         #TKIP Cipher
  '\x01\x00'                 #1 Authentication Key Managment Suite (line below)
  '\x00\x0f\xac\x02'         #Pre-Shared Key
  '\x00\x00'))               #RSN Capabilities (no extra capabilities)


frame = RadioTap()/dot11/dot11beacon/dot11essid/rsn
print (ssid,frame)

sendp(frame, iface=iface, inter=0.0100 if len(frames)<10 else 0, loop=1)
