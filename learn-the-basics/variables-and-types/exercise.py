# Create a String, a Floating Point Number, and an Integer
MY_STRING = "hello"
MY_FLOAT = 10.0
MY_INT = 20

# Testing Code
if MY_STRING == "hello":
    print("String: %s" % MY_STRING)
if isinstance(MY_FLOAT, float) and MY_FLOAT == 10.0:
    print("Float: %f" % MY_FLOAT)
if isinstance(MY_INT, int) and MY_INT == 20:
    print("Integer: %d" % MY_INT)
