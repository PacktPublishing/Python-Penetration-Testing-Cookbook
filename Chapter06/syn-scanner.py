from scapy.all import *

host = 'www.dvwa.co.uk'
ip = socket.gethostbyname(host)

openp = []
filterdp = []
common_ports = { 21, 22, 23, 25, 53, 69, 80, 88, 109, 110, 
                 123, 137, 138, 139, 143, 156, 161, 389, 443, 
                 445, 500, 546, 547, 587, 660, 995, 993, 2086, 
                 2087, 2082, 2083, 3306, 8443, 10000 
                }
def is_up(ip):
    icmp = IP(dst=ip)/ICMP()
    resp = sr1(icmp, timeout=10)
    if resp == None:
        return False
    else:
        return True

def probe_port(ip, port, result = 1):
    src_port = RandShort()
    try:
        p = IP(dst=ip)/TCP(sport=src_port, dport=port, flags='S')
        resp = sr1(p, timeout=2) # Sending packet
        if str(type(resp)) == "<type 'NoneType'>":
            result = 0
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x12:
                send_rst = sr(IP(dst=ip)/TCP(sport=src_port, dport=port, flags='AR'), timeout=1)
                result = 1
            elif resp.getlayer(TCP).flags == 0x14:
                result = 0
            elif (int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                result = 2
    except Exception as e:
        pass

    return result


if __name__ == '__main__':
    conf.verb = 0 
    if is_up(ip):
        for port in common_ports:
            print (port)
            response = probe_port(ip, port)
            if response == 1:
                openp.append(port)

        if len(openp) != 0:
            print ("Open Ports:")
            print (openp)
        else:
            print ("Sorry, No open ports found.!!")

        if len(filterdp) != 0:
            print ("Possible Filtered Ports:")
            print (filterdp)
    else:
        print ("Host is Down")


