# Lists Title

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Lists](#lists)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Lists

Lists are very similar to arrays.
They can contain any type of variable, and they can contain as many variables as you wish.
Lists can also be iterated over in a very simple manner.
Here is an example of how to build a list.

```py
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)
```

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
using the brackets operator [].
Note that the index is zero-based,
so if you want to access the second item in the list, its index will be 1.

```py
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
second_name = None


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
```

This site is generously supported by DataCamp.
DataCamp offers online interactive Python Tutorials for Data Science.
Join over a million other learners and get started learning Python for data science today!
