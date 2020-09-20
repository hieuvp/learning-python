def print_msg_without_nonlocal(number):
    print('Without "nonlocal" keyword')

    def printer():
        number = 3
        print("- Inside  printer() : number = %s" % number)

    printer()

    print("- Outside printer() : number = %s" % number)


def print_msg_with_nonlocal(number):
    print('With "nonlocal" keyword')

    def printer():
        nonlocal number
        number = 3
        print("- Inside  printer() : number = %s" % number)

    printer()

    print("- Outside printer() : number = %s" % number)


print_msg_without_nonlocal(9)
print()
print_msg_with_nonlocal(9)
