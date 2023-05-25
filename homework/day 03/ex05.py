"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""
import random
a = int(input('Mời bạn chọn số: '))

#check số từ 1 đến 9
while a > 9 or a < 1:
    print('chọn số từ 1 - 9')
    a = int(input('Mời chọn lại: '))

def answer(a):
    rand = random.randrange(1,9,1)
    print(f'số của chương trình {rand}')
    if abs(rand - a) > 3:
        print('số bạn chọn quá xa')
    elif 0 < abs(rand - a) <= 3:
        print('số bạn chọn gần đúng')
    else:
        print('bạn chọn đúng số với chương trình')
    return ''
print(answer(a))


=======

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
    