# Define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str


# Create two new vehicles called car1 and car2
car1 = Vehicle()
car2 = Vehicle()

# Set car1 to be a red convertible worth $60,000.00 with a name of Fer
car1.name = "Fer"
car1.color = "red"
car1.value = 60000.00

print(car1.description())

# Set car2 to be a blue van named Jump worth $10,000.00
car2.name = "Jump"
car2.kind = "van"
car2.color = "blue"
car2.value = 10000.00

print(car2.description())
