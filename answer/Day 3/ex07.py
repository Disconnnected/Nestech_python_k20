"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password
"""
import string, random
    
#Aa-Zz
characters = string.ascii_letters

#0-9
number = string.digits

#Symbols and Ambiguous
scac = string.punctuation

# def check_user_input(x):
#     while True:
#         try:
#             x = int(x)
#             if x < 8:
#                 print("Your password lenght should be at least 8 characters.")
#                 x = input("Please, Enter your password lenght again: ")
#             else:
#                 return x
#         except:
#             print("Please, Enter numbers only.")
#             x = input("Enter your password lenght: ")

# user_input = input("Enter your password lenght: ")
# print(check_user_input(user_input))

# def password_generator(y):
