from random import randint

secret_number = randint(1, 20)

for guesses in range(6):
    if guesses == 5:
        print("You have failed to guess! Terrible!")
        break

    guess = int(input("Enter a guess from 1 to 20: "))

    if guess == secret_number:
        print("Correct!")
        break
    elif guess > secret_number:
        print("Go Lower")
    elif guess < secret_number:
        print("Go Higher")
