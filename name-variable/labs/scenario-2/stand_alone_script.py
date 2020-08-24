# Source: scenario-1/stand_alone_script.py

from os import path


def my_function():
    print('In "%s", the value of "__name__" is "%s".' % (path.basename(__file__), __name__))


def main():
    my_function()


if __name__ == "__main__":
    main()
