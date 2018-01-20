"""
While our script has an IF statement that checks a few vulnerable banners, it would be nice to occasionally add a new list of vulnerable banners.
For this example, let's assume we have a text file called vuln_banners.txt.
Each line in this file lists a specific service version with a previous vulnerability.
Instead of constructing a huge IF statement, let's read in this text file and use it to make decisions if our banner is vulnerable.
"""
## The list of banners is in the vuln-banners.txt file ##

"""

We will place our updated code in the checkVulns function.
Here, we will open the text file in read-only mode ('r').
We iterate through each line in the file using the method .readlines().
For each line, we compare it against our banner.
Notice that we must strip out the carriage return from each line using the method .strip('\r').
If we detect a match, we print the vulnerable service banner.
"""
def checkVulns(banner):
    f = open("vuln_banners.txt", 'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+] Server is vulnerable: " + banner.strip('\n')
    f.close()
