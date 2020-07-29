# Conditions

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Boolean Operators](#boolean-operators)
- [The `in` Operator](#the-in-operator)
- [The `is` Operator](#the-is-operator)
- [The `not` Operator](#the-not-operator)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

Python uses boolean variables to evaluate conditions.
The boolean values True and False are returned
when an expression is compared or evaluated.
For example:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=boolean_expression.py) -->
<!-- The below code snippet is automatically added from boolean_expression.py -->

```py
X = 2
print(X == 2)  # prints out True
print(X == 3)  # prints out False
print(X < 3)  # prints out True
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=boolean_expression.console) -->
<!-- The below code snippet is automatically added from boolean_expression.console -->

```console
+ python boolean_expression.py
True
False
True
```

<!-- AUTO-GENERATED-CONTENT:END -->

Notice that variable assignment is done using a single equals operator `=`,
whereas comparison between two variables is done using the double equals operator `==`.
The "not equals" operator is marked as `!=`.

## Boolean Operators

The "and" and "or" boolean operators allow building complex boolean expressions,
for example:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=boolean_operators.py) -->
<!-- The below code snippet is automatically added from boolean_operators.py -->

```py
NAME = "John"
AGE = 23

if NAME == "John" and AGE == 23:
    print("Your name is John, and you are also 23 years old.")

if NAME == "John" or NAME == "Rick":
    print("Your name is either John or Rick.")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=boolean_operators.console) -->
<!-- The below code snippet is automatically added from boolean_operators.console -->

```console
+ python boolean_operators.py
Your name is John, and you are also 23 years old.
Your name is either John or Rick.
```

<!-- AUTO-GENERATED-CONTENT:END -->

## The `in` Operator

The "in" operator could be used to check if
a specified object exists within an iterable object container,
such as a list:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=in_operator.py) -->
<!-- The below code snippet is automatically added from in_operator.py -->

```py
name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=in_operator.console) -->
<!-- The below code snippet is automatically added from in_operator.console -->

```console
+ python in_operator.py
Your name is either John or Rick.
```

<!-- AUTO-GENERATED-CONTENT:END -->

Python uses indentation to define code blocks, instead of brackets.
The standard Python indentation is 4 spaces,
although tabs and any other space size will work, as long as it is consistent.
Notice that code blocks do not need any termination.

Here is an example for using Python's `if` statement using code blocks:

```python
statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True: # else if
    # do something else
    pass
else:
    # do another thing
    pass
```

For example:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=if_statement.py) -->
<!-- The below code snippet is automatically added from if_statement.py -->

```py
X = 2
if X == 2:
    print("X equals two!")
else:
    print("X does not equal to two.")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=if_statement.console) -->
<!-- The below code snippet is automatically added from if_statement.console -->

```console
+ python if_statement.py
X equals two!
```

<!-- AUTO-GENERATED-CONTENT:END -->

A statement is evaulated as true if one of the following is correct:

1. The "True" boolean variable is given, or calculated using an expression,
   such as an arithmetic comparison.
2. An object which is not considered "empty" is passed.

Here are some examples for objects which are considered as empty:

1. An empty string: ""
2. An empty list: []
3. The number zero: 0
4. The false boolean variable: False

## The `is` Operator

Unlike the double equals operator "==",
the "is" operator does not match the values of the variables,
but the instances themselves.
For example:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=is_operator.py) -->
<!-- The below code snippet is automatically added from is_operator.py -->

```py
x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=is_operator.console) -->
<!-- The below code snippet is automatically added from is_operator.console -->

```console
+ python is_operator.py
True
False
```

<!-- AUTO-GENERATED-CONTENT:END -->

## The `not` Operator

Using "not" before a boolean expression inverts it:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=not_operator.py) -->
<!-- The below code snippet is automatically added from not_operator.py -->

```py
print(not False)  # Prints out True
print((not False) == (False))  # Prints out False
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=not_operator.console) -->
<!-- The below code snippet is automatically added from not_operator.console -->

```console
+ python not_operator.py
True
False
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

Change the variables in the first section,
so that each if statement resolves as True.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Change this code
NUMBER = 10
SECOND_NUMBER = 10
FIRST_ARRAY = []
SECOND_ARRAY = [1, 2, 3]

if NUMBER > 15:
    print("1")

if FIRST_ARRAY:
    print("2")

if len(SECOND_ARRAY) == 2:
    print("3")

if len(FIRST_ARRAY) + len(SECOND_ARRAY) == 5:
    print("4")

if FIRST_ARRAY and FIRST_ARRAY[0] == 1:
    print("5")

if not SECOND_NUMBER:
    print("6")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
```

<!-- AUTO-GENERATED-CONTENT:END -->
