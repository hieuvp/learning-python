# Basic String Operations

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [`print()`](#print)
- [`index()`](#index)
- [`count()`](#count)
- [`slice()`](#slice)
- [`upper()` and `lower()`](#upper-and-lower)
- [`startswith()` and `endswith()`](#startswith-and-endswith)
- [`split()`](#split)
- [Exercise](#exercise)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## `print()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print.py) -->
<!-- The below code snippet is automatically added from print.py -->

```py
A_STRING = "Hello world!"
print(len(A_STRING))

# We can use "single quotes" to assign a string
# However, we will face problems if the value to be assigned itself contains "single quotes"
# So we need "double quotes" in this case
print("single quotes are ' '")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=print.console) -->
<!-- The below code snippet is automatically added from print.console -->

```console
+ python print.py
12
single quotes are ' '
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `index()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_index.py) -->
<!-- The below code snippet is automatically added from string_index.py -->

```py
A_STRING = "Hello world!"

# There are actually two o's in the phrase
# This method only recognizes the first
print(A_STRING.index("o"))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_index.console) -->
<!-- The below code snippet is automatically added from string_index.console -->

```console
+ python string_index.py
4
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `count()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_count.py) -->
<!-- The below code snippet is automatically added from string_count.py -->

```py
A_STRING = "Hello world!"
print(A_STRING.count("l"))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_count.console) -->
<!-- The below code snippet is automatically added from string_count.console -->

```console
+ python string_count.py
3
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `slice()`

> Return a range of characters.

```python
slice(start, end, step)
[start:end:step]
```

| Parameter | Description                                                        |
| --------- | ------------------------------------------------------------------ |
| `start`   | The position to start the slicing. Default is `0`.                 |
| `end`     | The position to end the slicing. Slicing stops at index `end - 1`. |
| `step`    | The increment between each index for slicing. Default is `1`.      |

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_slice.py) -->
<!-- The below code snippet is automatically added from string_slice.py -->

```py
A_STRING = "Hello world!"

# Starting at index 2, and ending at index 6 (not 7)
print("A_STRING[2:7]   = %s" % A_STRING[2:7])

# Single character at an index
print("A_STRING[2]     = %s" % A_STRING[2])

# Slicing from the start to a number
print("A_STRING[:7]    = %s" % A_STRING[:7])

# Slicing from a first number to the end
print("A_STRING[2:]    = %s" % A_STRING[2:])

# Starting at the end of the string instead of the beginning by using a "negative number"
# This way, "-2" means "2nd character from the end"
print("A_STRING[-2:]   = %s" % A_STRING[-2:])

# Printing the characters of string from "2" to "7", skipping "2" characters
print("A_STRING[2:7:2] = %s" % A_STRING[2:7:2])

# Printing the characters of string from "2" to "7", skipping "1" character
# Both of these produce a same output
print("A_STRING[2:7]   = %s" % A_STRING[2:7])
print("A_STRING[2:7:1] = %s" % A_STRING[2:7:1])

# Reversing a string
print("A_STRING[::-1]  = %s" % A_STRING[::-1])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_slice.console) -->
<!-- The below code snippet is automatically added from string_slice.console -->

```console
+ python string_slice.py
A_STRING[2:7]   = llo w
A_STRING[2]     = l
A_STRING[:7]    = Hello w
A_STRING[2:]    = llo world!
A_STRING[-2:]   = d!
A_STRING[2:7:2] = low
A_STRING[2:7]   = llo w
A_STRING[2:7:1] = llo w
A_STRING[::-1]  = !dlrow olleH
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `upper()` and `lower()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_case.py) -->
<!-- The below code snippet is automatically added from string_case.py -->

```py
A_STRING = "Hello world!"
print(A_STRING.upper())
print(A_STRING.lower())
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_case.console) -->
<!-- The below code snippet is automatically added from string_case.console -->

```console
+ python string_case.py
HELLO WORLD!
hello world!
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `startswith()` and `endswith()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_check.py) -->
<!-- The below code snippet is automatically added from string_check.py -->

```py
A_STRING = "Hello world!"
print(A_STRING.startswith("Hello"))
print(A_STRING.endswith("asdfasdfasdf"))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_check.console) -->
<!-- The below code snippet is automatically added from string_check.console -->

```console
+ python string_check.py
True
False
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `split()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_split.py) -->
<!-- The below code snippet is automatically added from string_split.py -->

```py
A_STRING = "Hello world!"
A_FEW_WORDS = A_STRING.split(" ")

print(A_FEW_WORDS)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_split.console) -->
<!-- The below code snippet is automatically added from string_split.console -->

```console
+ python string_split.py
['Hello', 'world!']
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
TEXT = "String, what should it become!"

print("Length of TEXT = %d" % len(TEXT))
print("The first occurrence of the letter a = %d" % TEXT.index("a"))
print("Letter a occurs %d times" % TEXT.count("a"))
print()

# Slice the TEXT into bits
print("The first five characters are     => '%s'" % TEXT[:5])
print("The next five characters are      => '%s'" % TEXT[5:10])
print("The fourteenth character is       => '%s'" % TEXT[13])
print("The characters with odd index are => '%s'" % TEXT[1::2])
print("The last five characters are      => '%s'" % TEXT[-5:])
print()

print("TEXT in uppercase: %s" % TEXT.upper())  # Convert everything to uppercase
print("TEXT in lowercase: %s" % TEXT.lower())  # Convert everything to lowercase
print()

if TEXT.startswith("Str"):  # Check how a string starts
    print("TEXT starts with 'Str'. Good!")
if TEXT.endswith("ome!"):  # Check how a string ends
    print("TEXT ends with 'ome!'. Good!")
print()

# Split the TEXT into separate substrings, each containing only a word
print("Split the words of the TEXT: %s" % TEXT.split(" "))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
Length of TEXT = 30
The first occurrence of the letter a = 10
Letter a occurs 1 times

The first five characters are     => 'Strin'
The next five characters are      => 'g, wh'
The fourteenth character is       => 's'
The characters with odd index are => 'tig htsol tbcm!'
The last five characters are      => 'come!'

TEXT in uppercase: STRING, WHAT SHOULD IT BECOME!
TEXT in lowercase: string, what should it become!

TEXT starts with 'Str'. Good!
TEXT ends with 'ome!'. Good!

Split the words of the TEXT: ['String,', 'what', 'should', 'it', 'become!']
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Python `slice()` Function](https://www.w3schools.com/python/ref_func_slice.asp)
- [Python `slice()`](https://www.programiz.com/python-programming/methods/built-in/slice)
