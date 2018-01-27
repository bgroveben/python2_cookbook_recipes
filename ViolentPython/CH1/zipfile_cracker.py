# Let's use the technique of brute-forcing a password learned in the
# password_cracker.py program but apply it to zip files.
# This program should behave the same way as zipCrack.py.
# https://docs.python.org/2/library/zipfile.html

# Let's start with some examples first:

import zipfile

zFile = zipfile.ZipFile("evil.zip")
try:
    zFile.extractall(pwd="oranges")
except Exception, e:
    print e

# [=> ('Bad password for file', <zipfile.ZipInfo object at 0x106c7a2a8>)
"""
We can use the fact that an incorrect password throws an exception to test our
zip file against a dictionary file.
After instantiating a ZipFile class, we open a dictionary file and iterate
through and test each word in the dictionary.
If the method extractall() executes without error, we print a message indicat-
ing the working password.
However, if extractall() throws a bad password exception, we ignore the
exception and continue trying passwords in the dictionary.
"""

import zipfile
zFile = zipfile.ZipFile('evil.zip')
passFile = open('dictionary.txt')
for line in passFile.readlines():
    password = line.strip('\n')
    try:
        zFile.extractall(pwd=password)
        print '[+] Password = ' + password + '\n'
        exit(0)
    except Exception, e:
        pass

# Let’s clean up our code a little bit at this point.
# Instead of having a linear program, we will modularize our script with
# functions.
