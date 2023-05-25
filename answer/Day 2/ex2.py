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
string = 'Aquafina - Vị ngon của sự tinh khiết'
char_replace = [('a','@'), ('o','0'), ('s','$'), ('i','1')]
for char, char_replace in char_replace:
    if char in string:
        string = string.replace(char,char_replace)
print(string)



    
