"""
Ask the user for a number and determine whether the number is prime or not. (a prime number is a number that has no divisors.
"""

a = int(input('PLEASE ENTER NUMBER: ')) 
for i in range(2,int(a/2)):
    b = []
    b.append(i)
    if a % i == 0:
        print(f'{a} không là số nguyên tố')
