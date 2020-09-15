import re

# Slight optimization
pattern = re.compile(r"\[(on|off)\]")

# Returns a Match object!
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))

# Doesn't return anything
print(re.search(pattern, "Nada...:-("))


# Compiling a regular expression pattern that will match an email
REGEX_PATTERN = re.compile(r"^[a-z0-9._%+-]+[@][a-z0-9.-]+\.[a-z]{2,}$")


# Define a function for validating an email
def check(email):
    if not re.match(REGEX_PATTERN, email):
        print("You failed to match %s" % email)
    else:
        print("Pass")


check("john@example.com")
check("python-list@python.org")
check("wha.t.`1an?ug{}ly@email.com")
