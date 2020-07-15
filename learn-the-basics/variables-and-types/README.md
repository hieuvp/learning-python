# Variables and Types

> Python is completely object oriented, and not `statically typed`.<br />
> You do not need to declare variables before using them, or declare their type.<br />
> Every variable in Python is an object.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Numbers](#numbers)
  - [Integers](#integers)
  - [Floating Point Numbers](#floating-point-numbers)
- [Strings](#strings)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Numbers

### Integers

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=integer.py) -->
<!-- The below code snippet is automatically added from integer.py -->

```py
MY_INT = 7
print(MY_INT)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=integer.console) -->
<!-- The below code snippet is automatically added from integer.console -->

```console
+ python integer.py
7
```

<!-- AUTO-GENERATED-CONTENT:END -->

### Floating Point Numbers

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=float.py) -->
<!-- The below code snippet is automatically added from float.py -->

```py
MY_FLOAT = 7.0
print(MY_FLOAT)
MY_FLOAT = float(7)
print(MY_FLOAT)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=float.console) -->
<!-- The below code snippet is automatically added from float.console -->

```console
+ python float.py
7.0
7.0
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Strings

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string.py) -->
<!-- The below code snippet is automatically added from string.py -->

```py
# With a single quote
MY_STRING = 'hello'
print(MY_STRING)

# Or a double quotes
MY_STRING = "hello"
print(MY_STRING)

# The difference between the two is that
# using double quotes makes it easy to include apostrophes
# (whereas these would terminate the string if using single quotes)
MY_STRING = "Don't worry about apostrophes"
print(MY_STRING)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string.console) -->
<!-- The below code snippet is automatically added from string.console -->

```console
+ python string.py
hello
hello
Don't worry about apostrophes
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

There are additional variations on defining strings that make it easier to include things
such as carriage returns (`\r`), backslashes and Unicode characters.
<https://www.youtube.com/watch?v=fpRZsVrVrkU>
These are beyond the scope of this tutorial, but are covered in the Python documentation.
<https://docs.python.org/tutorial/introduction.html#strings>

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=simple_operators.py) -->
<!-- The below code snippet is automatically added from simple_operators.py -->

```py
# Simple operators can be executed on numbers and strings

ONE = 1
TWO = 2
THREE = ONE + TWO
print(THREE)

HELLO = "hello"
WORLD = "world"
HELLO_WORLD = HELLO + " " + WORLD
print(HELLO_WORLD)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=simple_operators.console) -->
<!-- The below code snippet is automatically added from simple_operators.console -->

```console
+ python simple_operators.py
3
hello world
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=assignments.py) -->
<!-- The below code snippet is automatically added from assignments.py -->

```py
# Assignments can be done
# on more than one variable "simultaneously" on the same line

a, b = 3, 4
print(a, b)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=assignments.console) -->
<!-- The below code snippet is automatically added from assignments.console -->

```console
+ python assignments.py
3 4
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=unsupported_operators.py) -->
<!-- The below code snippet is automatically added from unsupported_operators.py -->

```py
# Mixing operators between numbers and strings is not supported

ONE = 1
TWO = 2
HELLO = "hello"

print(ONE + TWO + HELLO)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=unsupported_operators.console) -->
<!-- The below code snippet is automatically added from unsupported_operators.console -->

```console
+ python unsupported_operators.py
Traceback (most recent call last):
  File "unsupported_operators.py", line 6, in <module>
    print(ONE + TWO + HELLO)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Create a String, an Integer, and a Floating Point Number
MY_STRING = "hello"
MY_FLOAT = 10.0
MY_INT = 20

# Testing Code
if MY_STRING == "hello":
    print("String: %s" % MY_STRING)
if isinstance(MY_FLOAT, float) and MY_FLOAT == 10.0:
    print("Float: %f" % MY_FLOAT)
if isinstance(MY_INT, int) and MY_INT == 20:
    print("Integer: %d" % MY_INT)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
String: hello
Float: 10.000000
Integer: 20
```

<!-- AUTO-GENERATED-CONTENT:END -->
