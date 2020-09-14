# Create partial functions
# by using the "partial" function from the "functools" library
from functools import partial


def multiply(x, y):
    return x * y


# Create a new function that multiplies by 2
double = partial(multiply, 2)
print("double(4) = %s" % double(4))
