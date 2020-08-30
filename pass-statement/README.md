# `pass` Statement

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Definition and Usage](#definition-and-usage)
- [More Examples](#more-examples)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

Create a placeholder for future code:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=loop.py) -->
<!-- The below code snippet is automatically added from loop.py -->

```py
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

## Definition and Usage

- The `pass` statement is used as a placeholder for future code.

- When the `pass` statement is executed, nothing happens,
  but you avoid getting an error when empty code is not allowed.

- Empty code is not allowed in
  loops, function definitions, class definitions, or in if statements.

## More Examples

Using the `pass` keyword in a `function` definition:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=function.py) -->
<!-- The below code snippet is automatically added from function.py -->

```py
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

Using the `pass` keyword in a `class` definition:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=class.py) -->
<!-- The below code snippet is automatically added from class.py -->

```py
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

Using the `pass` keyword in an `if` statement:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=if.py) -->
<!-- The below code snippet is automatically added from if.py -->

```py
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

- [Python `pass` Statement](https://www.w3schools.com/python/ref_keyword_pass.asp)
