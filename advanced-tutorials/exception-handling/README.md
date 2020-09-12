# Exception Handling

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> Python's solution to **errors** are **exceptions**.

<br />

You might have seen an exception before:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exception.py) -->
<!-- The below code snippet is automatically added from exception.py -->

```py
print(a)

# error
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'a' is not defined
# </module></stdin>
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exception.console) -->
<!-- The below code snippet is automatically added from exception.console -->

```console
+ python exception.py
Traceback (most recent call last):
  File "exception.py", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
+ true
```

<!-- AUTO-GENERATED-CONTENT:END -->

Oops! Forgot to assign a value to the `'a'` variable.

But sometimes you don't want exceptions to completely stop the program.
You might want to do something special when an exception is raised.
This is done in a try/except block.

Here's a trivial example: Suppose you're iterating over a list.
You need to iterate over 20 numbers, but the list is made from user input,
and might not have 20 numbers in it.
After you reach the end of the list,
you just want the rest of the numbers to be interpreted as a 0.
Here's how you could do that:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example.py) -->
<!-- The below code snippet is automatically added from example.py -->

```py
def do_stuff_with_number(n):
    print(n)


def catch_this():
    the_list = (1, 2, 3, 4, 5)

    for i in range(20):
        try:
            do_stuff_with_number(the_list[i])
        except IndexError:  # Raised when accessing a non-existing index of a list
            do_stuff_with_number(0)


catch_this()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example.console) -->
<!-- The below code snippet is automatically added from example.console -->

```console
+ python example.py
1
2
3
4
5
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
```

<!-- AUTO-GENERATED-CONTENT:END -->

There, that wasn't too hard! You can do that with any exception.
For more details on handling exceptions, look no further than the Python Docs
<https://docs.python.org/tutorial/errors.html#handling-exceptions>

## Exercise

Handle all the exception!
Think back to the previous lessons to return the last name of the actor.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Setup
actor = {"name": "John Cleese", "rank": "awesome"}

# Function to modify!!!
# def get_last_name():
#     return actor["last_name"]

# Test code
# get_last_name()
# print("All exceptions caught! Good job!")
# print("The actor's last name is %s" % get_last_name())
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
```

<!-- AUTO-GENERATED-CONTENT:END -->
