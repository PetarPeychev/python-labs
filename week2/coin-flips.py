from random import randint

heads_count = 0
tails_count = 0

for i in range(0, 100):
    flip = randint(0, 1)

    if flip == 0:
        print("Heads")
        heads_count += 1
    else:
        print("Tails")
        tails_count += 1
print("Number of Heads:", heads_count, "Number of Tails:", tails_count)
