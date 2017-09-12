import random

def user_input():
    try:
        n = int(input("Enter an integer between 0-20."))
    except ValueError:
        print("Give me an integer!")
        return user_input()
    else:
        if 0 > n or n > 20:
            print("Not in the range!")
            return user_input()
    return n

num = random.randint(0, 20)
count = 0

while count < 10:
    guess = user_input()
    chance = 9 - count
    count += 1

    if guess == num:
        print("Bingo!!!!!!")
        break
    elif guess > num:
        print("Your number is bigger .\nYou have %s chance." % chance)
    elif guess < num:
        print("Your number is smaller .\nYou have %s chance." % chance)
else:
    print("Game over.")
