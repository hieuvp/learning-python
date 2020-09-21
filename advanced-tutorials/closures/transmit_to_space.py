def transmit_to_space(message):
    """Enclosing Function"""

    def data_transmitter():
        """Nested Function"""
        print(message)

    return data_transmitter


# Even functions are objects
func = transmit_to_space("Burn the Sun!")
func()
