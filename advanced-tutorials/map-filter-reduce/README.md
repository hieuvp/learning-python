# Map, Filter, Reduce

> **Map**, **Filter**, and **Reduce** are paradigms of **functional programming**.
> <br />They allow the programmer to write simpler, shorter code,
> <br />without necessarily needing to bother about intricacies like loops and branching.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [`map()`](#map)
- [`zip()`](#zip)
- [`filter()`](#filter)
- [`reduce()`](#reduce)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## `map()`

```python
# Syntax
map(func, *iterables)
```

Where `func` is the function on which
each element in iterables (as many as they are) would be applied on.
Notice the asterisk(`*`) on iterables? It means there can be as many iterables as possible,
in so far func has that exact number as required input arguments.
Before we move on to an example, it's important that you note the following:

1. In Python 3, the function returns a **map object** which is a **generator object**.
   To get the result as a **list**, the built-in `list()` function can be called on the **map object**.
   i.e. `list(map(func, *iterables))`
1. The number of arguments to `func` must be the number of `iterables` listed.

<br />

Let's see how these rules play out with the following examples:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=map_pets.py) -->
<!-- The below code snippet is automatically added from map_pets.py -->

```py
# Say, we have an iterable list of our favourite pet names, all in lowercase
pets = ["alfred", "tabitha", "william", "arla"]
print("pets = %s" % pets)
print()


# We need them in uppercase
upper_pets = []
for pet in pets:
    upper_pet = pet.upper()
    upper_pets.append(upper_pet)

print("By following traditional style, upper_pets = %s" % upper_pets)
print()


# With "map()",
# it's not only easier, but it's also much more flexible
upper_pets = map(str.upper, pets)
print("By using a Map, list(upper_pets) = %s" % list(upper_pets))
print("- type(upper_pets)       = %s" % type(upper_pets))
print("- type(list(upper_pets)) = %s" % type(list(upper_pets)))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=map_pets.console) -->
<!-- The below code snippet is automatically added from map_pets.console -->

```console
+ python map_pets.py
pets = ['alfred', 'tabitha', 'william', 'arla']

By following traditional style, upper_pets = ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']

By using a Map, list(upper_pets) = ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
- type(upper_pets)       = <class 'map'>
- type(list(upper_pets)) = <class 'list'>
```

<!-- AUTO-GENERATED-CONTENT:END -->

What is more important to note is that the `str.upper` function
requires only **one argument** by definition,
and so we passed just **one iterable** to it.

<br />

So, if the function you're passing requires **two**, or **three**, or **n arguments**,
then you need to pass in **two**, **three** or **n iterables** to it:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=map_circle_areas.py) -->
<!-- The below code snippet is automatically added from map_circle_areas.py -->

```py
# Say we have a list of circle areas, all in five decimal places
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

# We need to round each element in the list up to its position decimal places
# e.g.
# - Round up the first element in the list to one decimal place
# - The second element in the list to two decimal places
# - The third element in the list to three decimal places
round_circle_areas = list(map(round, circle_areas, range(1, 7)))

print("circle_areas       = %s" % circle_areas)
print("round_circle_areas = %s" % round_circle_areas)
```

<!-- AUTO-GENERATED-CONTENT:END -->

Python already blesses us with the `round()` built-in function that takes **two arguments**,
the number to round up and the number of decimal places to round the number up to.
So, since the function requires **two arguments**, we need to pass in **two iterables**.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=map_circle_areas.console) -->
<!-- The below code snippet is automatically added from map_circle_areas.console -->

```console
+ python map_circle_areas.py
circle_areas       = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
round_circle_areas = [3.6, 5.58, 4.009, 56.2424, 9.01344, 32.00013]
```

<!-- AUTO-GENERATED-CONTENT:END -->

1. So as **map** iterates through `circle_areas`, during the first iteration,
   the first element of `circle_areas, 3.56773` is passed
   along with the first element of `range(1,7), 1` to `round`,
   making it effectively become `round(3.56773, 1)`.
1. During the second iteration, the second element of `circle_areas, 5.57668`
   along with the second element of `range(1,7), 2`
   is passed to round making it translate to `round(5.57668, 2)`.
1. This happens until the end of the `circle_areas` list is reached.

<br />

I'm sure you're wondering:
"What if I pass in an iterable less than or more than the length of the first iterable?
That is, what if I pass range(1,3) or range(1, 9999) as the second iterable in the above function".
And the answer is simple: nothing! Okay, that's not true.
"Nothing" happens in the sense that the map() function will not raise any exception,
it will simply iterate over the elements until it can't find a second argument to the function,
at which point it simply stops and returns the result.

So, for example, if you evaluate result = list(map(round, circle_areas, range(1,3))),
you won't get any error even as the length of circle_areas and the length of range(1,3) differ.
Instead, this is what Python does:
It takes the first element of circle_areas and the first element of range(1,3) and passes it to round.
round evaluates it then saves the result.
Then it goes on to the second iteration,
second element of circle_areas and second element of range(1,3), round saves it again.
Now, in the third iteration (circle_areas has a third element),
Python takes the third element of circle_areas and then tries to take the third element of range(1,3)
but since range(1,3) does not have a third element,
Python simply stops and returns the result,
which in this case would simply be `[3.6, 5.58]`.

Go ahead, try it:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=map_inequable_iterables.py) -->
<!-- The below code snippet is automatically added from map_inequable_iterables.py -->

```py
circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]
print(list(map(round, circle_areas, range(1, 3))))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=map_inequable_iterables.console) -->
<!-- The below code snippet is automatically added from map_inequable_iterables.console -->

```console
+ python map_inequable_iterables.py
[3.6, 5.58]
```

<!-- AUTO-GENERATED-CONTENT:END -->

The same thing happens if `circle_areas` is less than the length of the second iterable.
Python simply stops when it can't find the next element in one of the iterables.

## `zip()`

To consolidate our knowledge of the `map()` function,
we are going to use it to implement our own custom `zip()` function.
The `zip()` function is a function that takes a number of iterables
and then creates a tuple containing each of the elements in the iterables.
Like `map()`, in Python 3, it returns a generator object,
which can be easily converted to a **list** by calling the built-in `list()` function on it.
Use the below interpreter session to get a grip of `zip()` before we create ours with `map()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=zip_strings_numbers.py) -->
<!-- The below code snippet is automatically added from zip_strings_numbers.py -->

```py
strings = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3, 4, 5]

print(list(zip(strings, numbers)))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=zip_strings_numbers.console) -->
<!-- The below code snippet is automatically added from zip_strings_numbers.console -->

