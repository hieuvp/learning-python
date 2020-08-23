# Source: initialize_module/draw.py


def draw_game(name):
    print('draw_game("%s")' % name)
    clear_screen(name)


def clear_screen(game):
    print('clear_screen("%s")' % game)

    # When clearing the screen,
    # we can use the "main_screen" object initialized in this module
    print("main_screen.x = %s" % main_screen.x)
    print("main_screen.y = %s" % main_screen.y)


class Screen:
    x = 0
    y = 0

    # The "__init__()" method is called the "constructor"
    def __init__(self):
        print("Instantiating a Screen object...")
        self.x = 100
        self.y = 200


# Initialize "main_screen" as a singleton
main_screen = Screen()
