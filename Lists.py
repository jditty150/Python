# Creating a list and appending it
# appending adds an element to the list
myList = []
myList.append(1)
myList.append(2)
myList.append(3)

# Creating a list for strings
second_name = []
second_name.append('Hello')
second_name.append('World')

# Printing it all out
print(myList[0])
print(myList[1])
print(myList[2])
print(second_name[0])
print(second_name[1])

# Creating a list with elements inside
# If elements are inside just say which area of the index should be printed from the array

bog = [1,2,3]
print(bog[2])

# The Lists Exercise itself

numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here
numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)
