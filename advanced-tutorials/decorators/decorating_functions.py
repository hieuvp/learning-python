# Change the output
def double_out(old_function):
    def new_function(*args, **kwargs):
        # Modify the returned value
        return 2 * old_function(*args, **kwargs)

    return new_function


# Change the input
def double_input(old_function):
    # Only works if the old function has one argument
    def new_function(args):
        # Modify the argument passed
        return old_function(args * 2)

    return new_function


# Do checking
def check(old_function):
    def new_function(args):
        if args < 0:
            # This causes an error,
            # which is better than it does the wrong thing
            raise (ValueError, "Negative Argument")
        old_function(args)

    return new_function
