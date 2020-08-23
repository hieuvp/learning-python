# `__name__` - A Special Variable

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Introduction](#introduction)
- [Scenario 1: Stand-alone Script](#scenario-1-stand-alone-script)
- [Scenario 2: Importing Script](#scenario-2-importing-script)
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
    # "__name__" value depending on how we execute the containing script
    print("__name__       = %s" % __name__)
    print("type(__name__) = %s" % type(__name__))


# This means that if this script is executed,
# then "main()" will be executed
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

## Scenario 1: Stand-alone Script

> When you run any well-written stand-alone python script
> which is not referring to any other script,
> the value of `__name__` variable is equal to `__main__`.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/scenario-1/stand_alone_script.py) -->
<!-- The below code snippet is automatically added from labs/scenario-1/stand_alone_script.py -->

```py
# Source: scenario-1/stand_alone_script.py


def my_function():
    print('The value of "__name__" is "%s"' % __name__)


def main():
    my_function()


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/scenario-1.console) -->
<!-- The below code snippet is automatically added from labs/scenario-1.console -->

```console
+ tree -a -I '*.pyc' scenario-1
scenario-1
└── stand_alone_script.py

0 directories, 1 file
+ set +x

+ python scenario-1/stand_alone_script.py
The value of "__name__" is "__main__"
```

<!-- AUTO-GENERATED-CONTENT:END -->

Before all other code is run,
the `__name__` variable is set to `__main__`.

## Scenario 2: Importing Script

> When you import one python script into another.
> In such a scenario, there seem to be two different scopes
> which can be considered as the `main()` function.
> The first scope can be the `__main__` variable of the currently running program
> and the second the scope of the `__main__` variable of the imported script
> used in the current program.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/scenario-2/importing_script.py) -->
<!-- The below code snippet is automatically added from labs/scenario-2/importing_script.py -->

```py
# Source: scenario-2/importing_script.py

import stand_alone_script as sas


print('The value of "__name__" is "%s"' % __name__)

sas.my_function()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=labs/scenario-2.console) -->
<!-- The below code snippet is automatically added from labs/scenario-2.console -->

```console
+ tree -a -I '*.pyc' scenario-2
scenario-2
├── importing_script.py
└── stand_alone_script.py -> ../scenario-1/stand_alone_script.py

0 directories, 2 files
+ set +x

+ python scenario-2/importing_script.py
The value of "__name__" is "__main__"
The value of "__name__" is "stand_alone_script"
```

<!-- AUTO-GENERATED-CONTENT:END -->

We then have two scopes: one of importingScript and the second scope of nameScript.
In the illustration,
you'll see how it differs from the first use case.

In importingScript.py the `__name__` variable is set to `__main__`.
By importing nameScript, Python starts looking for a file by adding `.py` to the module name.
It then runs the code contained in the imported file.

But this time it is set to nameScript.
Again the def statements for main and myFunction are run.
But, now the condition evaluates to false and main is not called.

In `importingScript.py` we call myFunction which outputs nameScript.
NameScript is known to myFunction when that function was defined.

If you would print `__name__` in the importingScript,
this would output `__main__`.
The reason for this is that Python uses the value known in the scope of importingScript.

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
