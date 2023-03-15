"""
Ask the user for a number and determine whether the number is prime or not. (a prime number is a number that has no divisors.
"""

def check_prime(input_number):
    if input_number == 0 or input_number == 1:
        return "wrong input"
    else:
        for i in range(2,input_number):
            if input_number % i == 0:
                return f"{input_number} is not prime"
        return f"{input_number} is prime"

while True:
    input_number = int(input("Input Number: \n"))
    print(check_prime(input_number))
