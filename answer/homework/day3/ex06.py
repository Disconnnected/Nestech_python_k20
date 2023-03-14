"""
Ask the user for a number and determine whether the number is prime or not. (a prime number is a number that has no divisors.
"""

def check_prime(number):
    for i in range(2,number):
        if number % i ==0:
            return f"=> {number} không phải là số nguyên tố"
        return f"=> {number} là số nguyên tố"

print("Kiểm tra 1 số có phải là số nguyên tố không?")
number = input("Nhập 1 số: \n")
while True:
    try:
        number = int(number)
        if number > 1:
            print(check_prime(number))
            number = input("Nhập 1 số khác hoặc nhấn q/quit để thoát: \n")
        else:
            print("=> Phải nhập 1 số lớn hơn 1")
            number = input("Nhập 1 số khác hoặc nhấn q/quit để thoát: \n")

    except ValueError:
        if (number == 'q' or number == 'quit'):
            print("Hẹn gặp lại")
            break
        else:
            print("=> Không phải là 1 số đúng")
            number = input("Nhập 1 số khác hoặc nhấn q/quit để thoát: \n")
