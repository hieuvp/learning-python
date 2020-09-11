def transmit_to_space(message):
    """This is the enclosing function"""

    def data_transmitter():
        """This is the nested function"""
        """It is a function defined inside another function"""

        print(message)
        """Nested functions can access the variables of the enclosing scope"""
        """These variables are readonly"""
        """However, one can use the "nonlocal" keyword explicitly in order to modify them"""

    data_transmitter()


print(transmit_to_space("Test message"))
