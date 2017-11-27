from scapy.all import *

host = 'rejahrehim.com'
ip = socket.gethostbyname(host)
port = 80

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
        p = IP(dst=ip)/TCP(sport=src_port, dport=port, flags='A', seq=12345)
        resp = sr1(p, timeout=2) # Sending packet
        if str(type(resp)) == "<type 'NoneType'>":
            result = 1
        elif resp.haslayer(TCP):
            if resp.getlayer(TCP).flags == 0x4:
                result = 0
            elif (int(resp.getlayer(ICMP).type)==3 and int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]):
                result = 1

    except Exception as e:
        pass

    return result


if __name__ == '__main__':
    conf.verb = 0 
    if is_up(ip):
            response = probe_port(ip, port)
            if response == 1:
                 print ("Filtered | Stateful firewall present")
            elif response == 0:
                 print ("Unfiltered | Stateful firewall absent")
    else:
        print ("Host is Down")


