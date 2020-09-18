# Lambda Functions

> A **Lambda Function** is a small **Anonymous Function**.

- An **anonymous function** is a function that is defined without a name.
- While **normal functions** are defined using the `def` keyword,
  **anonymous functions** are defined using the `lambda` keyword.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Syntax](#syntax)
- [Examples](#examples)
  - [`double()`](#double)
  - [`multiply()`](#multiply)
  - [`sum()`](#sum)
- [Why Use Lambda Functions](#why-use-lambda-functions)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Syntax

> A **lambda function** can take **any number of arguments**,
> but can only have **one expression**:

```python
lambda arguments: expression
```

The `expression` is evaluated and result is returned.

## Examples

### `double()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=double.py) -->
<!-- The below code snippet is automatically added from double.py -->

```py
# A lambda function that doubles to the number passed in as an argument
lambda_double = lambda x: x * 2


# The statement is nearly the same as
def normal_double(x):
    return x * 2


print("lambda_double(8) = %s" % lambda_double(8))
print("normal_double(8) = %s" % normal_double(8))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=double.console) -->
<!-- The below code snippet is automatically added from double.console -->

```console
+ python double.py
lambda_double(8) = 16
normal_double(8) = 16
```

<!-- AUTO-GENERATED-CONTENT:END -->

### `multiply()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.py) -->
<!-- The below code snippet is automatically added from multiply.py -->

```py
# A lambda function that multiplies argument a with argument b
multiply = lambda a, b: a * b
print(multiply(5, 6))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=multiply.console) -->
<!-- The below code snippet is automatically added from multiply.console -->

```console
+ python multiply.py
30
```

<!-- AUTO-GENERATED-CONTENT:END -->

### `sum()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=sum.py) -->
<!-- The below code snippet is automatically added from sum.py -->

```py
# A lambda function that sums argument a, b, and c
sum = lambda a, b, c: a + b + c
print(sum(5, 6, 2))
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

> Use **lambda functions**
> when an **anonymous function** is required for a short period of time.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=functions.py) -->
<!-- The below code snippet is automatically added from functions.py -->

```py
# The power of lambda is better shown
# when you use them as an anonymous function inside another function

# Having a function definition that takes one argument
def my_func(n):
    # The argument will be multiplied with an unknown number
    return lambda a: a * n


# Using that function definition to make a function
# that always doubles the number you send in
my_doubler = my_func(2)
print("my_doubler(11) = %s" % my_doubler(11))


# Or, using the same function definition to make a function
# that always triples the number you send in
my_tripler = my_func(3)
print("my_tripler(11) = %s" % my_tripler(11))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=functions.console) -->
<!-- The below code snippet is automatically added from functions.console -->

```console
+ python functions.py
my_doubler(11) = 22
my_tripler(11) = 33
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Python Lambda](https://www.w3schools.com/python/python_lambda.asp)
- [Python Anonymous/Lambda Function](https://www.programiz.com/python-programming/anonymous-function)
