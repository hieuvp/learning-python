# Multiple Function Arguments

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> Every function in Python receives a predefined number of arguments,
> if declared normally, like this:

```python
def my_function(first, second, third):
    # do something with the 3 variables
    ...
```

<br />

It is possible to declare functions which receive a variable number of arguments,
using the following syntax:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=args.py) -->
<!-- The below code snippet is automatically added from args.py -->

```py
# "the_rest" variable is a list of variables,
# which receives all arguments which were given to the function after the first 3 arguments
def function(first, second, third, *the_rest):
    print("first    = %s" % first)
    print("second   = %s" % second)
    print("third    = %s" % third)
    print("the_rest = %s" % list(the_rest))


function(1, 2, 3, 4, 5)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=args.console) -->
<!-- The below code snippet is automatically added from args.console -->

```console
+ python args.py
first    = 1
second   = 2
third    = 3
the_rest = [4, 5]
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

It is also possible to send functions arguments by keyword,
so that the order of the argument does not matter, using the following syntax.
The following code yields the following output: The sum is: 6 Result: 1

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=kwargs.py) -->
<!-- The below code snippet is automatically added from kwargs.py -->

```py
def function(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first

    return None


RESULT = function(1, 2, 3, action="sum", number="first")
print("Result: %d" % RESULT)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=kwargs.console) -->
<!-- The below code snippet is automatically added from kwargs.console -->

```console
+ python kwargs.py
The sum is: 6
Result: 1
```

<!-- AUTO-GENERATED-CONTENT:END -->

The "bar" function receives 3 arguments.
If an additional "action" argument is received, and it instructs on summing up the numbers,
then the sum is printed out.
Alternatively, the function also knows it must return the first argument,
if the value of the "number" parameter, passed into the function, is equal to "first".

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Fill in the foo and bar functions
# so they can receive a variable amount of arguments (3 or more)
# The foo function must return the amount of extra arguments received.
# The bar must return True if the argument with the keyword magicnumber is worth 7,
# and False otherwise.


# Edit the functions prototype and implementation
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

## References

- [Python args and kwargs: Demystified](https://realpython.com/python-kwargs-and-args)
- [Python `*args`](https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp)
- [Python `**kwargs`](https://www.w3schools.com/python/gloss_python_function_arbitrary_keyword_arguments.asp)
