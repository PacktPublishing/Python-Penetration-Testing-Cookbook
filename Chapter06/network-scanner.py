import socket, re
from scapy.all import *

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
ip = s.getsockname()[0]
 
#Get the Local IP
end = re.search('^[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.[\d]{1,3}', ip)

print (end)
create_ip = re.search('^[\d]{1,3}.[\d]{1,3}.[\d]{1,3}.', ip)
 
def is_up(ip):
    icmp = IP(dst=ip)/ICMP()
    resp = sr1(icmp, timeout=10)
    if resp == None:
        return False
    else:
        return True 
def CheckLoopBack(ip):
    if (end.group(0) == '127.0.0.1'):
        return True
 
try:
    if not CheckLoopBack(create_ip):
        conf.verb = 0 
        for i in range(1, 10):
            test_ip = str(create_ip.group(0)) + str(i)
            if is_up(test_ip):
                print (test_ip + " Is Up")
except KeyboardInterrupt:
    print('interrupted!')
