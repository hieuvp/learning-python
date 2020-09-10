def make_counter():
    i = 0

    # counter() is a closure
    def counter():
        nonlocal i
        i += 1
        return i

    return counter


c1 = make_counter()
c2 = make_counter()

print(c1(), c1(), c2(), c2())
