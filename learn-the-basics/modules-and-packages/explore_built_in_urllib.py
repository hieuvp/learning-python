# If we want to import the module urllib,
# which enables us to create read data from URLs,
# we simply import the module:
import urllib.request

# urllib.request - Extensible library for opening URLs
# https://docs.python.org/3/library/urllib.request.html

# Use it
# urllib.request.urlopen("https://www.shopback.com")

# Two very important functions come in handy when exploring modules in Python
# The "dir" and "help" functions
print("\n+ print(dir(urllib.request))")
print(dir(urllib.request))

print("\n+ help(urllib.request.urlopen)")
help(urllib.request.urlopen)
