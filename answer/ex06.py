"""
Ask the user for a number and determine whether the number is prime or not. (a prime number is a number that has no divisors.
"""
while True:
    a = int(input('PLEASE ENTER NUMBER: ')) 
    for i in a:
        if a == 1:
            print (f'{a} is prime')
        if a % i ==0:
            print (f'{a} is not prime')
        
