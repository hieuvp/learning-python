# You can also make it change the output


def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds)  # modify the return value

    return new_function


# change input


def double_Ii(old_function):
    def new_function(arg):  # only works if the old function has one argument
        return old_function(arg * 2)  # modify the argument passed

    return new_function


# and do checking.


def check(old_function):
    def new_function(arg):
        if arg < 0:
            # This causes an error, which is better than it doing the wrong thing
            raise (ValueError, "Negative Argument")
        old_function(arg)

    return new_function
