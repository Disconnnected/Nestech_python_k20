"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password
"""
import random
import string

def generate_password(length):
    # Tạo một danh sách chứa tất cả các ký tự được cho phép trong mật khẩu
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Sử dụng module random để lấy ngẫu nhiên các ký tự từ danh sách
    password = ''.join(random.choice(all_chars) for i in range(length))

    print(f"{random.choice(all_chars)}" for i in range(length))
    return password

# Hỏi người dùng về độ dài mật khẩu
length = 10

# Tạo và in ra mật khẩu mới
password = generate_password(length)
print("Mật khẩu mới của bạn là:", password)
