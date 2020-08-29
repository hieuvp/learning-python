# Multiple Function Arguments

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

Every function in Python receives a predefined number of arguments,
if declared normally, like this:

```python
def myfunction(first, second, third):
    # do something with the 3 variables
    ...
```

It is possible to declare functions which receive a variable number of arguments,
using the following syntax:

```python
def foo(first, second, third, *therest):
    print("First: %s" % first)
    print("Second: %s" % second)
    print("Third: %s" % third)
    print("And all the rest... %s" % list(therest))
```

The "therest" variable is a list of variables,
which receives all arguments which were given to the "foo" function after the first 3 arguments.
So calling foo(1,2,3,4,5) will print out:

```python
def foo(first, second, third, *therest):
    print("First: %s" %(first))
    print("Second: %s" %(second))
    print("Third: %s" %(third))
    print("And all the rest... %s" %(list(therest)))

foo(1,2,3,4,5)
```

It is also possible to send functions arguments by keyword,
so that the order of the argument does not matter, using the following syntax.
The following code yields the following output: The sum is: 6 Result: 1

```python
def bar(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" %(first + second + third))

    if options.get("number") == "first":
        return first

result = bar(1, 2, 3, action = "sum", number = "first")
print("Result: %d" %(result))
```

The "bar" function receives 3 arguments.
If an additional "action" argument is received, and it instructs on summing up the numbers,
then the sum is printed out.
Alternatively, the function also knows it must return the first argument,
if the value of the "number" parameter, passed into the function, is equal to "first".

## Exercise

Fill in the foo and bar functions so they can receive a variable amount of arguments (3 or more)
The foo function must return the amount of extra arguments received.
The bar must return True if the argument with the keyword magicnumber is worth 7,
and False otherwise.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# edit the functions prototype and implementation
# def foo(a, b, c):
#     pass
#
# def bar(a, b, c):
#     pass


# Test code
# if foo(1,2,3,4) == 1:
#     print("Good.")
# if foo(1,2,3,4,5) == 2:
#     print("Better.")
# if bar(1,2,3,magicnumber = 6) == False:
#     print("Great.")
# if bar(1,2,3,magicnumber = 7) == True:
#     print("Awesome!")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
```

<!-- AUTO-GENERATED-CONTENT:END -->
