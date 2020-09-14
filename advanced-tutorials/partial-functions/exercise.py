from functools import partial


# Edit this "func()" function by calling "partial()"
# and replacing the first three variables
def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


new_func = partial(func, 7, 6, 5)

# Print with the new partial function, using only one input variable
# so that the output equals "60"
print("new_func(4) = %s" % new_func(4))
