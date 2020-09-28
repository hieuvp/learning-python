# Sets

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Usages](#usages)
  - [`intersection()`](#intersection)
  - [`symmetric_difference()`](#symmetric_difference)
  - [`difference()`](#difference)
  - [`union()`](#union)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> **Sets** are lists with no duplicate entries.

<br />

Let's say you want to collect a list of words used in a paragraph:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=words.py) -->
<!-- The below code snippet is automatically added from words.py -->

```py
sentence = "my name is Harrison and Harrison is my name"
print(set(sentence.split()))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=words.console) -->
<!-- The below code snippet is automatically added from words.console -->

```console
+ python words.py
{'is', 'Harrison', 'my', 'and', 'name'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

Since the rest of the sentence uses words which are already in the set,
they are not inserted twice.

## Usages

> **Sets** are a powerful tool in Python since they have the ability
> to calculate **differences** and **intersections** between **other sets**.

### `intersection()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=intersection.py) -->
<!-- The below code snippet is automatically added from intersection.py -->

```py
# Say we have a list of participants in events A and B
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended both events
print(a.intersection(b))
print(b.intersection(a))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=intersection.console) -->
<!-- The below code snippet is automatically added from intersection.console -->

```console
+ python intersection.py
{'John'}
{'John'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

### `symmetric_difference()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=symmetric_difference.py) -->
<!-- The below code snippet is automatically added from symmetric_difference.py -->

```py
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended only one of the events
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=symmetric_difference.console) -->
<!-- The below code snippet is automatically added from symmetric_difference.console -->

```console
+ python symmetric_difference.py
{'Jill', 'Eric', 'Jake'}
{'Jill', 'Eric', 'Jake'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

### `difference()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=difference.py) -->
<!-- The below code snippet is automatically added from difference.py -->

```py
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended only one event and not the other
print(a.difference(b))
print(b.difference(a))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=difference.console) -->
<!-- The below code snippet is automatically added from difference.console -->

```console
+ python difference.py
{'Eric', 'Jake'}
{'Jill'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

### `union()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=union.py) -->
<!-- The below code snippet is automatically added from union.py -->

```py
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To receive a list of all participants
print(a.union(b))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=union.console) -->
<!-- The below code snippet is automatically added from union.console -->

```console
+ python union.py
{'Jill', 'John', 'Jake', 'Eric'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

# Print out all participants from the event A who did not attend the event B
print(set(a).difference(set(b)))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
{'Eric', 'Jake'}
```

<!-- AUTO-GENERATED-CONTENT:END -->
