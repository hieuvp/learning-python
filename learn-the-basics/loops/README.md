# Loops

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [`for`](#for)
- [`while`](#while)
- [`break` and `continue` statements](#break-and-continue-statements)
- [can we use `else` clause for loops](#can-we-use-else-clause-for-loops)
- [Exercise](#exercise)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## `for`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=for_loop.py) -->
<!-- The below code snippet is automatically added from for_loop.py -->

```py
PRIMES = [2, 3, 5, 7]

# "for" loop iterate over a given sequence
for prime in PRIMES:
    print(prime)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=for_loop.console) -->
<!-- The below code snippet is automatically added from for_loop.console -->

```console
+ python for_loop.py
2
3
5
7
```

<!-- AUTO-GENERATED-CONTENT:END -->

For loops can iterate over a sequence of numbers
using the "range" and "xrange" functions.
The difference between range and xrange is that
the range function returns a new list with numbers of that specified range,
whereas xrange returns an iterator, which is more efficient.
(Python 3 uses the range function, which acts like xrange).
Note that the range function is zero-based.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=for_range_loops.py) -->
<!-- The below code snippet is automatically added from for_range_loops.py -->

```py
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
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=for_range_loops.console) -->
<!-- The below code snippet is automatically added from for_range_loops.console -->

```console
+ python for_range_loops.py
range(5)       = 0 1 2 3 4
range(3, 6)    = 3 4 5
range(3, 8, 2) = 3 5 7
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `while`

While loops repeat as long as a certain boolean condition is met.
For example:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=while_loop.py) -->
<!-- The below code snippet is automatically added from while_loop.py -->

```py
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=while_loop.console) -->
<!-- The below code snippet is automatically added from while_loop.console -->

```console
+ python while_loop.py
0
1
2
3
4
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `break` and `continue` statements

break is used to exit a for loop or a while loop,
whereas continue is used to skip the current block,
and return to the "for" or "while" statement.
A few examples:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=break_continue_statements.py) -->
<!-- The below code snippet is automatically added from break_continue_statements.py -->

```py
# Prints out 0,1,2,3,4

count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break

# Prints out only odd numbers - 1,3,5,7,9
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=break_continue_statements.console) -->
<!-- The below code snippet is automatically added from break_continue_statements.console -->

```console
+ python break_continue_statements.py
0
1
2
3
4
1
3
5
7
9
```

<!-- AUTO-GENERATED-CONTENT:END -->

## can we use `else` clause for loops

unlike languages like C,CPP.. we can use else for loops.
When the loop condition of "for" or "while" statement fails then code part in "else" is executed.
If break statement is executed inside for loop then the "else" part is skipped.
Note that "else" part is executed even if there is a continue statement.

Here are a few examples:

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=else_clause.py) -->
<!-- The below code snippet is automatically added from else_clause.py -->

```py
# Prints out 0,1,2,3,4 and then it prints "count value reached 5"

count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if i % 5 == 0:
        break
    print(i)
else:
    print(
        "this is not printed because for loop is terminated because of break but not due to fail in condition"
    )
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=else_clause.console) -->
<!-- The below code snippet is automatically added from else_clause.console -->

```console
+ python else_clause.py
0
1
2
3
4
count value reached 5
1
2
3
4
```

<!-- AUTO-GENERATED-CONTENT:END -->

## Exercise

Loop through and print out all even numbers from the numbers list in the same order they are received.
Don't print any numbers that come after 237 in the sequence.

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

# your code goes here
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
```

<!-- AUTO-GENERATED-CONTENT:END -->
