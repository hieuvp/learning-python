def my_function():
    print("Hello, From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function! I wish you %s" % (username, greeting))


def sum_two_numbers(a, b):
    return a + b


# Call functions from above

my_function()

my_function_with_args("John Doe", "a great year!")

x = sum_two_numbers(1, 2)
print("x = %s" % x)
