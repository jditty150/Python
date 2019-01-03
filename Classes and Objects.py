# basic class looks like

class MyClass:
    variable= "blah"
    # define a function in the class
    # have it do something
    def function(self):
        print("This is a message inside the class.")
# holds the object of the class
# this case the class is MyClass
myobjectx = MyClass()
# this allows you to access the variable inside the class
myobjectx.variable
# having the print statement will print out the variable
print(myobjectx.variable)

# can create multiple different objects that are in the same class.
myobjecty = MyClass()

# can define an object to any type of variable
# Note each object would contain an independent variable copy from the same class

myobjecty.variable = "yachety"

# will print out that variable string itself
print(myobjecty.variable)

# this will access the function of the object
myobjectx.function

# We have a class defined for vehicles. Create two new vehicles called car1 and car2.
# Set car1 to be a red convertible worth $60,000.00 with a name of Fer, and car2 to be a blue van named Jump worth $10,000.00.

class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

car1 = Vehicle()
car1.name = "Fer"
car1.color = "red"
car1.kind = "convertible"
car1.value = 60000.00

car2 = Vehicle()
car2.name = "Jump"
car2.color = "blue"
car2.kind = "van"
car2.value = 10000.00

print(car1.description())
print(car2.description())

# create vheicle class that has the value of name, kind, color, value
# create a function called description where the string will be the above using the string laws.
# creating 2 cars and adding them to the vehicle class
# giving each car a name, color, kind, and value
# then print the car description
