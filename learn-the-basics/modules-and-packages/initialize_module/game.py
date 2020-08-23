# Source: initialize_module/game.py

# import the draw module
import draw


def play_game():
    return "ping pong"


def main():
    name = play_game()
    draw.draw_game(name)


# This means that if this script is executed,
# then "main()" will be executed
if __name__ == "__main__":
    main()
