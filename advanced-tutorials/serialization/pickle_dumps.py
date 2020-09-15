import pickle

pickled_bytes = pickle.dumps({"name": "John", "age": 30, "city": "New York"})
print("pickled_bytes       = %s" % pickled_bytes)
print("type(pickled_bytes) = %s" % type(pickled_bytes))

print()

pickled_dict = pickle.loads(pickled_bytes)
print("pickled_dict        = %s" % pickled_dict)
print("type(pickled_dict)  = %s" % type(pickled_dict))
