list_1 = [-28,-2,2,-3,-6,5,-4,0]
list_2 = []

for i in list_1:
    if i < 0:
        list_2.append(i)
        
print(list_2)      
list_2 =sum(list_2) / len(list_2)
print(list_2)
list_1.insert(min(list_1), list_2) 
list_1.remove(min(list_1))
print(list_1)