import random


# A "generator function" which returns "7" random integers
def lottery():

    for i in range(6):
        # Returning "6" numbers between 1 and 40
        yield random.randint(1, 40)

    # Returning a "7th" number between 1 and 15
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % random_number)
