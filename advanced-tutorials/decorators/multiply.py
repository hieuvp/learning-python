# Let's say we want to multiply the output by a variable amount


def multiply(multiplier):
    def multiply_decorator(old_function):
        def new_function(*args, **kwargs):
            return multiplier * old_function(*args, **kwargs)

        return new_function

    # Return the new decorator
    return multiply_decorator


# "multiply" is not a "decorator", but "multiply(3)" is
@multiply(3)
def get_number(number):
    return number


# Now, "get_number()" is decorated and reassigned into itself
print(get_number(5))
