from math import *

print("Hello, welcome you to Comparasion magnitude!")

a = int(input("Pls enter num:"))
b = int(input("Pls enter num:"))


if abs(a) > abs(b) :
    print("This num {} has the greatest magnitude".format(a))
elif abs(a) < abs(b) :
    print("This num {} has the greatest magnitude".format(b))
