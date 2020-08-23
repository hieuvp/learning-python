# Source: write_package/ping_pong.py

import pkg


def main():
    name = pkg.play_game()
    pkg.draw_game(name)


if __name__ == "__main__":
    main()
