# Making a function to get multiple multiplication functions
def multiplier_of(number):
    def wrapper(multiplicand):
        return number * multiplicand

    return wrapper


multiply_with_4 = multiplier_of(4)
print("multiply_with_4(9) = %s" % multiply_with_4(9))


multiply_with_5 = multiplier_of(5)
print("multiply_with_5(9) = %s" % multiply_with_5(9))
