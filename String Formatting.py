# must print following string using formats

# Creating string for name
Name = "John Doe"
# Creating a float value for money
money = 53.44
# This is where the actual string is printed
# %s is for the name
# %f is for float
# to actually have the number of digits right you actually have to put %.<number of digits>f
print("Hello %s. Your current balance is $%.2f" % (Name, money))

# The real exercise itself
# can use %s multiple times

data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
