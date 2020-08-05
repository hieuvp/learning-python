# Functions

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [What are Functions](#what-are-functions)
- [How do you write functions in Python](#how-do-you-write-functions-in-python)
- [How do you call functions in Python](#how-do-you-call-functions-in-python)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## What are Functions

Functions are a convenient way to divide your code into useful blocks,
allowing us to order our code, make it more readable, reuse it and save some time.
Also functions are a key way to define interfaces so programmers can share their code.

## How do you write functions in Python

As we have seen on previous tutorials, Python makes use of blocks.

A block is a area of code of written in the format of:

```python
block_head:
    1st block line
    2nd block line
    ...
```

Where a block line is more Python code (even another block),
and the block head is of the following format: block_keyword block_name(argument1,argument2, ...)
Block keywords you already know are "if", "for", and "while".

Functions in python are defined using the block keyword "def",
followed with the function's name as the block's name.
For example:

```python
def my_function():
    print("Hello From My Function!")
```

Functions may also receive arguments (variables passed from the caller to the function).
For example:

```python
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))
```

Functions may return a value to the caller, using the keyword- 'return' .
For example:

```python
def sum_two_numbers(a, b):
    return a + b
```

## How do you call functions in Python

Simply write the function's name followed by (), placing any required arguments within the brackets.
For example, lets call the functions written above (in the previous example):

```python
# Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)
```

## Exercise

In this exercise you'll use an existing function,
and while adding your own to create a fully functional program.

1. Add a function named list_benefits() that returns the following list of strings:
   "More organized code",
   "More readable code",
   "Easier code reuse",
   "Allowing programmers to share and connect code together"
1. Add a function named build_sentence(info)
   which receives a single argument containing a string
   and returns a sentence starting with the given string
   and ending with the string " is a benefit of functions!"
1. Run and see all the functions work together!

```python
# Modify this function to return a list of strings as defined above
def list_benefits():
    pass

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    pass

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()
```
