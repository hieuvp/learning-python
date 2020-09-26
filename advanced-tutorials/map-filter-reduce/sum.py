from functools import reduce


def sum(first, second):
    return first + second


numbers = [6, 7, 8, 9]

print(reduce(sum, numbers))
