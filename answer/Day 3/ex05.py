"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""

import random

#Puzzle Game
def puzzle_random_numb(x):
    correct_numb = random.randrange(1,9)
    x = int(x)
    if x < correct_numb:
        return f'{x} is too low. Accurate results: {correct_numb}'
    elif x > correct_numb:
        return f'{x} is too high. Accurate results: {correct_numb}'
    else:
        return f'Congratulations! {x} is exactly right. Accurate results: {correct_numb}'

#Checking Function
def check(x):
    while True:
      try:
        x = int(x)
        if x in range(1,10):
            run = x
            break
        elif x > 9:
            print('Please only enter numbers from 1 to 9. Try again...')
            x = input('Enter your answer: ')
      except:
            print('The answer must be a number. Try again...')
            x = input('Enter your answer: ')
    return puzzle_random_numb(run)

message = f'''
  *****<<WELCOME TO THE RANDOM PUZZLE>>*****
   THE NUMBER WILL BEGIN AT 1 AND END AT 9
    FILL IN THE BLANKS WITH YOUR RESPONSE
'''
print(message)
user_guess = input('Enter your answer: ')
print(check(user_guess))