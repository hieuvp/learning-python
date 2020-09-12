def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


def function(message):
    print(message)


# This passes the function to the decorator,
# and reassigns it to the function
function = decorator(function)

function("Hello! Decorators")

# As you may have seen,
# a decorator is just another function which takes a functions and returns one.
