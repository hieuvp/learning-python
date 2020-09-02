# Look at the tutorial code and expected output to see
# what it is if you are confused (I know I would be).
# Using "isinstance(object, type_of_object)" or "type(object)" might help.

# A decorator factory
# which returns a decorator that decorates functions with one argument
def type_check(correct_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for argument in args:
                # If it is wrong, it should print("Bad Type")
                # In reality, it should raise an error, but error raising isn't in this tutorial
                if not isinstance(argument, correct_type):
                    print("Bad Type")

            return func(*args, **kwargs)

        return wrapper

    # Return a decorator that makes function
    # should check if the input is the correct type
    return decorator


@type_check(int)
def times(multiplier, multiplicand):
    return multiplier * multiplicand


print(times(2, 3))
times(2, "Not A Number")

#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
#
# print(first_letter("Hello World"))
# first_letter(["Not", "A", "String"])
