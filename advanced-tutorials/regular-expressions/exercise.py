import re

# Slight optimization
pattern = re.compile(r"\[(on|off)\]")

# Returning a matched object
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))

# Doesn't return anything
print(re.search(pattern, "Nada...:-("))

print()

# Compiling a regular expression pattern that will match an email
REGEX = re.compile(r"^[a-z0-9._%+-]+[@][a-z0-9.-]+\.[a-z]{2,}$")


# Define a function for validating an email
def check(email):
    if re.match(REGEX, email):
        print('Passed! "%s" is an email.' % email)
    else:
        print('Failed! "%s" does not match the email pattern "%s".' % (email, REGEX.pattern))


check("john@example.com")
check("python-list@python.org")
check("wha.t.`1an?ug{}ly@email.com")
