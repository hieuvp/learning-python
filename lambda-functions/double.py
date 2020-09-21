# A lambda function that doubles to the number passed in as an argument
lambda_double = lambda x: x * 2


# The above statement is nearly the same as
def normal_double(x):
    return x * 2


print("lambda_double(8) = %s" % lambda_double(8))
print("normal_double(8) = %s" % normal_double(8))
