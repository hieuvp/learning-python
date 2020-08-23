# Source: initialize_module/draw.py


def draw_game(name):
    print('draw_game("%s")' % name)
    clear_screen(name)


def clear_screen(game):
    # When clearing the screen,
    # we can use the "main_screen" object initialized in this module
    print(
        'clear_screen("%s") with main_screen.x = %d and main_screen.y = %d'
        % (game, main_screen.x, main_screen.y)
    )


class Screen:
    x = 0
    y = 0

    # The "__init__()" method is called the Constructor
    def __init__(self):
        print('Instantiating a Screen object in the "draw" module...\n')
        self.x = 100
        self.y = 200


# Initialize "main_screen" as a Singleton
main_screen = Screen()
