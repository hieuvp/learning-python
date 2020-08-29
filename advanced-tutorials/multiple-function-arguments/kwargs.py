def function(first, second, third, **options):
    if options.get("action") == "sum":
        print("The sum is: %d" % (first + second + third))

    if options.get("number") == "first":
        return first


result = function(1, 2, 3, action="sum", number="first")
print("Result: %d" % result)
