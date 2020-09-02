def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwargs):
            return multiplier * old_function(*args, **kwargs)

        return new_function

    # it returns the new generator
    return multiply_generator


# Usage
# multiply is not a generator, but multiply(3) is
@multiply(3)
def return_num(num):
    return num


# Now return_num is decorated and reassigned into itself
return_num(5)
# should return 15
