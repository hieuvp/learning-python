# Source: ping_pong/game.py
# This module is responsible for the game logic


# It will use the function `draw_game` from the file `draw.py`,
# or in other words, the `draw` module,
# that implements the logic for drawing the game on the screen.
#
# Modules are imported from other modules using the `import` command.
# In this example, the `game.py` script may look something like this:
#
# In this example, the game module imports the draw module,
# which enables it to use functions implemented in that module.
# The main function would use the local function `play_game` to run the game,
# and then draw the result of the game
# using a function implemented in the draw module called `draw_game`.
# To use the function `draw_game` from the `draw` module,
# we would need to specify in which module the function is implemented,
# using the dot operator.
# To reference the `draw_game` function from the `game` module,
# we would need to import the draw module and only then call `draw.draw_game()`.
#
# When the import `draw` directive will run,
# the Python interpreter will look for a file in the directory
# which the script was executed from,
# by the name of the module with a `.py` prefix,
# so in our case it will try to look for `draw.py`.
# If it will find one, it will import it.
# If not, he will continue to look for built-in modules.

# Importing the "draw" module
import draw


def play_game():
    return "ping pong"


def main():
    name = play_game()
    draw.draw_game(name)
    draw.clear_screen(name)


# Special "__name__" variable
# https://github.com/hieuvp/learning-python/blob/master/name-variable/README.md
if __name__ == "__main__":
    main()
