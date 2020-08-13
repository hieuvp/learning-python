# draw.py


def draw_game(result):
    # when clearing the screen
    # we can use the main screen object initialized in this module
    clear_screen(main_screen)


def clear_screen(screen):
    print("clear_screen(screen)")


class Screen:
    x = 0
    y = 0


# initialize main_screen as a singleton
main_screen = Screen()
