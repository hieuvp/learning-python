# Basic String Operations

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [`print()`](#print)
- [`index()`](#index)
- [`count()`](#count)
- [Slicing Strings](#slicing-strings)
- [Uppercase and Lowercase](#uppercase-and-lowercase)
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

# You can use single quotes to assign a string.
# However, you will face problems
# if the value to be assigned itself contains single quotes.
# You need double quotes in this case.
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

But why didn't it print out 5?
Isn't "o" the fifth character in the string?
To make things more simple,
Python (and most other programming languages) start things at 0 instead of 1.
So the index of "o" is 4.

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

For those of you using silly fonts, that is a lowercase L, not a number one.
This counts the number of l's in the string. Therefore, it should print 3.

## Slicing Strings

> You can return a range of characters by using the slice syntax.
> Specify the start index and the end index, separated by a colon,
> to return a part of the string.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_slice.py) -->
<!-- The below code snippet is automatically added from string_slice.py -->

```py
A_STRING = "Hello world!"

print("A_STRING[3:7]   = %s" % A_STRING[3:7])

# This prints a slice of the string, starting at index 3, and ending at index 6.
# But why 6 and not 7? Again, most programming languages do this -
# it makes doing math inside those brackets easier.
#
# If you just have one number in the brackets,
# it will give you the single character at that index.
# If you leave out the first number but keep the colon,
# it will give you a slice from the start to the number you left in.
# If you leave out the second number,
# it will give you a slice from the first number to the end.
#
# You can even put negative numbers inside the brackets.
# They are an easy way of starting at the end of the string instead of the beginning.
# This way, -3 means "3rd character from the end".

print("A_STRING[3:7:2] = %s" % A_STRING[3:7:2])

# This prints the characters of string from 3 to 7 skipping one character.
# This is extended slice syntax. The general form is `[start:stop:step]`.

print("A_STRING[3:7]   = %s" % A_STRING[3:7])
print("A_STRING[3:7:1] = %s" % A_STRING[3:7:1])

# Note that both of them produce same output
#
# There is no function like strrev in C to reverse a string.
# But with the above mentioned type of slice syntax you can easily reverse a string like this

print("A_STRING[::-1]  = %s" % A_STRING[::-1])
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=string_slice.console) -->
<!-- The below code snippet is automatically added from string_slice.console -->

```console
+ python string_slice.py
A_STRING[3:7]   = lo w
A_STRING[3:7:2] = l
A_STRING[3:7]   = lo w
A_STRING[3:7:1] = lo w
A_STRING[::-1]  = !dlrow olleH
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Uppercase and Lowercase

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

These make a new string with all letters converted to uppercase and lowercase, respectively.

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

This is used to determine whether the string starts with something or ends with something, respectively.
The first one will print True, as the string starts with "Hello".
The second one will print False, as the string certainly does not end with "asdfasdfasdf".

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

This splits the string into a bunch of strings grouped together in a list.
Since this example splits at a space, the first item in the list will be "Hello",
and the second will be "world!".

## Exercise

Try to fix the code to print out the correct information by changing the string.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
TEXT = "Hey there! what should this string be?"
# Length should be 20
print("Length of s = %d" % len(TEXT))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % TEXT.index("a"))

# Number of a's should be 2
print("a occurs %d times" % TEXT.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % TEXT[:5])  # Start to 5
print("The next five characters are '%s'" % TEXT[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % TEXT[12])  # Just number 12
print("The characters with odd index are '%s'" % TEXT[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % TEXT[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % TEXT.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % TEXT.lower())

# Check how a string starts
if TEXT.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if TEXT.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % TEXT.split(" "))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
Length of s = 38
The first occurrence of the letter a = 13
a occurs 1 times
The first five characters are 'Hey t'
The next five characters are 'here!'
The thirteenth character is 'h'
The characters with odd index are 'e hr!wa hudti tigb?'
The last five characters are 'g be?'
String in uppercase: HEY THERE! WHAT SHOULD THIS STRING BE?
String in lowercase: hey there! what should this string be?
Split the words of the string: ['Hey', 'there!', 'what', 'should', 'this', 'string', 'be?']
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Python Slice Strings](https://www.w3schools.com/python/gloss_python_string_slice.asp)
