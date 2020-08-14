# Functions

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Writing Functions](#writing-functions)
- [Calling Functions](#calling-functions)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Writing Functions

A block is an area of code of written in the format of:

```python
block_head:
    1st block line
    2nd block line
    ...
```

Where a **block_line** is more Python code (even another block),
and the **block_head** is of the following format:
`block_keyword block_name(argument1, argument2, ...)`
Block keywords you already know are `if`, `for`, and `while`.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=write_functions.py) -->
<!-- The below code snippet is automatically added from write_functions.py -->

```py
# Functions in python are defined using the block keyword "def",
# followed with the function's name as the block's name.
def my_function():
    print("Hello From My Function!")


# Functions may also receive arguments
# (variables passed from the caller to the function)
def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))


# Functions may return a value to the caller, using the keyword - 'return'
def sum_two_numbers(a, b):
    return a + b
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Calling Functions

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=call_functions.py) -->
<!-- The below code snippet is automatically added from call_functions.py -->

```py
# Define our 3 functions
def my_function():
    print("Hello From My Function!")


def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))


def sum_two_numbers(a, b):
    return a + b


# Let's call the functions written above

# print(a simple greeting)
my_function()

# prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# After this line x will hold the value 3!
x = sum_two_numbers(1, 2)
print("x = %s" % x)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=call_functions.console) -->
<!-- The below code snippet is automatically added from call_functions.console -->

```console
+ python call_functions.py
Hello From My Function!
Hello, John Doe , From My Function!, I wish you a great year!
x = 3
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
def list_benefits():
    return [
        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together",
    ]


def build_sentence(benefit):
    return "%s is a benefit of functions!" % benefit


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


# Run and see all the functions work together
name_the_benefits_of_functions()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
More organized code is a benefit of functions!
More readable code is a benefit of functions!
Easier code reuse is a benefit of functions!
Allowing programmers to share and connect code together is a benefit of functions!
```

<!-- AUTO-GENERATED-CONTENT:END -->
