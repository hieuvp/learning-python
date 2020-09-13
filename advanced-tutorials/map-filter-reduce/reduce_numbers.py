# Let's create our own version of Python's built-in sum() function.
# The sum() function returns the sum of all the items in the iterable passed to it.

# Python 3
from functools import reduce

numbers = [3, 4, 6, 9, 34, 12]


def custom_sum(first, second):
    return first + second


result = reduce(custom_sum, numbers)
print(result)
