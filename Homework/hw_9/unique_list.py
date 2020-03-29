list1 = [1,1,2,3,5,8,13,21,34,55,89]
list2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
set1 = set(list1)
set2 = set(list2)
set3 = set1.union(set2)
set3 =sorted(set3)
print(set3)