# Source: import_module_objects/game.py

# import the draw module
from draw import draw_game


def play_game():
    return "ping pong"


def main():
    name = play_game()
    draw_game(name)


if __name__ == "__main__":
    main()
