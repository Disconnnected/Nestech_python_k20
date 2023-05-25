"""
Ask the user for a number and determine whether the number is prime or not. (a prime number is a number that has no divisors.
"""
def check_prime(number):
    for i in range(2,int(number/2)):
        if number % i ==0:
            return f"=> {number} không phải là số nguyên tố"
        return f"=> {number} là số nguyên tố"

number = int(input("check số: "))
print(check_prime(number))
