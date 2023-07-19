import random

rnd_number = random.randint(1, 100)
if rnd_number < 50:
    print("Heads")
else:
    print("Tails")

# Alternative Solution
rnd_number_alternative = random.randint(0, 1)
if rnd_number_alternative ==1:
    print("Heads")
else:
    print("Tails")
