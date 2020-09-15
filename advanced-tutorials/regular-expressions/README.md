# Regular Expressions

> **Regular Expressions** (sometimes shortened to `regexp`, `regex`, or `re`)
> are a tool for matching patterns in text.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Example](#example)
  - [Explanation](#explanation)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Example

An example regex is `r"^(From|To|Cc).*?python-list@python.org"`.

### Explanation

- The caret `^` matches text at the beginning of a line.
- The following group,
  the part with `(From|To|Cc)` means that
  the line has to start with one of the words that are separated by the pipe `|`.
  That is called the OR operator,
  and the regex will match if the line starts with any of the words in the group.
- The `.*?` means to un-greedily match any number of characters, except the newline `\n` character.
  The un-greedy part means to match as few repetitions as possible.
- The `.` character means any non-newline character,
  the `*` means to repeat 0 or more times, and the `?` character makes it un-greedy.

So, the following lines would be matched by that regex:
`From: python-list@python.org To: !asp]<,. python-list@python.org`

<br />

A complete reference for the re syntax is available at the python docs.
<https://docs.python.org/library/re.html#regular-expression-syntax%22RE%20syntax>

As an example of a "proper" email-matching regex (like the one in the exercise), see this
<http://www.ex-parrot.com/pdw/Mail-RFC822-Address.html>

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Example:
import re

pattern = re.compile(r"\[(on|off)\]")  # Slight optimization
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))
# Returns a Match object!
print(re.search(pattern, "Nada...:-("))
# Doesn't return anything.
# End Example


# Exercise: make a regular expression that will match an email
def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")


# Your pattern here!
pattern = r""
test_email(pattern)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
<re.Match object; span=(35, 39), match='[on]'>
None
Forgot to enter a pattern!
Forgot to enter a pattern!
Forgot to enter a pattern!
```

<!-- AUTO-GENERATED-CONTENT:END -->
