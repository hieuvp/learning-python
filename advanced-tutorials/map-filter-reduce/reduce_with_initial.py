from functools import reduce


def custom_sum(first, second):
    return first + second


numbers = [3, 4, 6, 10]

# Initially, uses "10" as the first argument to "custom_sum"
print(reduce(custom_sum, numbers, 10))
