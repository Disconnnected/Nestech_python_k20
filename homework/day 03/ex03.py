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
print('phân biệt hoa, thường')
word_1 = input("Điền từ cần nhập: ")


#check cách đọc
def check_read(a):
    if word_1 == word_1[::-1]:
        print("xuôi ngược là 1")
    else:
        print('khác nhau hoàn toàn')
    return ''
print(check_read(word_1))

#không phân biệt hoa, thường
#input từ
print('không phân biệt hoa thường')
word_2 = input("Điền từ cần nhập: ").upper()


#check cách đọc
def check_read(a):
    if word_2 == word_2[::-1]:
        print("xuôi ngược là 1")
    else:
        print('khác nhau hoàn toàn')
    return ''
print(check_read(word_2))

