# Functions = organized blocks of reusable code.
# Python functions begin with the def keyword.
# Continuing with the previous FTP vulnerability-scanning example, let's create
# a function to perform just the action of connecting to the FTP server and
# returning the banner.

import socket

def retBanner(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        # Like that? If it fouls up, just return None.
        return

def not_dunder_main():
    ip1 = '192.168.95.148'
    ip2 = '192.168.95.149'
    port = 21


    banner1 = retBanner(ip1, port)
    if banner1:
        print '[+] ' + ip1 + ': ' + banner1
    banner2 = retBanner(ip2, port)
    if banner2:
        print '[+] ' + ip1 + ': ' + banner2

    print "You need to open and FTP server for this code to run."

if __name__ == '__main__':
    not_dunder_main()
