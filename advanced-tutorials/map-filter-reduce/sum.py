from functools import reduce


def sum(first, second):
    return first + second


print(reduce(sum, [6, 7, 8, 9]))
