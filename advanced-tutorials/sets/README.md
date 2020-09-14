# Sets

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

Sets are lists with no duplicate entries.
Let's say you want to collect a list of words used in a paragraph:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=words.py) -->
<!-- The below code snippet is automatically added from words.py -->

```py
print(set("my name is Eric and Eric is my name".split()))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=words.console) -->
<!-- The below code snippet is automatically added from words.console -->

```console
+ python words.py
{'my', 'and', 'is', 'Eric', 'name'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

This will print out a list containing "my", "name", "is", "Eric", and finally "and".
Since the rest of the sentence uses words which are already in the set,
they are not inserted twice.

Sets are a powerful tool in Python since they have the ability to calculate differences
and intersections between other sets.
For example, say you have a list of participants in events A and B:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=participants.py) -->
<!-- The below code snippet is automatically added from participants.py -->

```py
a = set(["Jake", "John", "Eric"])
print(a)

b = set(["John", "Jill"])
print(b)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=participants.console) -->
<!-- The below code snippet is automatically added from participants.console -->

```console
+ python participants.py
{'Eric', 'Jake', 'John'}
{'Jill', 'John'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

To find out which members attended both events, you may use the "intersection" method:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=intersection.py) -->
<!-- The below code snippet is automatically added from intersection.py -->

```py
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

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

To find out which members attended only one of the events,
use the "symmetric_difference" method:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=symmetric_difference.py) -->
<!-- The below code snippet is automatically added from symmetric_difference.py -->

```py
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=symmetric_difference.console) -->
<!-- The below code snippet is automatically added from symmetric_difference.console -->

```console
+ python symmetric_difference.py
{'Jake', 'Eric', 'Jill'}
{'Jill', 'Jake', 'Eric'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

To find out which members attended only one event and not the other,
use the "difference" method:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=difference.py) -->
<!-- The below code snippet is automatically added from difference.py -->

```py
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=difference.console) -->
<!-- The below code snippet is automatically added from difference.console -->

```console
+ python difference.py
{'Jake', 'Eric'}
{'Jill'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

To receive a list of all participants, use the "union" method:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=union.py) -->
<!-- The below code snippet is automatically added from union.py -->

```py
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.union(b))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=union.console) -->
<!-- The below code snippet is automatically added from union.console -->

```console
+ python union.py
{'Jake', 'John', 'Eric', 'Jill'}
```

<!-- AUTO-GENERATED-CONTENT:END -->

In the exercise below,
use the given lists to print out a set containing all the participants
from event A which did not attend event B.

```python
a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]
```

## References
