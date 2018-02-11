# Threading the Scan

"""
Depending on the timeout variable for a socket, a scan of each socket can take several seconds.
While this appears trivial, it quickly adds up if we are scanning multiple hosts or ports.
Ideally, we would like to scan sockets simultaneously as opposed to sequentially.
Threading provides a way to perform these kinds of executions simultaneously.
To utilize this in our scan, we will modify the iteration loop in our portScan() function.
Notice how we call the connScan function as a thread.
Each thread created in the iteration will now appear to execute at the same time.
"""
for tgtPort in tgtPorts:
    t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
    t.start()

"""
A simple semaphore provides us a lock to prevent other threads from proceeding.
By utilizing this semaphore, we now ensure only one thread can print to the screen at any given point in time.
In our exception handling code, the keyword finally executes the following code before terminating the block.
"""
screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+] %d/tcp open' %tgtPort
        print '[+] ' + str(results)
    except:
        screenLock.acquire()
        print '[-] %d/tcp closed' %tgtPort
    finally:
        screenLock.release()
        connSkt.close()
