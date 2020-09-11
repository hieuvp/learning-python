def transmit_to_space(message):
    """This is the enclosing function"""

    def data_transmitter():
        """The nested function"""
        print(message)

    return data_transmitter


# We call the function as follows:
# Remember that even functions are objects
fun2 = transmit_to_space("Burn the Sun!")
fun2()
