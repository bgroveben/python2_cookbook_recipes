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

# And now back to the book:

"""
FUNCTIONS crypt(...)
    crypt(word, salt) -> string
    word will usually be a user's password.
    salt is a 2-character string which will be used to select one of 4096
    variations of DES.
    The characters in salt must be either ".", "/", or an alphanumeric
    character.
    Returns the hashed password as a string, which will be composed of
    characters from the same alphabet as the salt.
"""




"""
Firing up the Python interpreter, we see that the crypt library already exists
in the Python standard library.
To calculate an encrypted UNIX password hash, we simply call the function
crypt.crypt() and pass it the password and salt as parameters.
This function returns the hashed password as a string.
"""
