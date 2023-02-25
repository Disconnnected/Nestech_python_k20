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
string = input("Type your string here: ").lower()
def palindrome_check(a):
    if a == a[::-1]:
        return f"{a} is palidrome."
    else:
        return f"{a} isn't palidrome."
print(palindrome_check(string))
