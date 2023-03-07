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



#check cách đọc
def check_read_1(a):
    word = input("Điền từ cần nhập: ")
    if word == word[::-1]:
        return ("xuôi ngược là 1")
    else:
        return ('khác nhau hoàn toàn')

#không phân biệt hoa, thường
#input từ

#check cách đọc
def check_read_2(a):
    word = input("Điền từ cần nhập: ").upper()
    if word == word[::-1]:
        print("xuôi ngược là 1")
        return main(a)
    else:
        print('khác nhau hoàn toàn')
        return main(a)

def main(user_input):
    while (True):
        try:
            
            if user_input == 1:
                print(check_read_1(user_input))
                return main(user_input)
            elif user_input == 2:
                print( check_read_2(user_input))
                return main(user_input)
            elif user_input == 3:
                print('Exist....')
                exit()
        except ValueError:
            user_input = user_input = input('please choose 1, 2, 3 : ')


user_input = int(input(''''
<----->palindrome<----->
    1. Phân biệt hoa, thường
    2. Không phân biệt hoa, thường
    3. Exit

YOUR CHOOSE: 
'''))
print(main(user_input))
