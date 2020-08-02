# Change these variables, so that each if statement resolves as "True"
NUMBER = 10               # Original NUMBER = 10
SECOND_NUMBER = 10        # Original SECOND_NUMBER = 10
FIRST_ARRAY = []          # Original FIRST_ARRAY = []
SECOND_ARRAY = [1, 2, 3]  # Original SECOND_ARRAY = [1, 2, 3]

if NUMBER > 15:
    print("1")

if FIRST_ARRAY:
    print("2")

if len(SECOND_ARRAY) == 2:
    print("3")

if len(FIRST_ARRAY) + len(SECOND_ARRAY) == 5:
    print("4")

if FIRST_ARRAY and FIRST_ARRAY[0] == 1:
    print("5")

if not SECOND_NUMBER:
    print("6")