```console
+ python zip_strings_numbers.py
[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
```

<!-- AUTO-GENERATED-CONTENT:END -->

As a bonus,
can you guess what would happen in the above session
if my_strings and my_numbers are not of the same length?
No? try it! Change the length of one of them.

Onto our own custom `zip()` function!

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=map_strings_numbers.py) -->
<!-- The below code snippet is automatically added from map_strings_numbers.py -->

```py
strings = ["a", "b", "c", "d", "e"]
numbers = [1, 2, 3, 4, 5]

print(list(map(lambda x, y: (x, y), strings, numbers)))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=map_strings_numbers.console) -->
<!-- The below code snippet is automatically added from map_strings_numbers.console -->

```console
+ python map_strings_numbers.py
[('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)]
```

<!-- AUTO-GENERATED-CONTENT:END -->

Just look at that! We have the same result as zip.

Did you also notice that I didn't even need
to create a function using the def my_function() standard way?
That's how flexible map(), and Python in general, is! I simply used a lambda function.
This is not to say that using the standard function definition method
(of def function_name()) isn't allowed, it still is.
I simply preferred to write less code (be "Pythonic").

## `filter()`

```python
# Syntax
filter(func, iterable)
```

The following points are to be noted regarding `filter()`:

1. Unlike `map()`, only **one iterable** is required.
1. The `func` argument is required to return a **boolean type**.
   If it doesn't, filter simply returns the iterable passed to it.
   Also, as only one iterable is required,
   it is implicit that `func` must only take one argument.
1. `filter()` passes each element in the iterable through `func`
   and returns only the ones that evaluate to `True`.

<br />

Let's see some examples:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=filter_scores.py) -->
<!-- The below code snippet is automatically added from filter_scores.py -->

```py
# The following is a list of the scores of 10 students in a Chemistry exam
all_students = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
print("all_students    = %s" % all_students)


# Find out those who passed with scores more than 75
def is_passed(score):
    return score > 75


passed_students = list(filter(is_passed, all_students))
print("passed_students = %s" % passed_students)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=filter_scores.console) -->
<!-- The below code snippet is automatically added from filter_scores.console -->

```console
+ python filter_scores.py
all_students    = [66, 90, 68, 59, 76, 60, 88, 74, 81, 65]
passed_students = [90, 76, 88, 81]
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

The next example will be a **palindrome detector**.<br />
A **palindrome** is a word, phrase, or sequence that reads the same backwards as forwards.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=filter_dromes.py) -->
<!-- The below code snippet is automatically added from filter_dromes.py -->

```py
# Filter out words that are palindromes
# from a tuple (iterable) of suspected palindromes
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
palindromes = list(filter(lambda word: word == word[::-1], dromes))

print("type(dromes) = %s" % type(dromes))
print("list(dromes) = %s" % list(dromes))
print("palindromes  = %s" % palindromes)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=filter_dromes.console) -->
<!-- The below code snippet is automatically added from filter_dromes.console -->

