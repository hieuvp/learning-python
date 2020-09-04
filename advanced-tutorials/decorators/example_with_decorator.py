# The Syntax


def decorator(func):
    def wrapper(*args, **kwargs):

        return func(*args, **kwargs)

    return wrapper


@decorator
def function(args):
    return args
