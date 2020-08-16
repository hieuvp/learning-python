# Modules and Packages

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Writing Modules](#writing-modules)
- [Importing Module Objects To The Current Namespace](#importing-module-objects-to-the-current-namespace)
- [Importing All Objects From A Module](#importing-all-objects-from-a-module)
- [Custom Import Name](#custom-import-name)
- [Module Initialization](#module-initialization)
- [Extending Module Load Path](#extending-module-load-path)
- [Exploring Built-in Modules](#exploring-built-in-modules)
- [Writing Packages](#writing-packages)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

When building a ping pong game,
one module would be responsible for the game logic,
and another module would be responsible for drawing the game on the screen.

## Writing Modules

Modules in Python are simply Python files with a `.py` extension.
The name of the module will be the name of the file.
A Python module can have a set of functions, classes or variables defined and implemented.
In the example above, we will have two files, we will have:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=ping_pong.console) -->
<!-- The below code snippet is automatically added from ping_pong.console -->

```console
+ tree -a -I __pycache__ ping_pong
ping_pong
├── draw.py
└── game.py

0 directories, 2 files
+ set +x

+ python ping_pong/game.py
draw_game("winner")
```

<!-- AUTO-GENERATED-CONTENT:END -->

The Python script `game.py` will implement the game.
It will use the function `draw_game` from the file `draw.py`,
or in other words, the `draw` module,
that implements the logic for drawing the game on the screen.

Modules are imported from other modules using the `import` command.
In this example, the `game.py` script may look something like this:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=ping_pong/game.py) -->
<!-- The below code snippet is automatically added from ping_pong/game.py -->

```py
# Source: my_game/game.py

# import the draw module
import draw


def play_game():
    return "winner"


def main():
    result = play_game()
    draw.draw_game(result)


# This means that if this script is executed,
# then "main()" will be executed
if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

The `draw` module may look something like this:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=ping_pong/draw.py) -->
<!-- The below code snippet is automatically added from ping_pong/draw.py -->

```py
# Source: my_game/draw.py


def draw_game(result):
    print('draw_game("%s")' % result)


def clear_screen(screen):
    print('clear_screen("%s")' % screen)
```

<!-- AUTO-GENERATED-CONTENT:END -->

In this example, the game module imports the draw module,
which enables it to use functions implemented in that module.
The main function would use the local function `play_game` to run the game,
and then draw the result of the game using a function implemented in the draw module called `draw_game`.
To use the function `draw_game` from the `draw` module,
we would need to specify in which module the function is implemented,
using the dot operator.
To reference the `draw_game` function from the `game` module,
we would need to import the draw module and only then call `draw.draw_game()`.

When the import `draw` directive will run,
the Python interpreter will look for a file in the directory which the script was executed from,
by the name of the module with a `.py` prefix,
so in our case it will try to look for `draw.py`.
If it will find one, it will import it.
If not, he will continue to look for built-in modules.

You may have noticed that when importing a module,
a `.pyc` file appears, which is a compiled Python file.
Python compiles files into Python bytecode
so that it won't have to parse the files each time modules are loaded.
If a `.pyc` file exists, it gets loaded instead of the `.py` file,
but this process is transparent to the user.

## Importing Module Objects To The Current Namespace

We may also import the function `draw_game` directly
into the main script's namespace,
by using the from command.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=import_module_objects/game.py) -->
<!-- The below code snippet is automatically added from import_module_objects/game.py -->

```py
# Source: import-module-objects/game.py

# import the draw module
from draw import draw_game


def play_game():
    return "winner"


def main():
    result = play_game()
    draw_game(result)


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=import_module_objects.console) -->
<!-- The below code snippet is automatically added from import_module_objects.console -->

```console
+ python import_module_objects/game.py
draw_game("winner")
```

<!-- AUTO-GENERATED-CONTENT:END -->

You may have noticed that in this example,
`draw_game` does not precede with the name of the module it is imported from,
because we've specified the module name in the import command.

The advantages of using this notation is that
it is easier to use the functions inside the current module
because you don't need to specify which module the function comes from.
However, any namespace cannot have two objects with the exact same name,
so the import command may replace an existing object in the namespace.

## Importing All Objects From A Module

We may also use the `import *` command to import all objects from a specific module,
like this:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=import_all_module_objects/game.py) -->
<!-- The below code snippet is automatically added from import_all_module_objects/game.py -->

```py
# Source: import_all_module_objects/game.py

# import the draw module
from draw import *


def play_game():
    return "winner"


def main():
    result = play_game()
    draw_game(result)


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=import_all_module_objects.console) -->
<!-- The below code snippet is automatically added from import_all_module_objects.console -->

```console
+ python import_all_module_objects/game.py
draw_game("winner")
```

<!-- AUTO-GENERATED-CONTENT:END -->

This might be a bit risky as changes in the module might affect the module which imports it,
but it is shorter and also does not require you to specify
which objects you wish to import from the module.

## Custom Import Name

We may also load modules under any name we want.
This is useful when we want to import a module conditionally
to use the same name in the rest of the code.

For example, if you have two draw modules with slighty different names -
you may do the following:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=customize_import_name/game.py) -->
<!-- The below code snippet is automatically added from customize_import_name/game.py -->

```py
# Source: custom_import_name/game.py

VISUAL_MODE = True

# Import the draw module
if VISUAL_MODE:
    # In the visual mode, we draw using graphics
    import draw_visual as draw
else:
    # In the textual mode, we print out text
    import draw_textual as draw


def play_game():
    return "winner"


def main():
    result = play_game()
    # This can either be visual or textual depending on VISUAL_MODE
    draw.draw_game(result)


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=customize_import_name/draw_textual.py) -->
<!-- The below code snippet is automatically added from customize_import_name/draw_textual.py -->

```py
# Source: custom_import_name/draw.py


def draw_game(result):
    print('draw_game("%s") in textual mode' % result)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=customize_import_name/draw_visual.py) -->
<!-- The below code snippet is automatically added from customize_import_name/draw_visual.py -->

```py
# Source: custom_import_name/draw.py


def draw_game(result):
    print('draw_game("%s") in visual mode' % result)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=customize_import_name.console) -->
<!-- The below code snippet is automatically added from customize_import_name.console -->

```console
+ python customize_import_name/game.py
draw_game("winner") in visual mode
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Module Initialization

The first time a module is loaded into a running Python script,
it is initialized by executing the code in the module once.
If another module in your code imports the same module again,
it will not be loaded twice but once only -
so local variables inside the module act as a "singleton" -
they are initialized only once.

This is useful to know, because this means that
you can rely on this behavior for initializing objects.
For example:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=initialize_module/game.py) -->
<!-- The below code snippet is automatically added from initialize_module/game.py -->

```py
# Source: module-initialization/game.py

# import the draw module
import draw


def play_game():
    return "winner"


def main():
    result = play_game()
    draw.draw_game(result)


# This means that if this script is executed,
# then "main()" will be executed
if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=initialize_module/draw.py) -->
<!-- The below code snippet is automatically added from initialize_module/draw.py -->

```py
# draw.py


def draw_game(result):
    # when clearing the screen
    # we can use the main screen object initialized in this module
    clear_screen(result)


def clear_screen(screen):
    print('clear_screen("%s")' % screen)


class Screen:
    x = 0
    y = 0


# initialize main_screen as a singleton
main_screen = Screen()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=initialize_module.console) -->
<!-- The below code snippet is automatically added from initialize_module.console -->

```console
+ python initialize_module/game.py
clear_screen("winner")
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Extending Module Load Path

There are a couple of ways we could tell the Python interpreter where to look for modules,
aside from the default, which is the local directory and the built-in modules.
You could either use the environment variable `PYTHONPATH`
to specify additional directories to look for modules in,
like this:

```shell script
PYTHONPATH=/foo python game.py
```

This will execute `game.py`,
and will enable the script to load modules from the foo directory as well as the local directory.

Another method is the `sys.path.append` function.
You may execute it before running an import command:

```python
sys.path.append("/foo")
```

This will add the foo directory to the list of paths to look for modules in as well.

## Exploring Built-in Modules

Check out the full list of built-in modules in the Python standard library here.
[The Python Standard Library](https://docs.python.org/3/library/index.html)

Two very important functions come in handy when exploring modules in Python -
the `dir` and `help` functions.

If we want to import the module urllib,
which enables us to create read data from URLs,
we simply import the module:

```python
# import the library
import urllib

# use it
urllib.urlopen(...)
```

We can look for which functions are implemented in each module by using the dir function:

```shell script
$ python
Python 3.8.3 (default, Jul  8 2020, 14:27:55)
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import urllib
>>> dir(urllib)
['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__']
```

When we find the function in the module we want to use,
we can read about it more using the `help` function,
inside the Python interpreter:

```python
help(urllib.urlopen)
```

## Writing Packages

Packages are namespaces which contain multiple packages and modules themselves.
They are simply directories, but with a twist.

Each package in Python is a directory which MUST contain a special file called `__init__.py`.
This file can be empty, and it indicates that the directory it contains is a Python package,
so it can be imported the same way a module can be imported.

If we create a directory called foo, which marks the package name,
we can then create a module inside that package called bar.
We also must not forget to add the `__init__.py` file inside the foo directory.

To use the module bar, we can import it in two ways:

```python
import foo.bar
```

or:

```python
from foo import bar
```

In the first method, we must use the foo prefix whenever we access the module bar.
In the second method, we don't, because we import the module to our module's namespace.

The `__init__.py` file can also decide which modules the package exports as the API,
while keeping other modules internal, by overriding the `__all__` variable, like so:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=write_packages/__init__.py) -->
<!-- The below code snippet is automatically added from write_packages/__init__.py -->

```py
# Source: write_packages/__init__.py

# __all__ = ["bar"]
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Print an alphabetically sorted list of all functions in the "re" module

import re
from inspect import getmembers, isfunction

# inspect.getmembers(object[, predicate])
# https://docs.python.org/3/library/inspect.html#inspect.getmembers
for member in getmembers(re):
    name, value = member
    if isfunction(value):
        print(name)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
_compile
_expand
_pickle
_subx
compile
escape
findall
finditer
fullmatch
match
purge
search
split
sub
subn
template
```

<!-- AUTO-GENERATED-CONTENT:END -->
