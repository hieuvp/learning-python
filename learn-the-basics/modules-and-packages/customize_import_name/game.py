# Source: customize_import_name/game.py

VISUAL_MODE = True

# Import the draw module
if VISUAL_MODE:
    # In the visual mode, we draw using graphics
    import draw_visual as draw
else:
    # In the textual mode, we print out text
    import draw_textual as draw


def play_game():
    return "winner"


def main():
    result = play_game()
    # This can either be visual or textual depending on VISUAL_MODE
    draw.draw_game(result)


if __name__ == "__main__":
    main()
