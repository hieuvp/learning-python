from functools import reduce


# Create our own version of Python's built-in "sum()" function
def custom_sum(first, second):
    return first + second


numbers = [3, 4, 6, 10]

print(reduce(custom_sum, numbers))
