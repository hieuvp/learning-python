import re

# Compile a regular expression pattern that will match an email
REGEX = re.compile(r"^[a-z0-9._%+-]+[@][a-z0-9.-]+\.[a-z]{2,}$")


# Define a function for validating an email
def check(email):
    if re.match(REGEX, email):
        print('Passed! "%s" is an email' % email)
    else:
        print('Failed! "%s" does not match the email pattern "%s"' % (email, REGEX.pattern))


check("john@example.com")
check("python-list@python.org")
check("wha.t.`1an?ug{}ly@email.com")
