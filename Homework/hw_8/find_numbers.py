list_1 = [0,5,-1,2,-2,3,-64,82,-50,79,0,8]
i = j = 0
i1 = i3 = i6 = 0

while i < len(list_1):
    print(list_1[i])
    if list_1[i]>0:
        j+=1
        if j == 1:
            i1 = list_1[i]
        elif j == 3:
            i3 = list_1[i]
        elif j == 6:
            i6 = list_1[i]
            break
    i+=1  
if i6>0:
    s_list = i1*i3*i6
print(i1,i3,i6)
print(s_list)



