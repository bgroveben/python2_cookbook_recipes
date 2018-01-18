# Using a for loop instead of rewriting things.
# Never take that for granted.

for x in range(1, 15):
    print "192.168.95."+str(x)

print

portList = [21, 22, 25, 80, 110]
for port in portList:
    print port

print
# Now we can nest our for loops, then print out each IP address and its ports.
for x in range(1, 15):
    for port in portList:
        print "[+] Checking 192.168.95."\
                +str(x)+": "+str(port)
