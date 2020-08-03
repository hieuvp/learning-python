count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        # "break" is used to exit a loop
        break

print()

for x in range(10):
    if x % 2 == 0:
        # "continue" returns the control to the beginning of a loop
        continue

    # Print out only odd numbers
    print(x)
