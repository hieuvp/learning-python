# Source: ping_pong/game.py
# This "game" module is responsible for the game logic


# Modules are imported from other modules using the "import" command.
# In this example, this "game" module imports the "draw" module
# which enables it to use functions implemented in that "draw" module.
import draw


# When the "import draw" directive run,
# the Python interpreter will look for a file
# in the directory which the script was executed from,
# by the name of the module with a ".py" suffix
# (in this case it will try to look for "draw.py").
#
# - If found one, it will import it
# - If not, it will continue to look for "built-in modules"


def play_game():
    return "ping pong"


def main():
    name = play_game()

    # Using the function "draw_game" from the file "draw.py",
    # or in other words, the "draw" module,
    # that implements the logic for drawing the game on the screen
    draw.draw_game(name)

    draw.clear_screen(name)


# Special "__name__" variable
# https://github.com/hieuvp/learning-python/blob/master/name-variable/README.md
if __name__ == "__main__":
    main()
