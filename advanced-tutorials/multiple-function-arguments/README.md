# Multiple Function Arguments

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
  - [`*args` - Arbitrary Arguments](#args---arbitrary-arguments)
  - [`**kwargs` - Arbitrary Keyword Arguments](#kwargs---arbitrary-keyword-arguments)
- [Exercise](#exercise)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> Every function in Python receives a predefined number of arguments,
> if declared normally, like this:

<br />

```python
def my_function(first, second, third):
    # do something with the 3 variables
    ...
```

### `*args` - Arbitrary Arguments

> It is possible to declare functions which receive a variable number of arguments,
> using the following syntax:

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=args.py) -->
<!-- The below code snippet is automatically added from args.py -->

```py
# "rest" receives all arguments
# which were given to the "function" after the first 3 arguments
def function(first, second, third, *rest):
    print("first  = %s" % first)
    print("second = %s" % second)
    print("third  = %s" % third)

    print()
    print("type(rest) = %s" % type(rest))
    print("list(rest) = %s" % list(rest))


function(1, 2, 3, 4, 5, 6, 7)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=args.console) -->
<!-- The below code snippet is automatically added from args.console -->

```console
+ python args.py
first  = 1
second = 2
third  = 3

type(rest) = <class 'tuple'>
list(rest) = [4, 5, 6, 7]
```

<!-- AUTO-GENERATED-CONTENT:END -->

### `**kwargs` - Arbitrary Keyword Arguments

> It is also possible to send functions arguments by keyword,
> so that the order of the argument does not matter.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=kwargs.py) -->
<!-- The below code snippet is automatically added from kwargs.py -->

```py
def function(first, second, third, **options):
    if options.get("action") == "sum":
        sum = first + second + third
        print("sum    = %s" % sum)

    if options.get("number") == "first":
        return first

    return None


result = function(1, 2, 3, action="sum", number="first")
print("result = %s" % result)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=kwargs.console) -->
<!-- The below code snippet is automatically added from kwargs.console -->

```console
+ python kwargs.py
sum    = 6
result = 1
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
# Return the amount of extra arguments received
def foo(a, b, c, *rest):
    return len(rest)


# Return True if the argument with the keyword "magic_number" is worth "7"
def bar(a, b, c, **options):
    if options.get("magic_number") == 7:
        return True

    return False


# Testing Code
if foo(1, 2, 3, 4) == 1:
    print("Good")

if foo(1, 2, 3, 4, 5) == 2:
    print("Better")

if not bar(1, 2, 3, magic_number=6):
    print("Great")

if bar(1, 2, 3, magic_number=7):
    print("Awesome")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
Good
Better
Great
Awesome
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Python args and kwargs: Demystified](https://realpython.com/python-kwargs-and-args)
- [Python `*args`](https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp)
- [Python `**kwargs`](https://www.w3schools.com/python/gloss_python_function_arbitrary_keyword_arguments.asp)
