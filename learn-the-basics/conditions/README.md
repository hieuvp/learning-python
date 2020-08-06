# Conditions

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Boolean Expressions](#boolean-expressions)
- [`and` and `or` Boolean Operators](#and-and-or-boolean-operators)
- [`in` Operator](#in-operator)
- [`if` Statements](#if-statements)
- [`is` Operator](#is-operator)
- [`not` Operator](#not-operator)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Boolean Expressions

> Python uses boolean variables to evaluate conditions.<br />
> The boolean values `True` and `False` are returned
> when an expression is compared or evaluated.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=boolean_expression.py) -->
<!-- The below code snippet is automatically added from boolean_expression.py -->

```py
# Variable assignment is done using a single equals operator `=`
X = 2

# Whereas comparison between two variables is done using the double equals operator `==`
print("(X == 2) = %s" % (X == 2))

# The "not equals" operator is marked as `!=`
print("(X != 2) = %s" % (X != 2))

print("(X < 3)  = %s" % (X < 3))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=boolean_expression.console) -->
<!-- The below code snippet is automatically added from boolean_expression.console -->

```console
+ python boolean_expression.py
(X == 2) = True
(X != 2) = False
(X < 3)  = True
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `and` and `or` Boolean Operators

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

## `in` Operator

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=in_operator.py) -->
<!-- The below code snippet is automatically added from in_operator.py -->

```py
NAME = "John"

# The "in" operator could be used to check if
# a specified object exists within an iterable object container (e.g. list)
if NAME in ["John", "Rick"]:
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

## `if` Statements

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

<br />

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

<br />

A statement is evaluated as `True` if one of the following is correct:

1. The `True` boolean variable is given,
   or calculated using an expression (such as an arithmetic comparison).
2. An object which is not considered **empty** is passed.

Here are some examples for objects which are considered as **empty**:

1. An empty **list**: `[]`
1. An empty **string**: `""`
1. The **number** zero: `0`
1. The false **boolean** variable: `False`

## `is` Operator

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=is_operator.py) -->
<!-- The below code snippet is automatically added from is_operator.py -->

```py
x = [1, 2, 3]
y = [1, 2, 3]

print("(x == y) = %s" % (x == y))

# Unlike the "double equals (==)" operator,
# "is" operator does not match the "values" of the variables, but the "instances" themselves
print("(x is y) = %s" % (x is y))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=is_operator.console) -->
<!-- The below code snippet is automatically added from is_operator.console -->

```console
+ python is_operator.py
(x == y) = True
(x is y) = False
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `not` Operator

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=not_operator.py) -->
<!-- The below code snippet is automatically added from not_operator.py -->

```py
# Using "not" before a "boolean expression" inverts it
print(not False)
print((not False) == False)
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

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Change these variables, so that each "if" statement resolves as "True"
NUMBER = 16              # Original NUMBER = 10
SECOND_NUMBER = 0        # Original SECOND_NUMBER = 10
FIRST_ARRAY = [1, 2, 3]  # Original FIRST_ARRAY = []
SECOND_ARRAY = [4, 5]    # Original SECOND_ARRAY = [1, 2, 3]

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
1
2
3
4
5
6
```

<!-- AUTO-GENERATED-CONTENT:END -->
