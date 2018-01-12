# The Python dictionary (dict) data structure provides a hash table that
# can store any number of Python objects as key/value pairs.

services = { 'ftp': 21, 'ssh': 22, 'smtp': 25, 'http': 80 }
print services.keys()
print services.items()
print services.has_key('ftp')
print services['ftp']
print "[+] Found vulnerability with FTP on port "+str(services['ftp'])
