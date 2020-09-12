# Using the "help()" function to see what each function does:
# - help(dir)
# - help(hasattr)
# - help(id)


# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# Print a list of all attributes of the Vehicle class
for attribute in dir(Vehicle):
    if hasattr(Vehicle, attribute):
        print(attribute)
