import random


# A generator function which returns 7 random integers
def lottery():
    # Return 6 numbers between 1 and 40
    for i in range(6):
        print("i = %s" % i)
        yield random.randint(1, 40)

    # Return a 7th number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % random_number)
