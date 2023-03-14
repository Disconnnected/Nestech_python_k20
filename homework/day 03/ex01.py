"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
extra: Depending on whether the number is even or odd, print out an appropriate message to the user ("your age is odd/even")
"""

fullname = input("Name: \n")
age = input("age: \n")

age = int(age)

birthyear = 2023 - age
year_will_turn_100 = birthyear + 100

print(f"{fullname} will turn 100 in {year_will_turn_100}")


