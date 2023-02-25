"""
Ask the user for a number and determine whether the number is prime or not. (a prime number is a number that has no divisors).
"""

import sympy

def prime_check(x):
    while True:
      try:
        x = int(x)
        if sympy.isprime(x):
            return f"< {x} > is prime"
        else:
            return f"< {x} > isn't prime"
      except:
            print("Please only enter integers. Try again...")
            x = input('To test Prime, enter a number: ')

user_enter = input('To test Prime, enter a number: ')
print(prime_check(user_enter))