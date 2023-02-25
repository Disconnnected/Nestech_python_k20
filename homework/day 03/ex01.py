"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
extra: Depending on whether the number is even or odd, print out an appropriate message to the user ("your age is odd/even")
"""

name = input('Nhập tên của bạn: ')
age = int(input("Nhập tuổi của bạn: "))

import datetime


def showNameAgeTo100(name, age):
    current_year = datetime.datetime.now().year
    if(age%2==0):
        print(f"{name} à tuổi của bạn là chăn và Năm {current_year+(100-age)} bạn sẽ được 100 tuổi ")
    else:
        print(f"{name} à tuổi của bạn là lẻ và Năm {current_year+(100-age)} bạn sẽ được 100 tuổi ")
showNameAgeTo100(name,age)


