import random


# A "generator function" which returns "7" random integers
def lottery():
    # This function decides how to generate the random numbers on its own,
    # executes the "yield" statements one at a time,
    # pausing in between to "yield" execution back to the main "for" loop

    for i in range(6):
        # Returning "6" numbers between "1" and "40"
        yield random.randint(1, 40)

    # Returning a "7th" number between "1" and "15"
    yield random.randint(1, 15)


for random_number in lottery():
    print("And the next number is... %d!" % random_number)
