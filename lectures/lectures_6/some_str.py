some_str = input("Enter some string:")

if len(some_str) > 2:
    print(list(some_str)[1:-1])
else:
    print("String lenght less than 2 chars")