# Modules and Packages

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Writing **Modules**](#writing-modules)
- [Importing Module Objects To The Current Namespace](#importing-module-objects-to-the-current-namespace)
- [Importing All Objects From A Module](#importing-all-objects-from-a-module)
- [Customizing Import Name](#customizing-import-name)
- [Module Initialization](#module-initialization)
- [Extending Module Load Path](#extending-module-load-path)
- [Exploring Built-in Modules](#exploring-built-in-modules)
- [Writing **Packages**](#writing-packages)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Writing **Modules**

1. Modules in Python are simply Python files with a `.py` extension.
1. The name of the module will be the name of the file.
1. A Python module can have a set of functions, classes or variables defined and implemented.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=ping_pong/game.py) -->
<!-- The below code snippet is automatically added from ping_pong/game.py -->

```py
# Source: ping_pong/game.py
# This "game" module is responsible for the game logic


# Modules are imported from other modules using the "import" command.
# In this example, this "game" module imports the "draw" module
# which enables it to use functions implemented in that module.
import draw


# When the "import draw" directive run,
# the Python interpreter will look for a file in the directory
# which the script was executed from,
# by the name of the module with a ".py" suffix,
# so in our case it will try to look for "draw.py".
# If it will find one, it will import it.
# If not, it will continue to look for built-in modules.


def play_game():
    return "ping pong"


def main():
    # The main function would use the local function "play_game" to run the game,
    # and then draw the result of the game
    # using a function implemented in the draw module called "draw_game".
    # To use the function "draw_game" from the "draw" module,
    # we would need to specify in which module the function is implemented,
    # using the dot operator.
    # To reference the "draw_game" function from the "game" module,
    # we would need to import the "draw" module and only then call "draw.draw_game()".
    name = play_game()

    # Using the function "draw_game"
    # from the file "draw.py", or in other words, the "draw" module,
    # that implements the logic for drawing the game on the screen.
    draw.draw_game(name)

    draw.clear_screen(name)


# Special "__name__" variable
# https://github.com/hieuvp/learning-python/blob/master/name-variable/README.md
if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=ping_pong/draw.py) -->
<!-- The below code snippet is automatically added from ping_pong/draw.py -->

```py
# Source: ping_pong/draw.py
# This "draw" module is responsible for drawing the game on the screen


def draw_game(name):
    print('draw_game("%s")' % name)


def clear_screen(game):
    print('clear_screen("%s")' % game)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=ping_pong.console) -->
<!-- The below code snippet is automatically added from ping_pong.console -->

```console
+ tree -a ping_pong
ping_pong
├── __pycache__
│   └── draw.cpython-38.pyc
├── draw.py
└── game.py

1 directory, 3 files
+ set +x

+ python ping_pong/game.py
draw_game("ping pong")
clear_screen("ping pong")
```

<!-- AUTO-GENERATED-CONTENT:END -->

You may have noticed that when importing a module,
a `.pyc` file appears, which is a compiled Python file.
Python compiles files into Python bytecode
so that it won't have to parse the files each time modules are loaded.
If a `.pyc` file exists, it gets loaded instead of the `.py` file,
but this process is transparent to the user.

## Importing Module Objects To The Current Namespace

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=import_module_objects/game.py) -->
<!-- The below code snippet is automatically added from import_module_objects/game.py -->

```py
# Source: import_module_objects/game.py

# Using the "from" command
# to import the function "draw_game" directly into the main script's namespace
from draw import draw_game


def main():
    # "draw_game" does not precede with the name of the module it is imported from,
    # because we've specified the "module name" in the "import" command
    draw_game("ping pong")


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=import_module_objects.console) -->
<!-- The below code snippet is automatically added from import_module_objects.console -->

```console
+ python import_module_objects/game.py
draw_game("ping pong")
```

<!-- AUTO-GENERATED-CONTENT:END -->

The advantages of using this notation is that
it is easier to use the functions inside the current module
because you don't need to specify which module the function comes from.
However, any namespace cannot have two objects with the exact same name,
so the import command may replace an existing object in the namespace.

## Importing All Objects From A Module

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=import_all_module_objects/game.py) -->
<!-- The below code snippet is automatically added from import_all_module_objects/game.py -->

```py
# Source: import_all_module_objects/game.py

# Using the "import *" command
# to import all objects from a specific module
from draw import *


def main():
    draw_game("ping pong")


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=import_all_module_objects.console) -->
<!-- The below code snippet is automatically added from import_all_module_objects.console -->

```console
+ python import_all_module_objects/game.py
draw_game("ping pong")
```

<!-- AUTO-GENERATED-CONTENT:END -->

This might be a bit risky as changes in the module might affect the module which imports it,
but it is shorter and also does not require you to specify
which objects you wish to import from the module.

## Customizing Import Name

> We are able to load modules under any name we want.

<br />

For example, if we have two `draw` modules with slightly different names.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=customize_import_name/draw_textual.py) -->
<!-- The below code snippet is automatically added from customize_import_name/draw_textual.py -->

```py
# Source: customize_import_name/draw_textual.py


def draw_game(name):
    print('draw_game("%s") in textual mode' % name)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=customize_import_name/draw_visual.py) -->
<!-- The below code snippet is automatically added from customize_import_name/draw_visual.py -->

```py
# Source: customize_import_name/draw_visual.py


def draw_game(name):
    print('draw_game("%s") in visual mode' % name)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

We can import these modules conditionally
to use the same name in the rest of the code.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=customize_import_name/game.py) -->
<!-- The below code snippet is automatically added from customize_import_name/game.py -->

```py
# Source: customize_import_name/game.py

VISUAL_MODE = True

# Importing the "draw" module
if VISUAL_MODE:
    import draw_visual as draw  # In the visual mode, we draw using graphics
else:
    import draw_textual as draw  # In the textual mode, we print out text


def play_game():
    return "ping pong"


def main():
    name = play_game()

    # This can either be "visual" or "textual" depending on "VISUAL_MODE"
    draw.draw_game(name)


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=customize_import_name.console) -->
<!-- The below code snippet is automatically added from customize_import_name.console -->

```console
+ python customize_import_name/game.py
draw_game("ping pong") in visual mode
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Module Initialization

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=initialize_module/game.py) -->
<!-- The below code snippet is automatically added from initialize_module/game.py -->

```py
# Source: initialize_module/game.py

import draw

# The first time a module is loaded into a running Python script,
# it is initialized by executing the code in the module "once".
#
# If another module in the code imports the same module again,
# it will not be loaded twice but "once only".
#
# So local variables inside the module act as a "Singleton",
# they are initialized "only once".


def main():
    draw.draw_game("ping pong")


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=initialize_module/draw.py) -->
<!-- The below code snippet is automatically added from initialize_module/draw.py -->

```py
# Source: initialize_module/draw.py


def draw_game(name):
    print('draw_game("%s")' % name)
    clear_screen(name)


def clear_screen(game):
    # When clearing the screen,
    # we can use the "main_screen" object initialized in this module
    print(
        'clear_screen("%s") with main_screen.x = %d and main_screen.y = %d'
        % (game, main_screen.x, main_screen.y)
    )


class Screen:
    x = 0
    y = 0

    # The "__init__()" method is called the Constructor
    def __init__(self):
        print('Initializing a Screen object in the "draw" module...\n')
        self.x = 100
        self.y = 200


# Initialize "main_screen" object as a Singleton
main_screen = Screen()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=initialize_module.console) -->
<!-- The below code snippet is automatically added from initialize_module.console -->

