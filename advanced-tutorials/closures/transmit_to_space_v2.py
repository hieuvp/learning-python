def transmit_to_space(message):
    """Enclosing Function"""

    def data_transmitter():
        """Nested Function"""
        print(message)

    return data_transmitter


# Even functions are objects
fun2 = transmit_to_space("Burn the Sun!")
fun2()
