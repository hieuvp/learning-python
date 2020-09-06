# Lambda Functions

> A lambda function is a small anonymous function.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Syntax](#syntax)
- [Examples](#examples)
- [Why Use Lambda Functions](#why-use-lambda-functions)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Syntax

> A lambda function can take any number of arguments,
> but can only have one expression.

```python
lambda arguments : expression
```

The expression is executed and the result is returned:

## Examples

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=add.py) -->
<!-- The below code snippet is automatically added from add.py -->

```py
# A lambda function that adds 10 to the number passed in as an argument,
# and print the result:
x = lambda a: a + 10
print(x(5))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=add.console) -->
<!-- The below code snippet is automatically added from add.console -->

```console
+ python add.py
15
```

<!-- AUTO-GENERATED-CONTENT:END -->

Lambda functions can take any number of arguments:

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.py) -->
<!-- The below code snippet is automatically added from multiply.py -->

```py
# A lambda function that multiplies argument a with argument b
# and print the result:
x = lambda a, b: a * b
print(x(5, 6))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.console) -->
<!-- The below code snippet is automatically added from multiply.console -->

```console
+ python multiply.py
30
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=sum.py) -->
<!-- The below code snippet is automatically added from sum.py -->

```py
# A lambda function that sums argument a, b, and c and print the result:
x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=sum.console) -->
<!-- The below code snippet is automatically added from sum.console -->

```console
+ python sum.py
13
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Why Use Lambda Functions

> The power of lambda is better shown
> when you use them as an anonymous function inside another function.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=functions.py) -->
<!-- The below code snippet is automatically added from functions.py -->

```py

```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=functions.console) -->
<!-- The below code snippet is automatically added from functions.console -->

```console
+ python functions.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

Say you have a function definition that takes one argument,
and that argument will be multiplied with an unknown number:

```python
def myfunc(n):
  return lambda a : a * n
```

Use that function definition to make a function that always doubles the number you send in:

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
```

Or, use the same function definition to make a function that always triples the number you send in:

```python
def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
```

Or, use the same function definition to make both functions, in the same program:

```python
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
```

Use lambda functions when an anonymous function is required for a short period of time.

## References

- [Python Lambda](https://www.w3schools.com/python/python_lambda.asp)
- [ ] [Python Anonymous/Lambda Function](https://www.programiz.com/python-programming/anonymous-function)
