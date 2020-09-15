# Generators

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> **Generator Functions** are a special kind of function that return a **Lazy Iterator**.
> <br />These are objects that you can loop over like a list.
> However, unlike lists, **Lazy Iterators** do not store their contents in memory.

<br />

- A **generator function** is defined like a **normal function**,
  <br />but whenever it needs to generate a value,
  it does so with the `yield` keyword rather than `return`.
- If the body of a `def` contains `yield`,
  the function automatically becomes a **generator function**.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=generator_function.py) -->
<!-- The below code snippet is automatically added from generator_function.py -->

```py
import random


# A "generator function" which returns "7" random integers
def lottery():
    # This function decides how to generate the random numbers on its own,
    # and executes the "yield" statements one at a time,
    # pausing in between to "yield" execution back to the main "for" loop

    for i in range(6):
        # Returning "6" numbers between 1 and 40
        yield random.randint(1, 40)

    # Returning a "7th" number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % random_number)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=generator_function.console) -->
<!-- The below code snippet is automatically added from generator_function.console -->

```console
+ python generator_function.py
And the next number is... 14!
And the next number is... 28!
And the next number is... 11!
And the next number is... 14!
And the next number is... 20!
And the next number is... 34!
And the next number is... 4!
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

1. When an iteration over a set of item starts using the `for` statement,
   the generator is run.
1. Once the generator function's code reaches a `yield` statement,
   <br />the generator yields its execution back to the `for` loop,
   returning a new value from the set.
1. The generator function can generate as many values (possibly **infinite**) as it wants,
   yielding each one in its turn.

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
from types import GeneratorType


# A generator function which returns the Fibonacci series
def fibonacci():
    # The first two numbers of the series is always equal to 1
    a = b = 1

    while True:
        yield a

        # Each consecutive number returned is the sum of the last two numbers
        # Simultaneously assign the values of "a" and "b"
        a, b = b, a + b


# Testing Code
if isinstance(fibonacci(), GeneratorType):
    print("Good! The fibonacci() function is a generator")

    counter = 0
    for number in fibonacci():

        # To not add a newline to the end of the string
        # https://docs.python.org/library/functions.html#print
        print("%d " % number, end="")

        counter += 1
        if counter == 10:
            break

    print()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
Good! The fibonacci() function is a generator
1 1 2 3 5 8 13 21 34 55
```

<!-- AUTO-GENERATED-CONTENT:END -->
