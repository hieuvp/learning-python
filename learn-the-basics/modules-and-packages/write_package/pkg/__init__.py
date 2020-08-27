# Source: write_package/pkg/__init__.py

# Each package in Python is a directory
# which MUST contain a special file called "__init__.py"
#
# This file can be empty, and it indicates
# that the directory it contains is a "Python package",
# so it can be imported the same way a "Python module" can be imported

from .game import play_game
from .draw import draw_game

# The "." before the module name is necessary as of (Vietnamese: kể từ) Python 3
# since it is more strict regarding relative imports
# https://stackoverflow.com/questions/12172791/changes-in-import-statement-python3

__all__ = ["play_game", "draw_game"]

# This "__init__.py" file can also decide
# which "modules" the "package" exports as the API, while keeping other "modules" internal,
# by overwriting the "__all__" variable
# https://riptutorial.com/python/example/2894/the---all---special-variable
