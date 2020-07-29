# String Formatting

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Outputting Formatted String](#outputting-formatted-string)
- [Outputting Formatted Object](#outputting-formatted-object)
- [Specifiers](#specifiers)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Outputting Formatted String

Python uses C-style string formatting to create new, formatted strings.
The "%" operator is used to format a set of variables enclosed in a "tuple" (a fixed size list),
together with a format string,
which contains normal text together with "argument specifiers",
special symbols like "%s" and "%d".

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_formatted_strings.py) -->
<!-- The below code snippet is automatically added from print_formatted_strings.py -->

```py
# Let's say you have a variable called "name" with your user name in it,
# and you would then like to print(out a greeting to that user.)
# This prints out "Hello, John!"
NAME = "John"
print("Hello, %s!" % NAME)

# To use two or more argument specifiers, use a tuple (parentheses):
# This prints out "John is 23 years old."
NAME = "John"
AGE = 23
print("%s is %d years old." % (NAME, AGE))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_formatted_strings.console) -->
<!-- The below code snippet is automatically added from print_formatted_strings.console -->

```console
+ python print_formatted_strings.py
Hello, John!
John is 23 years old.
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Outputting Formatted Object

Any object which is not a string can be formatted using the %s operator as well.
The string which returns from the `repr` method of that object is formatted as the string.

> The `repr()` function returns a printable representation of the given object.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_formatted_object.py) -->
<!-- The below code snippet is automatically added from print_formatted_object.py -->

```py
# This prints out: A list: [1, 2, 3]
my_list = [1, 2, 3]

print(repr(my_list))
print("A list: %s" % my_list)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_formatted_object.console) -->
<!-- The below code snippet is automatically added from print_formatted_object.console -->

```console
+ python print_formatted_object.py
[1, 2, 3]
A list: [1, 2, 3]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Specifiers

> Here are some basic argument specifiers you should know.

| Specifier               | Description                                                                   |
| ----------------------- | ----------------------------------------------------------------------------- |
| `%s`                    | String (or any object with a string representation, like numbers).            |
| `%d`                    | Integers.                                                                     |
| `%f`                    | Floating point numbers.                                                       |
| `%.<number of digits>f` | Floating point numbers with a fixed amount of digits to the right of the dot. |
| `%x/%X`                 | Integers in hex representation (lowercase/uppercase).                         |

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
data = ("John", "Doe", 53.44)

# A format string which prints out the data
FORMAT_STRING = "Hello %s %s. Your current balance is $%.2f"

print(FORMAT_STRING % data)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
Hello John Doe. Your current balance is $53.44
```

<!-- AUTO-GENERATED-CONTENT:END -->
