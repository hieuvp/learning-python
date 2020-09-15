# In order to use the json module, it must first be imported
import json

# To encode a data structure to JSON, use the "dumps()" method
# This method takes an object and returns a "string":
json_str = json.dumps({"name": "John", "age": 30, "city": "New York"})
print("json_str        = %s" % json_str)
print("type(json_str)  = %s" % type(json_str))

print()

# To load JSON back to a data structure, use the "loads()" method
# This method takes a string and turns it back into the json object data structure:
json_dict = json.loads(json_str)
print("json_dict       = %s" % json_dict)
print("type(json_dict) = %s" % type(json_dict))
