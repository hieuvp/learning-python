# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:


def my_func(n):
    return lambda a: a * n
