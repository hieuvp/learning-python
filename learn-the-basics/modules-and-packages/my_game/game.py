# Source: my_game/game.py

# import the draw module
import draw


def play_game():
    return "play_game"


def main():
    result = play_game()
    draw.draw_game(result)


# This means that if this script is executed,
# then "main()" will be executed
if __name__ == "__main__":
    main()
