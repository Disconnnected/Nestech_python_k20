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

    password_list = []
    
    for i in range(round(12/4)):
        password_list.append(characters_upper[i])
        password_list.append(characters_lower[i])
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
            if x == 2:
                print("Exiting...")
                exit()
            elif x != 1:
                x = x = input("Enter your next choice again (1 or 2): ")
            else:
                print(password_generator(x))
                x = input("""Enter your next choice: """)
                return main(x)
        except ValueError:
            x = x = input("Enter your next choice again (1 or 2): ")
                
user_input = input("""
<----->GENERATOR PASSWORD<----->
        Choose 1 or 2
    1. Create new password
    2. Exit

Enter your choice: """)
print(main(user_input))