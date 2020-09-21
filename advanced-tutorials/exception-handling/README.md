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

We might have seen an exception before:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exception.py) -->
<!-- The below code snippet is automatically added from exception.py -->

```py
print(a)
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

<br />

Sometimes we don't want exceptions to completely stop the program,
we might want to do something special when an exception is raised.
<br />This is done in a `try`/`except` block:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example.py) -->
<!-- The below code snippet is automatically added from example.py -->

```py
def do_stuff_with_number(number):
    print("number = %s" % number)


def catch_this():
    # This list only has "3" numbers in it
    numbers = (11, 22, 33)

    # Iterate over "5" numbers
    for index in range(5):
        try:
            number = numbers[index]
            do_stuff_with_number(number)

        # Raised when accessing a non-existing index of a list
        except IndexError:
            # After reaching the end of "numbers",
            # we just want the rest to be interpreted as a "0"
            number = 0
            do_stuff_with_number(number)


catch_this()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example.console) -->
<!-- The below code snippet is automatically added from example.console -->

```console
+ python example.py
number = 11
number = 22
number = 33
number = 0
number = 0
```

<!-- AUTO-GENERATED-CONTENT:END -->

There, that wasn't too hard! You can do that with any exception.
<br />For more details on handling exceptions,
look no further than the
[Python Docs - Handling Exceptions](https://docs.python.org/tutorial/errors.html#handling-exceptions).

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
from pprint import pprint

actor = {"name": "John Cleese", "rank": "Awesome"}


# Get the last name of the actor
def get_last_name():
    full_name = actor["name"].split()
    last_name = full_name[-1]

    return last_name


# Exception handling
try:
    print('The actor\'s last name is "%s"' % get_last_name())
    print()
    print(actor["last name"])
except Exception as err:
    print("Exception caught!")
    pprint(err)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
The actor's last name is "Cleese"

Exception caught!
KeyError('last name')
```

<!-- AUTO-GENERATED-CONTENT:END -->
