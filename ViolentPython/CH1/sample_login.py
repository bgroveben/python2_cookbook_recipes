# The real strength of the Python programming language lies in the wide array
# of standard and third-party libraries.
# To write our UNIX password cracker, we will need to use the crypt() algorithm
# that hashes UNIX passwords.
# From the docs:
# https://docs.python.org/2/library/crypt.html

import crypt, getpass, pwd

def login():
    username = raw_input('Python login: ')
    cryptedpasswd = pwd.getpwnam(username)[1]
    if cryptedpasswd:
        if cryptedpasswd == 'x' or cryptedpasswd == '*':
            raise NotImplementedError(
                "Sorry, shadow passwords are not accepted."
            )
        cleartext = getpass.getpass()
        return crypt.crypt(cleartext, cryptedpasswd) == cryptedpasswd
    else:
        return 1
