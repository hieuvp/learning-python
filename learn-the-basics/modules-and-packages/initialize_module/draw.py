# Source: initialize_module/draw.py


def draw_game(name):
    # when clearing the screen
    # we can use the main screen object initialized in this module
    clear_screen(name)


def clear_screen(game):
    print('clear_screen("%s")' % game)


class Screen:
    x = 0
    y = 0

    # Default constructor
    def __init__(self):
        print("Screen __init__")
        self.geek = "GeekforGeeks"


# Initialize main_screen as a singleton
main_screen = Screen()
