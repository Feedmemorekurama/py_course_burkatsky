my_list = [15, 2, 7 ,17, 35, 5 ,-12, 49]
new_list = []
idx = 0
for i in my_list:
    if idx == 0:
        idx+=1
    elif i % idx ==0:
        new_list.append(i)
        idx+=1
    else:
        idx+=1

print(new_list)