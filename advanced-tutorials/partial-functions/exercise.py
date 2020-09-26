from functools import partial


def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


# Edit "func()" and replace the first three variables
new_func = partial(func, 1, 2, 3)


# Use "new_func()" with only one input variable
print("new_func(4) = %s" % new_func(4))
