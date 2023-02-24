"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
extra: Depending on whether the number is even or odd, print out an appropriate message to the user ("your age is odd/even")
"""

name = input("what's your name: ")
age = int(input("how old r u: "))
if age%2==0:
    print('ur age is even')
else:
    print('ur age is odd')

print(f'u still have {100-age} to 100 years old')