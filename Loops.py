# The Range Function
# Parameters are always integers
for x in range(5):
    print(x)

for x in range(3, 6):
    print(x)

for x in range(3, 8, 2):
    print(x)

# range(5) meaning it stops at the 5 element note it starts from 0
# so will be 0,1,2,3,4

# range(3,6) meaning it will start after the first part of the parmeter and stop and the second parameter
# range(start,stop)
# so will be 3,4,5

# range(3,8,2) meaning it will start after first element, stop from second paramenter
# and will difference between the numbers themselves
# range(start, stop, step)
# start: starting number of sequence
# stop: generate numbers up to not including 
# step: difference between each number in the sequence
# so it will be 3,5,7


# simple for loop

primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)

# simple while loop
count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1

# this while loop has count at 0 and will continue to increment it until it reaches less than 5
# if it is 5 of greater then it will break the loop
count = 0
while True:
    print(count)
    count += 1
    if count >= 5:
        break
# so it will be 0,1,2,3,4

# now this for loop will be using the range of 10 so it will be looping all the numbers from 0 to 9 normally
# however when we check the remainder of the numbers and it is 0 that means it is even and the loop will continue
# continue means that it will skip that current block the loop is in and continue moving forward till the end of the loop
# therefore it will be 1,3,5,7,9 in other words all odd numbers from the for loop
for x in range(10):
    # Check if x is even
    if x % 2 == 0:
        continue
    print(x)


# the else clause can be used in loops
# it else will be used if the loop fails
# else is still used even if a continue is used
# prints out 0,1,2,3,4 and then prints outs count value reached (the count value)
count=0
while(count<5):
    print(count)
    count +=1
else:
    print("count value reached %d" %(count))

# Prints out 1,2,3,4
# if there is a break then the else will not activate since it will be skipped
for i in range(1, 10):
    if(i%5==0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")

# exercise
# loop through and print all even numbers from the list and don't print any numbers after 237

numbers = [
    951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544,
    615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941,
    386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,
    399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,
    815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,
    958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470,
    743, 527
]

for number in numbers:
    if number == 237:
        break

    if number % 2 == 1:
        continue

    print(number)
