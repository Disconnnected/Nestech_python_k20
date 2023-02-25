"""
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old
extra: Depending on whether the number is even or odd, print out an appropriate message to the user ("your age is odd/even")
"""
import datetime

def next_100_years(n,a):
    #Get datetime
    today = datetime.date.today()
    thisyear = today.year
    age_in_this_year = a
    
    #Caculate years
    next_100_year = (100 - int(a)) + thisyear
    
    #Check age is even or odd
    age_checked = ''
    if int(a) % 2 == 0:
        age_checked = 'your age is even'
    else:
        age_checked = 'your age is odd'
    
    #Output
    message = f'''
    Hello {n}
    Your age in this year is {age_in_this_year}, and {age_checked}.
    But if you survive to be 100 years old, your will advance in {next_100_year}.    
    '''

    return message

namefield = input('Please enter your name: ')
age = input('Please enter your age: ')

print(next_100_years(namefield,age))
