# Print an alphabetically sorted list of all functions in the "re" module

import re
from inspect import getmembers, isfunction

# https://docs.python.org/library/inspect.html#inspect.getmembers
# inspect.getmembers(object[, predicate])
for member in getmembers(re):
    name, value = member
    if isfunction(value):
        print(name)
