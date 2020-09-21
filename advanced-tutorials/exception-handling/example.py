def do_stuff_with_number(number):
    print("number = %s" % number)


def catch_this():
    # This list only has "3" numbers in it
    numbers = (11, 22, 33)

    # Iterate over "5" numbers
    for index in range(5):
        try:
            number = numbers[index]
            do_stuff_with_number(number)

        # Raised when accessing a non-existing index of a list
        except IndexError:
            # After reaching the end of "numbers",
            # we just want the rest to be interpreted as a "0"
            number = 0
            do_stuff_with_number(number)


catch_this()
