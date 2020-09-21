from types import GeneratorType


# A generator function which returns the Fibonacci series
def fibonacci():
    # The first two numbers of the series is always equal to 1
    a = b = 1

    while True:
        yield a

        # Each consecutive number returned is the sum of the last two numbers
        # Simultaneously assign the values of "a" and "b"
        a, b = b, a + b


# Testing Code
if isinstance(fibonacci(), GeneratorType):
    print("Good! The fibonacci() function is a generator")

    counter = 0
    for number in fibonacci():

        # To not add a newline to the end of the string
        # https://docs.python.org/library/functions.html#print
        print("%d " % number, end="")

        counter += 1
        if counter == 10:
            break

    print()
