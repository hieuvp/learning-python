# String Formatting

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Formatted Strings](#formatted-strings)
- [Formatted Objects](#formatted-objects)
- [Argument Specifiers](#argument-specifiers)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Formatted Strings

- The `%` operator is used to format a set of variables
  enclosed in a [**tuple**](https://dictionary.cambridge.org/pronunciation/english/tuple)
  (a fixed size list).
- A format string contains normal text together with [**argument specifiers**](#argument-specifiers)
  (special symbols like `%s` and `%d`).

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_formatted_strings.py) -->
<!-- The below code snippet is automatically added from print_formatted_strings.py -->

```py
NAME = "John"
print("Hello, %s!" % NAME)

# For two or more argument specifiers, use a "tuple" e.g. "(NAME, AGE)"
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

## Formatted Objects

- Any **object** which is not a string can be formatted using the `%s` specifier.
- The returned string is a result from the `repr()` function of that **object**.
- `repr()` function returns a printable **string representation** of a given **object**.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_formatted_object.py) -->
<!-- The below code snippet is automatically added from print_formatted_object.py -->

```py
MY_LIST = [1, 2, 3]

print("repr(MY_LIST) = %s" % repr(MY_LIST))
print("MY_LIST       = %s" % MY_LIST)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print_formatted_object.console) -->
<!-- The below code snippet is automatically added from print_formatted_object.console -->

```console
+ python print_formatted_object.py
repr(MY_LIST) = [1, 2, 3]
MY_LIST       = [1, 2, 3]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Argument Specifiers

| Specifier               | Description                                                                  |
| ----------------------- | ---------------------------------------------------------------------------- |
| `%s`                    | String or any object with a string representation (like number).             |
| `%d`                    | Integer.                                                                     |
| `%f`                    | Floating point number.                                                       |
| `%.<number of digits>f` | Floating point number with a fixed amount of digits to the right of the dot. |
| `%x/%X`                 | Integer in hex representation (lowercase/uppercase).                         |

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
FORMAT_STRING = "Hello %s %s. Your current balance is $%.2f"
DATA = ("John", "Doe", 53.44)

print(FORMAT_STRING % DATA)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
Hello John Doe. Your current balance is $53.44
```

<!-- AUTO-GENERATED-CONTENT:END -->
