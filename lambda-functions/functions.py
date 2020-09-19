# The power of lambda is better shown
# when you use them as an anonymous function inside another function


def func(n):
    # A function definition that takes one argument,
    # which will be multiplied with an unknown number
    return lambda a: a * n


# Use that function definition to make a function
# that always doubles the number you send in
double = func(2)
print("double(11) = %s" % double(11))


# Use the same function definition to make a function
# that always triples the number you send in
triple = func(3)
print("triple(11) = %s" % triple(11))
