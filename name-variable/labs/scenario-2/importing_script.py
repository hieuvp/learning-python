# Source: scenario-2/importing_script.py

from os import path

import standalone_script as ss


def main():
    print('In "%s", the value of "__name__" is "%s".' % (path.basename(__file__), __name__))
    ss.function()


if __name__ == "__main__":
    main()
