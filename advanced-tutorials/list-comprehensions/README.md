# List Comprehensions

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Concepts](#concepts)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Concepts

> **List Comprehension** is a very powerful tool,
> <br />which creates a new list based on another list, in a single, readable line.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=list_comprehension.py) -->
<!-- The below code snippet is automatically added from list_comprehension.py -->

```py
words = "the quick brown fox jumps over the lazy dog".split()
print("words = %s\n" % words)


# Create a list of integers
# which specifies the length of each word in the sentence,
# but only if the "word" is not the word "the"

lengths = []
for word in words:
    if word != "the":
        lengths.append(len(word))
print("By traditional style,        lengths = %s" % lengths)

# When using a "List Comprehension", we could simplify this process
lengths = [len(word) for word in words if word != "the"]
print("By using List Comprehension, lengths = %s" % lengths)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=list_comprehension.console) -->
<!-- The below code snippet is automatically added from list_comprehension.console -->

```console
+ python list_comprehension.py
words = ['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

By traditional style,        lengths = [5, 5, 3, 5, 4, 4, 3]
By using List Comprehension, lengths = [5, 5, 3, 5, 4, 4, 3]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Use a "List Comprehension"
# to create a list of "positive_integers" out of "numbers"
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_integers = [int(number) for number in numbers if number > 0]

print("numbers           = %s" % numbers)
print("positive_integers = %s" % positive_integers)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
numbers           = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
positive_integers = [34, 44, 68, 44, 12]
```

<!-- AUTO-GENERATED-CONTENT:END -->
