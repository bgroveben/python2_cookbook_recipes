# The book refers to an if statement as a 'conditional select statement'.
# Anyhow, continuing with our banner-grabbing script, we would like to know if
# the specific FTP server is vulnerable to attack.
# To do this, we will compare our results against some known vulnerable FTP
# server versions.

import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.95.148", 21))
ans = s.recv(1024)

if ("FreeFloat Ftp Server (Version 1.00)" in ans):
    print "[+] FreeFloat FTP Server is vulnerable."
elif ("3Com 3CDaemon FTP Server Version 2.0" in banner):
    print "[+] 3CDaemon FTP Server is vulnerable."
elif ("Ability Server 2.34" in banner):
    print "[+] Ability FTP Server is vulnerable."
elif ("Sami FTP Server 2.0.2" in banner):
    print "[+] Sami FTP Server is vulnerable."
else:
    print "[-] FTP Server is not vulnerable."

# By the way, unless you're running an FTP server on port 21, your code will
# time-out, so don't worry about your machine complaining.
