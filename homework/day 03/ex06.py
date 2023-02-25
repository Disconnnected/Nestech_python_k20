<<<<<<< HEAD
num = int(input("Nhập một số nguyên dương: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print(num, "là số nguyên tố")
else:
    print(num, "không là số nguyên tố")
=======
"""
Ask the user for a number and determine whether the number is prime or not. (a prime number is a number that has no divisors.
"""
>>>>>>> ce1be8cee6e60a1d7368aec84d539cd6d1a7b484
