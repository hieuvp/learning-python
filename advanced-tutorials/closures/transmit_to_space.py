def transmit_to_space(message):
    """This is an Enclosing Function"""

    def data_transmitter():
        """This is a Nested Function"""
        """A Function defined inside another Function"""

        print(message)

        """Nested Functions can access the variables of the enclosing scope"""
        """These variables are readonly"""
        """However, one can use the "nonlocal" keyword explicitly in order to modify them"""

    data_transmitter()


transmit_to_space("Test Message")
