from functools import partial


# Editing the "func()" by calling "partial()" and replacing the first three variables
def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


# Creating a new partial function
new_func = partial(func, 7, 6, 5)


# Printing with the "new_func()", using only one input variable
# so that the output equals "60"
print("new_func(4) = %s" % new_func(4))
