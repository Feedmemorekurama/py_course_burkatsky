roles = {
    "admin": ['Markus','John','Rob'],
    "maintainer": ['Bobby','Andy','Carlsen'],
    "manager": ['Garry','Mob','Ozzy'],
    "developer": ['Carlos','Max','Artur']}

name = input("My name is, ")
for i in roles.items():
    if name in roles['admin']:
        print("Hello, admin!")
    elif name in roles['maintainer']:
        print("Hello, maintainer!")
    elif name in roles['manager']:
        print("Hello, manager!")
    elif name in roles['developer']:
        print("Hello, developer!")
    else:
        print("Hello, Guess")
    break