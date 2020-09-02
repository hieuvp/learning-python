# Decorators

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> **Decorators** allow you to make simple modifications
> to callable objects like **functions**, **methods**, or **classes**.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example.py) -->
<!-- The below code snippet is automatically added from example.py -->

```py
# The syntax


def decorator(func):
    pass


@decorator
def functions(args):
    return "value"


# Is equivalent to
# def function(arg):
#     return "value"


# This passes the function to the decorator,
# and reassigns it to the functions
# functions = decorator(function)


# As you may have seen,
# a decorator is just another function which takes a functions and returns one.
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example.console) -->
<!-- The below code snippet is automatically added from example.console -->

```console
+ python example.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=repeater.py) -->
<!-- The below code snippet is automatically added from repeater.py -->

```py
def repeater(old_function):
    def new_function(*args, **kwargs):
        old_function(*args, **kwargs)  # we run the old function
        old_function(*args, **kwargs)  # we do it twice

    # we have to return the new_function, or it wouldn't reassign it to the value
    return new_function


# This would make a function repeat twice


@repeater
def multiply(num1, num2):
    print(num1 * num2)


multiply(2, 3)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=repeater.console) -->
<!-- The below code snippet is automatically added from repeater.console -->

```console
+ python repeater.py
6
6
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=decorating_functions.py) -->
<!-- The below code snippet is automatically added from decorating_functions.py -->

```py

```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=decorating_functions.console) -->
<!-- The below code snippet is automatically added from decorating_functions.console -->

```console
+ python decorating_functions.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

You can also make it change the output

```python
def double_out(old_function):
    def new_function(*args, **kwds):
        return 2 * old_function(*args, **kwds) # modify the return value
    return new_function
```

change input

```python
def double_Ii(old_function):
    def new_function(arg): # only works if the old function has one argument
        return old_function(arg * 2) # modify the argument passed
    return new_function
```

and do checking.

```python
def check(old_function):
    def new_function(arg):
        if arg < 0: raise (ValueError, "Negative Argument") # This causes an error, which is better than it doing the wrong thing
        old_function(arg)
    return new_function
```

Let's say you want to multiply the output by a variable amount.
You could define the decorator and use it as follows:

```python
def multiply(multiplier):
    def multiply_generator(old_function):
        def new_function(*args, **kwds):
            return multiplier * old_function(*args, **kwds)
        return new_function
    return multiply_generator # it returns the new generator

# Usage
@multiply(3) # multiply is not a generator, but multiply(3) is
def return_num(num):
    return num

# Now return_num is decorated and reassigned into itself
return_num(5) # should return 15
```

You can do anything you want with the old function,
even completely ignore it! Advanced decorators can also manipulate the doc string and argument number.
For some snazzy decorators,
go to <http://wiki.python.org/moin/PythonDecoratorLibrary.>

## Exercise

Make a decorator factory which returns a decorator that decorates functions with one argument.
The factory should take one argument, a type,
and then returns a decorator that makes function should check if the input is the correct type.
If it is wrong, it should print("Bad Type") (In reality, it should raise an error,
but error raising isn't in this tutorial).
Look at the tutorial code and expected output to see
what it is if you are confused (I know I would be.)
Using `isinstance(object, type_of_object)` or `type(object)` might help.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# def type_check(correct_type):
#     # put code here
#     pass


# @type_check(int)
# def times2(num):
#     return num * 2
#
#
# print(times2(2))
# times2("Not A Number")
#
#
# @type_check(str)
# def first_letter(word):
#     return word[0]
#
#
# print(first_letter("Hello World"))
# first_letter(["Not", "A", "String"])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
```

<!-- AUTO-GENERATED-CONTENT:END -->
