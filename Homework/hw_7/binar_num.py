str_num = input('Enter something numbers:')
new_str_num = ''
print(str_num.isdigit())
for i in str_num:
    if int(i) < 5:
        i = 0
        new_str_num += str(i)
    elif int(i) >= 5:
        i = 1
        new_str_num += str(i)

print(new_str_num)
    
