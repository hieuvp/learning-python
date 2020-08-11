# Loops

## Table of Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [`for`](#for)
- [`while`](#while)
- [`break` and `continue` Statements](#break-and-continue-statements)
- [`else` Clauses](#else-clauses)
- [Exercise](#exercise)
- [References](#references)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## `for`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=for_loop.py) -->
<!-- The below code snippet is automatically added from for_loop.py -->

```py
PRIMES = [2, 3, 5, 7]

# Iterate over a given sequence
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

<br />

> `range()` returns a sequence of numbers.

```python
range(start, stop, step)
```

| Parameter               | Description                                   |
| ----------------------- | --------------------------------------------- |
| `start` (optional)      | The position to start. Default is `0`.        |
| `stop` &nbsp;(required) | The position to stop, but not include itself. |
| `step` &nbsp;(optional) | The incrementation. Default is `1`.           |

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=for_range_loops.py) -->
<!-- The below code snippet is automatically added from for_range_loops.py -->

```py
output = "range(5)       =>"
for x in range(5):
    output += " %d" % x

print(output)

output = "range(3, 6)    =>"
for x in range(3, 6):
    output += " %d" % x

print(output)

output = "range(3, 8, 2) =>"
for x in range(3, 8, 2):
    output += " %d" % x

print(output)
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=for_range_loops.console) -->
<!-- The below code snippet is automatically added from for_range_loops.console -->

```console
+ python for_range_loops.py
range(5)       => 0 1 2 3 4
range(3, 6)    => 3 4 5
range(3, 8, 2) => 3 5 7
```

<!-- AUTO-GENERATED-CONTENT:END -->

## `while`

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=while_loop.py) -->
<!-- The below code snippet is automatically added from while_loop.py -->

```py
count = 0

# Repeat as long as a certain boolean condition is met
while count < 5:
    print(count)
    count += 1  # Same as "count = count + 1"
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

## `break` and `continue` Statements

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=break_continue_statements.py) -->
<!-- The below code snippet is automatically added from break_continue_statements.py -->

```py
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break  # exit the loop

print()

for x in range(10):
    if x % 2 == 0:
        continue  # return the control to beginning of the loop
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

## `else` Clauses

> In other languages, `else` functionality is only provided in `if-else` pairs.<br />
> But Python allows us to implement the `else` functionality with **loops** as well.

<br />

When the **loop terminates normally**, the `else` is **executed**.
For instance:

1. When a loop condition fails.
1. Even if there is a `continue` statement, it is still executed.

<br />

When the **loop terminates forcefully**, the `else` is **skipped**.
For instance:

1. `break` statement is executed inside a loop.

<br />

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=else_clause.py) -->
<!-- The below code snippet is automatically added from else_clause.py -->

```py
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

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.py) -->
<!-- The below code snippet is automatically added from exercise.py -->

```py
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
```

<!-- AUTO-GENERATED-CONTENT:END -->

<!-- AUTO-GENERATED-CONTENT:START (CODE:src=exercise.console) -->
<!-- The below code snippet is automatically added from exercise.console -->

```console
+ python exercise.py
162
758
918
```

<!-- AUTO-GENERATED-CONTENT:END -->

## References

- [Python `range()` Function](https://www.w3schools.com/python/ref_func_range.asp)
- [Using `else` Conditional Statement With `for` Loop In Python](https://www.tutorialspoint.com/using-else-conditional-statement-with-for-loop-in-python)
