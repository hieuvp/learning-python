def repeater(old_function):
    def new_function(*args, **kwargs):
        old_function(*args, **kwargs)  # we run the old function
        old_function(*args, **kwargs)  # we do it twice

    # we have to return the new_function, or it wouldn't reassign it to the value
    return new_function


# This would make a function repeat twice


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 3)
