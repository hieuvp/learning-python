# Having a function definition that takes one argument
def my_func(n):
    # The argument will be multiplied with an unknown number
    return lambda a: a * n


# Using that function definition to make a function
# that always doubles the number you send in
my_doubler = my_func(2)
print("my_doubler(11) = %s" % my_doubler(11))


# Or, using the same function definition to make a function
# that always triples the number you send in
my_tripler = my_func(3)
print("my_tripler(11) = %s" % my_tripler(11))
