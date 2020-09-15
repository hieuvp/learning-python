import json

# To encode a data structure to JSON, use the "dumps()" method
json_string = json.dumps([1, 2, 3, "a", "b", "c"])

# The method takes an object and returns a "string"
print(json_string)