```console
+ python initialize_module/game.py
Initializing a Screen object in the "draw" module...

draw_game("ping pong")
clear_screen("ping pong") with main_screen.x = 100 and main_screen.y = 200
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Extending Module Load Path

> There are a couple of ways we could tell the Python interpreter where to look for modules,
> aside from the default, which is the local directory and the built-in modules.

- You could either use the environment variable
  [`PYTHONPATH`](https://docs.python.org/3/using/cmdline.html#envvar-PYTHONPATH)
  to specify additional directories to look for modules in
  (augment the default search path for module files).

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=extend_module_search_path.sh) -->
<!-- The below code snippet is automatically added from extend_module_search_path.sh -->

```sh
#!/usr/bin/env bash

set -eoux pipefail

python extend_module_search_path.py

set +x
echo
set -x

# Enabling the Python script to load modules
# from ".." (meaning: "/learning-python/learn-the-basics") directory
PYTHONPATH=".." python extend_module_search_path.py
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=extend_module_search_path.py) -->
<!-- The below code snippet is automatically added from extend_module_search_path.py -->

```py
import sys
from pprint import pprint

# sys.path
# https://docs.python.org/3/library/sys.html#sys.path
# Return a list of strings that specifies the search path for modules.
# Initialized from the environment variable "PYTHONPATH",
# plus an installation-dependent default.
pprint(sys.path)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=extend_module_search_path.console) -->
<!-- The below code snippet is automatically added from extend_module_search_path.console -->

```console
+ python extend_module_search_path.py
['/Users/hieu.van/Desktop/Workspace/Experiment/learning-python/learn-the-basics/modules-and-packages',
 '/usr/local/opt/python@3.8/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
 '/usr/local/opt/python@3.8/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
 '/usr/local/opt/python@3.8/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
 '/Users/hieu.van/Desktop/Workspace/Experiment/learning-python/venv/lib/python3.8/site-packages']
