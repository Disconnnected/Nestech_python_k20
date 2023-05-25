"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password
"""
import string, random
def password(a):
    #set characters
    lowercase = list(string.ascii_lowercase)
    uppercase = list(string.ascii_uppercase)
    number = list(string.digits)
    symbol = list(string.punctuation)
    
    #shuffle characters
    # random.shuffle(lowercase)
    # random.shuffle(uppercase)
    # random.shuffle(number)
    # random.shuffle(symbol)
    
    #condition: sum b + c + d + e = a
    while True:
        b = a - random.randint(3,a-1)
        c = a - random.randint(3,a-1)
        d = a - random.randint(3,a-1)
        e = a - random.randint(3,a-1)
        if a == b + c + d + e:
            break
    #choose characters
    random.choices(lowercase,k=b )
    random.choices(uppercase,k=c )
    random.choices(number,k=d )
    random.choices(symbol,k=e )
    #write password
    password = []
    for i in range(b):
        password.append(lowercase[i])
    for i in range(c):
        password.append(uppercase[i])
    for i in range(d):
        password.append(number[i])
    for i in range(e):
        password.append(symbol[i])
    random.shuffle(password)
    #print password
    password = ''.join(password)
    return password

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
                a = int(input("Password's Length (at least 4): "))
                print(password(a))
                x = input("""
<----->GENERATOR PASSWORD<----->
        Choose 1 or 2
    1. Create new password
    2. Exit
Enter your next choice: """)
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
=======
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
