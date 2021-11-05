# 
# Jaylen Wilson
# Comp 163 - 4
# 10/26/21
# Find the "area of frustration" within an unknown quantity of integers.
#
Aggie_line = []
userLength = int(input("How many people are in the registration line? "))
position = 0

while position < userLength:
    current_aggie = int(input("What is the position of one of the Aggies? "))
    if current_aggie in Aggie_line:
        print("That Aggie has alread been added, try again.")
    else:
        Aggie_line.append(current_aggie)
        position += 1

Aggie_line.sort()
print(Aggie_line)

smallestFrustration = 1000000001
for pos in Aggie_line[1:-1]:
    leftSpace = (pos + Aggie_line[Aggie_line.index(pos) - 1]) / 2
    rightSpace = (pos + Aggie_line[Aggie_line.index(pos) + 1]) / 2
    frustration = rightSpace - leftSpace
    if frustration < smallestFrustration:
        smallestFrustration = frustration
    # print("Left space of", pos, "is: ", leftSpace)
    # print("Right space of", pos, "is:", rightSpace)
    # print("Area of frustration", frustration)
    # print("The smallest area of frustration is:", smallestFrustration)
print("The smallest area of frustration is:", smallestFrustration)