+ set +x

+ PYTHONPATH=..
+ python extend_module_search_path.py
['/Users/hieu.van/Desktop/Workspace/Experiment/learning-python/learn-the-basics/modules-and-packages',
 '/Users/hieu.van/Desktop/Workspace/Experiment/learning-python/learn-the-basics',
 '/usr/local/opt/python@3.8/Frameworks/Python.framework/Versions/3.8/lib/python38.zip',
 '/usr/local/opt/python@3.8/Frameworks/Python.framework/Versions/3.8/lib/python3.8',
 '/usr/local/opt/python@3.8/Frameworks/Python.framework/Versions/3.8/lib/python3.8/lib-dynload',
 '/Users/hieu.van/Desktop/Workspace/Experiment/learning-python/venv/lib/python3.8/site-packages']
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

- Another method is the `sys.path.append` function.
  You may execute it before running an `import` command:

```python
# This will add the "foo" directory
# to the list of paths to look for modules in as well
sys.path.append("/foo")
```

## Exploring Built-in Modules

Check out the full list of built-in modules in [The Python Standard Library](https://docs.python.org/3/library/index.html).

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=explore_built_in_urllib.py) -->
<!-- The below code snippet is automatically added from explore_built_in_urllib.py -->

```py
# urllib.request - Extensible library for opening URLs
# https://docs.python.org/3/library/urllib.request.html

# Importing the "urllib.request" module
import urllib.request


# Usage:
# urllib.request.urlopen("https://www.shopback.com")

# Two very important functions come in handy when exploring modules in Python
# The "dir" and "help" functions
print("\n+ print(dir(urllib.request))")
print(dir(urllib.request))

print("\n+ help(urllib.request.urlopen)")
help(urllib.request.urlopen)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=explore_built_in_urllib.console) -->
<!-- The below code snippet is automatically added from explore_built_in_urllib.console -->

```console
+ python explore_built_in_urllib.py

+ print(dir(urllib.request))
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_get_proxies', '_get_proxy_settings', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_splitattr', '_splithost', '_splitpasswd', '_splitport', '_splitquery', '_splittag', '_splittype', '_splituser', '_splitvalue', '_thishost', '_to_bytes', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_macosx_sysconf', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote', 're', 'request_host', 'socket', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']

+ help(urllib.request.urlopen)
Help on function urlopen in module urllib.request:

urlopen(url, data=None, timeout=<object object at 0x109c6ff30>, *, cafile=None, capath=None, cadefault=False, context=None)
    Open the URL url, which can be either a string or a Request object.

    ...
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

We can look for which functions are implemented in each module by using the `dir` function:

```shell script
$ python
Python 3.8.3 (default, Jul  8 2020, 14:27:55)
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import urllib.request
>>> dir(urllib.request)
['AbstractBasicAuthHandler', 'AbstractDigestAuthHandler', 'AbstractHTTPHandler', 'BaseHandler', 'CacheFTPHandler', 'ContentTooShortError', 'DataHandler', 'FTPHandler', 'FancyURLopener', 'FileHandler', 'HTTPBasicAuthHandler', 'HTTPCookieProcessor', 'HTTPDefaultErrorHandler', 'HTTPDigestAuthHandler', 'HTTPError', 'HTTPErrorProcessor', 'HTTPHandler', 'HTTPPasswordMgr', 'HTTPPasswordMgrWithDefaultRealm', 'HTTPPasswordMgrWithPriorAuth', 'HTTPRedirectHandler', 'HTTPSHandler', 'MAXFTPCACHE', 'OpenerDirector', 'ProxyBasicAuthHandler', 'ProxyDigestAuthHandler', 'ProxyHandler', 'Request', 'URLError', 'URLopener', 'UnknownHandler', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '__version__', '_cut_port_re', '_ftperrors', '_get_proxies', '_get_proxy_settings', '_have_ssl', '_localhost', '_noheaders', '_opener', '_parse_proxy', '_proxy_bypass_macosx_sysconf', '_randombytes', '_safe_gethostbyname', '_splitattr', '_splithost', '_splitpasswd', '_splitport', '_splitquery', '_splittag', '_splittype', '_splituser', '_splitvalue', '_thishost', '_to_bytes', '_url_tempfiles', 'addclosehook', 'addinfourl', 'base64', 'bisect', 'build_opener', 'contextlib', 'email', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 'getproxies_environment', 'getproxies_macosx_sysconf', 'hashlib', 'http', 'install_opener', 'io', 'localhost', 'noheaders', 'os', 'parse_http_list', 'parse_keqv_list', 'pathname2url', 'posixpath', 'proxy_bypass', 'proxy_bypass_environment', 'proxy_bypass_macosx_sysconf', 'quote', 're', 'request_host', 'socket', 'ssl', 'string', 'sys', 'tempfile', 'thishost', 'time', 'unquote', 'unquote_to_bytes', 'unwrap', 'url2pathname', 'urlcleanup', 'urljoin', 'urlopen', 'urlparse', 'urlretrieve', 'urlsplit', 'urlunparse', 'warnings']
```

