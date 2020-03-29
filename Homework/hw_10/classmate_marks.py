import random
my_dict ={'A':0,'B':0,'C':0,'D':0,'F':0}
mylist = []
while len(mylist) <30:
    mylist.append(random.randint(0,100))

print(mylist)

for marks in mylist:
    if 90 < marks <= 100:
        my_dict['A'] +=1
    elif 80 < marks <= 90:
        my_dict['B'] +=1
    elif 70 < marks <= 80:
        my_dict['C'] +=1
    elif 60 < marks <= 70:
        my_dict['D'] +=1
    else:
        my_dict['F'] +=1
    
print(my_dict)