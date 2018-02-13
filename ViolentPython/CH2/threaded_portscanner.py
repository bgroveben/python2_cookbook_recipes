# # Threading the Scan
#
# """
# Depending on the timeout variable for a socket, a scan of each socket can take several seconds.
# While this appears trivial, it quickly adds up if we are scanning multiple hosts or ports.
# Ideally, we would like to scan sockets simultaneously as opposed to sequentially.
# Threading provides a way to perform these kinds of executions simultaneously.
# To utilize this in our scan, we will modify the iteration loop in our portScan() function.
# Notice how we call the connScan function as a thread.
# Each thread created in the iteration will now appear to execute at the same time.
# """
# for tgtPort in tgtPorts:
#     t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
#     t.start()
#
# """
# A simple semaphore provides us a lock to prevent other threads from proceeding.
# By utilizing this semaphore, we now ensure only one thread can print to the screen at any given point in time.
# In our exception handling code, the keyword finally executes the following code before terminating the block.
# """
# screenLock = Semaphore(value=1)
# def connScan(tgtHost, tgtPort):
#     try:
#         connSkt = socket(AF_INET, SOCK_STREAM)
#         connSkt.connect((tgtHost, tgtPort))
#         connSkt.send('ViolentPython\r\n')
#         results = connSkt.recv(100)
#         screenLock.acquire()
#         print '[+] %d/tcp open' %tgtPort
#         print '[+] ' + str(results)
#     except:
#         screenLock.acquire()
#         print '[-] %d/tcp closed' %tgtPort
#     finally:
#         screenLock.release()
#         connSkt.close()

################################################################################
# Placing all other functions into the same script and adding some option
# parsing, we produce our final port scanner script.
################################################################################

import optparse
from socket import *
from threading import *

screenLock = Semaphore(value=1)

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connskt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+] %d/tcp open'%tgtPort
        print '[+] ' + str(results)
    except:
        screenLock.acquire()
        print '[-] %d/tcp closed'%tgtPort
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot resolve '%s': Unknown host"%tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scan Results for: ' + tgtName[0]
    except:
        print '\n[+] Scan Results for: ' + tgtIP
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('This program requires the following arguments: -H <target host> -p <target port>')
    parser.add_option('-H', dest='tgtHost', type='string', \
        help='Please specify target host')
    parser.add_option('-p', dest='tgtPort', type='string', \
        help='Please separate multiple ports with a comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(',')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print '[-] Please specify a target host and at least one port'
        exit(0)
    portScan(tgtHost, tgtPorts)


if __name__ == '__main__':
    main()
