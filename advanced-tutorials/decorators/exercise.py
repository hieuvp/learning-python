# A "Decorator Factory" which returns a "Decorator"
def type_check(correct_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for argument in args:
                if not isinstance(argument, correct_type):
                    print('Bad Type! "%s" is not of type "%s"' % (argument, correct_type))
                    # In reality, it should raise an error,
                    # but error raising isn't in this tutorial

            return func(*args, **kwargs)

        return wrapper

    # Return a decorator that makes a function
    # checks if the input type is correct
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print()
print('first_letter("Hello World") = %s' % first_letter("Hello World"))

print()
print('first_letter(["Not", "A", "String"])')
first_letter(["Not", "A", "String"])


@type_check(int)
def times(multiplier, multiplicand):
    return multiplier * multiplicand


print()
print("times(2, 3) = %s" % times(2, 3))

print()
print('times(2, "Not A Number")')
times(2, "Not A Number")
