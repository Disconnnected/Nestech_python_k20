"""
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
"""

number1 = 20
number2 = 30
number3 = 11

def find_max(num1,num2,num3):
    number_max = num1
    if (number_max < num2):
        number_max = num2
    if (number_max < num3):
        number_max = num3
    return number_max

print(f"số lớn nhất là: {find_max(number1,number2,number3)}")