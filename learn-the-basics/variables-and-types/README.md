# Variables and Types

Python is completely object oriented, and not "statically typed".
You do not need to declare variables before using them, or declare their type.
Every variable in Python is an object.

This tutorial will go over a few basic types of variables.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Numbers](#numbers)
- [Strings](#strings)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Numbers

Python supports two types of numbers - integers and floating point numbers.
(It also supports complex numbers, which will not be explained in this tutorial).

To define an integer, use the following syntax:

```python
myint = 7
print(myint)
```

To define a floating point number, you may use one of the following notations:

```python
myfloat = 7.0
print(myfloat)
myfloat = float(7)
print(myfloat)
```

## Strings

Strings are defined either with a single quote or a double quotes.

```python
mystring = 'hello'
print(mystring)
mystring = "hello"
print(mystring)
```

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

```python
# change this code
mystring = None
myfloat = None
myint = None

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
```
