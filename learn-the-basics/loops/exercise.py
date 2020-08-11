NUMBERS = [
    399, 162, 758, 219, 918,
    237, 412, 566, 826, 248,
    866, 950, 626
]

for number in NUMBERS:
    # Print out all even numbers
    if number % 2 == 0:
        print(number)

    # Do not print any numbers that come after "237"
    if number == 237:
        break
