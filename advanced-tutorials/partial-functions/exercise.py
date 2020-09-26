from functools import partial


def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


# Editing the "func()" and replacing the first three variables
new_func = partial(func, 1, 2, 3)


# Printing with the "new_func()", using only one input variable
# so that the output equals "60"
print("new_func(4) = %s" % new_func(4))
