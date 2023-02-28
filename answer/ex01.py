"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
extra: Depending on whether the number is even or odd, print out an appropriate message to the user ("your age is odd/even")
"""
import datetime
def one_00(name, age):
    now = datetime.date.today()
    this_year = now.year
    age = age
    year_to_100 = 100 - int(age) + this_year
    print(f"your age is: {age}")
    check = ''
    if age%2==0:
        check = 'ur age is even'
    else:
        check = 'ur age is odd'
    
    #message
    message = f'''
hello {name}
you are {age}, {check} and {year_to_100} you will be 100 year-old
    '''
    return message

name = input("what's ur name: ")
age = int(input("your age: "))
print(one_00(name,age))