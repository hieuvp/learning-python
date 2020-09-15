# Serialization

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [`json`](#json)
- [`pickle`](#pickle)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## `json`

> Python provides built-in JSON libraries to encode and decode JSON.

There are two basic formats for JSON data.
Either in a string or the object datastructure.
The object datastructure, in Python, consists of lists and dictionaries nested inside each other.
The object datastructure allows one to use python methods (for lists and dictionaries)
to add, list, search and remove elements from the datastructure.
The String format is mainly used to pass the data into another program or load into a datastructure.

To load JSON back to a data structure, use the "loads" method.
This method takes a string and turns it back into the json object datastructure:

```python
# In order to use the json module, it must first be imported
import json

print(json.loads(json_string))
```

To encode a data structure to JSON, use the "dumps" method.
This method takes an object and returns a String:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=json_dumps.py) -->
<!-- The below code snippet is automatically added from json_dumps.py -->

```py
import json

json_string = json.dumps([1, 2, 3, "a", "b", "c"])
print(json_string)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=json_dumps.console) -->
<!-- The below code snippet is automatically added from json_dumps.console -->

```console
+ python json_dumps.py
[1, 2, 3, "a", "b", "c"]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `pickle`

Python supports a Python proprietary data serialization method called pickle
(and a faster alternative called cPickle).

You can use it exactly the same way.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=pickle_dumps.py) -->
<!-- The below code snippet is automatically added from pickle_dumps.py -->

```py
import pickle

pickled_string = pickle.dumps([1, 2, 3, "a", "b", "c"])
print(pickle.loads(pickled_string))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=pickle_dumps.console) -->
<!-- The below code snippet is automatically added from pickle_dumps.console -->

```console
+ python pickle_dumps.py
[1, 2, 3, 'a', 'b', 'c']
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

The aim of this exercise is
to print out the JSON string with key-value pair "Me" : 800 added to it.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# import json


# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json, name, salary):
    # Add your code here

    return salaries_json


# Testing Code
# salaries = '{"Alfred" : 300, "Jane" : 400 }'
# new_salaries = add_employee(salaries, "Me", 800)
# decoded_salaries = json.loads(new_salaries)
# print(decoded_salaries["Alfred"])
# print(decoded_salaries["Jane"])
# print(decoded_salaries["Me"])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
```

<!-- AUTO-GENERATED-CONTENT:END -->
