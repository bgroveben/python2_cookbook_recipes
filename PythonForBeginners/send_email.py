## https://www.pythonforbeginners.com/code-snippets-source-code/using-python-to-send-email/

### Using Python to Send Email ###

# Python includes several modules in the standard library for dealing with emails and email servers.

"""
The smtplib module defines an SMTP client session object that can be used to send
mail to any Internet machine with an SMTP or ESMTP listener daemon.
Sending mail is done with Python's smtplib using an SMTP (Simple Mail Transfer Protocol) server.
The instructions here are based on sending email through Gmail.
"""
## https://en.wikibooks.org/wiki/Python_Programming/Email

import smtplib

# Create an SMTP object.
# Each object is used for a connection with one server.
# The first argument is the server's hostname, the second identifies the port.
server = smtplib.SMTP('smtp.gmail.com', 587)

# Next, set up the proper connection for sending email.
server.ehlo()
server.starttls()
server.ehlo()

# These steps may not be necessary depending on the server you connect to.
# The ehlo() method is used for ESMTP servers.
# For non-ESMTP servers, use helo() instead.
# See Wikipedia's article about the SMTP protocol for more information about this.
# The starttls() function starts Transport Layer Security mode, which is required by Gmail.
# Other mail systems may not use this, or it may not be available.

# To log in to the server:
server.login("emailusername", "password")

# Now, to send the email:
msg = "\nHello Email!"
server.sendmail('you@gmail.com', 'target@example.com', msg)

# Note that this is a rather crude example.
# Use the email package to include a subject, or any other headers.

### Email Package Usage
