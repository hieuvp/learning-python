# Regular Expressions

> **Regular Expressions** (sometimes shortened to **`regexp`**, **`regex`**, or **`re`**)
> are a tool for matching patterns in text.

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Example](#example)
  - [Explanation](#explanation)
- [`re.search()`](#research)
- [`re.match()`](#rematch)
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

## `re.search()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=search.py) -->
<!-- The below code snippet is automatically added from search.py -->

```py
import re

# Slight optimization
pattern = re.compile(r"\[(on|off)\]")

# Returning a matched object
print(re.search(pattern, "Mono: Playback 65 [75%] [-16.50dB] [on]"))

# Doesn't return anything
print(re.search(pattern, "Nada...:-("))
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=search.console) -->
<!-- The below code snippet is automatically added from search.console -->

```console
+ python search.py
<re.Match object; span=(35, 39), match='[on]'>
None
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `re.match()`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=match.py) -->
<!-- The below code snippet is automatically added from match.py -->

```py
import re

# Compile a regular expression pattern that will match an email
REGEX = re.compile(r"^[a-z0-9._%+-]+[@][a-z0-9.-]+\.[a-z]{2,}$")


# Define a function for validating an email
def check(email):
    if re.match(REGEX, email):
        print('Passed! "%s" is an email' % email)
    else:
        print('Failed! "%s" does not match the email pattern "%s"' % (email, REGEX.pattern))


check("john@example.com")
check("python-list@python.org")
check("wha.t.`1an?ug{}ly@email.com")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=match.console) -->
<!-- The below code snippet is automatically added from match.console -->

```console
+ python match.py
Passed! "john@example.com" is an email
Passed! "python-list@python.org" is an email
Failed! "wha.t.`1an?ug{}ly@email.com" does not match the email pattern "^[a-z0-9._%+-]+[@][a-z0-9.-]+\.[a-z]{2,}$"
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [`re` - Regular Expression Operations](https://docs.python.org/library/re.html)
- [Mail::RFC822::Address: regexp-based address validation](https://www.ex-parrot.com/pdw/Mail-RFC822-Address.html)
