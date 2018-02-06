# http://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python
"""
Port Scanner in Python using the Sockets module.
This small port scanner program will try to connect on every port you define for a particular host.
"""
# https://docs.python.org/2/howto/sockets.html
# https://docs.python.org/2/library/socket.html

import socket
import subprocess
import sys
from datetime import datetime
