# Source: ping_pong/game.py
# This module is responsible for the game logic

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
