# Source: write_package/pkg/__init__.py

# Each package in Python is a directory
# which MUST contain a special file called "__init__.py"
#
# This file can be empty, and it indicates
# that the directory it contains is a "Python package",
# so it can be imported the same way a module can be imported

from .game import play_game
from .draw import draw_game

# This "__init__.py" file can also decide
# which "modules" "the package" exports as the API, while keeping other modules internal,
# by overriding the "__all__" variable

__all__ = ["play_game", "draw_game"]
