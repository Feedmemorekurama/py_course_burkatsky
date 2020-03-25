import random
n = 10
list1 = []
while len(list1) < 10:
    list1.append(random.randint(0,50))

print(list1)
for i in range(n-1):
    for j in range(i+1,n):     
        if list1[i] == list1[j]:
            print("the numbers are repeated ")
            quit()
print("All number unique")