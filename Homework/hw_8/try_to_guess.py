import random

tries = 0
number = random.randint(1, 50)
print(number)

print("Try to guess!")
while tries < 6:
    attempts = int(input("Enter your num:"))

    tries+=1
    if attempts < number:
        print("You guess is too low")
    elif attempts > number:
        print("Your guess is too high")
    elif attempts == number:
        print("Congrats! You guessed my number!")    
    elif guess !=number and tries ==6:
        print("Sorry, but your didn't make it.")