# `pass` Statement

> Create a placeholder for future code.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Definition and Usage](#definition-and-usage)
- [Syntax](#syntax)
- [More Examples](#more-examples)
  - [Loops](#loops)
  - [Function Definitions](#function-definitions)
  - [Class Definitions](#class-definitions)
  - [If Statements](#if-statements)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

<!-- AUTO-GENERATED-CONTENT:END -->

## Definition and Usage

- The `pass` statement is used as a placeholder for future code.

- When the `pass` statement is executed, nothing happens,
  but you avoid getting an error when empty code is not allowed.

- Empty code is not allowed in
  loops, function definitions, class definitions, or in if statements.

- It is used when a statement is required syntactically
  but you do not want any command or code to execute.

- The `pass` statement is a **null** operation, nothing happens when it executes.

- The `pass` is also useful in places where your code will eventually go,
  but has not been written yet (e.g., in stubs for example)

## Syntax

```python
pass
```

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example.py) -->
<!-- The below code snippet is automatically added from example.py -->

```py
for letter in "Python":
    if letter == "h":
        pass
        print("This is pass block")
    print("Current Letter :%s" % letter)

print("Good bye!")
```

<!-- AUTO-GENERATED-CONTENT:END -->

When the above code is executed, it produces following result:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=example.console) -->
<!-- The below code snippet is automatically added from example.console -->

```console
+ python example.py
Current Letter :P
Current Letter :y
Current Letter :t
This is pass block
Current Letter :h
Current Letter :o
Current Letter :n
Good bye!
```

<!-- AUTO-GENERATED-CONTENT:END -->

## More Examples

### Loops

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=loop.py) -->
<!-- The below code snippet is automatically added from loop.py -->

```py
# Using the `pass` keyword in a `for` loop

for x in [0, 1, 2]:
    pass
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=loop.console) -->
<!-- The below code snippet is automatically added from loop.console -->

```console
+ python loop.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

### Function Definitions

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=function.py) -->
<!-- The below code snippet is automatically added from function.py -->

```py
# Using the `pass` keyword in a `function` definition:


def my_function():
    pass
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=function.console) -->
<!-- The below code snippet is automatically added from function.console -->

```console
+ python function.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

### Class Definitions

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=class.py) -->
<!-- The below code snippet is automatically added from class.py -->

```py
# Using the `pass` keyword in a `class` definition:


class Person:
    pass
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=class.console) -->
<!-- The below code snippet is automatically added from class.console -->

```console
+ python class.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

### If Statements

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=if.py) -->
<!-- The below code snippet is automatically added from if.py -->

```py
# Using the `pass` keyword in an `if` statement:

a = 33
b = 200

if b > a:
    pass
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=if.console) -->
<!-- The below code snippet is automatically added from if.console -->

```console
+ python if.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Python `pass` Statement - W3Schools](https://www.w3schools.com/python/ref_keyword_pass.asp)
- [Python `pass` Statement - Tutorialspoint](https://www.tutorialspoint.com/python/python_pass_statement.htm)
