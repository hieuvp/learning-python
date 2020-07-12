# Hello, World

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [`print()`](#print)
- [Indentation](#indentation)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## `print()`

It simply prints out a line (and also includes a newline).

There are two major Python versions, Python 2 and Python 3.
Python 2 and 3 are quite different.
This tutorial uses Python 3, because it more semantically correct and supports newer features.

For example, one difference between Python 2 and 3 is the print statement.
In Python 2, the "print" statement is not a function, and therefore it is invoked without parentheses.
However, in Python 3, it is a function, and must be invoked with parentheses.

To print a string in Python 3, just write:

```python
print("This line will be printed.")
```

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print.py) -->
<!-- The below code snippet is automatically added from print.py -->

```py
print("Hello, World!")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print.console) -->
<!-- The below code snippet is automatically added from print.console -->

```console
+ python exercise.py
Hello, World!
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Indentation

Python uses indentation for blocks, instead of curly braces.
Both tabs and spaces are supported,
but the standard indentation requires standard Python code to use four spaces.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=indentation.py) -->
<!-- The below code snippet is automatically added from indentation.py -->

```py
x = 1
if x == 1:
    # Indented four spaces
    print("x is 1.")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=indentation.console) -->
<!-- The below code snippet is automatically added from indentation.console -->

```console
+ python indentation.py
x is 1.
```

<!-- AUTO-GENERATED-CONTENT:END -->
