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
#phân biệt hoa, thường
#input từ
word_1 = input("Điền từ cần nhập: ")


#check cách đọc
def check_read(a):
    if word_1 == word_1[::-1]:
        return ("xuôi ngược là 1")
    else:
        return ('khác nhau hoàn toàn')

#không phân biệt hoa, thường
#input từ
word_2 = input("Điền từ cần nhập: ").upper()

#check cách đọc
def check_read(a):
    if word_2 == word_2[::-1]:
        return "xuôi ngược là 1"
    else:
        return 'khác nhau hoàn toàn'

while True:
    message = """
Please choose one number:
    1. Phân biệt hoa thường
    2. Không phân biệt hoa thường
    3. Quit
----------------------------------
    """
=======
"""

while True:
    string_input = input("input string: \n")
    if string_input == string_input[::-1]:
        print(f"Correct answer: {string_input} \n \n")
    else:
        print("wrong answer. try again")