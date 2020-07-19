# Lists

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concept](#concept)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concept

Lists are very similar to arrays.
They can contain any type of variable, and they can contain as many variables as you wish.
Lists can also be iterated over in a very simple manner.
Here is an example of how to build a list.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=list.py) -->
<!-- The below code snippet is automatically added from list.py -->

```py
my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)

print(my_list[0])  # prints 1
print(my_list[1])  # prints 2
print(my_list[2])  # prints 3

# Prints out 1,2,3
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

Accessing an index which does not exist generates an exception (an error).

```py
mylist = [1,2,3]
print(mylist[10])
```

## Exercise

In this exercise,
you will need to add numbers and strings to the correct lists using the "append" list method.
You must add the numbers 1,2, and 3 to the "numbers" list,
and the words 'hello' and 'world' to the strings variable.

You will also have to fill in the variable second_name with the second name in the names list,
using the brackets operator `[]`.
Note that the index is zero-based,
so if you want to access the second item in the list, its index will be 1.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# Write your code here
SECOND_NAME = None

# This code should write out the filled arrays
# and the second name in the names list (Eric)
print(numbers)
print(strings)
print("The second name on the names list is %s" % SECOND_NAME)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
[]
[]
The second name on the names list is None
```

<!-- AUTO-GENERATED-CONTENT:END -->
