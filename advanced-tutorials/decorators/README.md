# Decorators

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [More Examples](#more-examples)
  - [`@repeater`](#repeater)
  - [`@multiply()`](#multiply)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> **Decorators** allow you to make simple modifications
> to callable objects like **functions**, **methods**, or **classes**.

<br />

The syntax:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example_with_decorator.py) -->
<!-- The below code snippet is automatically added from example_with_decorator.py -->

```py
def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


@decorator
def function(message):
    print(message)


function("Hello! Decorators")
```

<!-- AUTO-GENERATED-CONTENT:END -->

Is equivalent to:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example_without_decorator.py) -->
<!-- The below code snippet is automatically added from example_without_decorator.py -->

```py
def decorator(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)

    return wrapper


def function(message):
    print(message)


# Pass the "function" to the "decorator", and reassign it to a new "function"
function = decorator(function)


function("Hello! Decorators")
```

<!-- AUTO-GENERATED-CONTENT:END -->

As you may have seen,
a **decorator** is just another function which takes a function and returns one.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example.console) -->
<!-- The below code snippet is automatically added from example.console -->

```console
+ python example_with_decorator.py
Hello! Decorators
Hello! Decorators
+ set +x

+ python example_without_decorator.py
Hello! Decorators
Hello! Decorators
```

<!-- AUTO-GENERATED-CONTENT:END -->

## More Examples

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=decorating_functions.py) -->
<!-- The below code snippet is automatically added from decorating_functions.py -->

```py
# Change the output
def double_output(old_function):
    def new_function(*args, **kwargs):
        # Modify the returned value
        return 2 * old_function(*args, **kwargs)

    return new_function


# Change the input
def double_input(old_function):
    # Only works if the "old_function" has one argument
    def new_function(args):
        # Modify the argument passed
        return old_function(args * 2)

    return new_function


# Do checking
def check(old_function):
    def new_function(args):
        if args < 0:
            # This causes an error,
            # which is better than it does the wrong thing
            raise (ValueError, "Negative Argument")
        old_function(args)

    return new_function
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

> You can do anything you want with the old function, even completely ignore it!
> <br />Advanced decorators can also manipulate the doc string and argument number.
> <br />For some snazzy decorators,
> go to [PythonDecoratorLibrary](https://wiki.python.org/moin/PythonDecoratorLibrary).

### `@repeater`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=repeater.py) -->
<!-- The below code snippet is automatically added from repeater.py -->

```py
# A decorator that makes a function repeats twice
def repeater(old_function):
    def new_function(*args, **kwargs):
        old_function(*args, **kwargs)  # Run the "old_function()"
        old_function(*args, **kwargs)  # Do it twice

    # Return the "new_function()", or it wouldn't reassign it to the new value
    return new_function


@repeater
def multiply(multiplier, multiplicand):
    print("%d x %d = %d" % (multiplier, multiplicand, multiplier * multiplicand))


multiply(2, 3)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=repeater.console) -->
<!-- The below code snippet is automatically added from repeater.console -->

```console
+ python repeater.py
2 x 3 = 6
2 x 3 = 6
```

<!-- AUTO-GENERATED-CONTENT:END -->

### `@multiply()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.py) -->
<!-- The below code snippet is automatically added from multiply.py -->

```py
# Let's say we want to multiply the output by a variable amount


def multiply(multiplier):
    def multiply_decorator(old_function):
        def new_function(*args, **kwargs):
            return multiplier * old_function(*args, **kwargs)

        return new_function

    # Return the new decorator
    return multiply_decorator


# "@multiply" is not a "decorator", but "@multiply(3)" is
@multiply(3)
def get_number(number):
    return number


# Now, "get_number()" is decorated and reassigned into itself
print(get_number(5))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.console) -->
<!-- The below code snippet is automatically added from multiply.console -->

```console
+ python multiply.py
15
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# A "decorator factory" which returns a "decorator"
# that checks if the input type is correct
def type_check(correct_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for argument in args:
                if not isinstance(argument, correct_type):
                    print('Bad Type! "%s" is not of type "%s"' % (argument, correct_type))
                    # In reality, it should raise an error

            return func(*args, **kwargs)

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print()
print('first_letter("Hello World") = %s' % first_letter("Hello World"))

print()
print('first_letter(["Not", "A", "String"])')
first_letter(["Not", "A", "String"])


@type_check(int)
def times(multiplier, multiplicand):
    return multiplier * multiplicand


print()
print("times(2, 3) = %s" % times(2, 3))

print()
print('times(2, "Not A Number")')
times(2, "Not A Number")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py

first_letter("Hello World") = H

first_letter(["Not", "A", "String"])
Bad Type! "['Not', 'A', 'String']" is not of type "<class 'str'>"

times(2, 3) = 6

times(2, "Not A Number")
Bad Type! "Not A Number" is not of type "<class 'int'>"
```

<!-- AUTO-GENERATED-CONTENT:END -->
