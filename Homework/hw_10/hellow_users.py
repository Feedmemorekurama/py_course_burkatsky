roles = {
    "admin": ['Markus','John','Rob'],
    "maintainer": ['Bobby','Andy','Carlsen'],
    "manager": ['Garry','Mob','Ozzy'],
    "developer": ['Carlos','Max','Artur']}

name = input("My name is, ")
for role, names in roles.items():
    if name in names:
        print(f"Hello, {role}")
        break
else:
    print("Hello, Guess")
