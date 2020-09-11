def transmit_to_space(message):
    """This is the enclosing function"""

    def data_transmitter():
        """This is the nested function"""
        """It is a function defined inside another function"""

        print(message)
        """The nested functions can access the variables of the enclosing scope"""
        """They are readonly"""
        """However, one can use the `nonlocal` keyword explicitly with these variables in order to modify them"""

    data_transmitter()


print(transmit_to_space("Test message"))
