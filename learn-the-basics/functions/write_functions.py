# Functions are defined using the block keyword "def",
# followed with the function's name as the block's name
def my_function():
    print("Hello, From My Function!")


# Functions may also receive arguments,
# which are variables passed from the caller to the function
def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function! I wish you %s" % (username, greeting))


# Functions may return a value to the caller,
# using the keyword "return"
def sum_two_numbers(a, b):
    return a + b
