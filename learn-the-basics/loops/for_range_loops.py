RESULT = "range(5)       ="
for x in range(5):
    RESULT += " %d" % x
print(RESULT)  # Print out the numbers 0,1,2,3,4

RESULT = "range(3, 6)    ="
for x in range(3, 6):
    RESULT += " %d" % x
print(RESULT)  # Print out 3,4,5

RESULT = "range(3, 8, 2) ="
for x in range(3, 8, 2):
    RESULT += " %d" % x
print(RESULT)  # Print out 3,5,7
