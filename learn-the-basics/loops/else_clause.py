count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % count)

print()

for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print("This is not printed")
