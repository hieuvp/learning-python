# Say you have a function definition that takes one argument,
# and that argument will be multiplied with an unknown number:

def my_func(n):
    return lambda a: a * n


# Use that function definition to make a function
# that always doubles the number you send in:
my_doubler = my_func(2)
print(my_doubler(11))


# Or, use the same function definition to make a function
# that always triples the number you send in:
my_tripler = my_func(3)
print(my_tripler(11))


# Or, use the same function definition to make both functions, in the same program:
