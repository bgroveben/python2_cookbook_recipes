"""
Creating a PortScanner() class object will allow us the capability to perform a scan on that object.
The PortScanner class has a function scan() that takes a list of targets and ports as input and performs a basic Nmap scan.
Additionally, we can now index the object by target hosts and print the status of the port.
This section and the ones that follow will build upon this ability to locate and identify targets.
"""

import nmap
import optparse

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state=nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print " [*] " + tgtHost = " tcp/" + tgtPort + " " + state

def main():
