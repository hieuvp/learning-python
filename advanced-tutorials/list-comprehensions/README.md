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
SENTENCE = "the quick brown fox jumps over the lazy dog"
WORDS = SENTENCE.split()


# Create a list of integers
# which specify the length of each word in a certain sentence,
# but only if the word is not the word "the"
word_lengths = []
for word in WORDS:
    if word != "the":
        word_lengths.append(len(word))
print(WORDS)
print(word_lengths)

print()

# When using a "List Comprehension", we could simplify this process
word_lengths = [len(word) for word in WORDS if word != "the"]
print(WORDS)
print(word_lengths)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=list_comprehension.console) -->
<!-- The below code snippet is automatically added from list_comprehension.console -->

```console
+ python list_comprehension.py
['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
[5, 5, 3, 5, 4, 4, 3]

['the', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
[5, 5, 3, 5, 4, 4, 3]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
print("numbers           = %s" % numbers)


# Using a "List Comprehension"
# to create a list of "positive_integers" out of the "numbers" list
positive_integers = [int(number) for number in numbers if number > 0]
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
