# Source: custom_import_name/game.py

VISUAL_MODE = True

# import the draw module
if VISUAL_MODE:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw


def play_game():
    return "play_game"


def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)


if __name__ == "__main__":
    main()
