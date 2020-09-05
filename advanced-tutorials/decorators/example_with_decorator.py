# The Syntax


def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@decorator
def function(message):
    print(message)


function("Hello! Decorators")
