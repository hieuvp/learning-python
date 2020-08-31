from types import GeneratorType


# Write a generator function which returns the Fibonacci series
def fib():
    # The first two numbers of the series is always equal to 1
    a = b = 1

    while True:
        yield a

        # Each consecutive number returned is the sum of the last two numbers
        a, b = b, a + b


# Testing code
if isinstance(fib(), GeneratorType):
    print("Good! The fib() function is a generator")

    counter = 0
    for n in fib():

        # To not add a newline to the end of the string
        # https://docs.python.org/library/functions.html#print
        print("%d, " % n, end="")

        counter += 1
        if counter == 10:
            break

    print()
