# Basic Operators

This section explains how to use basic operators in Python.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Arithmetic Operators](#arithmetic-operators)
- [Using Operators with Strings](#using-operators-with-strings)
- [Using Operators with Lists](#using-operators-with-lists)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Arithmetic Operators

Just as any other programming languages,
the addition, subtraction, multiplication, and division operators can be used with numbers.

```py
number = 1 + 2 * 3 / 4.0
print(number)
```

Try to predict what the answer will be. Does python follow order of operations?

Another operator available is the modulo (%) operator,
which returns the integer remainder of the division. dividend % divisor = remainder.

```py
remainder = 11 % 3
print(remainder)
```

Using two multiplication symbols makes a power relationship.

```py
squared = 7 ** 2
cubed = 2 ** 3
print(squared)
print(cubed)
```

## Using Operators with Strings

Python supports concatenating strings using the addition operator:

```py
helloworld = "hello" + " " + "world"
print(helloworld)
```

Python also supports multiplying strings to form a string with a repeating sequence:

```py
lotsofhellos = "hello" * 10
print(lotsofhellos)
```

## Using Operators with Lists

Lists can be joined with the addition operators:

```py
even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
```

Just as in strings,
Python supports forming new lists with a repeating sequence using the multiplication operator:

```py
print([1,2,3] * 3)
```

## Exercise

The target of this exercise is to create two lists called x_list and y_list,
which contain 10 instances of the variables x and y, respectively.
You are also required to create a list called big_list,
which contains the variables x and y, 10 times each,
by concatenating the two lists you have created.

```py
x = object()
y = object()

# TODO: change this code
x_list = [x]
y_list = [y]
big_list = []

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
```

This site is generously supported by DataCamp.
DataCamp offers online interactive Python Tutorials for Data Science.
Join over a million other learners and get started learning Python for data science today!
