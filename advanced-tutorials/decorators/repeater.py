def repeater(old_function):
    def new_function(
        *args, **kwargs
    ):  # See learnpython.org/en/Multiple%20Function%20Arguments for how *args and **kwds works
        old_function(*args, **kwargs)  # we run the old function
        old_function(*args, **kwargs)  # we do it twice

    return new_function  # we have to return the new_function, or it wouldn't reassign it to the value


# This would make a function repeat twice


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 3)
