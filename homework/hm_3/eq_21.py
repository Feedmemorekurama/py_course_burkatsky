from math import *

x = int(input("Enter x ="))
y = ((log(x)**1/4) + acos(x + 3)) * ((1) / (abs(x + (2*x**2))))
print(y) # Выводит ввести x, но при любом введении выдает "math domain error"
