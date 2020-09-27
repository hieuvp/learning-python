# Return the amount of extra arguments received
def foo(a, b, c, *rest):
    return len(rest)


# Return True if the argument with the keyword "magic_number" is worth "7"
def bar(a, b, c, **options):
    if options.get("magic_number") == 7:
        return True

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
