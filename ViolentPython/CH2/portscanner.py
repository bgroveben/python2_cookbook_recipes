
"""
This program is part of a simulated computer worm.

Can we use the Python programming language to re-create a version of the Morris Worm?
https://en.wikipedia.org/wiki/Morris_worm

In this program, we will build a recon script that scans a target host for open TCP ports.
In order to interact with TCP ports, we need to construct TCP sockets.
https://en.wikipedia.org/wiki/Network_socket

In order to better understand how our TCP Port Scanner works, we will break our script into five unique steps and write Python code for each of them.
First, we will input a hostname and a comma separated list of ports to scan.
Next, we will translate the hostname into an IPv4 Internet address.
For each port in the list, we will also connect to the target address and specific port.
Finally, to determine the specific service running on the port, we will send garbage data and read the banner results sent back by the specific application.

Python, like most modern languages, provides access to the BSD socket interface.
https://en.wikipedia.org/wiki/Berkeley_sockets
BSD sockets provide an application-programming interface that allows coders to write applications in order to perform network communications between hosts.
Through a series of socket API functions, we can create, bind, listen, connect, or send traffic on TCP/IP sockets.
At this point, a greater understanding of TCP/IP and sockets are needed in order to help further develop our own attacks.

An attacker routinely performs a port scan in the opening salvo of any successful cyber assault.
One type of port scan includes sending a TCP SYN packet to a series of common ports and waiting for a TCP ACK response that will result in signaling an open port.
In contrast, a TCP Connect Scan uses the full three-way handshake to determine the availability of the service or port.
"""

import optparse
from socket import *
################################################################################
# The following example shows a quick method for parsing the target hostname
# and port to scan.
parser = optparse.OptionParser('This program requires the following arguments: -H <target host> -p <target port>')
parser.add_option('-H', dest='tgtHost', type='string', \
    help='specify target host')
parser.add_option('-p', dest='tgtPort', type='string',\
    help='specify target port[s] separated by comma')
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPorts = str(options.tgtPort).split(',')

if (tgtHost == None) | (tgtPorts == None):
    print parser.usage
    exit(0)

################################################################################
# Next, we will build two functions connScan and portScan.

# The portScan function takes the hostname and target ports as arguments.
# It will first attempt to resolve an IP address to a friendly hostname using
# the gethostbyname() function.
# Next, it will print the hostname (or IP address) and enumerate through each
# individual port attempting to connect using the connScan function.

# The connScan function will take two arguments: tgtHost and tgtPort, and
# attempt to create a connection to the target host and port.
# If it is successful, connScan will print an open port message.
# If unsuccessful, it will print the closed port message.

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print '[+] %d / tcp open'%tgtPort
        connSkt.close()
    except:
        print '[-] %d / tcp closed'%tgtPort

def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': unknown host"%tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIp
    setdefaulttimeout(1)

    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))
