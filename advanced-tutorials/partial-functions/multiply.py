# Create Partial Functions
# by using "partial" function from "functools" library
from functools import partial


def multiply(x, y):
    return x * y


# Create a new function that multiplies by 2
double = partial(multiply, 2)
print("double(4) = %s" % double(4))
