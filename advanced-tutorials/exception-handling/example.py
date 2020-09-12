def do_stuff_with_number(n):
    print(n)


def catch_this():
    the_list = (1, 2, 3, 4, 5)

    # We need to iterate over "10" numbers,
    # but "the_list" is made from user input, and might not have "10" numbers in it
    for i in range(10):
        try:
            do_stuff_with_number(the_list[i])

        # Raised when accessing a non-existing index of a list
        except IndexError:
            # After reaching the end of "the_list",
            # we just want the rest of the numbers to be interpreted as a "0"
            do_stuff_with_number(0)


catch_this()
