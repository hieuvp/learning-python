# Closures

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> **Objects** are data with methods attached.
> <br />**Closures** are functions with data attached.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=make_counter.py) -->
<!-- The below code snippet is automatically added from make_counter.py -->

```py
def make_counter():
    i = 0

    # "counter()" is a "closure"
    def counter():
        nonlocal i
        i += 1
        return i

    return counter


c1 = make_counter()
c2 = make_counter()

print(c1(), c1(), c2(), c2())
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=make_counter.console) -->
<!-- The below code snippet is automatically added from make_counter.console -->

```console
+ python make_counter.py
1 2 1 2
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

> A **closure** is a **nested function**
> which has access to a free variable from an **enclosing function**
> that has finished its execution.
> <br />Three characteristics of a Python closure are:

1. It is a **nested function**.
1. It has access to a **free variable** in outer scope.
1. It is returned from the **enclosing function**.

> A **free variable** is a variable that is not bound in the local scope.
> <br />In order for **closures** to work with immutable variables
> such as numbers and strings, we have to use the `nonlocal` keyword.

<br />

The `nonlocal` keyword is used to work with variables inside nested functions,
where the variable should not belong to the inner function.

Use the keyword `nonlocal` to declare that the variable is not local.

To demonstrate the use of the `nonlocal` keyword, consider this:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_msg.py) -->
<!-- The below code snippet is automatically added from print_msg.py -->

```py
def print_msg_without_nonlocal(number):
    print('Without "nonlocal" keyword')

    def printer():
        number = 3
        print("- Inside  printer() : number = %s" % number)

    printer()

    print("- Outside printer() : number = %s" % number)


def print_msg_with_nonlocal(number):
    print('With "nonlocal" keyword')

    def printer():
        nonlocal number
        number = 3
        print("- Inside  printer() : number = %s" % number)

    printer()

    print("- Outside printer() : number = %s" % number)


print_msg_without_nonlocal(9)
print()
print_msg_with_nonlocal(9)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_msg.console) -->
<!-- The below code snippet is automatically added from print_msg.console -->

```console
+ python print_msg.py
Without "nonlocal" keyword
- Inside  printer() : number = 3
- Outside printer() : number = 9

With "nonlocal" keyword
- Inside  printer() : number = 3
- Outside printer() : number = 3
```

<!-- AUTO-GENERATED-CONTENT:END -->

However, with its usage, the value of the `number` variable gets modified.

<br />

Now, how about we return the function object rather than calling the nested function within.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=transmit_to_space.py) -->
<!-- The below code snippet is automatically added from transmit_to_space.py -->

```py
def transmit_to_space(message):
    """Enclosing Function"""

    def data_transmitter():
        """Nested Function"""
        print(message)

    return data_transmitter


# Even functions are objects
func = transmit_to_space("Burn the Sun!")
func()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=transmit_to_space.console) -->
<!-- The below code snippet is automatically added from transmit_to_space.console -->

```console
+ python transmit_to_space.py
Burn the Sun!
```

<!-- AUTO-GENERATED-CONTENT:END -->

Even though the execution of the `transmit_to_space()` was completed,
the `message` was rather preserved.
This technique by which the data is attached to some code
even after end of those other original functions is called as closures in Python.

<br />

- **Closures** can avoid use of global variables and provides some form of data hiding.
  (e.g. When there are few methods in a class, use closures instead).
- [**Decorators**](../decorators/README.md) make extensive use of **Closures**.

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# A function to make multiple multiplication functions
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

## References

- [Python `nonlocal` Keyword](https://www.w3schools.com/python/ref_keyword_nonlocal.asp)
