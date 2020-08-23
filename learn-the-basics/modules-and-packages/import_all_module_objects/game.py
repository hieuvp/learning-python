# Source: import_all_module_objects/game.py

# Using the "import *" command
# to import all objects from a specific module
from draw import *


def play_game():
    return "ping pong"


def main():
    name = play_game()
    draw_game(name)


if __name__ == "__main__":
    main()
