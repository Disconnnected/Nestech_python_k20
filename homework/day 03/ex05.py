"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

# random

import random

x = random.randint(1,9)



while True:
    user_guess = int(input("Let's guess: \n"))
    if user_guess > x:
        print("It's too high")
    elif user_guess < x:
        print("it's too low")
    else:
        print("you are correct")
    print(f"Số X là: {x}")
    
