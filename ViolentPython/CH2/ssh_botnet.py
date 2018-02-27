# Let's implement our own automated SSH Worm that brute forces user credentials
# against a target.
# The Pexpect module has the ability to interact with programs, watch for
# expected outputs, and then respond based on the expected outputs.
# This makes it an excellent tool of choice for automating the process of brute
# forcing SSH user credentials.

"""
Examine the function connect().
This function takes a username, hostname, and password and returns an SSH connection resulting in an SSH spawned connection.
Utilizing the pexpect library, it then waits for an expected output.
Three possible expected outputs can occur -- a timeout, a message indicating that the host has a new public key, or a password prompt.
If a timeout occurs, then the session.expect() method returns to zero.
The following selection statement notices this and prints an error message before returning.
If the child.expect() method catches the ssh_newkey message, it returns a 1.
This forces the function to send a message 'yes' to accept the new key.
Following this, the function waits for the password prompt before sending the SSH password.
"""

# https://github.com/pexpect/pexpect
import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user, host, password):
    ssh_newkey = "Do you wish to continue?"
    connStr = ' ssh ' + user + '@' + host
    child = pexpect.spawn(connStr)
    ret = child.expect([pexpect.TIMEOUT, ssh_newkey, \
    '[P|p]assword:'])
    if ret == 0:
        print '[-] Error Connecting'
        return
    if ret == 1:
        child.sendline('yes')
        ret = child.expect([pexpect.TIMEOUT, \
        '[P|p]assword:'])
    child.sendline(password)
    child.expect(PROMPT)
    return child
