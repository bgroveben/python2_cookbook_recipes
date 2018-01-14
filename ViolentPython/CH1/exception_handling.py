# Because you want to handle your errors within the context of the running
# program or script.

import socket

socket.setdefaulttimeout(2)
s = socket.socket()
try:
    s.connect(("192.168.95.149", 21))
except Exception, e:
    print "[-] Error = "+str(e)
