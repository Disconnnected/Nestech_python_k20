"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
"""
from random import randrange

def check_number(number):
    numberRandom = randrange(1,10)
    if number < numberRandom:
        print(f"=> too low. Kết quả: {numberRandom}")
    elif number > numberRandom:
        print(f"=> too high. Kết quả: {numberRandom}")
    elif number == numberRandom:
        print(f"=> exactly right. Kết quả: {numberRandom}")
        
print("Trò chơi đoán sô")
number = input("Nhập vào 1 số bất kì từ 1 đến 9: \n")

while True:
    try:
        number = int(number)
        if number in range(1,10):
            check_number(number)
        else:
            print("=> Số không nằm trong 1-9")
        number = input("Nhập 1 số khác hoặc nhấn q/quit để thoát: \n")
    except ValueError:
        if (number =="q" or number == "quit"):
            print("Hẹn gặp lại!")
            break
        else:
            print("=> không phải là 1 số")
        number = input("Nhập 1 số khác hoặc nhấn q/quit để thoát: \n")



