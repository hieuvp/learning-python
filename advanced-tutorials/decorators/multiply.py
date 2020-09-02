def multiply(multiplier):
    def multiply_decorator(old_function):
        def new_function(*args, **kwargs):
            return multiplier * old_function(*args, **kwargs)

        return new_function

    # it returns the new decorator
    return multiply_decorator


# Usage
# multiply is not a generator, but multiply(3) is
@multiply(3)
def return_number(number):
    return number


# Now return_number is decorated and reassigned into itself
output = return_number(5)
print(output)
