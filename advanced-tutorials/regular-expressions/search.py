import re

pattern = re.compile(r"\[(on|off)\]")
print("pattern = %s" % pattern)


# Return a "Match" object if found
string = "Mono: Playback 65 [75%] [-16.50dB] [on]"
print()
print("string                     = %s" % string)
print("re.search(pattern, string) = %s" % re.search(pattern, string))


# Return "None" if not match
string = "Nada...:-("
print()
print("string                     = %s" % string)
print("re.search(pattern, string) = %s" % re.search(pattern, string))
