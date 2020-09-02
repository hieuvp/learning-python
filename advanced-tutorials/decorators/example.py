# The syntax


def decorator(func):
    pass


@decorator
def functions(args):
    return "value"


# Is equivalent to
# def function(arg):
#     return "value"


# This passes the function to the decorator,
# and reassigns it to the functions
# functions = decorator(function)


# As you may have seen,
# a decorator is just another function which takes a functions and returns one.
