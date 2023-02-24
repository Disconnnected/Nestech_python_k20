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
print("Kiểm tra xem 1 chữ có phải là palindrome hay không?")
string = input("Nhập vào 1 chữ bất kì:\n")

def check_palindrome(string):
    if string == string[::-1]:
        return "This is a palindrome"
    else:
        return "This isn't a palindrome"

print(check_palindrome(string))
