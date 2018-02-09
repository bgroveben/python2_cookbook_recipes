
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
################################################################################
# The following example shows a quick method for parsing the target hostname
# and port to scan.
parser = optparse.OptionParser('This program requires the following arguments: -H <target host> -p <target port>')
parser.add_option('-H', dest='tgtHost', type='string', \
    help='specify target host')
parser.add_option('-p', dest='tgtPort', type='int', \
    help='specify target port')
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort

if (tgtHost == None) | (tgtPort == None):
    print parser.usage
    exit(0)
