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
# Change the output
def double_out(old_function):
    def new_function(*args, **kwargs):
        # modify the return value
        return 2 * old_function(*args, **kwargs)

    return new_function


# Change the input
def double_input(old_function):
    # only works if the old function has one argument
    def new_function(args):
        # modify the argument passed
        return old_function(args * 2)

    return new_function


# Do checking
def check(old_function):
    def new_function(args):
        if args < 0:
            # This causes an error, which is better than it does the wrong thing
            raise (ValueError, "Negative Argument")
        old_function(args)

    return new_function
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=decorating_functions.console) -->
<!-- The below code snippet is automatically added from decorating_functions.console -->

```console
+ python decorating_functions.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

Let's say you want to multiply the output by a variable amount.
You could define the decorator and use it as follows:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.py) -->
<!-- The below code snippet is automatically added from multiply.py -->

```py
def multiply(multiplier):
    def multiply_decorator(old_function):
        def new_function(*args, **kwargs):
            return multiplier * old_function(*args, **kwargs)

        return new_function

    # it returns the new decorator
    return multiply_decorator


# Usage
# multiply is not a generator, but multiply(3) is
@multiply(3)
def return_number(number):
    return number


# Now return_number is decorated and reassigned into itself
output = return_number(5)
print(output)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.console) -->
<!-- The below code snippet is automatically added from multiply.console -->

```console
+ python multiply.py
15
```

<!-- AUTO-GENERATED-CONTENT:END -->

You can do anything you want with the old function, even completely ignore it!
Advanced decorators can also manipulate the doc string and argument number.
For some snazzy decorators, go to [PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary)

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Look at the tutorial code and expected output to see
# what it is if you are confused (I know I would be).
# Using "isinstance(object, type_of_object)" or "type(object)" might help.

# A decorator factory
# which returns a decorator that decorates functions with one argument
def type_check(correct_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for argument in args:
                # If it is wrong, it should print("Bad Type")
                # In reality, it should raise an error, but error raising isn't in this tutorial
                if not isinstance(argument, correct_type):
                    print("Bad Type")

            return func(*args, **kwargs)

        return wrapper

    # Return a decorator that makes function
    # should check if the input is the correct type
    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print()
print(first_letter("Hello World"))
first_letter(["Not", "A", "String"])


@type_check(int)
def times(multiplier, multiplicand):
    return multiplier * multiplicand


print()
print(times(2, 3))
times(2, "Not A Number")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py

H
Bad Type

6
Bad Type
```

<!-- AUTO-GENERATED-CONTENT:END -->
