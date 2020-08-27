# Extensible library for opening URLs
# https://docs.python.org/3/library/urllib.request.html
import urllib.request

# Usage:
# urllib.request.urlopen("https://www.shopback.com")

# Two very important functions come in handy when exploring modules in Python
# The "dir" and "help" functions:

# If called without an argument, return the names in the current scope.
# Else, return an alphabetized list of names comprising (some of) the attributes
# of the given object, and of attributes reachable from it.
# If the object supplies a method named __dir__, it will be used; otherwise
# the default dir() logic is used and returns:
#   for a module object: the module's attributes.
#   for a class object: its attributes, and recursively the attributes of its bases.
#   for any other object: its attributes, its class's attributes, and
#     recursively the attributes of its class's base classes.
print("\n+ print(dir(urllib.request))")
print(dir(urllib.request))

# This is a wrapper around pydoc.help that provides a helpful message
# when 'help' is typed at the Python interactive prompt.
#
# Calling help() at the Python prompt starts an interactive help session.
# Calling help(thing) prints help for the python object 'thing'.
print("\n+ help(urllib.request.urlopen)")
help(urllib.request.urlopen)
