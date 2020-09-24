# Code Introspection

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> **Code Introspection** is the ability
> to examine **classes**, **functions** and **keywords**<br />
> to know what they are, what they do and what they know.

<br />

Python provides several functions and utilities for **code introspection**:

```python
help()
dir()
hasattr()
id()
type()
repr()
callable()
issubclass()
isinstance()
__doc__
__name__
```

<br />

Often the most important one is the **`help()`** function,
since you can use it to find what other functions do.

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Use the "help()" function to see what each function does:
# - help(dir)
# - help(hasattr)
# - help(id)


# Define the "Vehicle" class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        return "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)


# List all attributes of the "Vehicle" class
for attribute in dir(Vehicle):
    if hasattr(Vehicle, attribute) and not attribute.startswith("__"):
        print(attribute)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
color
description
kind
name
value
```

<!-- AUTO-GENERATED-CONTENT:END -->
