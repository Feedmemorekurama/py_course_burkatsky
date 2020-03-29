roles = {
    "admin": 'Markus',
    "maintainer": 'Bobby',
    "manager": 'Garry',
    "developer": 'Carlos'}

name = input("My name is, ")
for i in roles.values():
    if name == 'Markus':
        print("Hello, admin!")
    elif name == 'Bobby':
        print("Hello, maintainer!")
    elif name == 'Garry':
        print("Hello, manager!")
    elif name == 'Carlos':
        print("Hello, developer!")
    else:
        print("Hello, Guess")
    break