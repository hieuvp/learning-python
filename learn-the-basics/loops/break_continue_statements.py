count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # exit the loop

print()

# Print out only odd numbers
for x in range(10):
    if x % 2 == 0:
        continue  # return the control to beginning of the loop
    print(x)
