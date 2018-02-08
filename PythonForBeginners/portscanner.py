# http://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python
"""
Port Scanner in Python using the Sockets module.
This small port scanner program will try to connect on every port you define for a particular host.
"""
# https://en.wikipedia.org/wiki/Port_scanner
# https://docs.python.org/2/howto/sockets.html
# https://docs.python.org/2/library/socket.html

import socket
import subprocess
import sys
from datetime import datetime

# Blank slate and clear screen:
subprocess.call('clear', shell=True)

remoteServer = raw_input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# Banner to give the user information about the host about to be scanned:
print "-" * 60
print "Please wait while the remote host " + str(remoteServerIP) + " is scanned."
print "-" * 60

# Mark the time that the scan begins and specify all ports between 1 and 1024:
t1 = datetime.now()
try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}:     Open".format(port)
        sock.close
except KeyboardInterrupt:
    print "You have pressed Ctrl+C. This machine will now self-destruct."
    sys.exit()
except socket.gaierror:
    print "Hostname could not be resolved. Exiting. Someone else's machine will now self-destruct."
    sys.exit()
except socket.error:
    print "Couldn't connect to the server. Now the server will self-destruct."
    sys.exit()

# Calculate the time difference to see how long the script took to run:
t2 = datetime.now()
total = t2 - t1
print "The scan took " + str(total) + " minutes to complete."
