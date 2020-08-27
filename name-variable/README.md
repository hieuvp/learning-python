# `__name__` - A Special Variable

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Introduction](#introduction)
- [Scenario 1: Standalone Script](#scenario-1-standalone-script)
- [Scenario 2: Importing Script](#scenario-2-importing-script)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Introduction

> Unlike other programming languages,
> Python is not designed to start execution of the code from a **main function** explicitly.
> <br />A special variable called `__name__` provides the functionality of the **main function**.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/introduction/example.py) -->
<!-- The below code snippet is automatically added from labs/introduction/example.py -->

```py
def main():
    # "__name__" value depending on
    # how we execute the containing script
    print("__name__       = %s" % __name__)
    print("type(__name__) = %s" % type(__name__))


# When this script is executed, the "main()" will be executed
if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/introduction.console) -->
<!-- The below code snippet is automatically added from labs/introduction.console -->

```console
+ python introduction/example.py
__name__       = __main__
type(__name__) = <type 'str'>
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Scenario 1: Standalone Script

> When you run any well-written standalone Python script
> which is not referring to any other script,
> <br />the value of `__name__` variable is equal to `__main__`.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/scenario-1/standalone_script.py) -->
<!-- The below code snippet is automatically added from labs/scenario-1/standalone_script.py -->

```py
# Source: scenario-1/standalone_script.py

from os import path


def function():
    print('In "%s", the value of "__name__" is "%s".' % (path.basename(__file__), __name__))


def main():
    function()


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/scenario-1.console) -->
<!-- The below code snippet is automatically added from labs/scenario-1.console -->

```console
+ tree -a -I '*.pyc' scenario-1
scenario-1
└── standalone_script.py

0 directories, 1 file
+ set +x

+ python scenario-1/standalone_script.py
In "standalone_script.py", the value of "__name__" is "__main__".
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Scenario 2: Importing Script

> When importing one Python script into another,
> there seem to be two different scopes.

1. `__name__` variable of the currently running program.
1. `__name__` variable of the imported script used in the current program.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/scenario-2/importing_script.py) -->
<!-- The below code snippet is automatically added from labs/scenario-2/importing_script.py -->

```py
# Source: scenario-2/importing_script.py

from os import path
import standalone_script as ss


def main():
    print('In "%s", the value of "__name__" is "%s".' % (path.basename(__file__), __name__))
    ss.function()


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/scenario-2.console) -->
<!-- The below code snippet is automatically added from labs/scenario-2.console -->

```console
+ tree -a -I '*.pyc' scenario-2
scenario-2
├── importing_script.py
└── standalone_script.py

0 directories, 2 files
+ set +x

+ python scenario-2/importing_script.py
In "importing_script.py", the value of "__name__" is "__main__".
In "standalone_script.py", the value of "__name__" is "standalone_script".
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [What's in a (Python's) `__name__`?](https://www.freecodecamp.org/news/whats-in-a-python-s-name-506262fe61e8)
- [`__name__` (A Special variable) in Python](https://www.tutorialspoint.com/name-a-special-variable-in-python)