When we find the function in the module we want to use,
we can read about it more using the `help` function,
inside the Python interpreter:

```shell script
$ python
Python 3.8.3 (default, Jul  8 2020, 14:27:55)
[Clang 11.0.3 (clang-1103.0.32.62)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import urllib.request
>>> help(urllib.request.urlopen)

>>>
```

## Writing **Packages**

> Packages are namespaces which contain multiple packages and modules themselves.
> <br />They are simply directories, but with a twist.

- A Python package is simply an organized collection of python modules.
- A python module is simply a single python file.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=write_package/pkg/__init__.py) -->
<!-- The below code snippet is automatically added from write_package/pkg/__init__.py -->

```py
# Source: write_package/pkg/__init__.py

# Each package in Python is a directory
# which MUST contain a special file called "__init__.py"
#
# This file can be empty, and it indicates
# that the directory it contains is a "Python package",
# so it can be imported the same way a module can be imported

from .game import play_game
from .draw import draw_game

# Note that the "." before the module name is necessary as of Python 3
# since it is more strict regarding relative imports
# https://stackoverflow.com/questions/12172791/changes-in-import-statement-python3

__all__ = ["play_game", "draw_game"]

# This "__init__.py" file can also decide
# which "modules" "the package" exports as the API, while keeping other modules internal,
# by overriding the "__all__" variable
# https://riptutorial.com/python/example/2894/the---all---special-variable
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=write_package/pkg/draw.py) -->
<!-- The below code snippet is automatically added from write_package/pkg/draw.py -->

```py
# Source: write_package/pkg/draw.py


def draw_game(name):
    print('draw_game("%s")' % name)


def clear_screen(game):
    print('clear_screen("%s")' % game)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=write_package/pkg/game.py) -->
<!-- The below code snippet is automatically added from write_package/pkg/game.py -->

```py
# Source: write_package/pkg/game.py


def play_game():
    return "ping pong"
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=write_package/ping_pong.py) -->
<!-- The below code snippet is automatically added from write_package/ping_pong.py -->

```py
# Source: write_package/ping_pong.py

import pkg


def main():
    name = pkg.play_game()
    pkg.draw_game(name)


if __name__ == "__main__":
    main()
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=write_package.console) -->
<!-- The below code snippet is automatically added from write_package.console -->

```console
+ tree -a -I __pycache__ write_package
write_package
├── ping_pong.py
└── pkg
    ├── __init__.py
    ├── draw.py
    └── game.py

1 directory, 4 files
+ set +x

+ python write_package/ping_pong.py
draw_game("ping pong")
```

<!-- AUTO-GENERATED-CONTENT:END -->

<br />

If we create a directory called `foo`, which marks the package name,
we can then create a module inside that package called `bar`.
We also must not forget to add the `__init__.py` file inside the foo directory.

To use the module `bar`, we can import it in two ways:

```python
import foo.bar

# Or

from foo import bar
```

In the first method, we must use the foo prefix whenever we access the module bar.
In the second method, we don't, because we import the module to our module's namespace.

## Exercise

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
# Print an alphabetically sorted list of all functions in the "re" module

import re
from inspect import getmembers, isfunction

# https://docs.python.org/3/library/inspect.html#inspect.getmembers
# inspect.getmembers(object[, predicate])
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
