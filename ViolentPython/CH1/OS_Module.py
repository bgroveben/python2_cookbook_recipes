"""
The built-in OS module provides a wealth of OS routines for Mac, NT, or Posix operating systems.
This module allows the program to independently interact with the OS environment, file-system, user database, and permissions.
Consider, for example, the last section, where the user passed the name of a text file as a command line argument.
It might prove valuable to check to see if that file exists and the current user has read permissions to that file.
If either condition fails, it would be useful to display an appropriate error message to the user.
"""
import sys
import os

if len(sys.argv) == 2:
    filename = sys.argv[1]
    if not os.path.isfile(filename):
        print '[-] ' + filename + ' does not exist.'
        exit(0)
    # https://docs.python.org/2/library/os.html#os.access
    if not os.access(filename, os.R_OK):
        print '[-] ' + filename + ' access denied.'
        exit(0)
    print '[+] Reading Vulnerabilities From: ' + filename

###############################################################################
# To verify our code, we initially try to read a file that does not exist,
# which causes our script to print an error.
# Next, we create the specific filename and successfully read it.
# Finally, we restrict permission and see that our script correctly prints the
# access-denied message.
