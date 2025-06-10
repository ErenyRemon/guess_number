# Play with Python and Guess the Correct Number!!
import random
numbers = [1,2,3,4,5,6,7,8,9,10]
guess_com = random.choice(numbers)

guess_user = int(input("Guess a number between 1 and 10: "))
while guess_com != guess_user:
    if guess_com > guess_user:
        print("Too low! ")
        guess_user = int(input("Guess again: "))
    else:
        print("Too high!")
        guess_user = int(input("Guess again: "))
print("Congratulations! You guess the number!")



