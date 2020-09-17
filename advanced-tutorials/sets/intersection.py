# Say we have a list of participants in events A and B
a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

# To find out which members attended both events
print(a.intersection(b))
print(b.intersection(a))
