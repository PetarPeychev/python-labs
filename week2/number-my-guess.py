from random import randint

print("Think of a number from 1 to 100")

previous_highest_guess = 100
previous_lowest_guess = 1

for guesses in range(11):
    if guesses == 10:
        print("The computer has failed to guess your number! Terrible!")
        break

    guess = randint(previous_lowest_guess, previous_highest_guess + 1)

    if input("Is you number " + str(guess) + "? [y/n] ") == "y":
        print("YAY!")
        break
    else:
        if input("Is your number lower or higher? [l/h] ") == "l":
            previous_highest_guess = guess - 1
        else:
            previous_lowest_guess = guess + 1
