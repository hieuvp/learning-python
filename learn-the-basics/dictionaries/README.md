# Dictionaries

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Iterating Over Dictionaries](#iterating-over-dictionaries)
- [Removing A Value](#removing-a-value)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> A **dictionary** is a data type similar to **array**,
> but works with **keys** and **values** instead of **indexes**.
> <br />Each **value** stored in a **dictionary** can be accessed using a **key**,
> which is any type of object (string, number, list,...)
> <br />instead of using its **index** to address it.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=initialization.py) -->
<!-- The below code snippet is automatically added from initialization.py -->

```py
# A database of phone numbers could be stored using a dictionary
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

# Alternatively,
# a dictionary can be initialized with the same values in the following notation
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}
print(phonebook)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=initialization.console) -->
<!-- The below code snippet is automatically added from initialization.console -->

```console
+ python initialization.py
{'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}
{'John': 938477566, 'Jack': 938377264, 'Jill': 947662781}
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Iterating Over Dictionaries

> Dictionaries can be iterated over, just like lists.
> <br />However, a dictionary, unlike a list,
> it **does not keep the order of the values** stored in it.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=iteration.py) -->
<!-- The below code snippet is automatically added from iteration.py -->

```py
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}

# Iterate over key value pairs
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

## Removing A Value

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=remove.py) -->
<!-- The below code snippet is automatically added from remove.py -->

```py
# To remove a specified index,
# use either one of the following notations

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

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
phonebook = {"John": 938477566, "Jack": 938377264, "Jill": 947662781}

# Remove "Jill" from the "phonebook"
phonebook.pop("Jill")
if "Jill" not in phonebook:
    print("Jill is not listed in the phonebook.")

# Add "Jake" to the "phonebook" with the phone number "938273443"
phonebook["Jake"] = 938273443
if "Jake" in phonebook:
    print("Jake is listed in the phonebook.")

print("phonebook = %s" % phonebook)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
Jill is not listed in the phonebook.
Jake is listed in the phonebook.
phonebook = {'John': 938477566, 'Jack': 938377264, 'Jake': 938273443}
```

<!-- AUTO-GENERATED-CONTENT:END -->
