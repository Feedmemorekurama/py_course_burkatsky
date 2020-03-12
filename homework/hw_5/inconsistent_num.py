lst = [1,2,3,4,6,7] #Делаем проверку списка непоследовательного
i =0 
for j in lst:
    if j - i != 1:
        i +=1
    
else:
    print(f"The number {i} is not sequential")

lst_1 =[1,2,3,4,5] #Делаем проверку на последовательный список
l = 0
for k in lst_1:
    if k - l != 1:
        continue
    l += 1
    
print(f"The list {lst_1} is consistent")