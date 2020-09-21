a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended only one of the events
print(a.symmetric_difference(b))
print(b.symmetric_difference(a))
