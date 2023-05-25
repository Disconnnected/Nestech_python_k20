"""
cho 1 chuỗi có sẵn, in ra màn hình chuỗi trong đó các ký tự đc yêu cầu sẽ được thay thế cho các ký tự có sẵn

đề bài: 
    - chuỗi đã cho: "Aquafina - Vị ngon của sự tinh khiết"
    - Yêu cầu: 
        - ký tự "a" đổi thành "@"
        - Ký tự "o" đổi thành "0"
        - Ký tự "s" đổi thành "$"
        - Ký tự "i" đổi thành "1"

"""
input_text = 'Aquafina - Vị ngon của sự tinh khiết'
output = ''

for char in input_text:
    if char == 'a':
        output += '@'
    elif char == 'o':
        output += '0'
    elif char == 's':
        output += '$'
    elif char == 'i':
        output += '1'   
    else:
        output += char
print(output)

# cách khác
output2 = ''

output2 = input_text.replace('a','@')
output2 = output2.replace('o','0')
output2 = output2.replace('s','$')
output2 = output2.replace('i','1')

print(output2)

# cách khác dict

input_dict = {'a': '@', 'o': '0', 's':'$','i':'1'}
output3 = ''

for char in input_text:
    if char in input_dict:
        output3 += input_dict[char]
    else:
        output3 += char
print(output3)

#  cách khác với list
lst_find = ['a', 'o', 's', 'i']
lst_replace = ['@','0','$','1']

output4 = ''


for char in input_text:
    if char in lst_find:
        index = lst_find.index(char)
        output4 += lst_replace[index]
    else:
        output4 += char
print(output4)