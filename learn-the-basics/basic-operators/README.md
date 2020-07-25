# Basic Operators

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Arithmetic Operators](#arithmetic-operators)
- [Using Operators with Strings](#using-operators-with-strings)
- [Using Operators with Lists](#using-operators-with-lists)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Arithmetic Operators

> The addition, subtraction, multiplication, and division operators can be used with numbers.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=simple_operator.py) -->
<!-- The below code snippet is automatically added from simple_operator.py -->

```py
NUMBER = 1 + 2 * 3 / 4.0
print(NUMBER)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=simple_operator.console) -->
<!-- The below code snippet is automatically added from simple_operator.console -->

```console
+ python simple_operator.py
2.5
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

> The modulo (`%`) operator,
> which returns the integer remainder of the division.
> <br />`dividend /ˈdɪvɪdend/ % divisor = remainder`.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=modulo_operator.py) -->
<!-- The below code snippet is automatically added from modulo_operator.py -->

```py
REMAINDER = 11 % 3
print(REMAINDER)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=modulo_operator.console) -->
<!-- The below code snippet is automatically added from modulo_operator.console -->

```console
+ python modulo_operator.py
2
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

> Using two multiplication symbols makes a power relationship.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=power_operator.py) -->
<!-- The below code snippet is automatically added from power_operator.py -->

```py
SQUARED = 7 ** 2
CUBED = 2 ** 3
print(SQUARED)
print(CUBED)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=power_operator.console) -->
<!-- The below code snippet is automatically added from power_operator.console -->

```console
+ python power_operator.py
49
8
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Using Operators with Strings

> Python supports concatenating strings using the addition operator.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=concatenate_strings.py) -->
<!-- The below code snippet is automatically added from concatenate_strings.py -->

```py
HELLO_WORLD = "hello" + " " + "world"
print(HELLO_WORLD)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=concatenate_strings.console) -->
<!-- The below code snippet is automatically added from concatenate_strings.console -->

```console
+ python concatenate_strings.py
hello world
```

<!-- AUTO-GENERATED-CONTENT:END -->

> Python also supports multiplying strings to form a string with a repeating sequence.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply_strings.py) -->
<!-- The below code snippet is automatically added from multiply_strings.py -->

```py
LOTS_OF_HELLOS = "hello_" * 10
print(LOTS_OF_HELLOS)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply_strings.console) -->
<!-- The below code snippet is automatically added from multiply_strings.console -->

```console
+ python multiply_strings.py
hello_hello_hello_hello_hello_hello_hello_hello_hello_hello_
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Using Operators with Lists

> Lists can be joined with the addition operators.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=join_lists.py) -->
<!-- The below code snippet is automatically added from join_lists.py -->

```py
even_numbers = [2, 4, 6, 8]
odd_numbers = [1, 3, 5, 7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=join_lists.console) -->
<!-- The below code snippet is automatically added from join_lists.console -->

```console
+ python join_lists.py
[1, 3, 5, 7, 2, 4, 6, 8]
```

<!-- AUTO-GENERATED-CONTENT:END -->

> Just as in strings,
> Python supports forming new lists with a repeating sequence using the multiplication operator.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=repeat_list.py) -->
<!-- The below code snippet is automatically added from repeat_list.py -->

```py
print([1, 2, 3] * 3)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=repeat_list.console) -->
<!-- The below code snippet is automatically added from repeat_list.console -->

```console
+ python repeat_list.py
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
x = object()
y = object()

# Create two lists
# which contain 10 instances of the variables x and y, respectively
x_list = [x] * 10
y_list = [y] * 10

# Create a list
# which contains the variables x and y, 10 times each,
# by concatenating the two lists you have just created
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# Testing Code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
x_list contains 10 objects
y_list contains 10 objects
big_list contains 20 objects
Almost there...
Great!
```

<!-- AUTO-GENERATED-CONTENT:END -->
