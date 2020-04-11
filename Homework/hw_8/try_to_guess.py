import random

tries = 6
number = random.randint(1, 50)

print("Try to guess!")
while tries > 0:
    attempts = int(input("Enter your num:"))
    tries-=1
    if attempts < number:
        print("You guess is too low")
    elif attempts > number:
        print("Your guess is too high")
    elif attempts == number:
        print("Congrats! You guessed my number!")   
        break 
else:
    print("Sorry, but your didn't make it.")