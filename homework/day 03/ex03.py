"""
Ask the user for a string and print out whether this string is a palindrome or not. (A palindrome is a string that reads the same forwards and backwards.)

example: 
    - anna
    - civic
    - level
    - madam
    - mom
    - noon
    - radar
    - wow

"""

while True:
    string_input = input("input string: \n")
    if string_input == string_input[::-1]:
        print(f"Correct answer: {string_input} \n \n")
    else:
        print("wrong answer. try again")