# Print an alphabetically sorted list of all functions in the "re" module

import re
from inspect import getmembers, isfunction

# inspect.getmembers(object[, predicate])
# https://docs.python.org/3/library/inspect.html#inspect.getmembers
for member in getmembers(re):
    name, value = member
    if isfunction(value):
        print(name)
