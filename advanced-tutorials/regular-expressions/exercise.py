import re

# Slight optimization
pattern = re.compile(r"\[(on|off)\]")

# Returns a Match object!
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))

# Doesn't return anything
print(re.search(pattern, "Nada...:-("))


def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % email)
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")


# Making a regular expression that will match an email
pattern = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"
test_email(pattern)
