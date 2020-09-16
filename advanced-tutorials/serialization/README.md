# Serialization

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [`import json`](#import-json)
- [`import pickle`](#import-pickle)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## `import json`

> Python provides built-in JSON libraries to encode and decode JSON.

<br />

There are two basic formats for JSON data.
Either in a string or the object data structure.

- The **object data structure**, consists of lists and dictionaries nested inside each other.
  <br />The **object data structure** allows one to use Python methods (for lists and dictionaries)
  to add, list, search and remove elements from the data structure.
- The **string** format is mainly used to pass the data into another program
  or load into a data structure.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=json_dumps.py) -->
<!-- The below code snippet is automatically added from json_dumps.py -->

```py
# In order to use the json module, it must first be imported
import json

origin = {"name": "John", "age": 30, "city": "New York"}
print("origin          = %s" % origin)
print("type(origin)    = %s" % type(origin))


# To encode a data structure to JSON, use the "dumps()" method
# This method takes an object and returns a "string":
json_str = json.dumps(origin)
print()
print("json_str        = %s" % json_str)
print("type(json_str)  = %s" % type(json_str))


# To load JSON back to a data structure, use the "loads()" method
# This method takes a string and turns it back into the json object data structure:
json_dict = json.loads(json_str)
print()
print("json_dict       = %s" % json_dict)
print("type(json_dict) = %s" % type(json_dict))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=json_dumps.console) -->
<!-- The below code snippet is automatically added from json_dumps.console -->

```console
+ python json_dumps.py
origin          = {'name': 'John', 'age': 30, 'city': 'New York'}
type(origin)    = <class 'dict'>

json_str        = {"name": "John", "age": 30, "city": "New York"}
type(json_str)  = <class 'str'>

json_dict       = {'name': 'John', 'age': 30, 'city': 'New York'}
type(json_dict) = <class 'dict'>
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `import pickle`

> Python supports a Python proprietary data serialization method called `pickle`
> (and a faster alternative called `cPickle`).

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=pickle_dumps.py) -->
<!-- The below code snippet is automatically added from pickle_dumps.py -->

```py
import pickle

pickled_bytes = pickle.dumps({"name": "John", "age": 30, "city": "New York"})
print("pickled_bytes       = %s" % pickled_bytes)
print("type(pickled_bytes) = %s" % type(pickled_bytes))

print()

pickled_dict = pickle.loads(pickled_bytes)
print("pickled_dict        = %s" % pickled_dict)
print("type(pickled_dict)  = %s" % type(pickled_dict))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=pickle_dumps.console) -->
<!-- The below code snippet is automatically added from pickle_dumps.console -->

```console
+ python pickle_dumps.py
pickled_bytes       = b'\x80\x04\x95-\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x04name\x94\x8c\x04John\x94\x8c\x03age\x94K\x1e\x8c\x04city\x94\x8c\x08New York\x94u.'
type(pickled_bytes) = <class 'bytes'>

pickled_dict        = {'name': 'John', 'age': 30, 'city': 'New York'}
type(pickled_dict)  = <class 'dict'>
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
import json


# Add the given "name"/"salary" pair to "salaries_json"
def add_employee(salaries_json, name, salary):
    salaries = json.loads(salaries_json)
    salaries[name] = salary

    json_str = json.dumps(salaries)

    return json_str


# Testing Code
def main():
    salaries_json = '{"Alfred" : 300, "Jane" : 400 }'

    # Add key-value pair {"Me" : 800}
    new_salaries_json = add_employee(salaries_json, "Me", 800)
    salaries = json.loads(new_salaries_json)

    # Print out the JSON string
    print('salaries["Alfred"] = %s' % salaries["Alfred"])
    print('salaries["Jane"]   = %s' % salaries["Jane"])
    print('salaries["Me"]     = %s' % salaries["Me"])


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
salaries["Alfred"] = 300
salaries["Jane"]   = 400
salaries["Me"]     = 800
```

<!-- AUTO-GENERATED-CONTENT:END -->