```console
+ python filter_dromes.py
type(dromes) = <class 'tuple'>
list(dromes) = ['demigod', 'rewire', 'madam', 'freer', 'anutforajaroftuna', 'kiosk']
palindromes  = ['madam', 'anutforajaroftuna']
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `reduce()`

```python
# Syntax
reduce(func, iterable[, initial])
```

Where `func` is the function on which each element in the `iterable` gets cumulatively applied to,
and `initial` is the optional value that gets placed
before the elements of the `iterable` in the calculation,
and serves as a default when the `iterable` is empty.
The following should be noted about `reduce()`:

1. `func` requires two arguments,
   the first of which is the first element in `iterable` (if `initial` is not supplied)
   and the second is the second element in `iterable`.
   If `initial` is supplied, then it becomes the first argument to `func`
   and the first element in `iterable` becomes the second element.
1. `reduce` **reduces** `iterable` into a single value.

<br />

As usual, let's see some examples:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=sum.py) -->
<!-- The below code snippet is automatically added from sum.py -->

```py
from functools import reduce


def sum(first, second):
    return first + second


print(reduce(sum, [6, 7, 8, 9]))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=sum.console) -->
<!-- The below code snippet is automatically added from sum.console -->

```console
+ python sum.py
30
```

<!-- AUTO-GENERATED-CONTENT:END -->

So, what happened?

As usual, it's all about iterations:
`reduce` takes the first and second elements in numbers and passes them to custom_sum respectively.
custom_sum computes their sum and returns it to reduce.
reduce then takes that result and applies it as the first element to custom_sum
and takes the next element (third) in numbers as the second element to custom_sum.
It does this continuously (cumulatively) until numbers is exhausted.

Let's see what happens when I use the optional initial value.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=sum_with_initial.py) -->
<!-- The below code snippet is automatically added from sum_with_initial.py -->

```py
from functools import reduce


def sum(first, second):
    return first + second


# Initially, using "10" as the first argument to "sum()"
print(reduce(sum, [6, 7, 8, 9], 10))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=sum_with_initial.console) -->
<!-- The below code snippet is automatically added from sum_with_initial.console -->

```console
+ python sum_with_initial.py
40
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

- **product** (mathematics)
  - a quantity obtained by multiplying one number by another
  - tích số

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
from functools import reduce

# Compute the square of each floating-point numbers rounded to two decimal places
original_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
square_floats = list(map(lambda number: round(number ** 2, 2), original_floats))
print("original_floats = %s" % original_floats)
print("square_floats   = %s" % square_floats)
print()

# Compute the names that are less than or equal to seven letters
original_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
short_names = list(filter(lambda name: len(name) <= 7, original_names))
print("original_names = %s" % original_names)
print("short_names    = %s" % short_names)
print()

# Compute the product of numbers
numbers = [1, 2, 3, 4, 5]
product_of_numbers = reduce(lambda x, y: x * y, numbers)
print("numbers            = %s" % numbers)
print("product_of_numbers = %s" % product_of_numbers)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
original_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
square_floats   = [18.92, 37.09, 10.56, 95.45, 4.67, 78.85, 21.07]

original_names = ['olumide', 'akinremi', 'josiah', 'temidayo', 'omoseun']
short_names    = ['olumide', 'josiah', 'omoseun']

numbers            = [1, 2, 3, 4, 5]
product_of_numbers = 120
```

<!-- AUTO-GENERATED-CONTENT:END -->
