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
    print("Good! The fib() function is a generator.\n")

    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == 10:
            break
