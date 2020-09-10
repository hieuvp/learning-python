def print_msg(number):
    def printer():
        """Here we are using the nonlocal keyword"""
        nonlocal number
        number = 3
        print("Inside printer(),   number = %s" % number)

    printer()
    print("Inside print_msg(), number = %s" % number)


print_msg(9)
