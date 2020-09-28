import json

origin = {"name": "John", "age": 30, "city": "New York"}
print("origin       = %s" % origin)
print("type(origin) = %s" % type(origin))


# To encode a data structure to JSON, use the "dumps()" method
# This method takes an object and returns a "string":
json_str = json.dumps(origin)
print()
print("json_str       = %s" % json_str)
print("type(json_str) = %s" % type(json_str))


# To load JSON back to a data structure, use the "loads()" method
# This method takes a string and turns it back into the json object data structure:
json_dict = json.loads(json_str)
print()
print("json_dict       = %s" % json_dict)
print("type(json_dict) = %s" % type(json_dict))
