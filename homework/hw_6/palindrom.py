my_word = str(input("Enter your word:"))
a = my_word[::-1]
if my_word == a :
    print(f"this {my_word} is a palidrom")
else:
    print(f"This {my_word} not palindom")