# Python's socket module provides a library for making network connections.
# https://docs.python.org/2/howto/sockets.html

"""
Let's quickly write a banner-grabbing script.
Our script will print the banner after connecting to a specific IP address and
TCP port.
After importing the socket module, we instantiate a new variable s from the
class socket class.
Next, we use the connect() method to make a network connection to the IP
address and port.
Once successfully connected, we can read and write from the socket.
The recv(1024) method will read the next 1024 bytes on the socket.
We store the result of this method in a variable and then print the results to
the server.
"""
import socket

socket.setdefaulttimeout(2)
s = socket.socket()
s.connect(("192.168.95.148",21))
answer = s.recv(1024)
print answer

# By the way, unless you're running an FTP server on port 21, your code will
# time-out, so don't worry about your machine complaining.
