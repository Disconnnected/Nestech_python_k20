"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password
"""
import random, string
length = 8

lower = string.ascii_lowercase
upper = string.ascii_uppercase
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']


number = string.digits
list_char = lower + number + upper

password = ""

# generate 8 digit of password
for i in range(length):
    char = random.choice(list_char)
    password += char

# check if password has contain upper case letter
def check_password_upper(password):
    for char in password:
        if char in upper:
            return True

# check if password has contain lower case letter
def check_password_lower(password):
    for char in password:
        if char in lower:
            return True
            
# check if password has contain number letter
def check_password_number(password):
    for char in password:
        if char in number:
            return True

while ((check_password_lower(password) and check_password_upper(password) and check_password_number(password))):
    print(password)
    break
