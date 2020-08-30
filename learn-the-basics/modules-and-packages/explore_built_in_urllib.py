# Source: explore_built_in_urllib.py

# Extensible library for opening URLs
# https://docs.python.org/library/urllib.request.html
import urllib.request

# Usage:
# urllib.request.urlopen("https://www.shopback.com")

# Two very important functions come in handy when exploring modules in Python
# The "dir" and "help" functions.

# Return an alphabetized list of names comprising (some of)
# the attributes of the given object, and of attributes reachable from it
print("\n+ print(dir(urllib.request))")
print(dir(urllib.request))

# Provide a helpful message
print("\n+ help(urllib.request.urlopen)")
help(urllib.request.urlopen)
