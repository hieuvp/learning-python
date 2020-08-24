# Source: import_module_objects/game.py

# Using the "from" command
# to import the function "draw_game" directly into the main script's namespace
from draw import draw_game


def main():
    draw_game("ping pong")

    # You may have noticed that,
    # "draw_game" does not precede with the name of the module it is imported from,
    # because we've specified the module name in the import command.


if __name__ == "__main__":
    main()
