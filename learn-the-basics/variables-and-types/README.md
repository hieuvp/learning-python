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
my_int = 7
print(my_int)
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
my_float = 7.0
print(my_float)
my_float = float(7)
print(my_float)
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

Strings are defined either with a single quote or a double quotes.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string.py) -->
<!-- The below code snippet is automatically added from string.py -->

```py
# With a single quote
my_string = 'hello'
print(my_string)

# Or a double quotes
my_string = "hello"
print(my_string)

# The difference between the two is that
# using double quotes makes it easy to include apostrophes
# (whereas these would terminate the string if using single quotes)
my_string = "Don't worry about apostrophes"
print(my_string)
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

There are additional variations on defining strings that make it easier to include things
such as carriage returns, backslashes and Unicode characters.
These are beyond the scope of this tutorial, but are covered in the Python documentation.
<https://docs.python.org/tutorial/introduction.html#strings>

Simple operators can be executed on numbers and strings:

```python
one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)
```

Assignments can be done on more than one variable
"simultaneously" on the same line like this

```python
a, b = 3, 4
print(a,b)
```

Mixing operators between numbers and strings is not supported:

```python
# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)
```

## Exercise

The target of this exercise is to create a string, an integer,
and a floating point number.
The string should be named mystring and should contain the word "hello".
The floating point number should be named myfloat and should contain the number 10.0,
and the integer should be named myint and should contain the number 20.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Change this code
MY_STRING = "hello"
MY_FLOAT = 10.0
MY_INT = 20

# Testing code
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
