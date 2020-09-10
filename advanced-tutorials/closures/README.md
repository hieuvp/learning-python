# Closures

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> A **Closure** is a **function object** that remembers values in enclosing scopes
> even if they are not present in memory.

Firstly, a Nested Function is a function defined inside another function.
It's very important to note that the nested functions can access the variables of the enclosing scope.
However, at least in Python, they are only readonly.
However, one can use the `nonlocal` keyword explicitly with these variables in order to modify them.

For example:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=transmit_to_space.py) -->
<!-- The below code snippet is automatically added from transmit_to_space.py -->

```py
def transmit_to_space(message):
    """This is the enclosing function"""

    def data_transmitter():
        """The nested function"""
        print(message)

    data_transmitter()


print(transmit_to_space("Test message"))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=transmit_to_space.console) -->
<!-- The below code snippet is automatically added from transmit_to_space.console -->

```console
+ python transmit_to_space.py
Test message
None
```

<!-- AUTO-GENERATED-CONTENT:END -->

This works well as the `data_transmitter()` function can access the `message`.
To demonstrate the use of the `nonlocal` keyword, consider this:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_msg.py) -->
<!-- The below code snippet is automatically added from print_msg.py -->

```py
def print_msg(number):
    def printer():
        """Here we are using the nonlocal keyword"""
        nonlocal number
        number = 3
        print("Inside printer(),   number = %s" % number)

    printer()
    print("Inside print_msg(), number = %s" % number)


print_msg(9)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_msg.console) -->
<!-- The below code snippet is automatically added from print_msg.console -->

```console
+ python print_msg.py
Inside printer(),   number = 3
Inside print_msg(), number = 3
```

<!-- AUTO-GENERATED-CONTENT:END -->

Without the `nonlocal` keyword, the output would be `3 9`,
however, with its usage, we get `3 3`, that is the value of the `number` variable gets modified.

Now, how about we return the function object rather than calling the nested function within.
(Remember that even functions are objects. It's Python.)

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=transmit_to_space_v2.py) -->
<!-- The below code snippet is automatically added from transmit_to_space_v2.py -->

```py
def transmit_to_space(message):
    """This is the enclosing function"""

    def data_transmitter():
        """The nested function"""
        print(message)

    return data_transmitter


# We call the function as follows:
fun2 = transmit_to_space("Burn the Sun!")
fun2()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=transmit_to_space_v2.console) -->
<!-- The below code snippet is automatically added from transmit_to_space_v2.console -->

```console
+ python transmit_to_space_v2.py
Burn the Sun!
```

<!-- AUTO-GENERATED-CONTENT:END -->

Even though the execution of the `transmit_to_space()` was completed,
the message was rather preserved.
This technique by which the data is attached to some code
even after end of those other original functions is called as closures in Python.

ADVANTAGE : Closures can avoid use of global variables and provides some form of data hiding.
(e.g. When there are few methods in a class, use closures instead).

Also, [Decorators](../decorators/README.md) in Python make extensive use of closures.

A closure is a nested function
which has access to a free variable from an enclosing function that has finished its execution.
Three characteristics of a Python closure are:

- It is a nested function.
- It has access to a free variable in outer scope.
- It is returned from the enclosing function.

A free variable is a variable that is not bound in the local scope.
In order for closures to work with immutable variables such as numbers and strings,
we have to use the nonlocal keyword.

Python closures help avoiding the usage of global values and provide some form of data hiding.
They are used in Python decorators.

> Objects are data with methods attached, closures are functions with data attached.

```python
def make_counter():
    i = 0
    def counter(): # counter() is a closure
        nonlocal i
        i += 1
        return i
    return counter

c1 = make_counter()
c2 = make_counter()

print (c1(), c1(), c2(), c2())
# -> 1 2 1 2
```

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Make a nested loop and a python closure to make functions
# to get multiple multiplication functions using closures.
# That is using closures,
# one could make functions to create multiply_with_5() or multiply_with_4() functions using closures.


def multiplier_of(number):
    def wrapper(multiplicand):
        return number * multiplicand

    return wrapper


multiply_with_4 = multiplier_of(4)
print("multiply_with_4(9) = %s" % multiply_with_4(9))


multiply_with_5 = multiplier_of(5)
print("multiply_with_5(9) = %s" % multiply_with_5(9))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
multiply_with_4(9) = 36
multiply_with_5(9) = 45
```

<!-- AUTO-GENERATED-CONTENT:END -->
