def print_msg_without_nonlocal(number):
    def printer():
        number = 3
        print('Without "nonlocal" keyword, inside printer(),   number = %s' % number)

    printer()
    print('Without "nonlocal" keyword, inside print_msg(), number = %s' % number)


def print_msg_with_nonlocal(number):
    def printer():
        """Here we are using the nonlocal keyword"""
        nonlocal number
        number = 3
        print('With "nonlocal" keyword, inside printer(),   number = %s' % number)

    printer()
    print('With "nonlocal" keyword, inside print_msg(), number = %s' % number)


print_msg_without_nonlocal(9)
print()
print_msg_with_nonlocal(9)
