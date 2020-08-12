# Dictionaries

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Iterating over dictionaries](#iterating-over-dictionaries)
- [Removing a value](#removing-a-value)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

A dictionary is a data type similar to arrays, but works with keys and values instead of indexes.
Each value stored in a dictionary can be accessed using a key,
which is any type of object (a string, a number, a list, etc.)
instead of using its index to address it.

For example, a database of phone numbers could be stored using a dictionary like this:

```python
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)
```

Alternatively, a dictionary can be initialized with the same values in the following notation:

```python
phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)
```

## Iterating over dictionaries

Dictionaries can be iterated over, just like a list.
However, a dictionary, unlike a list, does not keep the order of the values stored in it.
To iterate over key value pairs, use the following syntax:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=iteration.py) -->
<!-- The below code snippet is automatically added from iteration.py -->

```py
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=iteration.console) -->
<!-- The below code snippet is automatically added from iteration.console -->

```console
+ python iteration.py
Phone number of John is 938477566
Phone number of Jack is 938377264
Phone number of Jill is 947662781
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Removing a value

To remove a specified index, use either one of the following notations:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=remove.py) -->
<!-- The below code snippet is automatically added from remove.py -->

```py
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
del phonebook["John"]
print(phonebook)

# Or

phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
phonebook.pop("John")
print(phonebook)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=remove.console) -->
<!-- The below code snippet is automatically added from remove.console -->

```console
+ python remove.py
{'Jack': 938377264, 'Jill': 947662781}
{'Jack': 938377264, 'Jill': 947662781}
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

Add "Jake" to the phonebook with the phone number 938273443,
and remove Jill from the phonebook.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}

# write your code here


# testing code
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
```

<!-- AUTO-GENERATED-CONTENT:END -->
