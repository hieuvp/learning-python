def transmit_to_space(message):
    """This is an Enclosing Function"""

    def data_transmitter():
        """This is a Nested Function"""
        """A Function defined inside another Function"""

        print(message)

    data_transmitter()


transmit_to_space("Test Message")
