x = object()
y = object()
# above creates objects makes x and y objects

# creating an x list list with having 10 intances of x same with y
x_list = [x] * 10
y_list = [y] * 10

# creating big list which is the combination of x and y list
big_list = x_list + y_list

print("x_list contains %d objects" % len(x_list))
print("y_list contains %d objects" % len(y_list))
print("big_list contains %d objects" % len(big_list))

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print("Almost there...")
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print("Great!")
