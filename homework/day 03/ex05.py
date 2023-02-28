"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

import random

random_number = random.randint(1, 9)

guess = int(input("Hãy đoán số từ 1 đến 9: "))
print(f"random_number is: {random_number}")
if guess < random_number:
    print("too low.")
elif guess > random_number:
    print("too high.")
else:
    print("exactly right")
