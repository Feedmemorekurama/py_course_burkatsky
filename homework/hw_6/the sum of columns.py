l_1 = [1, 5, 7]
l_2 = [5, 6, 3]
sum_l =[]
for i in range(0,len(l_1)):
    if len(l_1) != len(l_2):
        print("the length of lists is not equal to")
        break
    else:    
        sum_l = l_1[i] + l_2[i]
    print(sum_l)

