"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password
"""
import string, random


#Password Genterator
def password_generator(y):

    #Aa-Zz.
    characters_upper = list(string.ascii_uppercase)
    characters_lower = list(string.ascii_lowercase)

    #0-9.
    number = list(string.digits)

    #Symbols and Ambiguous.
    scac = list(string.punctuation)

    #Shuffle items in the list.
    random.shuffle(characters_upper)
    random.shuffle(characters_lower)
    random.shuffle(number)
    random.shuffle(scac)
    
    y = int(y)
    
    #Calculate % of number of character.
    cal_30 = round(y * (30/100)) #30%
    cal_20 = round(y * (20/100)) #20%

    password_list = []
    
    #Add Character calculated.
    for i in range(cal_30):
        password_list.append(characters_upper[i])
        password_list.append(characters_lower[i])

    #Add Number, Symbols and Ambiguous calculated.
    for i in range(cal_20):
        password_list.append(number[i])
        password_list.append(scac[i])

    #Shuffle one more time.
    random.shuffle(password_list)

    #Generate password.
    password = ''.join(password_list)
    
    return f"\nYour password is: {password}"


#Check user input and exit method
def main(x):
    while True:
        try:
            x = int(x)
            if x < 8:
                print("Your password lenght should be at least 8 characters.")
                x = input("Please, Enter your password lenght again: ")
            else:
                print(password_generator(x))
                x = input("Enter your new password lenght or <'q'> to Exit: ")
                main(x)
                break
        except ValueError:
            if x == "q":
                print("Exiting...")
                exit()
            else:
                x = input("Please, Enter numbers only or <'q'> to Exit.")
                
                
user_input = input("Enter your password lenght: ")
print(main(user_input))