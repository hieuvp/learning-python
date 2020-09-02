# You can also make it change the output
def double_out(old_function):
    def new_function(*args, **kwargs):
        # modify the return value
        return 2 * old_function(*args, **kwargs)

    return new_function


# Change input
def double_Ii(old_function):
    # only works if the old function has one argument
    def new_function(args):
        # modify the argument passed
        return old_function(args * 2)

    return new_function


# Do checking
def check(old_function):
    def new_function(arg):
        if arg < 0:
            # This causes an error, which is better than it doing the wrong thing
            raise (ValueError, "Negative Argument")
        old_function(arg)

    return new_function
