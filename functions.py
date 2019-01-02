# Functions is a convenient way to divide your code into useful blocks
# block_head:
#   1st block line
# function format: block_leyword block_name(arg1,arg2,etc)
# block keywords are like if, for and while

def my_function():
    print("Hello From My Function!")

# Functions can have multiple arguments(variables passed from the caller to the function)

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s"%(username, greeting))

# return is the keyword used to return any value created to the caller of the function

def sum_two_numbers(a,b):
    return a+b
# can simply call functions in python by writing the function's name
# with () and if you want placing and required arugments needed
# once that is done you can easily place whatever functions you may want to have
# and use them to print whatever you want that is within the functions

# this will print Hello From My Function!
my_function()

# This will print Hello, John Doe, From My Function!, I wish you a great year!
my_function_with_args("John Doe", "a great year!")

# this give x the value of 3 when it's finished with it's returning
x = sum_two_numbers(1,2)

# this will print x which already has the value of 3
print(x)

# exercise
# add a function named list_benefits() that returns the following list of strings
# "More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"
# Add a function named build_sentence(benefits) which receives a single
# argument containing a string and returns a sentence starting with the given string and ending with the string " is a benefit of functions!"

def list_benefits():
    return "More organized code", "more readable code", "Easier code resue", "Allowing programmers to share and conenct code together"
def build_sentence(benefits):
    return "%s is a benefit of functions!" % benefit
def name_the_benefits_of_function():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
name_the_benefits_of_function()


