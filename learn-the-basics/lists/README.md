# Lists

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concept](#concept)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concept

> Lists are very similar to arrays.<br />
> They can contain any type of variable, and they can contain as many variables as you wish.<br />
> Lists can also be iterated over in a very simple manner.<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=list.py) -->
<!-- The below code snippet is automatically added from list.py -->

```py
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list[0])
print(my_list[1])
print(my_list[2])

for x in my_list:
    print(x)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=list.console) -->
<!-- The below code snippet is automatically added from list.console -->

```console
+ python list.py
1
2
3
1
2
3
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=list_exception.py) -->
<!-- The below code snippet is automatically added from list_exception.py -->

```py
my_list = [1, 2, 3]

# Accessing an index which does not exist generates an exception (an error)
print(my_list[10])
```

<!-- The below code snippet is automatically added from list.console -->
<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=list_exception.console) -->
<!-- The below code snippet is automatically added from list_exception.console -->

```console
+ python list_exception.py
Traceback (most recent call last):
  File "list_exception.py", line 4, in <module>
    print(my_list[10])
IndexError: list index out of range
```

<!-- The below code snippet is automatically added from list.console -->
<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# Add Numbers and Strings to the Lists using the "append" list method
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("hello")
strings.append("world")

SECOND_NAME = None

# Fill in the variable SECOND_NAME with the second name in the "names" list
SECOND_NAME = names[1]

# Write out the filled arrays and the second name in the names list (Eric)
print(numbers)
print(strings)
print("The second name on the names list is %s" % SECOND_NAME)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
[1, 2, 3]
['hello', 'world']
The second name on the names list is Eric
```

<!-- AUTO-GENERATED-CONTENT:END -->
