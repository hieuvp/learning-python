# Source: scenario-1/stand_alone_script.py

from os import path


def function():
    print('In "%s", the value of "__name__" is "%s".' % (path.basename(__file__), __name__))


def main():
    function()


if __name__ == "__main__":
    main()
