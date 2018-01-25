# The real strength of the Python programming language lies in the wide array
# of standard and third-party libraries.
# To write our UNIX password cracker, we will need to use the crypt() algorithm
# that hashes UNIX passwords.

"""
FUNCTIONS:

crypt(...)
    crypt(word, salt) -> string
    word will usually be a user's password.
    salt is a 2-character string which will be used to select one of 4096
    variations of DES.
    The characters in salt must be either ".", "/", or an alphanumeric
    character.
    Returns the hashed password as a string, which will be composed of
    characters from the same alphabet as the salt.

main(...)
    Our main() function opens the encrypted password file "passwords.txt" and
    reads the contents of each line in the password file.
    For each line, it splits up the username and password.
    Then, for each individual hashed password, the main() function calls the
    testPass() function that tests passwords against a dictionary file.

testPass(...)
    Our testPass() function takes the encrypted password as a parameter and
    returns either after finding the password or exhausting the words in the
    dictionary.
    Notice that the function first strips out the salt from the first two
    characters of the encrypted password hash.
    Next, it opens the dictionary and iterates through each word in the
    dictionary, creating an encrypted password hash from the dictionary word
    and the salt.
    If the result matches our encrypted password hash, the function prints a
    message indicating the found password and returns.
    Otherwise, it continues to test every word in the dictionary.
"""
