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
