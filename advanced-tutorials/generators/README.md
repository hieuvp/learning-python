# Generators

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

Generators are very easy to implement, but a bit difficult to understand.

Generators are used to create iterators, but with a different approach.
Generators are simple functions which return an iterable set of items,
one at a time, in a special way.

When an iteration over a set of item starts using the for statement,
the generator is run.
Once the generator's function code reaches a `yield` statement,
the generator yields its execution back to the `for` loop,
returning a new value from the set.
The generator function can generate as many values (possibly infinite) as it wants,
yielding each one in its turn.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=generator_function.py) -->
<!-- The below code snippet is automatically added from generator_function.py -->

```py
import random


# A generator function which returns 7 random integers
def lottery():
    # Return 6 numbers between 1 and 40
    for i in range(6):
        print("i = %s" % i)
        yield random.randint(1, 40)

    # Return a 7th number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % random_number)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=generator_function.console) -->
<!-- The below code snippet is automatically added from generator_function.console -->

```console
+ python generator_function.py
i = 0
And the next number is... 34!
i = 1
And the next number is... 37!
i = 2
And the next number is... 29!
i = 3
And the next number is... 29!
i = 4
And the next number is... 40!
i = 5
And the next number is... 6!
And the next number is... 13!
```

<!-- AUTO-GENERATED-CONTENT:END -->

This function decides how to generate the random numbers on its own,
and executes the `yield` statements one at a time,
pausing in between to `yield` execution back to the main for loop.

## Exercise

Hint: Can you use only two variables in the generator function?
Remember that assignments can be done simultaneously.

```python
a = 1
b = 2

# Simultaneously switch the values of a and b
a, b = b, a
print(a, b)
```

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
from types import GeneratorType


# Write a generator function which returns the Fibonacci series
def fib():
    # The first two numbers of the series is always equal to 1
    a = b = 1

    while True:
        yield a

        # Each consecutive number returned is the sum of the last two numbers
        a, b = b, a + b


# Testing code
if isinstance(fib(), GeneratorType):
    print("Good! The fib() function is a generator")

    counter = 0
    for n in fib():

        # To not add a newline to the end of the string
        # https://docs.python.org/library/functions.html#print
        print("%d, " % n, end="")

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
Good! The fib() function is a generator
1, 1, 2, 3, 5, 8, 13, 21, 34, 55,
```

<!-- AUTO-GENERATED-CONTENT:END -->
