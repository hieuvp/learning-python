# A function that repeats twice
def repeater(old_function):
    def new_function(*args, **kwargs):
        old_function(*args, **kwargs)  # Run the "old_function()"
        old_function(*args, **kwargs)  # Do it twice

    # Return the "new_function", or it wouldn't reassign it to the value
    return new_function


@repeater
def multiply(multiplier, multiplicand):
    print("%d x %d = %d" % (multiplier, multiplicand, multiplier * multiplicand))


multiply(2, 3)
