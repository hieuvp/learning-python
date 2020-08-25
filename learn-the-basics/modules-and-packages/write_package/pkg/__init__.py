# Source: write_package/pkg/__init__.py

# Each package in Python is a directory
# which MUST contain a special file called "__init__.py"
#
# This file can be empty,
# and it indicates that the directory it contains is a Python package,
# so it can be imported the same way a module can be imported

from .game import play_game
from .draw import draw_game

__all__ = ["play_game", "draw_game"]

# References
# https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
# https://towardsdatascience.com/whats-init-for-me-d70a312da583
# https://yasoob.me/2013/07/28/what-is-__init__-py/
