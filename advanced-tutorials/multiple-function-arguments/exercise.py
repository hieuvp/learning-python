def foo(a, b, c, *rest):

    # Return the amount of extra arguments received
    return len(rest)


def bar(a, b, c, **options):

    # Return True if the argument with the keyword "magic_number" is worth 7
    if options.get("magic_number") == 7:
        return True

    # Otherwise, False
    return False


# Testing Code
if foo(1, 2, 3, 4) == 1:
    print("Good")

if foo(1, 2, 3, 4, 5) == 2:
    print("Better")

if not bar(1, 2, 3, magic_number=6):
    print("Great")

if bar(1, 2, 3, magic_number=7):
    print("Awesome")
