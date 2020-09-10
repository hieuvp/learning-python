# Make a nested loop and a python closure to make functions
# to get multiple multiplication functions using closures.
# That is using closures,
# one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.


def multiplier_of(number):
    def wrapper(multiplicand):
        return number * multiplicand

    return wrapper


multiply_with_4 = multiplier_of(4)
print("multiply_with_4(9) = %s" % multiply_with_4(9))


multiply_with_5 = multiplier_of(5)
print("multiply_with_5(9) = %s" % multiply_with_5(9))
