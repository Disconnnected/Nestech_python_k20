"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password
"""

import random
import string

lowercase_string = 'abcdefghijklmnopqrstuvwxyz'
uppercase_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digit_string ='0123456789'
symbols_string= "!#$%&()-/?@"

full_string = lowercase_string+uppercase_string+digit_string+symbols_string

def generate(length):
    password = ''.join(random.choices(full_string, k=length))
    return password

def check_password(password):
    check_lowercase = False
    check_uppercase = False
    check_digit = False
    check_symbols = False
    
    for i in password:
        if i in lowercase_string:
            check_lowercase = True
        if i in uppercase_string:
            check_uppercase = True
        if i in digit_string:
            check_digit = True
        if i in symbols_string:
            check_symbols = True
    if (check_lowercase and check_uppercase and check_digit and check_symbols):
        return True
    else:
        return False

print("Tạo 1 mật khẩu mới")
length = input("Nhập chiều dài ký tự cần tạo: \n")
while True:
    try:
        length = int(length)
        password = generate(length)
        while True:
            if (check_password(password)):
                break
            else:
                password = generate(length)
        print(f"=> Mật khẩu của bạn là: {password}")
        length = input("Nhập 1 con số để tạo mật khẩu khác hoặc nhấn q/quit để thoát: \n")
    except ValueError:
        if length == "q" or length == "quit":
            print("=> Cám ơn bạ đã sử dụng chương trình!")
            break
        else:
            print("=> Nhập sai chiều dài")
            length = input("Nhập lại chiều dài hoặc nhấn q/quit để thoát: \n")
