# Regular Expressions

> **Regular Expressions** (sometimes shortened to **`regexp`**, **`regex`**, or **`re`**)
> are a tool for matching patterns in text.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Example](#example)
  - [Explanation](#explanation)
- [Exercise](#exercise)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Example

An example regex is `r"^(From|To|Cc).*?python-list@python.org"`.

### Explanation

- The caret **`^`** matches text at the beginning of a line.
- The following group **`(From|To|Cc)`** means that:
  - The line has to start with one of the words
    that are separated by the pipe **`|`**, called the **OR** operator.
  - The regex will match if the line starts with any of the words in the group.
- The **`.*?`** means to **un-greedily** match any number of characters,
  except the newline **`\n`** character.
  <br />The **un-greedy** part means to match as few repetitions as possible.
  - The **`.`** character means any non-newline character.
  - The **`*`** means to repeat 0 or more times.
  - The **`?`** character makes it un-greedy.

<br />

So, the following lines would be matched by that regex:
`From: python-list@python.org To: !asp]<,. python-list@python.org`

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
import re

# Slight optimization
pattern = re.compile(r"\[(on|off)\]")

# Returns a Match object!
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))

# Doesn't return anything
print(re.search(pattern, "Nada...:-("))


def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org", "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % email)
        elif not your_pattern:
            print("Forgot to enter a pattern!")
        else:
            print("Pass")


# Making a regular expression that will match an email
pattern = r"^[a-z0-9._%+-]+[@][a-z0-9.-]+\.[a-z]{2,}$"
test_email(pattern)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
<re.Match object; span=(35, 39), match='[on]'>
None
Pass
Pass
You failed to match wha.t.`1an?ug{}ly@email.com
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [`re` - Regular Expression Operations](https://docs.python.org/library/re.html)
- [Mail::RFC822::Address: regexp-based address validation](https://www.ex-parrot.com/pdw/Mail-RFC822-Address.html)
