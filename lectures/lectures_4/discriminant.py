# ax^2 + bx + c = 0
# x1, x2 --> ?
from math import *

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
discr = b**2 - 4 * a * c

if discr < 0:
    print("Discriminant <0. No roots")
elif discr == 0:
    x = (b+sqrt(discr))/2*a
    print('x1, x2 = {}'.format(x))
else:
    x1= (b+sqrt(discr))/2*a
    x2= (b-sqrt(discr))/2*a
    print('x1 = {} and x2 = {}'.format(x1,x2))