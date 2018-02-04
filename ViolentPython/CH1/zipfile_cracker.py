# Let's use the technique of brute-forcing a password learned in the
# password_cracker.py program but apply it to zip files.
# This program should behave the same way as zipCrack.py.
# https://docs.python.org/2/library/zipfile.html

# Let's start with some examples first:

import zipfile
import optparse
from threading import Thread

def extractFile(zFile, password)
    try:
        zFile.extractall(pwd=password)
        print '[+] found password ' + password + '\n'
    except:
        pass

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

# Let's clean up our code a little bit at this point.
# Instead of having a linear program, we will modularize our script with
# functions.

import zipfile

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        return password
    except:
        return

def main():
    parser = optparse.OptionParser("usage%prog " +\
    "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', \
    help='Please specify zip file.')
    parser.add_option('-d', dest='dname', type='string', \
    help='Please specify dictionary file.')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()

    zFile = zipfile.ZipFile('evil.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(zFile, password)
        if guess:
            print '[+] Password = ' + password + '\n'
            exit(0)

if __name__ == '__main__':
    main()

# With our program modularized into separate functions, we can now increase our
# performance.
# Instead of trying each word in the dictionary one at a time, we will utilize
# threads of execution to allow simultaneous testing of multiple passwords.
# For each word in the dictionary, we will spawn a new thread of execution.
# https://docs.python.org/2/library/threading.html#thread-objects

import zipfile
from threading import Thread

"""
https://docs.python.org/2/library/threading.html
CPython implementation detail:
In CPython, due to the Global Interpreter Lock, only one thread can execute
Python code at once (even though certain performance-oriented libraries might
overcome this limitation).
If you want your application to make better use of the computational resources
of multi-core machines, you are advised to use multiprocessing.
However, threading is still an appropriate model if you want to run multiple
I/O-bound tasks simultaneously.
"""

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print '[+] Found Password: ' + password + '\n'
    except:
        pass

def main():
    zFile = zipfile.ZipFile('evil.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        password = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()

if __name__ == '__main__':
    main()
