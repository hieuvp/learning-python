a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended only one event and not the other
print(a.difference(b))
print(b.difference(a))
