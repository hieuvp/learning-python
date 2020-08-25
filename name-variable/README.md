# `__name__` - A Special Variable

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Introduction](#introduction)
- [Scenario 1 - Standalone Script](#scenario-1---standalone-script)
- [Scenario 2 - Importing Script](#scenario-2---importing-script)
- [Conclusion](#conclusion)
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

## Scenario 1 - Standalone Script

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

## Scenario 2 - Importing Script

> When you import one Python script into another,
> there seem to be two different scopes
> which can be considered as the **main function**.

1. The `__name__` variable of the currently running program.
1. The `__name__` variable of the imported script used in the current program.

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

We then have two scopes: one of `importing_script` and the second scope of `standalone_script`.
In the illustration,
you'll see how it differs from the first use case.

In `importing_script.py` the `__name__` variable is set to `__main__`.
By importing `standalone_script`,
Python starts looking for a file by adding `.py` to the module name.
It then runs the code contained in the imported file.

But this time it is set to `standalone_script`.
Again the `def` statements for `main` and `function` are run.
But, now the condition evaluates to false and main is not called.

In `importing_script` we call `function` which outputs `standalone_script`.
`standalone_script` is known to `function` when that function was defined.

If you would print `__name__` in the `importing_script`,
this would output `__main__`.
The reason for this is that Python uses the value known in the scope of `importing_script`.

## Conclusion

Thanks to this special variable,
you can decide whether you want to run the script.
Or that you want to import the functions defined in the script.

In this short article,
I explained how you can use the `__name__` variable to write Python modules.
You can also run these modules on their own.
This can be done by making use of how the values of these variables change
depending on where they occur.

The usefulness of this approach is when the code `if __name__ == "__main__":` is used,
the python interpreter checks if it's parsing the currently executed script,
or if it's temporarily parsing another external script.
This way the programmer has the ability to control the behaviors of different parts of the program
by choosing to run lines of code from the external script
as well as the currently executed script depending on the scenarios.

## References

- [What's in a (Python's) `__name__`?](https://www.freecodecamp.org/news/whats-in-a-python-s-name-506262fe61e8)
- [`__name__` (A Special variable) in Python](https://www.tutorialspoint.com/name-a-special-variable-in-python)
