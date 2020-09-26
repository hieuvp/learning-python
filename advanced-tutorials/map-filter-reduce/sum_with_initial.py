from functools import reduce


def sum(first, second):
    return first + second


numbers = [6, 7, 8, 9]

# Initially, uses "10" as the first argument to "sum()"
print(reduce(sum, numbers, 10))
