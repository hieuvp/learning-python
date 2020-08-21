# Source: scenario-1/name_script.py


def my_function():
    print('The value of "__name__" is "%s"' % __name__)


def main():
    my_function()


if __name__ == "__main__":
    main()
