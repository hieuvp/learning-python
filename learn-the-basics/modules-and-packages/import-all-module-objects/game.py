# Source: import-all-module-objects/game.py

# import the draw module
from draw import *


def play_game():
    return "play_game"


def main():
    result = play_game()
    draw_game(result)


if __name__ == "__main__":
    main()
