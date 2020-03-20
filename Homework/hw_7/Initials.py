name = input("Enter your name:")
print(name.isdigit())
print(len(name.split()))
s_name=''
idx = 0
while idx < len(name):
    if name[idx].isupper():
        s_name += name[idx]+'.'
    idx +=1

print(s_name)
