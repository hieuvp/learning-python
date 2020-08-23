# Source: customize_import_name/game.py

VISUAL_MODE = True

# Importing the "draw" module
if VISUAL_MODE:
    import draw_visual as draw  # In the visual mode, we draw using graphics
else:
    import draw_textual as draw  # In the textual mode, we print out text


def play_game():
    return "ping pong"


def main():
    name = play_game()
    # This can either be visual or textual
    # depending on "VISUAL_MODE"
    draw.draw_game(name)


if __name__ == "__main__":
    main()
