"""
Write a Python program that iterates the integers from 1 to 100. if multiples of three print "Fizz" instead of the number, multiples of five print "Buzz" and multiples of three and five, print "FizzBuzz".
"""

for i in range(1,101):
    if(i%3==0 and i%5==0):
        print('FizzBuzz')
    elif(i%3==0):
        print('Fizz')
    elif(i%5==0):
        print('Buzz')
    else:
        print(i)