def function(first, second, third, **options):
    if options.get("action") == "sum":
        sum = first + second + third
        print("sum   = %s" % sum)

    if options.get("number") == "first":
        print("first = %s" % first)


function(1, 2, 3, action="sum", number="first")
