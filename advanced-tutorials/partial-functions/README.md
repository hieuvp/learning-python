# Partial Functions

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> **Partial Functions** allow one to derive
> **a function with x parameters** to **a function with fewer parameters**<br />
> and fixed values set for the more limited function.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.py) -->
<!-- The below code snippet is automatically added from multiply.py -->

```py
# Create Partial Functions
# by using "partial" function from "functools" library
from functools import partial


def multiply(x, y):
    return x * y


# Create a new function that multiplies by 2
double = partial(multiply, 2)
print("double(4) = %s" % double(4))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.console) -->
<!-- The below code snippet is automatically added from multiply.console -->

```console
+ python multiply.py
double(4) = 8
```

<!-- AUTO-GENERATED-CONTENT:END -->

The default values will start replacing variables from the left:

- The `2` will replace `x`.
- `y` will equal `4` when `double(4)` is called.

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
from functools import partial


# Edit this "func()" by calling "partial()" and replacing the first three variables
def func(u, v, w, x):
    return u * 4 + v * 3 + w * 2 + x


# New partial function
new_func = partial(func, 7, 6, 5)


# Print with the "new_func()", using only one input variable
# so that the output equals "60"
print("new_func(4) = %s" % new_func(4))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
new_func(4) = 60
```

<!-- AUTO-GENERATED-CONTENT:END -->
