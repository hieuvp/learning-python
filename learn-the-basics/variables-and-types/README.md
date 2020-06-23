# Variables and Types

Python is completely object oriented, and not "statically typed".
You do not need to declare variables before using them, or declare their type.
Every variable in Python is an object.

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

To define an integer, use the following syntax:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=integer.py) -->
<!-- The below code snippet is automatically added from integer.py -->

```py
myint = 7
print(myint)
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

To define a floating point number, you may use one of the following notations:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=float.py) -->
<!-- The below code snippet is automatically added from float.py -->

```py
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
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
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string.console) -->
<!-- The below code snippet is automatically added from string.console -->

```console
+ python string.py
hello
hello
```

<!-- AUTO-GENERATED-CONTENT:END -->

The difference between the two is that using double quotes makes it easy to include apostrophes
(whereas these would terminate the string if using single quotes)

```python
mystring = "Don't worry about apostrophes"
print(mystring)
```

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
# change this code
mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
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
