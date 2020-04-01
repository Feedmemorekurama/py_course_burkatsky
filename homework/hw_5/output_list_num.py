list_num = [1,2,3,4,5,6,7,8,9,10]
del_num = int(input("Enter num:"))

for i in list_num:
    if del_num == 0:
        print("Sorry , but you can 't divide by 0")
    elif i % del_num == 0:
        print("this number {} is divided by {} ".format(i,del_num))
    
    else:
        print("You can 't divide by this number{}".format(del_num))