# Source: initialize_module/game.py

import draw

# The first time a module is loaded into a running Python script,
# it is initialized by executing the code in the module "once".
#
# If another module in the code imports the same module again,
# it will not be loaded twice but "once only".
#
# So local variables inside the module act as a "Singleton",
# they are initialized only once.


def main():
    draw.draw_game("ping pong")


if __name__ == "__main__":
    main()
