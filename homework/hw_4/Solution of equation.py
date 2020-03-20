#Solution a*x+b=0
print("You need to find a solution to the equation! \nenter a and b")
a = int(input("Enter a:"))
b = int(input("Enter b:"))
if a and b:
    x=-b/a
    print("x=", x)
elif b == 0 and a !=0:
    x=-b/a
    print("x=",x)
else: #Тот случай когда вводим а=0
    print("Has not root")
