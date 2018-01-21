################################################################################
# The built-in sys module provides access to objects used or maintained by the  # Python interpreter.
# https://docs.python.org/3/library/sys.html
# Interacting with the sys module can prove very helpful in creating Python
# scripts.
# Consider our vulnerability scanner: what if we wanted to pass the name of a
# text file as a command line argument?
################################################################################
# This next link is a somewhat related link to the Python docs on Memory
# Management.
# https://docs.python.org/3/c-api/memory.html
################################################################################

import sys
"""
The list sys.argv contains all the command line arguments.
The first index sys.argv[0] contains the name of the interpreter Python script.
The remaining items in the list contain all the following command line
arguments.
Thus, if we are only passing one additional argument, sys.argv should contain
two items.
"""
if len(sys.argv) == 2:
    filename = sys.argv[1]
    print "[+] Reading Vulnerabilities From: " + filename
