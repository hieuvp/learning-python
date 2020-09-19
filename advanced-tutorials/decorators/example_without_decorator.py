def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


def function(message):
    print(message)


# Pass the "function" to the "decorator", and reassign it to the new "function"
function = decorator(function)


function("Hello! Decorators")
