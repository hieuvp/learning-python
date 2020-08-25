# Source: scenario-2/importing_script.py

from os import path
import stand_alone_script as sas


def main():
    print('In "%s", the value of "__name__" is "%s".' % (path.basename(__file__), __name__))
    sas.function()


if __name__ == "__main__":
    main()
