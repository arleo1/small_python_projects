import random
import time

print("Welcome to Guess the Number!")
exit,game=False, False

while exit is not True:
    list = [i for i in range(1, 101)]
    num = random.choice(list)
    guess = int(input("Enter a guess between 1-100: "))

    while game is not True:
        if guess == num:
            print("You're right! The number was",num)
            game=True
        elif guess>num:
            print("Your guess was too high!")
            guess= int(input("Guess again: "))
        else:
            print("You guess was too low!")
            guess= int(input("Guess again: "))

    time.sleep(1)
    close= input("Press x to exit the game, or any other letter to play again: ")

    if close=="x":
        exit=True
        break
    elif close!="x":
        game=False
        time.sleep(1)