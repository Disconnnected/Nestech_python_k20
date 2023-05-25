"""
Đảo ngược thứ tự của 1 chuỗi bất kỳ
"""

str = 'abcdefgh'

str_new = str[::-1]
print('cach 1: ',str_new)

# cách 2 với list

lst_str = list(str)
lst_str.reverse()
str_new2 = ''.join(lst_str)
print('cach 2: ',str_new2)
