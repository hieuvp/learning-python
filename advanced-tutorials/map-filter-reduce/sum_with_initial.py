from functools import reduce


def sum(first, second):
    return first + second


# Initially, using "10" as the first argument to "sum()"
print(reduce(sum, [6, 7, 8, 9], 10))
